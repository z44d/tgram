from .on_all import OnAll
from .on_business_connection import OnBusinessConnection
from .on_business_message import OnBusinessMessage
from .on_callback_query import OnCallbackQuery
from .on_channel_post import OnChannelPost
from .on_chat_boost import OnChatBoost
from .on_chat_join_request import OnChatJoinRequest
from .on_chat_member import OnChatMember
from .on_chosen_inline_result import OnChosenInlineResult
from .on_deleted_business_messages import OnDeletedBusinessMessages
from .on_edited_business_message import OnEditedBusinessMessage
from .on_edited_channel_post import OnEditedChannelPost
from .on_edited_message import OnEditedMessage
from .on_inline_query import OnInlineQuery
from .on_message import OnMessage
from .on_message_reaction import OnMessageReaction
from .on_message_reaction_count import OnMessageReactionCount
from .on_my_chat_member import OnMyChatMember
from .on_poll import OnPoll
from .on_poll_answer import OnPollAnswer
from .on_pre_checkout_query import OnPreCheckoutQuery
from .on_purchased_paid_media import OnPurchasedPaidMedia
from .on_removed_chat_boost import OnRemovedChatBoost
from .on_shipping_query import OnShippingQuery


class Decorators(
    OnAll,
    OnBusinessConnection,
    OnBusinessMessage,
    OnCallbackQuery,
    OnChannelPost,
    OnChatBoost,
    OnChatJoinRequest,
    OnChatMember,
    OnChosenInlineResult,
    OnDeletedBusinessMessages,
    OnEditedBusinessMessage,
    OnEditedChannelPost,
    OnEditedMessage,
    OnInlineQuery,
    OnMessage,
    OnMessageReaction,
    OnMessageReactionCount,
    OnMyChatMember,
    OnPoll,
    OnPollAnswer,
    OnPreCheckoutQuery,
    OnPurchasedPaidMedia,
    OnRemovedChatBoost,
    OnShippingQuery,
):
    pass
