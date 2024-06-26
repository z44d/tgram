__all__ = ["types", "TgBot", "handlers", "filters", "API_URL", "ALL_UPDATES"]

from . import types, handlers, filters
from .tgbot import TgBot

API_URL = "https://api.telegram.org/"
ALL_UPDATES = [
    getattr(handlers.Handlers, i)
    for i in filter(lambda x: not x.startswith("_"), handlers.Handlers.__dict__)
]
