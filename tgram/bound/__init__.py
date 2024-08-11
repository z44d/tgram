from .message import MessageB
from .callback_query import CallbackB
from .user import UserB
from .chat import ChatB
from .inline_query import InlineQueryB

from tgram import sync

import inspect
import sys

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        sync.wrap(obj)

__all__ = ["MessageB", "CallbackB", "UserB", "ChatB", "InlineQueryB"]
