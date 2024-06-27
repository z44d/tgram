import aiohttp
import asyncio
import logging
import json
import tgram
import os
import io
import ssl
import certifi

from .methods import TelegramBotMethods
from .decorators import Decorators
from .errors import APIException
from .utils import API_URL
from .sync import wrap
from concurrent.futures.thread import ThreadPoolExecutor

from typing import List, Any, Literal, Callable

from pathlib import Path

logger = logging.getLogger(__name__)


class Dispatcher:
    _is_running = False
    _handlers: List["tgram.handlers.Handler"] = []

    async def run_for_updates(self: "TgBot", skip_updates: bool = True) -> None:
        offset, allowed_updates, limit = (
            -1 if skip_updates else None,
            self.allowed_updates,
            100,
        )
        self._is_running = True

        while self._is_running:
            try:
                updates = await self.get_updates(
                    offset=offset, limit=limit, allowed_updates=allowed_updates
                )
                for update in updates:
                    offset = update.update_id + 1
                    await self._check_update(update)
            except (asyncio.CancelledError, KeyboardInterrupt):
                self._is_running = False
            except Exception as e:
                logger.exception(e)

        session = await self._get_session()
        await session.close()

    async def _check_update(self: "TgBot", update: "tgram.types.Update") -> None:
        for handler in self._handlers:
            if handler.type == "all":
                await self._process_update(update, handler.callback)
            elif (attr := getattr(update, handler.type)) and handler.filter(attr):
                await self._process_update(attr, handler.callback)

    async def _process_update(self: "TgBot", update: Any, callback: Callable) -> None:
        logger.info("Processing update to %s func", callback.__name__)
        try:
            if asyncio.iscoroutinefunction(callback):
                await callback(self, update)
            else:
                await self.loop.run_in_executor(self.executor, callback, self, update)
        except Exception as e:
            logger.exception(e)


class TgBot(TelegramBotMethods, Decorators, Dispatcher):
    _session: "aiohttp.ClientSession" = aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(
            limit=50, ssl_context=ssl.create_default_context(cafile=certifi.where())
        ),
    )
    _api_url: str = None

    def __init__(
        self,
        bot_token: str,
        api_url: str = API_URL,
        allowed_updates: List[str] = [],
        link_preview_options: tgram.types.LinkPreviewOptions = None,
        parse_mode: Literal["Markdown", "MarkdownV2", "HTML"] = None,
        protect_content: bool = None,
        workers: int = None,
    ) -> None:
        self.bot_token = bot_token
        self.api_url = api_url
        self.allowed_updates = allowed_updates
        self.link_preview_options = link_preview_options
        self.parse_mode = parse_mode
        self.protect_content = protect_content
        self.workers = workers or min(32, (os.cpu_count() or 0) + 4)
        self.executor = ThreadPoolExecutor(self.workers, thread_name_prefix="Handlers")
        self.loop = asyncio.get_event_loop()

        if not api_url.endswith("/"):
            api_url += "/"

        self._api_url = f"{api_url}bot{bot_token}/"

    def add_handler(self, handler: "tgram.handlers.Handler") -> None:
        if (t := handler.type != "all") and t not in self.allowed_updates:
            self.allowed_updates.append(t)

        logger.info(
            "(%s) added to %s handlers",
            handler.callback.__name__,
            "Update." + handler.type if handler.type != "all" else "all",
        )
        self._handlers.append(handler)

    async def _new_session(self) -> None:
        session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(
                limit=50, ssl_context=ssl.create_default_context(cafile=certifi.where())
            )
        )
        self._session = session

    async def _get_session(self) -> "aiohttp.ClientSession":
        if self._session.closed:
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
            if value is None or key == "timeout":
                continue
            if isinstance(value, Path):
                has_files = True
                with open(value, "rb") as f:
                    value = f.read()
            elif isinstance(value, io.IOBase):
                has_files = True
                value = value.read()
            elif isinstance(value, bytes):
                has_files = True
            elif isinstance(value, (tgram.types.Type_, list)):
                value = json.dumps(
                    value, ensure_ascii=False, default=tgram.types.Type_.default
                )
            else:
                value = str(value)
            data.add_field(key, value)

        response = await session.request(
            "POST" if has_files else "GET",
            request_url,
            data=data,
            timeout=aiohttp.ClientTimeout(total=kwargs.get("timeout", 60)),
        )

        if not self._is_running:
            await session.close()

        response_json = await response.json()

        if not response_json["ok"]:
            del response_json["ok"]
            raise APIException(json.dumps(response_json))

        return response_json


wrap(Dispatcher)
wrap(TelegramBotMethods)
