__all__ = ["types", "TgBot", "handlers", "filters", "idle", "StopPropagation"]
__version__ = "1.10.7"

__author__ = "Zaid"
__copyright__ = "Copyright (C) 2024-present Zaid <https://github.com/2ei>"
__license__ = "MIT"

from . import types, handlers, filters
from .tgbot import TgBot
from .sync import idle

from .errors import StopPropagation
