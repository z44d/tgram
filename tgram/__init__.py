import aiohttp

from .methods import Methods
from .decorators import Decorators
from .filters import Filter
from .handlers import Handlers, Handler
from . import types

from typing import List, Callable

__all__ = ["types", "TgBot", "Handlers"]

API_URL = "https://api.telegram.org/"
ALL_UPDATES = [
    getattr(Handlers, i)
    for i in filter(lambda x: not x.startswith("_"), Handlers.__dict__)
]


class TgBot(Methods, Decorators):
    _session: "aiohttp.ClientSession" = None
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

    def add_handler(self, func: Callable, handler: Handlers, filters: Filter) -> bool:
        self._handlers.append(Handler(func, handler, filters))
        return True

    async def _new_session(self) -> None:
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=50))
        self._session = session

    async def _get_session(self) -> "aiohttp.ClientSession":
        if self._session is None or self._session.closed:
            await self._new_session()
        elif not self._session.loop.is_running():
            await self._session.close()
            await self._new_session()

        return self._session

    async def _send_request(self, method: str, data: dict):
        request_url = self._api_url + method
        session = await self._get_session()
        # TODO
