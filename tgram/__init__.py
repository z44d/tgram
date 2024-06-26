import aiohttp
import logging
import json

from .methods import TelegramBotMethods
from .decorators import Decorators
from .filters import Filter
from .handlers import Handlers, Handler
from .errors import APIException
from . import types

from typing import List, Callable, Any

__all__ = ["types", "TgBot", "Handlers"]

API_URL = "https://api.telegram.org/"
ALL_UPDATES = [
    getattr(Handlers, i)
    for i in filter(lambda x: not x.startswith("_"), Handlers.__dict__)
]

logger = logging.getLogger(__name__)


class TgBot(TelegramBotMethods, Decorators):
    _session: "aiohttp.ClientSession" = aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(limit=50)
    )
    _handlers: List["Handler"] = []
    _api_url: str = None

    def __init__(
        self, bot_token: str, api_url: str = API_URL, allowed_updates: List[str] = []
    ) -> None:
        self.bot_token = bot_token
        self.api_url = api_url
        self.allowed_updates = allowed_updates

        if not api_url.endswith("/"):
            api_url += "/"

        self._api_url = f"{api_url}bot{bot_token}/"

    def add_handler(
        self, func: Callable, handler: Handlers = None, filters: Filter = None
    ) -> None:
        self._handlers.append(Handler(func, handler, filters))

    async def _new_session(self) -> None:
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=50))
        self._session = session

    async def _get_session(self) -> "aiohttp.ClientSession":
        if self._session.closed:
            await self._new_session()
        elif not self._session.loop.is_running():
            await self._session.close()
            await self._new_session()

        return self._session

    async def _request(self, method: str, **kwargs) -> Any:
        request_url = self._api_url + method
        logger.info("Sending request using the method: %s", method)
        session = await self._get_session()
        data = aiohttp.FormData(quote_fields=False)

        for key, value in kwargs.items():
            if value is None:
                continue
            data.add_field(
                key,
                json.dumps(value._json, ensure_ascii=False)
                if isinstance(value, types.Type_)
                else str(value),
            )

        response = await session.request("POST", request_url, data=data)

        response_json = await response.json()

        if not response_json["ok"]:
            del response_json["ok"]
            raise APIException(json.dumps(response_json))

        return response_json
