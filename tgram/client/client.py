import asyncio
import inspect
import io
import json
import logging
import os
import ssl
from collections import OrderedDict
from importlib import import_module
from pathlib import Path
from typing import Any, Literal

import aiohttp
import certifi
from aiohttp.hdrs import USER_AGENT
from aiohttp.http import SERVER_SOFTWARE

import tgram

from ..decorators import Decorators
from ..errors import APIException
from ..methods import TelegramBotMethods
from ..storage import KvsqliteStorage, RedisStorage, StorageBase
from ..types.type_ import Response, Type_
from ..utils import ALL_UPDATES, API_URL, get_file_name
from .dispatcher import Dispatcher

logger = logging.getLogger(__name__)


class TgBot(TelegramBotMethods, Decorators, Dispatcher):
    """
    A class for creating a Telegram bot with extended functionality and
    support for various features like custom updates, storage engines, and more.

    Inherits from:
        - `TelegramBotMethods`: Provides various methods to interact with Telegram Bot API.
        - `Decorators`: Contains decorators to modify bot behavior.
        - `Dispatcher`: Manages event handling and dispatching for the bot.

    Attributes:
        bot_token (str): The bot token provided by the BotFather.
        api_url (str): The base API URL to communicate with Telegram servers.
        allowed_updates (List[str]): List of update types the bot should listen to.
        link_preview_options (tgram.types.LinkPreviewOptions): Options for link previews in messages.
        parse_mode (tgram.types.ParseMode): Default parse mode for formatting messages.
        protect_content (bool): Whether to protect content from being saved or forwarded.
        workers (int): Number of worker threads for handling updates.
        retry_after (Union[int, bool]): Time or condition for retrying failed requests.
        plugins (Union[Path, str]): Path to the directory containing bot plugins.
        skip_updates (bool): Whether to skip pending updates on bot startup.
        storage (Optional[StorageBase]): Storage engine instance for persisting data.
        storage_client (Any): Client for the storage engine (e.g., Redis or Kvsqlite).
        fetch_outgoing_messages (bool): Handling messages has been sent by the bot.
        loop (asyncio.AbstractEventLoop): Event loop used by the bot.
        is_running (bool): Indicates if the bot is currently running.
        me (tgram.types.User): The bot's user profile.
        handler_worker_tasks (List[asyncio.Task]): Tasks handling updates processing.
        locks_list (List[asyncio.Lock]): Locks used for synchronization.
        updates_queue (asyncio.Queue): Queue for managing incoming updates.
        groups (OrderedDict): Groups of handlers categorized by update types.
    """

    def __init__(
        self,
        bot_token: str,
        api_url: str = API_URL,
        allowed_updates: list[str] | None = None,
        link_preview_options: tgram.types.LinkPreviewOptions = None,
        parse_mode: tgram.types.ParseMode = None,
        protect_content: bool | None = None,
        workers: int | None = None,
        retry_after: int | bool | None = None,
        plugins: Path | str | None = None,
        skip_updates: bool = True,
        storage_engine: KvsqliteStorage | RedisStorage | Literal["kvsqlite", "redis"] = None,
        storage_client: Any = None,
        fetch_outgoing_messages: bool = False,
    ) -> None:
        if allowed_updates is None:
            allowed_updates = []
        self.bot_token = bot_token
        self.api_url = api_url
        self.allowed_updates = allowed_updates
        self.link_preview_options = link_preview_options
        self.parse_mode = parse_mode
        self.protect_content = protect_content
        self.workers = workers or min(32, (os.cpu_count() or 0) + 4)
        self.retry_after = retry_after
        self.plugins = Path(plugins) if isinstance(plugins, str) else plugins
        self.skip_updates = skip_updates
        self.storage: StorageBase | None = None
        self.storage_client = storage_engine
        self.fetch_outgoing_messages = fetch_outgoing_messages

        self.is_running: bool = None
        self._me: tgram.types.User = None

        self._listen_handlers: list[tgram.types.Listener] = []
        self._custom_types: dict = {}
        self._session: aiohttp.ClientSession = None

        self.handler_worker_tasks: list[asyncio.Task] = []
        self.locks_list: list[asyncio.Lock] = []
        self.updates_queue = asyncio.Queue()
        self.groups = OrderedDict()

        if not api_url.endswith("/"):
            api_url += "/"

        self._api_url: str = f"{api_url}bot{bot_token}/"

        # Initialize storage engine if provided
        if storage_engine:
            if isinstance(storage_engine, (KvsqliteStorage, RedisStorage)):
                self.storage = storage_engine
            else:
                if storage_engine.lower() == "kvsqlite":
                    try:
                        __import__("kvsqlite")
                    except ModuleNotFoundError:
                        raise ValueError(
                            "Please install kvsqlite module before using storage, see more https://pypi.org/project/Kvsqlite/"
                        )
                    else:
                        self.storage = KvsqliteStorage(self, storage_client)
                elif storage_engine.lower() == "redis":
                    try:
                        __import__("redis")
                    except ModuleNotFoundError:
                        raise ValueError(
                            "Please install redis module before using storage, see more https://pypi.org/project/redis/"
                        )
                    else:
                        self.storage = RedisStorage(self, storage_client)
                else:
                    raise ValueError(
                        "Unsupported storage engine {}, only {} are supported for now.".format(
                            storage_engine, " ,".join(i for i in ["redis", "kvsqlite"])
                        )
                    )

    def add_handler(self, handler: "tgram.handlers.Handler", group: int = 0) -> None:
        """
        Add a handler to the bot.

        Args:
            handler (tgram.handlers.Handler): The handler to add.
            group (int): The group to add the handler to.
        """
        if handler.type == "all":
            self.allowed_updates = ALL_UPDATES
        elif handler.type != "exception" and handler.type not in self.allowed_updates:
            self.allowed_updates.append(handler.type)

        if group not in self.groups:
            self.groups[group] = []
            self.groups = OrderedDict(sorted(self.groups.items()))
        self.groups[group].append(handler)
        logger.info(
            "(%s) added to %s handlers in group %s",
            handler.callback.__name__,
            "Update." + handler.type if handler.type != "all" else "all",
            group,
        )

    def remove_handler(self, handler: "tgram.handlers.Handler", group: int = 0) -> None:
        """
        Remove a handler from the bot.

        Args:
            handler (tgram.handlers.Handler): The handler to remove.
            group (int): The group to remove the handler from.
        """
        if group not in self.groups:
            raise ValueError(f"Group {group} does not exist. Handler was not removed.")
        self.groups[group].remove(handler)
        logger.info(
            "(%s) removed from %s handlers from group %s",
            handler.callback.__name__,
            "Update." + handler.type if handler.type != "all" else "all",
            group,
        )

    async def _new_session(self) -> None:
        """
        Create a new aiohttp session.
        """
        session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(
                limit=100,
                ssl_context=ssl.create_default_context(cafile=certifi.where()),
                ttl_dns_cache=3600,
            ),
            headers={USER_AGENT: f"{SERVER_SOFTWARE} tgram/{tgram.__version__}"},
        )
        self._session = session

    async def _get_session(self) -> "aiohttp.ClientSession":
        """
        Get the current aiohttp session, or create a new one if necessary.
        """
        if self._session is None or self._session.closed:
            await self._new_session()
        elif not self._session.loop.is_running():
            await self._session.close()
            await self._new_session()

        return self._session

    async def __call__(self, method: str, **kwargs) -> Response:
        """
        Make an API call to the Telegram Bot API.

        Args:
            method (str): The API method to call.
            **kwargs: Additional arguments for the API call.

        Returns:
            Any: The response from the API call.
        """
        request_url = self._api_url + method
        if method != "getUpdates":
            logger.info("Sending request using the method: %s", method)
        session = await self._get_session()
        data = aiohttp.FormData(quote_fields=False)
        has_files = False

        for key, value in kwargs.items():
            file = None
            if value is None or key == "timeout" or key == "retry":
                continue
            if isinstance(value, Path):
                has_files = True
                with open(value, "rb") as f:  # noqa: ASYNC230
                    value = f
                    file = f.read()
            elif isinstance(value, (io.BytesIO, io.BufferedReader, bytes)):
                has_files = True
                file = value if isinstance(value, bytes) else value.read()
            elif isinstance(value, (Type_, list)):
                value = json.dumps(value, ensure_ascii=False, default=Type_.default)
            else:
                value = str(value)
            data.add_field(
                key,
                file or value,
                filename=get_file_name(value) if file else None,
            )

        try:
            response = await session.request(
                "POST" if has_files else "GET",
                request_url,
                data=data,
                timeout=aiohttp.ClientTimeout(
                    total=kwargs.get("timeout", 60 if not has_files else 300)
                ),
            )
        except aiohttp.ClientConnectorError:
            logger.warning(
                "Network connection error occurred. Retrying in 5 seconds..."
            )
            await asyncio.sleep(5)
            return await self(method, **kwargs)

        if not self.is_running:
            await session.close()

        response_json = await response.json()

        if not response_json["ok"]:
            error = APIException._from_json(response_json)
            self.updates_queue.put_nowait({"e": error, "m": method, "kwargs": kwargs})
            try:
                raise error
            except tgram.errors.FloodWait as f:
                if self.retry_after and (not kwargs.get("retry")):
                    retry_after = (
                        f.value
                        if self.retry_after is True
                        else (
                            min(self.retry_after, f.value)
                        )
                    )
                    logger.warning(
                        "You got FloodWait for %s seconds, I will retry after %s",
                        f.value,
                        retry_after,
                    )
                    await asyncio.sleep(retry_after)
                    return await self(method, {"retry": 1, **kwargs})
            except Exception:
                raise

        return response_json

    def load_plugins(self) -> None:
        """
        Load plugins from the specified plugins directory.
        """
        for path in sorted(self.plugins.rglob("*.py")):
            module_path = ".".join(path.parent.parts + (path.stem,))
            module = import_module(module_path)
            for name in vars(module):
                obj = getattr(module, name)

                if hasattr(obj, "handlers"):
                    for handler, group in obj.handlers:
                        if isinstance(handler, tgram.handlers.Handler) and isinstance(
                            group, int
                        ):
                            self.add_handler(handler, group)

    def customize(self, old: type, new: type) -> Literal[True]:
        """
        Customize a type used by the bot.

        Args:
            old (type): The old type to replace.
            new (type): The new type to use.

        Returns:
            Literal[True]: Always returns True if customization is successful.
        """
        if Type_ not in inspect.getmro(old):
            raise ValueError("You can't customize this type, it's not tgram type.")

        # wrap(new)

        self._custom_types.update({old.__name__: new})

        return True

    @property
    def me(self) -> "tgram.types.User":
        """
        Get the bot's user profile.

        Returns:
            tgram.types.User: The bot's user profile.
        """
        return self._me
