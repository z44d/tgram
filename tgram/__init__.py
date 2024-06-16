from .methods import Methods
from .decorators import Decorators

from . import types

from typing import List

__all__ = ["types", "TgBot", "Handlers"]


class Handlers:
    MESSAGE = "message"
    EDITED_MESSAGE = "edited_message"
    CHANNEL_POST = "channel_post"
    EDITED_CHANNEL_POST = "edited_channel_post"
    BUSINESS_CONNECTION = "business_connection"
    BUSINESS_MESSAGE = "business_message"
    EDITED_BUSINESS_MESSAGE = "edited_business_message"
    DELETED_BUSINESS_MESSAGES = "deleted_business_messages"
    MESSAGE_REACTION = "message_reaction"
    MESSAGE_REACTION_COUNT = "message_reaction_count"
    INLINE_QUERY = "inline_query"
    CHOSEN_INLINE_RESULT = "chosen_inline_result"
    CALLBACK_QUERY = "callback_query"
    SHIPPING_QUERY = "shipping_query"
    PRE_CHECKOUT_QUERY = "pre_checkout_query"
    POLL = "poll"
    POLL_ANSWER = "poll_answer"
    MY_CHAT_MEMBER = "my_chat_member"
    CHAT_MEMBER = "chat_member"
    CHAT_JOIN_REQUEST = "chat_join_request"
    CHAT_BOOST = "chat_boost"
    REMOVED_CHAT_BOOST = "removed_chat_boost"


API_URL = "https://api.telegram.org/"
ALL_UPDATES = [
    getattr(Handlers, i)
    for i in filter(lambda x: not x.startswith("_"), Handlers.__dict__)
]


class TgBot(Methods, Decorators):
    def __init__(
        self, bot_token: str, api_url: str = API_URL, allowed_updates: List[str] = []
    ) -> None:
        self.bot_token = bot_token
        self.api_url = api_url
        self.allowed_updates = allowed_updates
