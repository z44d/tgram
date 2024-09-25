from .callback_query import CallbackB
from .chat_join_request import ChatJoinRequestB
from .chat_member_updated import ChatMemberUpdatedB
from .chat import ChatB
from .chosen_inline_result import ChosenInlineResultB
from .inline_query import InlineQueryB
from .message import MessageB
from .paid_media_purchased import PaidMediaPurchasedB
from .pre_checkout_query import PreCheckoutQueryB
from .shipping_query import ShippingQueryB
from .user import UserB

from tgram import sync

import inspect
import sys

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        sync.wrap(obj)

__all__ = [
    "CallbackB",
    "ChatJoinRequestB",
    "ChatMemberUpdatedB",
    "ChatB",
    "ChosenInlineResultB",
    "InlineQueryB",
    "MessageB",
    "PaidMediaPurchasedB",
    "PreCheckoutQueryB",
    "ShippingQueryB",
    "UserB",
]
