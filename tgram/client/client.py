import aiohttp
import asyncio
import logging
import json
import tgram
import os
import io
import ssl
import certifi
import inspect

from ..methods import TelegramBotMethods
from ..decorators import Decorators
from ..errors import APIException
from ..utils import API_URL, get_file_name, ALL_UPDATES
from ..sync import wrap
from ..storage import KvsqliteStorage, RedisStorage, StorageBase
from ..types.type_ import Type_
from .dispatcher import Dispatcher
from concurrent.futures.thread import ThreadPoolExecutor

from typing import List, Any, Literal, Union, Optional
from collections import OrderedDict

from pathlib import Path
from importlib import import_module

from aiohttp.hdrs import USER_AGENT
from aiohttp.http import SERVER_SOFTWARE

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
        executor (ThreadPoolExecutor): Executor for running handler threads.
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
        allowed_updates: List[str] = [],
        link_preview_options: tgram.types.LinkPreviewOptions = None,
        parse_mode: tgram.types.ParseMode = None,
        protect_content: bool = None,
        workers: int = None,
        retry_after: Union[int, bool] = None,
        plugins: Union[Path, str] = None,
        skip_updates: bool = True,
        storage_engine: Union[
            KvsqliteStorage, RedisStorage, Literal["kvsqlite", "redis"]
        ] = None,
        storage_client: Any = None,
    ) -> None:
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
        self.storage: Optional[StorageBase] = None
        self.storage_client = storage_engine

        self.executor = ThreadPoolExecutor(self.workers, thread_name_prefix="Handlers")
        self.loop = asyncio.get_event_loop()

        self.is_running: bool = None
        self._me: "tgram.types.User" = None

        self._listen_handlers: List["tgram.types.Listener"] = []
        self._custom_types: dict = {}
        self._session: "aiohttp.ClientSession" = None

        self.handler_worker_tasks: List["asyncio.Task"] = []
        self.locks_list: List["asyncio.Lock"] = []
        self.updates_queue = asyncio.Queue()
        self.groups = OrderedDict()

        if not api_url.endswith("/"):
            api_url += "/"

        self._api_url: str = f"{api_url}bot{bot_token}/"

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
        if handler.type == "all":
            self.allowed_updates = ALL_UPDATES
        elif handler.type != "exception" and handler.type not in self.allowed_updates:
            self.allowed_updates.append(handler.type)

        self.loop.create_task(self._add_grouped_handler(handler, group))

    def remove_handler(self, handler: "tgram.handlers.Handler", group: int = 0) -> None:
        self.loop.create_task(self._remove_grouped_handler(handler, group))

    async def _new_session(self) -> None:
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
        if self._session is None or self._session.closed:
            await self._new_session()
        elif not self._session.loop.is_running():
            await self._session.close()
            await self._new_session()

        return self._session

    async def _send_request(self, method: str, **kwargs) -> Any:
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
                with open(value, "rb") as f:
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

        response = await session.request(
            "POST" if has_files else "GET",
            request_url,
            data=data,
            timeout=aiohttp.ClientTimeout(
                total=kwargs.get("timeout", 60 if not has_files else 300)
            ),
        )

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
                            f.value if f.value < self.retry_after else self.retry_after
                        )
                    )
                    logger.warning(
                        "You got FloodWait for %s seconds, I will retry after %s",
                        f.value,
                        retry_after,
                    )
                    await asyncio.sleep(retry_after)
                    return await self._send_request(method, {"retry": 1, **kwargs})
            except Exception:
                raise

        return response_json

    def load_plugins(self) -> None:
        for path in sorted(self.plugins.rglob("*.py")):
            module_path = ".".join(path.parent.parts + (path.stem,))
            module = import_module(module_path)
            for name in vars(module).keys():
                obj = getattr(module, name)

                if hasattr(obj, "handlers"):
                    for handler, group in obj.handlers:
                        if isinstance(handler, tgram.handlers.Handler) and isinstance(
                            group, int
                        ):
                            self.add_handler(handler, group)

    def customize(self, old: type, new: type) -> Literal[True]:
        if Type_ not in inspect.getmro(old):
            raise ValueError("You can't customize this type, it's not tgram type.")

        wrap(new)

        self._custom_types.update({old.__name__: new})

        return True

    @property
    def me(self) -> "tgram.types.User":
        if self._me:
            return self._me

        from urllib.request import urlopen

        response = urlopen(self._api_url + "getMe", timeout=60.0)

        response_json = json.loads(response.read().decode("utf-8"))

        if not response_json["ok"]:
            raise APIException._from_json(response)

        self._me = tgram.types.User._parse(self, response_json["result"])

        return self._me


wrap(TelegramBotMethods)
