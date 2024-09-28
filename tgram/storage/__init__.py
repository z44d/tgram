from .base import StorageBase
from .kvsqlite_storage import KvsqliteStorage
from .redis_storage import RedisStorage

from . import utils

from tgram import sync

import inspect
import sys

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        sync.wrap(obj)

__all__ = ["StorageBase", "KvsqliteStorage", "RedisStorage", "utils"]
