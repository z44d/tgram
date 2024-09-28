from .client import TgBot
from .dispatcher import Dispatcher

from tgram import sync

import inspect
import sys

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        sync.wrap(obj)

__all__ = ["TgBot", "Dispatcher"]
