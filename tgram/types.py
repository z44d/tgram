import tgram
import random
import logging
from typing import List, Union, Optional, Callable
from pathlib import Path
from json import dumps

from .bound import MessageB, CallbackB, UserB

logger = logging.getLogger(__name__)


class Type_:
    def __init__(self, me: "tgram.TgBot" = None, json: dict = None) -> None:
        self._me = me if isinstance(self, (User, CallbackQuery, Message)) else None
        self._json = json

    @staticmethod
    def default(obj: "Type_"):
        if not isinstance(obj, Type_):
            return repr(obj)

        return {
            "_": obj.__class__.__name__,
            **{
                attr: (getattr(obj, attr))
                for attr in filter(
                    lambda x: not x.startswith("_") and getattr(obj, x) is not None,
                    obj.__dict__,
                )
            },
        }

    def __str__(self) -> str:
        return dumps(self, indent=2, default=Type_.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return "tgram.types.{}({})".format(
            self.__class__.__name__,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in filter(lambda x: not x.startswith("_"), self.__dict__)
                if getattr(self, attr) is not None
            ),
        )

    @staticmethod
    def _custom_parse(a: "Type_", b: type) -> type:
        try:
            obj = b()
            for attr in filter(
                lambda x: not x.startswith("_"),
                dir(a),
            ):
                setattr(obj, getattr(a, attr))
            return obj
        except Exception as e:
            logger.warn(
                "You got an error (%s) (The original type returned) when the bot trying to give you custom type, make sure you are doing it in right way, see the example here %s",
                str(e),
                "https://github.com/2ei/tgram/blob/main/examples/custom_types.py",
            )
            return a


class Listener(Type_):
    def __init__(
        self,
        update_type: str,
        next_step: Callable,
        data: dict,
        cancel: Callable = None,
        filters: "tgram.filters.Filter" = None,
    ) -> None:
        super().__init__(None, None)
        self.update_type = update_type
        self.next_step = next_step
        self.data = data
        self.cancel = cancel
        self.filters = filters


class Update(Type_):
    """
    This object represents an incoming update.At most one of the optional parameters can be present in any given update.

    Telegram Documentation: https://core.telegram.org/bots/api#update

    :param update_id: The update's unique identifier. Update identifiers start from a certain positive number and
        increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore
        repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates
        for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    :type update_id: :obj:`int`

    :param message: Optional. New incoming message of any kind - text, photo, sticker, etc.
    :type message: :class:`tgram.types.Message`

    :param edited_message: Optional. New version of a message that is known to the bot and was edited
    :type edited_message: :class:`tgram.types.Message`

    :param channel_post: Optional. New incoming channel post of any kind - text, photo, sticker, etc.
    :type channel_post: :class:`tgram.types.Message`

    :param edited_channel_post: Optional. New version of a channel post that is known to the bot and was edited
    :type edited_channel_post: :class:`tgram.types.Message`

    :param message_reaction: Optional. A reaction to a message was changed by a user. The bot must be an administrator in the chat
        and must explicitly specify "message_reaction" in the list of allowed_updates to receive these updates. The update isn't received for reactions set by bots.
    :type message_reaction: :class:`tgram.types.MessageReactionUpdated`

    :param message_reaction_count: Optional. Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify
        "message_reaction_count" in the list of allowed_updates to receive these updates.
    :type message_reaction_count: :class:`tgram.types.MessageReactionCountUpdated`

    :param inline_query: Optional. New incoming inline query
    :type inline_query: :class:`tgram.types.InlineQuery`

    :param chosen_inline_result: Optional. The result of an inline query that was chosen by a user and sent to their chat
        partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your
        bot.
    :type chosen_inline_result: :class:`tgram.types.ChosenInlineResult`

    :param callback_query: Optional. New incoming callback query
    :type callback_query: :class:`tgram.types.CallbackQuery`

    :param shipping_query: Optional. New incoming shipping query. Only for invoices with flexible price
    :type shipping_query: :class:`tgram.types.ShippingQuery`

    :param pre_checkout_query: Optional. New incoming pre-checkout query. Contains full information about
        checkout
    :type pre_checkout_query: :class:`tgram.types.PreCheckoutQuery`

    :param poll: Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the
        bot
    :type poll: :class:`tgram.types.Poll`

    :param poll_answer: Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in
        polls that were sent by the bot itself.
    :type poll_answer: :class:`tgram.types.PollAnswer`

    :param my_chat_member: Optional. The bot's chat member status was updated in a chat. For private chats, this update
        is received only when the bot is blocked or unblocked by the user.
    :type my_chat_member: :class:`tgram.types.ChatMemberUpdated`

    :param chat_member: Optional. A chat member's status was updated in a chat. The bot must be an administrator in the
        chat and must explicitly specify “chat_member” in the list of allowed_updates to receive these updates.
    :type chat_member: :class:`tgram.types.ChatMemberUpdated`

    :param chat_join_request: Optional. A request to join the chat has been sent. The bot must have the
        can_invite_users administrator right in the chat to receive these updates.
    :type chat_join_request: :class:`tgram.types.ChatJoinRequest`

    :param chat_boost: Optional. A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates.
    :type chat_boost: :class:`tgram.types.ChatBoostUpdated`

    :param removed_chat_boost: Optional. A chat boost was removed. The bot must be an administrator in the chat to receive these updates.
    :type removed_chat_boost: :class:`tgram.types.RemovedChatBoost`

    :param business_connection: Optional. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot
    :type business_connection: :class:`tgram.types.BusinessConnection`

    :param business_message: Optional. New non-service message from a connected business account
    :type business_message: :class:`tgram.types.Message`

    :param edited_business_message: Optional. New version of a non-service message from a connected business account that is known to the bot and was edited
    :type edited_business_message: :class:`tgram.types.Message`

    :param deleted_business_messages: Optional. Service message: the chat connected to the business account was deleted
    :type deleted_business_messages: :class:`tgram.types.BusinessMessagesDeleted`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Update`

    """

    def __init__(
        self,
        update_id: "int",
        message: "Message" = None,
        edited_message: "Message" = None,
        channel_post: "Message" = None,
        edited_channel_post: "Message" = None,
        business_connection: "BusinessConnection" = None,
        business_message: "Message" = None,
        edited_business_message: "Message" = None,
        deleted_business_messages: "BusinessMessagesDeleted" = None,
        message_reaction: "MessageReactionUpdated" = None,
        message_reaction_count: "MessageReactionCountUpdated" = None,
        inline_query: "InlineQuery" = None,
        chosen_inline_result: "ChosenInlineResult" = None,
        callback_query: "CallbackQuery" = None,
        shipping_query: "ShippingQuery" = None,
        pre_checkout_query: "PreCheckoutQuery" = None,
        poll: "Poll" = None,
        poll_answer: "PollAnswer" = None,
        my_chat_member: "ChatMemberUpdated" = None,
        chat_member: "ChatMemberUpdated" = None,
        chat_join_request: "ChatJoinRequest" = None,
        chat_boost: "ChatBoostUpdated" = None,
        removed_chat_boost: "ChatBoostRemoved" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.business_connection = business_connection
        self.business_message = business_message
        self.edited_business_message = edited_business_message
        self.deleted_business_messages = deleted_business_messages
        self.message_reaction = message_reaction
        self.message_reaction_count = message_reaction_count
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request
        self.chat_boost = chat_boost
        self.removed_chat_boost = removed_chat_boost

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Update"]:
        return (
            Update(
                me=me,
                json=d,
                update_id=d.get("update_id"),
                message=Message._parse(me=me, d=d.get("message")),
                edited_message=Message._parse(me=me, d=d.get("edited_message")),
                channel_post=Message._parse(me=me, d=d.get("channel_post")),
                edited_channel_post=Message._parse(
                    me=me, d=d.get("edited_channel_post")
                ),
                business_connection=BusinessConnection._parse(
                    me=me, d=d.get("business_connection")
                ),
                business_message=Message._parse(me=me, d=d.get("business_message")),
                edited_business_message=Message._parse(
                    me=me, d=d.get("edited_business_message")
                ),
                deleted_business_messages=BusinessMessagesDeleted._parse(
                    me=me, d=d.get("deleted_business_messages")
                ),
                message_reaction=MessageReactionUpdated._parse(
                    me=me, d=d.get("message_reaction")
                ),
                message_reaction_count=MessageReactionCountUpdated._parse(
                    me=me, d=d.get("message_reaction_count")
                ),
                inline_query=InlineQuery._parse(me=me, d=d.get("inline_query")),
                chosen_inline_result=ChosenInlineResult._parse(
                    me=me, d=d.get("chosen_inline_result")
                ),
                callback_query=CallbackQuery._parse(me=me, d=d.get("callback_query")),
                shipping_query=ShippingQuery._parse(me=me, d=d.get("shipping_query")),
                pre_checkout_query=PreCheckoutQuery._parse(
                    me=me, d=d.get("pre_checkout_query")
                ),
                poll=Poll._parse(me=me, d=d.get("poll")),
                poll_answer=PollAnswer._parse(me=me, d=d.get("poll_answer")),
                my_chat_member=ChatMemberUpdated._parse(
                    me=me, d=d.get("my_chat_member")
                ),
                chat_member=ChatMemberUpdated._parse(me=me, d=d.get("chat_member")),
                chat_join_request=ChatJoinRequest._parse(
                    me=me, d=d.get("chat_join_request")
                ),
                chat_boost=ChatBoostUpdated._parse(me=me, d=d.get("chat_boost")),
                removed_chat_boost=ChatBoostRemoved._parse(
                    me=me, d=d.get("removed_chat_boost")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class WebhookInfo(Type_):
    """
    Describes the current status of a webhook.

    Telegram Documentation: https://core.telegram.org/bots/api#webhookinfo

    :param url: Webhook URL, may be empty if webhook is not set up
    :type url: :obj:`str`

    :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
    :type has_custom_certificate: :obj:`bool`

    :param pending_update_count: Number of updates awaiting delivery
    :type pending_update_count: :obj:`int`

    :param ip_address: Optional. Currently used webhook IP address
    :type ip_address: :obj:`str`

    :param last_error_date: Optional. Unix time for the most recent error that happened when trying to deliver an
        update via webhook
    :type last_error_date: :obj:`int`

    :param last_error_message: Optional. Error message in human-readable format for the most recent error that
        happened when trying to deliver an update via webhook
    :type last_error_message: :obj:`str`

    :param last_synchronization_error_date: Optional. Unix time of the most recent error that happened when trying
        to synchronize available updates with Telegram datacenters
    :type last_synchronization_error_date: :obj:`int`

    :param max_connections: Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook
        for update delivery
    :type max_connections: :obj:`int`

    :param allowed_updates: Optional. A list of update types the bot is subscribed to. Defaults to all update types
        except chat_member
    :type allowed_updates: :obj:`list` of :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.WebhookInfo`
    """

    def __init__(
        self,
        url: "str",
        has_custom_certificate: "bool",
        pending_update_count: "int",
        ip_address: "str" = None,
        last_error_date: "int" = None,
        last_error_message: "str" = None,
        last_synchronization_error_date: "int" = None,
        max_connections: "int" = None,
        allowed_updates: List["str"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.last_synchronization_error_date = last_synchronization_error_date
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["WebhookInfo"]:
        return (
            WebhookInfo(
                me=me,
                json=d,
                url=d.get("url"),
                has_custom_certificate=d.get("has_custom_certificate"),
                pending_update_count=d.get("pending_update_count"),
                ip_address=d.get("ip_address"),
                last_error_date=d.get("last_error_date"),
                last_error_message=d.get("last_error_message"),
                last_synchronization_error_date=d.get(
                    "last_synchronization_error_date"
                ),
                max_connections=d.get("max_connections"),
                allowed_updates=d.get("allowed_updates"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class User(Type_, UserB):
    """
    This object represents a Telegram user or bot.

    Telegram Documentation: https://core.telegram.org/bots/api#user

    :param id: Unique identifier for this user or bot. This number may have more than 32 significant bits and some
        programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant
        bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type id: :obj:`int`

    :param is_bot: True, if this user is a bot
    :type is_bot: :obj:`bool`

    :param first_name: User's or bot's first name
    :type first_name: :obj:`str`

    :param last_name: Optional. User's or bot's last name
    :type last_name: :obj:`str`

    :param username: Optional. User's or bot's username
    :type username: :obj:`str`

    :param language_code: Optional. IETF language tag of the user's language
    :type language_code: :obj:`str`

    :param is_premium: Optional. :obj:`bool`, if this user is a Telegram Premium user
    :type is_premium: :obj:`bool`

    :param added_to_attachment_menu: Optional. :obj:`bool`, if this user added the bot to the attachment menu
    :type added_to_attachment_menu: :obj:`bool`

    :param can_join_groups: Optional. True, if the bot can be invited to groups. Returned only in getMe.
    :type can_join_groups: :obj:`bool`

    :param can_read_all_group_messages: Optional. True, if privacy mode is disabled for the bot. Returned only in
        getMe.
    :type can_read_all_group_messages: :obj:`bool`

    :param supports_inline_queries: Optional. True, if the bot supports inline queries. Returned only in getMe.
    :type supports_inline_queries: :obj:`bool`

    :param can_connect_to_business: Optional. True, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in getMe.
    :type can_connect_to_business: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.User`
    """

    def __init__(
        self,
        id: "int",
        is_bot: "bool",
        first_name: "str",
        last_name: "str" = None,
        username: "str" = None,
        language_code: "str" = None,
        is_premium: "bool" = None,
        added_to_attachment_menu: "bool" = None,
        can_join_groups: "bool" = None,
        can_read_all_group_messages: "bool" = None,
        supports_inline_queries: "bool" = None,
        can_connect_to_business: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
        self.can_connect_to_business = can_connect_to_business

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["User"]:
        return (
            User(
                me=me,
                json=d,
                id=d.get("id"),
                is_bot=d.get("is_bot"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                language_code=d.get("language_code"),
                is_premium=d.get("is_premium"),
                added_to_attachment_menu=d.get("added_to_attachment_menu"),
                can_join_groups=d.get("can_join_groups"),
                can_read_all_group_messages=d.get("can_read_all_group_messages"),
                supports_inline_queries=d.get("supports_inline_queries"),
                can_connect_to_business=d.get("can_connect_to_business"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Chat(Type_):
    """
    In BotAPI 7.3 Chat was reduced and full info moved to ChatFullInfo:
    "Split out the class ChatFullInfo from the class Chat and changed the return type of the method getChat to ChatFullInfo."

    https://core.telegram.org/bots/api#chatfullinfo

    Currently Chat is left as full copy of ChatFullInfo for compatibility.
    """

    def __init__(
        self,
        id: "int",
        type: "str",
        title: "str" = None,
        username: "str" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        is_forum: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Chat"]:
        return (
            Chat(
                me=me,
                json=d,
                id=d.get("id"),
                type=d.get("type"),
                title=d.get("title"),
                username=d.get("username"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                is_forum=d.get("is_forum"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatFullInfo(Type_):
    """
    This object represents a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chat

    :param id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming
        languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed
        64-bit integer or double-precision float type are safe for storing this identifier.
    :type id: :obj:`int`

    :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    :type type: :obj:`str`

    :param title: Optional. Title, for supergroups, channels and group chats
    :type title: :obj:`str`

    :param username: Optional. Username, for private chats, supergroups and channels if available
    :type username: :obj:`str`

    :param first_name: Optional. First name of the other party in a private chat
    :type first_name: :obj:`str`

    :param last_name: Optional. Last name of the other party in a private chat
    :type last_name: :obj:`str`

    :param is_forum: Optional. True, if the supergroup chat is a forum (has topics enabled)
    :type is_forum: :obj:`bool`

    :param max_reaction_count: Optional. The maximum number of reactions that can be set on a message in the chat
    :type max_reaction_count: :obj:`int`

    :param photo: Optional. Chat photo. Returned only in getChat.
    :type photo: :class:`tgram.types.ChatPhoto`

    :param active_usernames: Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels. Returned only in getChat.
    :type active_usernames: :obj:`list` of :obj:`str`

    :param birthdate: Optional. Birthdate of the other party in a private chat. Returned only in getChat.
    :type birthdate: :obj:`str`

    :param business_intro: Optional. Business intro for the chat. Returned only in getChat.
    :type business_intro: :class:`tgram.types.BusinessIntro`

    :param business_location: Optional. Business location for the chat. Returned only in getChat.
    :type business_location: :class:`tgram.types.BusinessLocation`

    :param business_opening_hours : Optional. Business opening hours for the chat. Returned only in getChat.
    :type business_opening_hours: :class:`tgram.types.BusinessHours`

    :param personal_chat: Optional. For private chats, the personal channel of the user. Returned only in getChat.
    :type personal_chat: :class:`tgram.types.Chat`

    :param available_reactions: Optional. List of available chat reactions; for private chats, supergroups and channels. Returned only in getChat.
    :type available_reactions: :obj:`list` of :class:`tgram.types.ReactionType`

    :param accent_color_id: Optional. Optional. Identifier of the accent color for the chat name and backgrounds of the chat photo,
        reply header, and link preview. See accent colors for more details. Returned only in getChat. Always returned in getChat.
    :type accent_color_id: :obj:`int`

    :param background_custom_emoji_id: Optional. Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background. Returned only in getChat.
    :type background_custom_emoji_id: :obj:`str`

    :param profile_accent_color_id: Optional. Identifier of the accent color for the chat's profile background. See profile accent colors for more details. Returned only in getChat.
    :type profile_accent_color_id: :obj:`int`

    :param profile_background_custom_emoji_id: Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background. Returned only in getChat.
    :type profile_background_custom_emoji_id: :obj:`str`

    :param emoji_status_custom_emoji_id: Optional. Custom emoji identifier of emoji status of the other party in a private chat. Returned only in getChat.
    :type emoji_status_custom_emoji_id: :obj:`str`

    :param emoji_status_expiration_date: Optional. Expiration date of the emoji status of the other party in a private chat, if any. Returned only in getChat.
    :type emoji_status_expiration_date: :obj:`int`

    :param bio: Optional. Bio of the other party in a private chat. Returned only in getChat.
    :type bio: :obj:`str`

    :param has_private_forwards: Optional. :obj:`bool`, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.
    :type has_private_forwards: :obj:`bool`

    :param has_restricted_voice_and_video_messages: Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat.
    :type :obj:`bool`

    :param join_to_send_messages: Optional. :obj:`bool`, if users need to join the supergroup before they can send messages. Returned only in getChat.
    :type join_to_send_messages: :obj:`bool`

    :param join_by_request: Optional. :obj:`bool`, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat.
    :type join_by_request: :obj:`bool`

    :param description: Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
    :type description: :obj:`str`

    :param invite_link: Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
    :type invite_link: :obj:`str`

    :param pinned_message: Optional. The most recent pinned message (by sending date). Returned only in getChat.
    :type pinned_message: :class:`tgram.types.Message`

    :param permissions: Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
    :type permissions: :class:`tgram.types.ChatPermissions`

    :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat.
    :type slow_mode_delay: :obj:`int`

    :param unrestrict_boost_count: Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions. Returned only in getChat.
    :type unrestrict_boost_count: :obj:`int`

    :param message_auto_delete_time: Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
    :type message_auto_delete_time: :obj:`int`

    :param has_aggressive_anti_spam_enabled: Optional. :obj:`bool`, if the chat has enabled aggressive anti-spam protection. Returned only in getChat.
    :type has_aggressive_anti_spam_enabled: :obj:`bool`

    :param has_hidden_members: Optional. :obj:`bool`, if the chat has enabled hidden members. Returned only in getChat.
    :type has_hidden_members: :obj:`bool`

    :param has_protected_content: Optional. :obj:`bool`, if messages from the chat can't be forwarded to other chats. Returned only in getChat.
    :type has_protected_content: :obj:`bool`

    :param has_visible_history: Optional. True, if new chat members will have access to old messages; available only to chat administrators. Returned only in getChat.
    :type has_visible_history: :obj:`bool`

    :param sticker_set_name: Optional. For supergroups, name of group sticker set. Returned only in getChat.
    :type sticker_set_name: :obj:`str`

    :param can_set_sticker_set: Optional. :obj:`bool`, if the bot can change the group sticker set. Returned only in getChat.
    :type can_set_sticker_set: :obj:`bool`

    :param custom_emoji_sticker_set_name: Optional. For supergroups, the name of the group's custom emoji sticker set.
        Custom emoji from this set can be used by all users and bots in the group. Returned only in getChat.
    :param custom_emoji_sticker_set_name: :obj:`str`

    :param linked_chat_id: Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for
        a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some
        programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a
        signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
    :type linked_chat_id: :obj:`int`

    :param location: Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat.
    :type location: :class:`tgram.types.ChatLocation`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatFullInfo`
    """

    def __init__(
        self,
        id: "int",
        type: "str",
        accent_color_id: "int",
        max_reaction_count: "int",
        title: "str" = None,
        username: "str" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        is_forum: "bool" = None,
        photo: "ChatPhoto" = None,
        active_usernames: List["str"] = None,
        birthdate: "Birthdate" = None,
        business_intro: "BusinessIntro" = None,
        business_location: "BusinessLocation" = None,
        business_opening_hours: "BusinessOpeningHours" = None,
        personal_chat: "Chat" = None,
        available_reactions: List["ReactionType"] = None,
        background_custom_emoji_id: "str" = None,
        profile_accent_color_id: "int" = None,
        profile_background_custom_emoji_id: "str" = None,
        emoji_status_custom_emoji_id: "str" = None,
        emoji_status_expiration_date: "int" = None,
        bio: "str" = None,
        has_private_forwards: "bool" = None,
        has_restricted_voice_and_video_messages: "bool" = None,
        join_to_send_messages: "bool" = None,
        join_by_request: "bool" = None,
        description: "str" = None,
        invite_link: "str" = None,
        pinned_message: "Message" = None,
        permissions: "ChatPermissions" = None,
        can_send_paid_media: bool = None,
        slow_mode_delay: "int" = None,
        unrestrict_boost_count: "int" = None,
        message_auto_delete_time: "int" = None,
        has_aggressive_anti_spam_enabled: "bool" = None,
        has_hidden_members: "bool" = None,
        has_protected_content: "bool" = None,
        has_visible_history: "bool" = None,
        sticker_set_name: "str" = None,
        can_set_sticker_set: "bool" = None,
        custom_emoji_sticker_set_name: "str" = None,
        linked_chat_id: "int" = None,
        location: "ChatLocation" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.accent_color_id = accent_color_id
        self.max_reaction_count = max_reaction_count
        self.photo = photo
        self.active_usernames = active_usernames
        self.birthdate = birthdate
        self.business_intro = business_intro
        self.business_location = business_location
        self.business_opening_hours = business_opening_hours
        self.personal_chat = personal_chat
        self.available_reactions = available_reactions
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = (
            has_restricted_voice_and_video_messages
        )
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.can_send_paid_media = can_send_paid_media
        self.slow_mode_delay = slow_mode_delay
        self.unrestrict_boost_count = unrestrict_boost_count
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.linked_chat_id = linked_chat_id
        self.location = location

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatFullInfo"]:
        return (
            ChatFullInfo(
                me=me,
                json=d,
                id=d.get("id"),
                type=d.get("type"),
                accent_color_id=d.get("accent_color_id"),
                max_reaction_count=d.get("max_reaction_count"),
                title=d.get("title"),
                username=d.get("username"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                is_forum=d.get("is_forum"),
                photo=ChatPhoto._parse(me=me, d=d.get("photo")),
                active_usernames=d.get("active_usernames"),
                birthdate=Birthdate._parse(me=me, d=d.get("birthdate")),
                business_intro=BusinessIntro._parse(me=me, d=d.get("business_intro")),
                business_location=BusinessLocation._parse(
                    me=me, d=d.get("business_location")
                ),
                business_opening_hours=BusinessOpeningHours._parse(
                    me=me, d=d.get("business_opening_hours")
                ),
                personal_chat=Chat._parse(me=me, d=d.get("personal_chat")),
                available_reactions=[
                    ReactionType._parse(me=me, d=i)
                    for i in d.get("available_reactions")
                ]
                if d.get("available_reactions")
                else None,
                background_custom_emoji_id=d.get("background_custom_emoji_id"),
                profile_accent_color_id=d.get("profile_accent_color_id"),
                profile_background_custom_emoji_id=d.get(
                    "profile_background_custom_emoji_id"
                ),
                emoji_status_custom_emoji_id=d.get("emoji_status_custom_emoji_id"),
                emoji_status_expiration_date=d.get("emoji_status_expiration_date"),
                bio=d.get("bio"),
                has_private_forwards=d.get("has_private_forwards"),
                has_restricted_voice_and_video_messages=d.get(
                    "has_restricted_voice_and_video_messages"
                ),
                join_to_send_messages=d.get("join_to_send_messages"),
                join_by_request=d.get("join_by_request"),
                description=d.get("description"),
                invite_link=d.get("invite_link"),
                pinned_message=Message._parse(me=me, d=d.get("pinned_message")),
                permissions=ChatPermissions._parse(me=me, d=d.get("permissions")),
                can_send_paid_media=d.get("can_send_paid_media"),
                slow_mode_delay=d.get("slow_mode_delay"),
                unrestrict_boost_count=d.get("unrestrict_boost_count"),
                message_auto_delete_time=d.get("message_auto_delete_time"),
                has_aggressive_anti_spam_enabled=d.get(
                    "has_aggressive_anti_spam_enabled"
                ),
                has_hidden_members=d.get("has_hidden_members"),
                has_protected_content=d.get("has_protected_content"),
                has_visible_history=d.get("has_visible_history"),
                sticker_set_name=d.get("sticker_set_name"),
                can_set_sticker_set=d.get("can_set_sticker_set"),
                custom_emoji_sticker_set_name=d.get("custom_emoji_sticker_set_name"),
                linked_chat_id=d.get("linked_chat_id"),
                location=ChatLocation._parse(me=me, d=d.get("location")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Message(Type_, MessageB):
    """
    This object represents a message.

    Telegram Documentation: https://core.telegram.org/bots/api#message

    :param message_id: Unique message identifier inside this chat
    :type message_id: :obj:`int`

    :param message_thread_id: Optional. Unique identifier of a message thread to which the message belongs; for supergroups only
    :type message_thread_id: :obj:`int`

    :param from_user: Optional. Sender of the message; empty for messages sent to channels. For backward compatibility, the
        field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    :type from_user: :class:`tgram.types.User`

    :param sender_chat: Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself for
        channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for
        messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a
        fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    :type sender_chat: :class:`tgram.types.Chat`

    :param sender_boost_count: Optional. If the sender of the message boosted the chat, the number of boosts added by the user
    :type sender_boost_count: :obj:`int`

    :param sender_business_bot info: Optional. Information about the business bot that sent the message
    :type sender_business_bot_info: :class:`tgram.types.User`

    :param date: Date the message was sent in Unix time
    :type date: :obj:`int`

    :param business_connection_id: Optional. Unique identifier of the business connection from which the message was received. If non-empty,
        the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.
    :type business_connection_id: :obj:`str`

    :param chat: Conversation the message belongs to
    :type chat: :class:`tgram.types.Chat`

    :forward_origin: Optional. For forwarded messages, information about the original message;
    :type forward_origin: :class:`tgram.types.MessageOrigin`

    :param is_topic_message: Optional. True, if the message is sent to a forum topic
    :type is_topic_message: :obj:`bool`

    :param is_automatic_forward: Optional. :obj:`bool`, if the message is a channel post that was automatically
        forwarded to the connected discussion group
    :type is_automatic_forward: :obj:`bool`

    :param reply_to_message: Optional. For replies, the original message. Note that the Message object in this field
        will not contain further reply_to_message fields even if it itself is a reply.
    :type reply_to_message: :class:`tgram.types.Message`

    :param external_reply: Optional. Information about the message that is being replied to, which may come from another chat or forum topic
    :type external_reply: :class:`tgram.types.ExternalReplyInfo`

    :param quote: Optional. For replies that quote part of the original message, the quoted part of the message
    :type quote: :class:`tgram.types.TextQuote`

    :param reply_to_story: Optional. For replies to a story, the original story
    :type reply_to_story: :class:`tgram.types.Story`

    :param via_bot: Optional. Bot through which the message was sent
    :type via_bot: :class:`tgram.types.User`

    :param edit_date: Optional. Date the message was last edited in Unix time
    :type edit_date: :obj:`int`

    :param has_protected_content: Optional. :obj:`bool`, if the message can't be forwarded
    :type has_protected_content: :obj:`bool`

    :param is_from_offline: Optional. True, if the message was sent by an implicit action, for example,
        as an away or a greeting business message, or as a scheduled message
    :type is_from_offline: :obj:`bool`

    :param media_group_id: Optional. The unique identifier of a media message group this message belongs to
    :type media_group_id: :obj:`str`

    :param author_signature: Optional. Signature of the post author for messages in channels, or the custom title of an
        anonymous group administrator
    :type author_signature: :obj:`str`

    :param text: Optional. For text messages, the actual UTF-8 text of the message
    :type text: :obj:`str`

    :param entities: Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that
        appear in the text
    :type entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param link_preview_options: Optional. Options used for link preview generation for the message,
        if it is a text message and link preview options were changed
    :type link_preview_options: :class:`tgram.types.LinkPreviewOptions`

    :param effect_id: Optional. Unique identifier of the message effect added to the message
    :type effect_id: :obj:`str`

    :param animation: Optional. Message is an animation, information about the animation. For backward
        compatibility, when this field is set, the document field will also be set
    :type animation: :class:`tgram.types.Animation`

    :param audio: Optional. Message is an audio file, information about the file
    :type audio: :class:`tgram.types.Audio`

    :param document: Optional. Message is a general file, information about the file
    :type document: :class:`tgram.types.Document`

    :param photo: Optional. Message is a photo, available sizes of the photo
    :type photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param sticker: Optional. Message is a sticker, information about the sticker
    :type sticker: :class:`tgram.types.Sticker`

    :param story: Optional. Message is a forwarded story
    :type story: :class:`tgram.types.Story`

    :param video: Optional. Message is a video, information about the video
    :type video: :class:`tgram.types.Video`

    :param video_note: Optional. Message is a video note, information about the video message
    :type video_note: :class:`tgram.types.VideoNote`

    :param voice: Optional. Message is a voice message, information about the file
    :type voice: :class:`tgram.types.Voice`

    :param caption: Optional. Caption for the animation, audio, document, photo, video or voice
    :type caption: :obj:`str`

    :param caption_entities: Optional. For messages with a caption, special entities like usernames, URLs, bot
        commands, etc. that appear in the caption
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param show_caption_above_media: Optional. True, if the caption must be shown above the message media
    :type show_caption_above_media: :obj:`bool`

    :param has_media_spoiler: Optional. True, if the message media is covered by a spoiler animation
    :type has_media_spoiler: :obj:`bool`

    :param contact: Optional. Message is a shared contact, information about the contact
    :type contact: :class:`tgram.types.Contact`

    :param dice: Optional. Message is a dice with random value
    :type dice: :class:`tgram.types.Dice`

    :param game: Optional. Message is a game, information about the game. More about games »
    :type game: :class:`tgram.types.Game`

    :param poll: Optional. Message is a native poll, information about the poll
    :type poll: :class:`tgram.types.Poll`

    :param venue: Optional. Message is a venue, information about the venue. For backward compatibility, when this
        field is set, the location field will also be set
    :type venue: :class:`tgram.types.Venue`

    :param location: Optional. Message is a shared location, information about the location
    :type location: :class:`tgram.types.Location`

    :param new_chat_members: Optional. New members that were added to the group or supergroup and information about
        them (the bot itself may be one of these members)
    :type new_chat_members: :obj:`list` of :class:`tgram.types.User`

    :param left_chat_member: Optional. A member was removed from the group, information about them (this member may be
        the bot itself)
    :type left_chat_member: :class:`tgram.types.User`

    :param new_chat_title: Optional. A chat title was changed to this value
    :type new_chat_title: :obj:`str`

    :param new_chat_photo: Optional. A chat photo was change to this value
    :type new_chat_photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param delete_chat_photo: Optional. Service message: the chat photo was deleted
    :type delete_chat_photo: :obj:`bool`

    :param group_chat_created: Optional. Service message: the group has been created
    :type group_chat_created: :obj:`bool`

    :param supergroup_chat_created: Optional. Service message: the supergroup has been created. This field can't be
        received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can
        only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    :type supergroup_chat_created: :obj:`bool`

    :param channel_chat_created: Optional. Service message: the channel has been created. This field can't be
        received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only
        be found in reply_to_message if someone replies to a very first message in a channel.
    :type channel_chat_created: :obj:`bool`

    :param message_auto_delete_timer_changed: Optional. Service message: auto-delete timer settings changed in
        the chat
    :type message_auto_delete_timer_changed: :class:`tgram.types.MessageAutoDeleteTimerChanged`

    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier.
        This number may have more than 32 significant bits and some programming languages may have difficulty/silent
        defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision
        float type are safe for storing this identifier.
    :type migrate_to_chat_id: :obj:`int`

    :param migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified
        identifier. This number may have more than 32 significant bits and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this identifier.
    :type migrate_from_chat_id: :obj:`int`

    :param pinned_message: Optional. Specified message was pinned. Note that the Message object in this field will not
        contain further reply_to_message fields even if it is itself a reply.
    :type pinned_message: :class:`tgram.types.Message` or :class:`tgram.types.InaccessibleMessage`

    :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More about payments »
    :type invoice: :class:`tgram.types.Invoice`

    :param successful_payment: Optional. Message is a service message about a successful payment, information about
        the payment. More about payments »
    :type successful_payment: :class:`tgram.types.SuccessfulPayment`

    :param users_shared: Optional. Service message: a user was shared with the bot
    :type users_shared: :class:`tgram.types.UsersShared`

    :param chat_shared: Optional. Service message: a chat was shared with the bot
    :type chat_shared: :class:`tgram.types.ChatShared`

    :param connected_website: Optional. The domain name of the website on which the user has logged in. More about
        Telegram Login »
    :type connected_website: :obj:`str`

    :param write_access_allowed: Optional. Service message: the user allowed the bot added to the attachment
        menu to write messages
    :type write_access_allowed: :class:`tgram.types.WriteAccessAllowed`

    :param passport_data: Optional. Telegram Passport data
    :type passport_data: :class:`tgram.types.PassportData`

    :param proximity_alert_triggered: Optional. Service message. A user in the chat triggered another user's
        proximity alert while sharing Live Location.
    :type proximity_alert_triggered: :class:`tgram.types.ProximityAlertTriggered`

    :param boost_added: Optional. Service message: user boosted the chat
    :type boost_added: :class:`tgram.types.ChatBoostAdded`

    :param chat_background_set: Optional. Service message: chat background set
    :type chat_background_set: :class:`tgram.types.ChatBackground`

    :param forum_topic_created: Optional. Service message: forum topic created
    :type forum_topic_created: :class:`tgram.types.ForumTopicCreated`

    :param forum_topic_edited: Optional. Service message: forum topic edited
    :type forum_topic_edited: :class:`tgram.types.ForumTopicEdited`

    :param forum_topic_closed: Optional. Service message: forum topic closed
    :type forum_topic_closed: :class:`tgram.types.ForumTopicClosed`

    :param forum_topic_reopened: Optional. Service message: forum topic reopened
    :type forum_topic_reopened: :class:`tgram.types.ForumTopicReopened`

    :param general_forum_topic_hidden: Optional. Service message: the 'General' forum topic hidden
    :type general_forum_topic_hidden: :class:`tgram.types.GeneralForumTopicHidden`

    :param general_forum_topic_unhidden: Optional. Service message: the 'General' forum topic unhidden
    :type general_forum_topic_unhidden: :class:`tgram.types.GeneralForumTopicUnhidden`

    :param giveaway_created: Optional. Service message: a giveaway has been created
    :type giveaway_created: :class:`tgram.types.GiveawayCreated`

    :param giveaway: Optional. The message is a scheduled giveaway message
    :type giveaway: :class:`tgram.types.Giveaway`

    :param giveaway_winners: Optional. Service message: giveaway winners(public winners)
    :type giveaway_winners: :class:`tgram.types.GiveawayWinners`

    :param giveaway_completed: Optional. Service message: giveaway completed, without public winners
    :type giveaway_completed: :class:`tgram.types.GiveawayCompleted`

    :param video_chat_scheduled: Optional. Service message: video chat scheduled
    :type video_chat_scheduled: :class:`tgram.types.VideoChatScheduled`

    :param video_chat_started: Optional. Service message: video chat started
    :type video_chat_started: :class:`tgram.types.VideoChatStarted`

    :param video_chat_ended: Optional. Service message: video chat ended
    :type video_chat_ended: :class:`tgram.types.VideoChatEnded`

    :param video_chat_participants_invited: Optional. Service message: new participants invited to a video chat
    :type video_chat_participants_invited: :class:`tgram.types.VideoChatParticipantsInvited`

    :param web_app_data: Optional. Service message: data sent by a Web App
    :type web_app_data: :class:`tgram.types.WebAppData`

    :param reply_markup: Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Message`
    """

    def __init__(
        self,
        message_id: "int",
        date: "int",
        chat: "Chat",
        message_thread_id: "int" = None,
        from_user: "User" = None,
        sender_chat: "Chat" = None,
        sender_boost_count: "int" = None,
        sender_business_bot: "User" = None,
        business_connection_id: "str" = None,
        forward_origin: "MessageOrigin" = None,
        is_topic_message: "bool" = None,
        is_automatic_forward: "bool" = None,
        reply_to_message: "Message" = None,
        external_reply: "ExternalReplyInfo" = None,
        quote: "TextQuote" = None,
        reply_to_story: "Story" = None,
        via_bot: "User" = None,
        edit_date: "int" = None,
        has_protected_content: "bool" = None,
        is_from_offline: "bool" = None,
        media_group_id: "str" = None,
        author_signature: "str" = None,
        text: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
        effect_id: "str" = None,
        animation: "Animation" = None,
        audio: "Audio" = None,
        document: "Document" = None,
        paid_media: "PaidMediaInfo" = None,
        photo: List["PhotoSize"] = None,
        sticker: "Sticker" = None,
        story: "Story" = None,
        video: "Video" = None,
        video_note: "VideoNote" = None,
        voice: "Voice" = None,
        caption: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        has_media_spoiler: "bool" = None,
        contact: "Contact" = None,
        dice: "Dice" = None,
        game: "Game" = None,
        poll: "Poll" = None,
        venue: "Venue" = None,
        location: "Location" = None,
        new_chat_members: List["User"] = None,
        left_chat_member: "User" = None,
        new_chat_title: "str" = None,
        new_chat_photo: List["PhotoSize"] = None,
        delete_chat_photo: "bool" = None,
        group_chat_created: "bool" = None,
        supergroup_chat_created: "bool" = None,
        channel_chat_created: "bool" = None,
        message_auto_delete_timer_changed: "MessageAutoDeleteTimerChanged" = None,
        migrate_to_chat_id: "int" = None,
        migrate_from_chat_id: "int" = None,
        pinned_message: "Message" = None,
        invoice: "Invoice" = None,
        successful_payment: "SuccessfulPayment" = None,
        refunded_payment: "RefundedPayment" = None,
        users_shared: "UsersShared" = None,
        chat_shared: "ChatShared" = None,
        connected_website: "str" = None,
        write_access_allowed: "WriteAccessAllowed" = None,
        passport_data: "PassportData" = None,
        proximity_alert_triggered: "ProximityAlertTriggered" = None,
        boost_added: "ChatBoostAdded" = None,
        chat_background_set: "ChatBackground" = None,
        forum_topic_created: "ForumTopicCreated" = None,
        forum_topic_edited: "ForumTopicEdited" = None,
        forum_topic_closed: "ForumTopicClosed" = None,
        forum_topic_reopened: "ForumTopicReopened" = None,
        general_forum_topic_hidden: "GeneralForumTopicHidden" = None,
        general_forum_topic_unhidden: "GeneralForumTopicUnhidden" = None,
        giveaway_created: "GiveawayCreated" = None,
        giveaway: "Giveaway" = None,
        giveaway_winners: "GiveawayWinners" = None,
        giveaway_completed: "GiveawayCompleted" = None,
        video_chat_scheduled: "VideoChatScheduled" = None,
        video_chat_started: "VideoChatStarted" = None,
        video_chat_ended: "VideoChatEnded" = None,
        video_chat_participants_invited: "VideoChatParticipantsInvited" = None,
        web_app_data: "WebAppData" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_id = message_id
        self.message_thread_id = message_thread_id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.sender_boost_count = sender_boost_count
        self.sender_business_bot = sender_business_bot
        self.date = date
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.forward_origin = forward_origin
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.external_reply = external_reply
        self.quote = quote
        self.reply_to_story = reply_to_story
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.is_from_offline = is_from_offline
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.effect_id = effect_id
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paid_media = paid_media
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = message_auto_delete_timer_changed
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.refunded_payment = refunded_payment
        self.users_shared = users_shared
        self.chat_shared = chat_shared
        self.connected_website = connected_website
        self.write_access_allowed = write_access_allowed
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.boost_added = boost_added
        self.chat_background_set = chat_background_set
        self.forum_topic_created = forum_topic_created
        self.forum_topic_edited = forum_topic_edited
        self.forum_topic_closed = forum_topic_closed
        self.forum_topic_reopened = forum_topic_reopened
        self.general_forum_topic_hidden = general_forum_topic_hidden
        self.general_forum_topic_unhidden = general_forum_topic_unhidden
        self.giveaway_created = giveaway_created
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.giveaway_completed = giveaway_completed
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Message"]:
        return (
            Message(
                me=me,
                json=d,
                message_id=d.get("message_id"),
                date=d.get("date"),
                chat=Chat._parse(me=me, d=d.get("chat")),
                message_thread_id=d.get("message_thread_id"),
                from_user=User._parse(me=me, d=d.get("from")),
                sender_chat=Chat._parse(me=me, d=d.get("sender_chat")),
                sender_boost_count=d.get("sender_boost_count"),
                sender_business_bot=User._parse(me=me, d=d.get("sender_business_bot")),
                business_connection_id=d.get("business_connection_id"),
                forward_origin=None
                if not d.get("forward_origin")
                else (
                    MessageOriginUser._parse(me=me, d=d.get("forward_origin"))
                    if d["forward_origin"].get("sender_user")
                    else MessageOriginHiddenUser._parse(
                        me=me, d=d.get("forward_origin")
                    )
                    if d["forward_origin"].get("sender_user_name")
                    else MessageOriginChat._parse(me=me, d=d.get("forward_origin"))
                    if d["forward_origin"].get("sender_chat")
                    else MessageOriginChannel._parse(me=me, d=d.get("forward_origin"))
                    if d["forward_origin"].get("author_signature")
                    else None
                ),
                is_topic_message=d.get("is_topic_message"),
                is_automatic_forward=d.get("is_automatic_forward"),
                reply_to_message=Message._parse(me=me, d=d.get("reply_to_message")),
                external_reply=ExternalReplyInfo._parse(
                    me=me, d=d.get("external_reply")
                ),
                quote=TextQuote._parse(me=me, d=d.get("quote")),
                reply_to_story=Story._parse(me=me, d=d.get("reply_to_story")),
                via_bot=User._parse(me=me, d=d.get("via_bot")),
                edit_date=d.get("edit_date"),
                has_protected_content=d.get("has_protected_content"),
                is_from_offline=d.get("is_from_offline"),
                media_group_id=d.get("media_group_id"),
                author_signature=d.get("author_signature"),
                text=d.get("text"),
                entities=[MessageEntity._parse(me=me, d=i) for i in d.get("entities")]
                if d.get("entities")
                else None,
                link_preview_options=LinkPreviewOptions._parse(
                    me=me, d=d.get("link_preview_options")
                ),
                effect_id=d.get("effect_id"),
                animation=Animation._parse(me=me, d=d.get("animation")),
                audio=Audio._parse(me=me, d=d.get("audio")),
                document=Document._parse(me=me, d=d.get("document")),
                paid_media=PaidMediaInfo._parse(me=me, d=d.get("paid_media")),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
                sticker=Sticker._parse(me=me, d=d.get("sticker")),
                story=Story._parse(me=me, d=d.get("story")),
                video=Video._parse(me=me, d=d.get("video")),
                video_note=VideoNote._parse(me=me, d=d.get("video_note")),
                voice=Voice._parse(me=me, d=d.get("voice")),
                caption=d.get("caption"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                has_media_spoiler=d.get("has_media_spoiler"),
                contact=Contact._parse(me=me, d=d.get("contact")),
                dice=Dice._parse(me=me, d=d.get("dice")),
                game=Game._parse(me=me, d=d.get("game")),
                poll=Poll._parse(me=me, d=d.get("poll")),
                venue=Venue._parse(me=me, d=d.get("venue")),
                location=Location._parse(me=me, d=d.get("location")),
                new_chat_members=[
                    User._parse(me=me, d=i) for i in d.get("new_chat_members")
                ]
                if d.get("new_chat_members")
                else None,
                left_chat_member=User._parse(me=me, d=d.get("left_chat_member")),
                new_chat_title=d.get("new_chat_title"),
                new_chat_photo=[
                    PhotoSize._parse(me=me, d=i) for i in d.get("new_chat_photo")
                ]
                if d.get("new_chat_photo")
                else None,
                delete_chat_photo=d.get("delete_chat_photo"),
                group_chat_created=d.get("group_chat_created"),
                supergroup_chat_created=d.get("supergroup_chat_created"),
                channel_chat_created=d.get("channel_chat_created"),
                message_auto_delete_timer_changed=MessageAutoDeleteTimerChanged._parse(
                    me=me, d=d.get("message_auto_delete_timer_changed")
                ),
                migrate_to_chat_id=d.get("migrate_to_chat_id"),
                migrate_from_chat_id=d.get("migrate_from_chat_id"),
                pinned_message=Message._parse(me=me, d=d.get("pinned_message")),
                invoice=Invoice._parse(me=me, d=d.get("invoice")),
                successful_payment=SuccessfulPayment._parse(
                    me=me, d=d.get("successful_payment")
                ),
                refunded_payment=RefundedPayment._parse(
                    me=me, d=d.get("refunded_payment")
                ),
                users_shared=UsersShared._parse(me=me, d=d.get("users_shared")),
                chat_shared=ChatShared._parse(me=me, d=d.get("chat_shared")),
                connected_website=d.get("connected_website"),
                write_access_allowed=WriteAccessAllowed._parse(
                    me=me, d=d.get("write_access_allowed")
                ),
                passport_data=PassportData._parse(me=me, d=d.get("passport_data")),
                proximity_alert_triggered=ProximityAlertTriggered._parse(
                    me=me, d=d.get("proximity_alert_triggered")
                ),
                boost_added=ChatBoostAdded._parse(me=me, d=d.get("boost_added")),
                chat_background_set=ChatBackground._parse(
                    me=me, d=d.get("chat_background_set")
                ),
                forum_topic_created=ForumTopicCreated._parse(
                    me=me, d=d.get("forum_topic_created")
                ),
                forum_topic_edited=ForumTopicEdited._parse(
                    me=me, d=d.get("forum_topic_edited")
                ),
                forum_topic_closed=ForumTopicClosed._parse(
                    me=me, d=d.get("forum_topic_closed")
                ),
                forum_topic_reopened=ForumTopicReopened._parse(
                    me=me, d=d.get("forum_topic_reopened")
                ),
                general_forum_topic_hidden=GeneralForumTopicHidden._parse(
                    me=me, d=d.get("general_forum_topic_hidden")
                ),
                general_forum_topic_unhidden=GeneralForumTopicUnhidden._parse(
                    me=me, d=d.get("general_forum_topic_unhidden")
                ),
                giveaway_created=GiveawayCreated._parse(
                    me=me, d=d.get("giveaway_created")
                ),
                giveaway=Giveaway._parse(me=me, d=d.get("giveaway")),
                giveaway_winners=GiveawayWinners._parse(
                    me=me, d=d.get("giveaway_winners")
                ),
                giveaway_completed=GiveawayCompleted._parse(
                    me=me, d=d.get("giveaway_completed")
                ),
                video_chat_scheduled=VideoChatScheduled._parse(
                    me=me, d=d.get("video_chat_scheduled")
                ),
                video_chat_started=VideoChatStarted._parse(
                    me=me, d=d.get("video_chat_started")
                ),
                video_chat_ended=VideoChatEnded._parse(
                    me=me, d=d.get("video_chat_ended")
                ),
                video_chat_participants_invited=VideoChatParticipantsInvited._parse(
                    me=me, d=d.get("video_chat_participants_invited")
                ),
                web_app_data=WebAppData._parse(me=me, d=d.get("web_app_data")),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MessageId(Type_):
    def __init__(
        self, message_id: "int", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.message_id = message_id

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["MessageId"]:
        return (
            MessageId(
                me=me,
                json=d,
                message_id=d.get("message_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InaccessibleMessage(Type_):
    """
    This object describes a message that was deleted or is otherwise inaccessible to the bot.

    Telegram documentation: https://core.telegram.org/bots/api#inaccessiblemessage

    :param chat: Chat the message belonged to
    :type chat: :class:`Chat`

    :param message_id: Unique message identifier inside the chat
    :type message_id: :obj:`int`

    :param date: Always 0. The field can be used to differentiate regular and inaccessible messages.
    :type date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`InaccessibleMessage`
    """

    def __init__(
        self,
        chat: "Chat",
        message_id: "int",
        date: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.message_id = message_id
        self.date = date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InaccessibleMessage"]:
        return (
            InaccessibleMessage(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
                date=d.get("date"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


MaybeInaccessibleMessage = Union["InaccessibleMessage", "Message"]


class MessageEntity(Type_):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    Telegram Documentation: https://core.telegram.org/bots/api#messageentity

    :param type: Type of the entity. Currently, can be “mention” (@username), “hashtag” (#hashtag), “cashtag” ($USD),
        “bot_command” (/start@jobs_bot),“url” (https://telegram.org), “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123),
        “bold” (bold text), “italic” (italic text), “underline” (underlined text), “strikethrough” (strikethrough text),
        “spoiler” (spoiler message), “blockquote” (block quotation), “expandable_blockquote” (collapsed-by-default block quotation),
        “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs),
        “text_mention” (for users without usernames), “custom_emoji” (for inline custom emoji stickers)
    :type type: :obj:`str`

    :param offset: Offset in UTF-16 code units to the start of the entity
    :type offset: :obj:`int`

    :param length: Length of the entity in UTF-16 code units
    :type length: :obj:`int`

    :param url: Optional. For “text_link” only, URL that will be opened after user taps on the text
    :type url: :obj:`str`

    :param user: Optional. For “text_mention” only, the mentioned user
    :type user: :class:`tgram.types.User`

    :param language: Optional. For “pre” only, the programming language of the entity text
    :type language: :obj:`str`

    :param custom_emoji_id: Optional. For “custom_emoji” only, unique identifier of the custom emoji.
        Use get_custom_emoji_stickers to get full information about the sticker.
    :type custom_emoji_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.MessageEntity`
    """

    def __init__(
        self,
        type: "str",
        offset: "int",
        length: "int",
        url: "str" = None,
        user: "User" = None,
        language: "str" = None,
        custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["MessageEntity"]:
        return (
            MessageEntity(
                me=me,
                json=d,
                type=d.get("type"),
                offset=d.get("offset"),
                length=d.get("length"),
                url=d.get("url"),
                user=User._parse(me=me, d=d.get("user")),
                language=d.get("language"),
                custom_emoji_id=d.get("custom_emoji_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class TextQuote(Type_):
    """
    This object contains information about the quoted part of a message that is replied to by the given message.

    Telegram documentation: https://core.telegram.org/bots/api#textquote

    :param text: Text of the quoted part of a message that is replied to by the given message
    :type text: :obj:`str`

    :param entities: Optional. Special entities that appear in the quote. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes.
    :type entities: :obj:`list` of :class:`MessageEntity`

    :param position: Approximate quote position in the original message in UTF-16 code units as specified by the sender
    :type position: :obj:`int`

    :param is_manual: Optional. True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server.
    :type is_manual: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`TextQuote`
    """

    def __init__(
        self,
        text: "str",
        position: "int",
        entities: List["MessageEntity"] = None,
        is_manual: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.entities = entities
        self.position = position
        self.is_manual = is_manual

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["TextQuote"]:
        return (
            TextQuote(
                me=me,
                json=d,
                text=d.get("text"),
                position=d.get("position"),
                entities=[MessageEntity._parse(me=me, d=i) for i in d.get("entities")]
                if d.get("entities")
                else None,
                is_manual=d.get("is_manual"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ExternalReplyInfo(Type_):
    """
    This object contains information about a message that is being replied to,
    which may come from another chat or forum topic.

    Telegram documentation: https://core.telegram.org/bots/api#externalreplyinfo

    :param origin: Origin of the message replied to by the given message
    :type origin: :class:`MessageOrigin`

    :param chat: Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel.
    :type chat: :class:`Chat`

    :param message_id: Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.
    :type message_id: :obj:`int`

    :param link_preview_options: Optional. Options used for link preview generation for the original message, if it is a text message
    :type link_preview_options: :class:`LinkPreviewOptions`

    :param animation: Optional. Message is an animation, information about the animation
    :type animation: :class:`Animation`

    :param audio: Optional. Message is an audio file, information about the file
    :type audio: :class:`Audio`

    :param document: Optional. Message is a general file, information about the file
    :type document: :class:`Document`

    :param photo: Optional. Message is a photo, available sizes of the photo
    :type photo: :obj:`list` of :class:`PhotoSize`

    :param sticker: Optional. Message is a sticker, information about the sticker
    :type sticker: :class:`Sticker`

    :param story: Optional. Message is a forwarded story
    :type story: :class:`Story`

    :param video: Optional. Message is a video, information about the video
    :type video: :class:`Video`

    :param video_note: Optional. Message is a video note, information about the video message
    :type video_note: :class:`VideoNote`

    :param voice: Optional. Message is a voice message, information about the file
    :type voice: :class:`Voice`

    :param has_media_spoiler: Optional. True, if the message media is covered by a spoiler animation
    :type has_media_spoiler: :obj:`bool`

    :param contact: Optional. Message is a shared contact, information about the contact
    :type contact: :class:`Contact`

    :param dice: Optional. Message is a dice with random value
    :type dice: :class:`Dice`

    :param game: Optional. Message is a game, information about the game. More about games »
    :type game: :class:`Game`

    :param giveaway: Optional. Message is a scheduled giveaway, information about the giveaway
    :type giveaway: :class:`Giveaway`

    :param giveaway_winners: Optional. A giveaway with public winners was completed
    :type giveaway_winners: :class:`GiveawayWinners`

    :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More about payments »
    :type invoice: :class:`Invoice`

    :param location: Optional. Message is a shared location, information about the location
    :type location: :class:`Location`

    :param poll: Optional. Message is a native poll, information about the poll
    :type poll: :class:`Poll`

    :param venue: Optional. Message is a venue, information about the venue
    :type venue: :class:`Venue`

    :return: Instance of the class
    :rtype: :class:`ExternalReplyInfo`
    """

    def __init__(
        self,
        origin: "MessageOrigin",
        chat: "Chat" = None,
        message_id: "int" = None,
        link_preview_options: "LinkPreviewOptions" = None,
        animation: "Animation" = None,
        audio: "Audio" = None,
        document: "Document" = None,
        paid_media: "PaidMediaInfo" = None,
        photo: List["PhotoSize"] = None,
        sticker: "Sticker" = None,
        story: "Story" = None,
        video: "Video" = None,
        video_note: "VideoNote" = None,
        voice: "Voice" = None,
        has_media_spoiler: "bool" = None,
        contact: "Contact" = None,
        dice: "Dice" = None,
        game: "Game" = None,
        giveaway: "Giveaway" = None,
        giveaway_winners: "GiveawayWinners" = None,
        invoice: "Invoice" = None,
        location: "Location" = None,
        poll: "Poll" = None,
        venue: "Venue" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.origin = origin
        self.chat = chat
        self.message_id = message_id
        self.link_preview_options = link_preview_options
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paid_media = paid_media
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.invoice = invoice
        self.location = location
        self.poll = poll
        self.venue = venue

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ExternalReplyInfo"]:
        return (
            ExternalReplyInfo(
                me=me,
                json=d,
                origin=None
                if not d.get("origin")
                else (
                    MessageOriginUser._parse(me=me, d=d.get("origin"))
                    if d["origin"].get("sender_user")
                    else MessageOriginHiddenUser._parse(me=me, d=d.get("origin"))
                    if d["origin"].get("sender_user_name")
                    else MessageOriginChat._parse(me=me, d=d.get("origin"))
                    if d["origin"].get("sender_chat")
                    else MessageOriginChannel._parse(me=me, d=d.get("origin"))
                    if d["origin"].get("author_signature")
                    else None
                ),
                chat=Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
                link_preview_options=LinkPreviewOptions._parse(
                    me=me, d=d.get("link_preview_options")
                ),
                animation=Animation._parse(me=me, d=d.get("animation")),
                audio=Audio._parse(me=me, d=d.get("audio")),
                document=Document._parse(me=me, d=d.get("document")),
                paid_media=PaidMediaInfo._parse(me=me, d=d.get("paid_media")),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
                sticker=Sticker._parse(me=me, d=d.get("sticker")),
                story=Story._parse(me=me, d=d.get("story")),
                video=Video._parse(me=me, d=d.get("video")),
                video_note=VideoNote._parse(me=me, d=d.get("video_note")),
                voice=Voice._parse(me=me, d=d.get("voice")),
                has_media_spoiler=d.get("has_media_spoiler"),
                contact=Contact._parse(me=me, d=d.get("contact")),
                dice=Dice._parse(me=me, d=d.get("dice")),
                game=Game._parse(me=me, d=d.get("game")),
                giveaway=Giveaway._parse(me=me, d=d.get("giveaway")),
                giveaway_winners=GiveawayWinners._parse(
                    me=me, d=d.get("giveaway_winners")
                ),
                invoice=Invoice._parse(me=me, d=d.get("invoice")),
                location=Location._parse(me=me, d=d.get("location")),
                poll=Poll._parse(me=me, d=d.get("poll")),
                venue=Venue._parse(me=me, d=d.get("venue")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ReplyParameters(Type_):
    """
    Describes reply parameters for the message that is being sent.

    Telegram documentation: https://core.telegram.org/bots/api#replyparameters

    :param message_id: Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified
    :type message_id: :obj:`int`

    :param chat_id: Optional. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername)
    :type chat_id: :obj:`int` or :obj:`str`

    :param allow_sending_without_reply: Optional. Pass True if the message should be sent even if the specified message to be replied to is not found; can be used only for replies in the same chat and forum topic.
    :type allow_sending_without_reply: :obj:`bool`

    :param quote: Optional. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold, italic, underline, strikethrough, spoiler, and custom_emoji entities. The message will fail to send if the quote isn't found in the original message.
    :type quote: :obj:`str`

    :param quote_parse_mode: Optional. Mode for parsing entities in the quote. See formatting options for more details.
    :type quote_parse_mode: :obj:`str`

    :param quote_entities: Optional. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of quote_parse_mode.
    :type quote_entities: :obj:`list` of :class:`MessageEntity`

    :param quote_position: Optional. Position of the quote in the original message in UTF-16 code units
    :type quote_position: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`ReplyParameters`
    """

    def __init__(
        self,
        message_id: "int",
        chat_id: Union["int", "str"] = None,
        allow_sending_without_reply: "bool" = None,
        quote: "str" = None,
        quote_parse_mode: "str" = None,
        quote_entities: List["MessageEntity"] = None,
        quote_position: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities
        self.quote_position = quote_position

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ReplyParameters"]:
        return (
            ReplyParameters(
                me=me,
                json=d,
                message_id=d.get("message_id"),
                chat_id=d.get("chat_id"),
                allow_sending_without_reply=d.get("allow_sending_without_reply"),
                quote=d.get("quote"),
                quote_parse_mode=d.get("quote_parse_mode"),
                quote_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("quote_entities")
                ]
                if d.get("quote_entities")
                else None,
                quote_position=d.get("quote_position"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


MessageOrigin = Union[
    "MessageOriginUser",
    "MessageOriginHiddenUser",
    "MessageOriginChat",
    "MessageOriginChannel",
]


class MessageOriginUser(Type_):
    """
    The message was originally sent by a known user.

    :param sender_user: User that sent the message originally
    :type sender_user: :class:`User`
    """

    def __init__(
        self,
        type: "str",
        date: "int",
        sender_user: "User",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.date = date
        self.sender_user = sender_user

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MessageOriginUser"]:
        return (
            MessageOriginUser(
                me=me,
                json=d,
                type=d.get("type"),
                date=d.get("date"),
                sender_user=User._parse(me=me, d=d.get("sender_user")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MessageOriginHiddenUser(Type_):
    """
    The message was originally sent by an unknown user.

    :param sender_user_name: Name of the user that sent the message originally
    :type sender_user_name: :obj:`str`
    """

    def __init__(
        self,
        type: "str",
        date: "int",
        sender_user_name: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.date = date
        self.sender_user_name = sender_user_name

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MessageOriginHiddenUser"]:
        return (
            MessageOriginHiddenUser(
                me=me,
                json=d,
                type=d.get("type"),
                date=d.get("date"),
                sender_user_name=d.get("sender_user_name"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MessageOriginChat(Type_):
    """
    The message was originally sent on behalf of a chat to a group chat.

    :param sender_chat: Chat that sent the message originally
    :type sender_chat: :class:`Chat`

    :param author_signature: Optional. For messages originally sent by an anonymous chat administrator, original message author signature
    :type author_signature: :obj:`str`
    """

    def __init__(
        self,
        type: "str",
        date: "int",
        sender_chat: "Chat",
        author_signature: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.date = date
        self.sender_chat = sender_chat
        self.author_signature = author_signature

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MessageOriginChat"]:
        return (
            MessageOriginChat(
                me=me,
                json=d,
                type=d.get("type"),
                date=d.get("date"),
                sender_chat=Chat._parse(me=me, d=d.get("sender_chat")),
                author_signature=d.get("author_signature"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MessageOriginChannel(Type_):
    """
    The message was originally sent to a channel chat.

    :param chat: Channel chat to which the message was originally sent
    :type chat: :class:`Chat`

    :param message_id: Unique message identifier inside the chat
    :type message_id: :obj:`int`

    :param author_signature: Optional. Signature of the original post author
    :type author_signature: :obj:`str`
    """

    def __init__(
        self,
        type: "str",
        date: "int",
        chat: "Chat",
        message_id: "int",
        author_signature: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.date = date
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MessageOriginChannel"]:
        return (
            MessageOriginChannel(
                me=me,
                json=d,
                type=d.get("type"),
                date=d.get("date"),
                chat=Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
                author_signature=d.get("author_signature"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PhotoSize(Type_):
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    Telegram Documentation: https://core.telegram.org/bots/api#photosize

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param width: Photo width
    :type width: :obj:`int`

    :param height: Photo height
    :type height: :obj:`int`

    :param file_size: Optional. File size in bytes
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PhotoSize`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        width: "int",
        height: "int",
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["PhotoSize"]:
        return (
            PhotoSize(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                file_size=d.get("file_size"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Animation(Type_):
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    Telegram Documentation: https://core.telegram.org/bots/api#animation

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param width: Video width as defined by sender
    :type width: :obj:`int`

    :param height: Video height as defined by sender
    :type height: :obj:`int`

    :param duration: Duration of the video in seconds as defined by sender
    :type duration: :obj:`int`

    :param thumbnail: Optional. Animation thumbnail as defined by sender
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :param file_name: Optional. Original animation filename as defined by sender
    :type file_name: :obj:`str`

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type mime_type: :obj:`str`

    :param file_size: Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Animation`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        width: "int",
        height: "int",
        duration: "int",
        thumbnail: "PhotoSize" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Animation"]:
        return (
            Animation(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                thumbnail=PhotoSize._parse(me=me, d=d.get("thumbnail")),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Audio(Type_):
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    Telegram Documentation: https://core.telegram.org/bots/api#audio

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param duration: Duration of the audio in seconds as defined by sender
    :type duration: :obj:`int`

    :param performer: Optional. Performer of the audio as defined by sender or by audio tags
    :type performer: :obj:`str`

    :param title: Optional. Title of the audio as defined by sender or by audio tags
    :type title: :obj:`str`

    :param file_name: Optional. Original filename as defined by sender
    :type file_name: :obj:`str`

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type mime_type: :obj:`str`

    :param file_size: Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`

    :param thumbnail: Optional. Thumbnail of the album cover to which the music file belongs
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Audio`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        duration: "int",
        performer: "str" = None,
        title: "str" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
        thumbnail: "PhotoSize" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Audio"]:
        return (
            Audio(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                duration=d.get("duration"),
                performer=d.get("performer"),
                title=d.get("title"),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
                thumbnail=PhotoSize._parse(me=me, d=d.get("thumbnail")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Document(Type_):
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    Telegram Documentation: https://core.telegram.org/bots/api#document

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param thumbnail: Optional. Document thumbnail as defined by sender
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :param file_name: Optional. Original filename as defined by sender
    :type file_name: :obj:`str`

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type mime_type: :obj:`str`

    :param file_size: Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Document`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        thumbnail: "PhotoSize" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Document"]:
        return (
            Document(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                thumbnail=PhotoSize._parse(me=me, d=d.get("thumbnail")),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Story(Type_):
    """
    This object represents a story.

    Telegram documentation: https://core.telegram.org/bots/api#story

    :param chat: Chat that posted the story
    :type chat: :class:`tgram.types.Chat`

    :param id: Unique identifier for the story in the chat
    :type id: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`Story`
    """

    def __init__(
        self, chat: "Chat", id: "int", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.id = id

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Story"]:
        return (
            Story(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                id=d.get("id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Video(Type_):
    """
    This object represents a video file.

    Telegram Documentation: https://core.telegram.org/bots/api#video

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param width: Video width as defined by sender
    :type width: :obj:`int`

    :param height: Video height as defined by sender
    :type height: :obj:`int`

    :param duration: Duration of the video in seconds as defined by sender
    :type duration: :obj:`int`

    :param thumbnail: Optional. Video thumbnail
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :param file_name: Optional. Original filename as defined by sender
    :type file_name: :obj:`str`

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type mime_type: :obj:`str`

    :param file_size: Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Video`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        width: "int",
        height: "int",
        duration: "int",
        thumbnail: "PhotoSize" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Video"]:
        return (
            Video(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                thumbnail=PhotoSize._parse(me=me, d=d.get("thumbnail")),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class VideoNote(Type_):
    """
    This object represents a video message (available in Telegram apps as of v.4.0).

    Telegram Documentation: https://core.telegram.org/bots/api#videonote

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param length: Video width and height (diameter of the video message) as defined by sender
    :type length: :obj:`int`

    :param duration: Duration of the video in seconds as defined by sender
    :type duration: :obj:`int`

    :param thumbnail: Optional. Video thumbnail
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :param file_size: Optional. File size in bytes
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoNote`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        length: "int",
        duration: "int",
        thumbnail: "PhotoSize" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["VideoNote"]:
        return (
            VideoNote(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                length=d.get("length"),
                duration=d.get("duration"),
                thumbnail=PhotoSize._parse(me=me, d=d.get("thumbnail")),
                file_size=d.get("file_size"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Voice(Type_):
    """
    This object represents a voice note.

    Telegram Documentation: https://core.telegram.org/bots/api#voice

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param duration: Duration of the audio in seconds as defined by sender
    :type duration: :obj:`int`

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type mime_type: :obj:`str`

    :param file_size: Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Voice`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        duration: "int",
        mime_type: "str" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Voice"]:
        return (
            Voice(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                duration=d.get("duration"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Contact(Type_):
    """
    This object represents a phone contact.

    Telegram Documentation: https://core.telegram.org/bots/api#contact

    :param phone_number: Contact's phone number
    :type phone_number: :obj:`str`

    :param first_name: Contact's first name
    :type first_name: :obj:`str`

    :param last_name: Optional. Contact's last name
    :type last_name: :obj:`str`

    :param user_id: Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits
        and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52
        significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type user_id: :obj:`int`

    :param vcard: Optional. Additional data about the contact in the form of a vCard
    :type vcard: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Contact`
    """

    def __init__(
        self,
        phone_number: "str",
        first_name: "str",
        last_name: "str" = None,
        user_id: "int" = None,
        vcard: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Contact"]:
        return (
            Contact(
                me=me,
                json=d,
                phone_number=d.get("phone_number"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                user_id=d.get("user_id"),
                vcard=d.get("vcard"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Dice(Type_):
    """
    This object represents an animated emoji that displays a random value.

    Telegram Documentation: https://core.telegram.org/bots/api#dice

    :param emoji: Emoji on which the dice throw animation is based
    :type emoji: :obj:`str`

    :param value: Value of the dice, 1-6 for “🎲”, “🎯” and “🎳” base emoji, 1-5 for “🏀” and “⚽” base emoji, 1-64 for “🎰” base emoji
    :type value: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Dice`
    """

    def __init__(
        self, emoji: "str", value: "int", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.emoji = emoji
        self.value = value

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Dice"]:
        return (
            Dice(
                me=me,
                json=d,
                emoji=d.get("emoji"),
                value=d.get("value"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PollOption(Type_):
    """
    This object contains information about one answer option in a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#polloption

    :param text: Option text, 1-100 characters
    :type text: :obj:`str`

    :param voter_count: Number of users that voted for this option
    :type voter_count: :obj:`int`

    :param text_entities: Optional. Special entities that appear in the option text. Currently, only custom emoji entities are allowed in poll option texts
    :type text_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollOption`
    """

    def __init__(
        self,
        text: "str",
        voter_count: "int",
        text_entities: List["MessageEntity"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.text_entities = text_entities
        self.voter_count = voter_count

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["PollOption"]:
        return (
            PollOption(
                me=me,
                json=d,
                text=d.get("text"),
                voter_count=d.get("voter_count"),
                text_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("text_entities")
                ]
                if d.get("text_entities")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputPollOption(Type_):
    """
    This object contains information about one answer option in a poll to send.

    Telegram Documentation: https://core.telegram.org/bots/api#inputpolloption

    :param text: Option text, 1-100 characters
    :type text: :obj:`str`

    :param text_parse_mode: Optional. Mode for parsing entities in the text. See formatting options for more details. Currently, only custom emoji entities are allowed
    :type text_parse_mode: :obj:`str`

    :param text_entities: Optional. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of text_parse_mode
    :type text_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollOption`
    """

    def __init__(
        self,
        text: "str",
        text_parse_mode: "str" = None,
        text_entities: List["MessageEntity"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["InputPollOption"]:
        return (
            InputPollOption(
                me=me,
                json=d,
                text=d.get("text"),
                text_parse_mode=d.get("text_parse_mode"),
                text_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("text_entities")
                ]
                if d.get("text_entities")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PollAnswer(Type_):
    """
    This object represents an answer of a user in a non-anonymous poll.

    Telegram Documentation: https://core.telegram.org/bots/api#pollanswer

    :param poll_id: Unique poll identifier
    :type poll_id: :obj:`str`

    :param voter_chat: Optional. The chat that changed the answer to the poll, if the voter is anonymous
    :type voter_chat: :class:`tgram.types.Chat`

    :param user: Optional. The user, who changed the answer to the poll
    :type user: :class:`tgram.types.User`

    :param option_ids: 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted
        their vote.
    :type option_ids: :obj:`list` of :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollAnswer`
    """

    def __init__(
        self,
        poll_id: "str",
        option_ids: List["int"],
        voter_chat: "Chat" = None,
        user: "User" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["PollAnswer"]:
        return (
            PollAnswer(
                me=me,
                json=d,
                poll_id=d.get("poll_id"),
                option_ids=d.get("option_ids"),
                voter_chat=Chat._parse(me=me, d=d.get("voter_chat")),
                user=User._parse(me=me, d=d.get("user")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Poll(Type_):
    """
    This object contains information about a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#poll

    :param id: Unique poll identifier
    :type id: :obj:`str`

    :param question: Poll question, 1-300 characters
    :type question: :obj:`str`

    :param options: List of poll options
    :type options: :obj:`list` of :class:`tgram.types.PollOption`

    :param total_voter_count: Total number of users that voted in the poll
    :type total_voter_count: :obj:`int`

    :param is_closed: True, if the poll is closed
    :type is_closed: :obj:`bool`

    :param is_anonymous: True, if the poll is anonymous
    :type is_anonymous: :obj:`bool`

    :param type: Poll type, currently can be “regular” or “quiz”
    :type type: :obj:`str`

    :param allows_multiple_answers: True, if the poll allows multiple answers
    :type allows_multiple_answers: :obj:`bool`

    :param correct_option_id: Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    :type correct_option_id: :obj:`int`

    :param explanation: Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    :type explanation: :obj:`str`

    :param explanation_entities: Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    :type explanation_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param open_period: Optional. Amount of time in seconds the poll will be active after creation
    :type open_period: :obj:`int`

    :param close_date: Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    :type close_date: :obj:`int`

    :param question_entities: Optional. Special entities that appear in the question. Currently, only custom emoji entities are allowed in poll questions
    :type question_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Poll`
    """

    def __init__(
        self,
        id: "str",
        question: "str",
        options: List["PollOption"],
        total_voter_count: "int",
        is_closed: "bool",
        is_anonymous: "bool",
        type: "str",
        allows_multiple_answers: "bool",
        question_entities: List["MessageEntity"] = None,
        correct_option_id: "int" = None,
        explanation: "str" = None,
        explanation_entities: List["MessageEntity"] = None,
        open_period: "int" = None,
        close_date: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.question = question
        self.question_entities = question_entities
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Poll"]:
        return (
            Poll(
                me=me,
                json=d,
                id=d.get("id"),
                question=d.get("question"),
                options=[PollOption._parse(me=me, d=i) for i in d.get("options")]
                if d.get("options")
                else None,
                total_voter_count=d.get("total_voter_count"),
                is_closed=d.get("is_closed"),
                is_anonymous=d.get("is_anonymous"),
                type=d.get("type"),
                allows_multiple_answers=d.get("allows_multiple_answers"),
                question_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("question_entities")
                ]
                if d.get("question_entities")
                else None,
                correct_option_id=d.get("correct_option_id"),
                explanation=d.get("explanation"),
                explanation_entities=[
                    MessageEntity._parse(me=me, d=i)
                    for i in d.get("explanation_entities")
                ]
                if d.get("explanation_entities")
                else None,
                open_period=d.get("open_period"),
                close_date=d.get("close_date"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Location(Type_):
    """
    This object represents a point on the map.

    Telegram Documentation: https://core.telegram.org/bots/api#location

    :param longitude: Longitude as defined by sender
    :type longitude: :obj:`float`

    :param latitude: Latitude as defined by sender
    :type latitude: :obj:`float`

    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :type horizontal_accuracy: :obj:`float` number

    :param live_period: Optional. Time relative to the message sending date, during which the location can be updated;
        in seconds. For active live locations only.
    :type live_period: :obj:`int`

    :param heading: Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
    :type heading: :obj:`int`

    :param proximity_alert_radius: Optional. The maximum distance for proximity alerts about approaching another
        chat member, in meters. For sent live locations only.
    :type proximity_alert_radius: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Location`
    """

    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Location"]:
        return (
            Location(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                horizontal_accuracy=d.get("horizontal_accuracy"),
                live_period=d.get("live_period"),
                heading=d.get("heading"),
                proximity_alert_radius=d.get("proximity_alert_radius"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Venue(Type_):
    """
    This object represents a venue.

    Telegram Documentation: https://core.telegram.org/bots/api#venue

    :param location: Venue location. Can't be a live location
    :type location: :class:`tgram.types.Location`

    :param title: Name of the venue
    :type title: :obj:`str`

    :param address: Address of the venue
    :type address: :obj:`str`

    :param foursquare_id: Optional. Foursquare identifier of the venue
    :type foursquare_id: :obj:`str`

    :param foursquare_type: Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”,
        “arts_entertainment/aquarium” or “food/icecream”.)
    :type foursquare_type: :obj:`str`

    :param google_place_id: Optional. Google Places identifier of the venue
    :type google_place_id: :obj:`str`

    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :type google_place_type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Venue`
    """

    def __init__(
        self,
        location: "Location",
        title: "str",
        address: "str",
        foursquare_id: "str" = None,
        foursquare_type: "str" = None,
        google_place_id: "str" = None,
        google_place_type: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Venue"]:
        return (
            Venue(
                me=me,
                json=d,
                location=Location._parse(me=me, d=d.get("location")),
                title=d.get("title"),
                address=d.get("address"),
                foursquare_id=d.get("foursquare_id"),
                foursquare_type=d.get("foursquare_type"),
                google_place_id=d.get("google_place_id"),
                google_place_type=d.get("google_place_type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class WebAppData(Type_):
    """
    Describes data sent from a Web App to the bot.

    Telegram Documentation: https://core.telegram.org/bots/api#webappdata

    :param data: The data. Be aware that a bad client can send arbitrary data in this field.
    :type data: :obj:`str`

    :param button_text: Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client
        can send arbitrary data in this field.
    :type button_text: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.WebAppData`
    """

    def __init__(
        self,
        data: "str",
        button_text: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.data = data
        self.button_text = button_text

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["WebAppData"]:
        return (
            WebAppData(
                me=me,
                json=d,
                data=d.get("data"),
                button_text=d.get("button_text"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ProximityAlertTriggered(Type_):
    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    Telegram Documentation: https://core.telegram.org/bots/api#proximityalerttriggered

    :param traveler: User that triggered the alert
    :type traveler: :class:`tgram.types.User`

    :param watcher: User that set the alert
    :type watcher: :class:`tgram.types.User`

    :param distance: The distance between the users
    :type distance: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ProximityAlertTriggered`
    """

    def __init__(
        self,
        traveler: "User",
        watcher: "User",
        distance: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ProximityAlertTriggered"]:
        return (
            ProximityAlertTriggered(
                me=me,
                json=d,
                traveler=User._parse(me=me, d=d.get("traveler")),
                watcher=User._parse(me=me, d=d.get("watcher")),
                distance=d.get("distance"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MessageAutoDeleteTimerChanged(Type_):
    """
    This object represents a service message about a change in auto-delete timer settings.

    Telegram Documentation: https://core.telegram.org/bots/api#messageautodeletetimerchanged

    :param message_auto_delete_time: New auto-delete time for messages in the chat; in seconds
    :type message_auto_delete_time: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.MessageAutoDeleteTimerChanged`
    """

    def __init__(
        self,
        message_auto_delete_time: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_auto_delete_time = message_auto_delete_time

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MessageAutoDeleteTimerChanged"]:
        return (
            MessageAutoDeleteTimerChanged(
                me=me,
                json=d,
                message_auto_delete_time=d.get("message_auto_delete_time"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBoostAdded(Type_):
    """
    This object represents a service message about a user boosting a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostadded

    :param boost_count: Number of boosts added by the user
    :type boost_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`ChatBoostAdded`
    """

    def __init__(
        self, boost_count: "int", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.boost_count = boost_count

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatBoostAdded"]:
        return (
            ChatBoostAdded(
                me=me,
                json=d,
                boost_count=d.get("boost_count"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundFill(Type_):
    """
    This object describes the way a background is filled based on the selected colors. Currently, it can be one of
        BackgroundFillSolid
        BackgroundFillGradient
        BackgroundFillFreeformGradient

    Telegram documentation: https://core.telegram.org/bots/api#backgroundfill

    :return: Instance of the class
    :rtype: :class:`BackgroundFillSolid` or :class:`BackgroundFillGradient` or :class:`BackgroundFillFreeformGradient`
    """

    def __init__(
        self, type: "str", color: "int", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.color = color

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["BackgroundFill"]:
        return (
            BackgroundFill(
                me=me,
                json=d,
                type=d.get("type"),
                color=d.get("color"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundFillSolid(Type_):
    """
    The background is filled using the selected color.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundfillsolid

    :param type: Type of the background fill, always “solid”
    :type type: :obj:`str`

    :param color: The color of the background fill in the RGB24 format
    :type color: :class:`int`

    :return: Instance of the class
    :rtype: :class:`BackgroundFillSolid`
    """

    def __init__(
        self, type: "str", color: "int", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.color = color

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BackgroundFillSolid"]:
        return (
            BackgroundFillSolid(
                me=me,
                json=d,
                type=d.get("type"),
                color=d.get("color"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundFillGradient(Type_):
    """
    The background is a gradient fill.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundfillgradient

    :param type: Type of the background fill, always “gradient”
    :type type: :obj:`str`

    :param top_color: Top color of the gradient in the RGB24 format
    :type top_color: :class:`int`

    :param bottom_color: Bottom color of the gradient in the RGB24 format
    :type bottom_color: :class:`int`

    :param rotation_angle: Clockwise rotation angle of the background fill in degrees; 0-359
    :type rotation_angle: :class:`int`

    :return: Instance of the class
    :rtype: :class:`BackgroundFillGradient`
    """

    def __init__(
        self,
        type: "str",
        top_color: "int",
        bottom_color: "int",
        rotation_angle: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.rotation_angle = rotation_angle

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BackgroundFillGradient"]:
        return (
            BackgroundFillGradient(
                me=me,
                json=d,
                type=d.get("type"),
                top_color=d.get("top_color"),
                bottom_color=d.get("bottom_color"),
                rotation_angle=d.get("rotation_angle"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundFillFreeformGradient(Type_):
    """
    The background is a freeform gradient that rotates after every message in the chat.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundfillfreeformgradient

    :param type: Type of the background fill, always “freeform_gradient”
    :type type: :obj:`str`

    :param colors: A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format
    :type colors: :obj:`list` of :class:`int`

    :return: Instance of the class
    :rtype: :class:`BackgroundFillFreeformGradient`
    """

    def __init__(
        self,
        type: "str",
        colors: List["int"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.colors = colors

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BackgroundFillFreeformGradient"]:
        return (
            BackgroundFillFreeformGradient(
                me=me,
                json=d,
                type=d.get("type"),
                colors=d.get("colors"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundType(Type_):
    """
    This object describes the type of a background. Currently, it can be one of
        BackgroundTypeFill
        BackgroundTypeWallpaper
        BackgroundTypePattern
        BackgroundTypeChatTheme

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtype

    :return: Instance of the class
    :rtype: :class:`BackgroundTypeFill` or :class:`BackgroundTypeWallpaper` or :class:`BackgroundTypePattern` or :class:`BackgroundTypeChatTheme`
    """

    def __init__(
        self,
        type: "str",
        fill: "BackgroundFill",
        dark_theme_dimming: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["BackgroundType"]:
        return (
            BackgroundType(
                me=me,
                json=d,
                type=d.get("type"),
                fill=BackgroundFill._parse(me=me, d=d.get("fill")),
                dark_theme_dimming=d.get("dark_theme_dimming"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundTypeFill(Type_):
    """
    The background is automatically filled based on the selected colors.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtypefill

    :param type: Type of the background, always “fill”
    :type type: :obj:`str`

    :param fill: The background fill
    :type fill: :class:`BackgroundFill`

    :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100
    :type dark_theme_dimming: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`BackgroundTypeFill`
    """

    def __init__(
        self,
        type: "str",
        fill: "BackgroundFill",
        dark_theme_dimming: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BackgroundTypeFill"]:
        return (
            BackgroundTypeFill(
                me=me,
                json=d,
                type=d.get("type"),
                fill=BackgroundFill._parse(me=me, d=d.get("fill")),
                dark_theme_dimming=d.get("dark_theme_dimming"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundTypeWallpaper(Type_):
    """
    The background is a wallpaper in the JPEG format.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtypewallpaper

    :param type: Type of the background, always “wallpaper”
    :type type: :obj:`str`

    :param document: Document with the wallpaper
    :type document: :class:`Document`

    :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100
    :type dark_theme_dimming: :obj:`int`

    :param is_blurred: Optional. True, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12
    :type is_blurred: :obj:`bool`

    :param is_moving: Optional. True, if the background moves slightly when the device is tilted
    :type is_moving: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`BackgroundTypeWallpaper`
    """

    def __init__(
        self,
        type: "str",
        document: "Document",
        dark_theme_dimming: "int",
        is_blurred: "bool" = None,
        is_moving: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.document = document
        self.dark_theme_dimming = dark_theme_dimming
        self.is_blurred = is_blurred
        self.is_moving = is_moving

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BackgroundTypeWallpaper"]:
        return (
            BackgroundTypeWallpaper(
                me=me,
                json=d,
                type=d.get("type"),
                document=Document._parse(me=me, d=d.get("document")),
                dark_theme_dimming=d.get("dark_theme_dimming"),
                is_blurred=d.get("is_blurred"),
                is_moving=d.get("is_moving"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundTypePattern(Type_):
    """
    The background is a wallpaper in the JPEG format.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtypepattern

    :param type: Type of the background, always “pattern”
    :type type: :obj:`str`

    :param document: Document with the pattern
    :type document: :class:`Document`

    :param fill: The background fill that is combined with the pattern
    :type fill: :class:`BackgroundFill`

    :param intensity: Intensity of the pattern when it is shown above the filled background; 0-100
    :type intensity: :obj:`int`

    :param is_inverted: Optional. True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only
    :type is_inverted: :obj:`bool`

    :param is_moving: Optional. True, if the background moves slightly when the device is tilted
    :type is_moving: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`BackgroundTypePattern`
    """

    def __init__(
        self,
        type: "str",
        document: "Document",
        fill: "BackgroundFill",
        intensity: "int",
        is_inverted: "bool" = None,
        is_moving: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.document = document
        self.fill = fill
        self.intensity = intensity
        self.is_inverted = is_inverted
        self.is_moving = is_moving

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BackgroundTypePattern"]:
        return (
            BackgroundTypePattern(
                me=me,
                json=d,
                type=d.get("type"),
                document=Document._parse(me=me, d=d.get("document")),
                fill=BackgroundFill._parse(me=me, d=d.get("fill")),
                intensity=d.get("intensity"),
                is_inverted=d.get("is_inverted"),
                is_moving=d.get("is_moving"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BackgroundTypeChatTheme(Type_):
    """
    The background is taken directly from a built-in chat theme.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtypechattheme

    :param type: Type of the background, always “chat_theme”
    :type type: :obj:`str`

    :param theme_name: Intensity of the pattern when it is shown above the filled background; 0-100
    :type theme_name: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`BackgroundTypeChatTheme`
    """

    def __init__(
        self,
        type: "str",
        theme_name: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.theme_name = theme_name

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BackgroundTypeChatTheme"]:
        return (
            BackgroundTypeChatTheme(
                me=me,
                json=d,
                type=d.get("type"),
                theme_name=d.get("theme_name"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBackground(Type_):
    """
    This object represents a chat background.

    Telegram documentation: https://core.telegram.org/bots/api#chatbackground

    :param type: Type of the background
    :type type: :class:`BackgroundType`

    :return: Instance of the class
    :rtype: :class:`ChatBackground`
    """

    def __init__(
        self, type: "BackgroundType", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatBackground"]:
        return (
            ChatBackground(
                me=me,
                json=d,
                type=BackgroundType._parse(me=me, d=d.get("type")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ForumTopicCreated(Type_):
    """
    This object represents a service message about a new forum topic created in the chat.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopiccreated

    :param name: Name of the topic
    :type name: :obj:`str`

    :param icon_color: Color of the topic icon in RGB format
    :type icon_color: :obj:`int`

    :param icon_custom_emoji_id: Optional. Unique identifier of the custom emoji shown as the topic icon
    :type icon_custom_emoji_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ForumTopicCreated`
    """

    def __init__(
        self,
        name: "str",
        icon_color: "int",
        icon_custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ForumTopicCreated"]:
        return (
            ForumTopicCreated(
                me=me,
                json=d,
                name=d.get("name"),
                icon_color=d.get("icon_color"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ForumTopicClosed(Type_):
    """
    This object represents a service message about a forum topic closed in the chat. Currently holds no information.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopicclosed
    """

    def __init__(
        self,
        name: "str" = None,
        icon_custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ForumTopicClosed"]:
        return (
            ForumTopicClosed(
                me=me,
                json=d,
                name=d.get("name"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ForumTopicEdited(Type_):
    """
    This object represents a service message about an edited forum topic.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopicedited

    :param name: Optional, Name of the topic(if updated)
    :type name: :obj:`str`

    :param icon_custom_emoji_id: Optional. New identifier of the custom emoji shown as the topic icon, if it was edited;
        an empty string if the icon was removed
    :type icon_custom_emoji_id: :obj:`str`
    """

    def __init__(
        self,
        name: "str" = None,
        icon_custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ForumTopicEdited"]:
        return (
            ForumTopicEdited(
                me=me,
                json=d,
                name=d.get("name"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ForumTopicReopened(Type_):
    """
    This object represents a service message about a forum topic reopened in the chat. Currently holds no information.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopicreopened
    """

    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ForumTopicReopened"]:
        return (
            ForumTopicReopened(
                me=me,
                json=d,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class GeneralForumTopicHidden(Type_):
    """
    This object represents a service message about General forum topic hidden in the chat.
    Currently holds no information.

    Telegram documentation: https://core.telegram.org/bots/api#generalforumtopichidden
    """

    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["GeneralForumTopicHidden"]:
        return (
            GeneralForumTopicHidden(
                me=me,
                json=d,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class GeneralForumTopicUnhidden(Type_):
    """
    This object represents a service message about General forum topic unhidden in the chat.
    Currently holds no information.

    Telegram documentation: https://core.telegram.org/bots/api#generalforumtopicunhidden
    """

    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["GeneralForumTopicUnhidden"]:
        return (
            GeneralForumTopicUnhidden(
                me=me,
                json=d,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class SharedUser(Type_):
    """
    This object contains information about a user that was shared with the bot using a KeyboardButtonRequestUser button.

    Telegram documentation: https://core.telegram.org/bots/api#shareduser

    :param user_id: Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.
    :type user_id: :obj:`int`

    :param first_name: Optional. First name of the user, if the name was requested by the bot
    :type first_name: :obj:`str`

    :param last_name: Optional. Last name of the user, if the name was requested by the bot
    :type last_name: :obj:`str`

    :param username: Optional. Username of the user, if the username was requested by the bot
    :type username: :obj:`str`

    :param photo: Optional. Available sizes of the chat photo, if the photo was requested by the bot
    :type photo: :obj:`list` of :class:`PhotoSize`

    :return: Instance of the class
    :rtype: :class:`SharedUser`
    """

    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["SharedUser"]:
        return (
            SharedUser(
                me=me,
                json=d,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class UsersShared(Type_):
    """
    This object contains information about the users whose identifiers were shared with the bot
    using a KeyboardButtonRequestUsers button.

    Telegram documentation: https://core.telegram.org/bots/api#usersshared

    :param request_id: Identifier of the request
    :type request_id: :obj:`int`

    :param users: Information about users shared with the bot
    :type users: :obj:`list` of :obj:`types.SharedUser`

    :return: Instance of the class
    :rtype: :class:`UsersShared`
    """

    def __init__(
        self,
        request_id: "int",
        users: List["SharedUser"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_id = request_id
        self.users = users

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["UsersShared"]:
        return (
            UsersShared(
                me=me,
                json=d,
                request_id=d.get("request_id"),
                users=[SharedUser._parse(me=me, d=i) for i in d.get("users")]
                if d.get("users")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatShared(Type_):
    """
    This object contains information about the chat whose identifier was shared with the bot using a
    `tgram.types.KeyboardButtonRequestChat` button.

    Telegram documentation: https://core.telegram.org/bots/api#Chatshared

    :param request_id: identifier of the request
    :type request_id: :obj:`int`

    :param chat_id: Identifier of the shared chat. This number may have more than 32 significant bits and some programming
        languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit
        integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat
        and could be unable to use this identifier, unless the chat is already known to the bot by some other means.
    :type chat_id: :obj:`int`

    :param title: Optional. Title of the shared chat
    :type title: :obj:`str`

    :param photo: Optional. Array of Photosize
    :type photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param username: Optional. Username of the shared chat
    :type username: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatShared`
    """

    def __init__(
        self,
        request_id: "int",
        chat_id: "int",
        title: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatShared"]:
        return (
            ChatShared(
                me=me,
                json=d,
                request_id=d.get("request_id"),
                chat_id=d.get("chat_id"),
                title=d.get("title"),
                username=d.get("username"),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class WriteAccessAllowed(Type_):
    """
    This object represents a service message about a user allowing a bot to write
    messages after adding it to the attachment menu, launching a Web App from a link,
    or accepting an explicit request from a Web App sent by the method requestWriteAccess.

    Telegram documentation: https://core.telegram.org/bots/api#writeaccessallowed

    :param from_request: Optional. True, if the access was granted after the user accepted an
        explicit request from a Web App sent by the method requestWriteAccess
    :type from_request: :obj:`bool`

    :param web_app_name: Optional. Name of the Web App which was launched from a link
    :type web_app_name: :obj:`str`

    :param from_attachment_menu: Optional. True, if the access was granted when the bot was added to the attachment or side menu
    :type from_attachment_menu: :obj:`bool`
    """

    def __init__(
        self,
        from_request: "bool" = None,
        web_app_name: "str" = None,
        from_attachment_menu: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["WriteAccessAllowed"]:
        return (
            WriteAccessAllowed(
                me=me,
                json=d,
                from_request=d.get("from_request"),
                web_app_name=d.get("web_app_name"),
                from_attachment_menu=d.get("from_attachment_menu"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class VideoChatScheduled(Type_):
    """
    This object represents a service message about a video chat scheduled in the chat.

    Telegram Documentation: https://core.telegram.org/bots/api#videochatscheduled

    :param start_date: Point in time (Unix timestamp) when the video chat is supposed to be started by a chat
        administrator
    :type start_date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoChatScheduled`
    """

    def __init__(
        self, start_date: "int", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.start_date = start_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["VideoChatScheduled"]:
        return (
            VideoChatScheduled(
                me=me,
                json=d,
                start_date=d.get("start_date"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class VideoChatStarted(Type_):
    """
    This object represents a service message about a video chat started in the chat. Currently holds no information.
    """

    def __init__(self, duration: "int", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.duration = duration

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["VideoChatStarted"]:
        return (
            VideoChatStarted(
                me=me,
                json=d,
                duration=d.get("duration"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class VideoChatEnded(Type_):
    """
    This object represents a service message about a video chat ended in the chat.

    Telegram Documentation: https://core.telegram.org/bots/api#videochatended

    :param duration: Video chat duration in seconds
    :type duration: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoChatEnded`
    """

    def __init__(self, duration: "int", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.duration = duration

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["VideoChatEnded"]:
        return (
            VideoChatEnded(
                me=me,
                json=d,
                duration=d.get("duration"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class VideoChatParticipantsInvited(Type_):
    """
    This object represents a service message about new members invited to a video chat.

    Telegram Documentation: https://core.telegram.org/bots/api#videochatparticipantsinvited

    :param users: New members that were invited to the video chat
    :type users: :obj:`list` of :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoChatParticipantsInvited`
    """

    def __init__(
        self, users: List["User"], me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.users = users

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["VideoChatParticipantsInvited"]:
        return (
            VideoChatParticipantsInvited(
                me=me,
                json=d,
                users=[User._parse(me=me, d=i) for i in d.get("users")]
                if d.get("users")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class GiveawayCreated(Type_):
    """
    This object represents a service message about the creation of a scheduled giveaway. Currently holds no information.
    """

    def __init__(
        self,
        chats: List["Chat"],
        winners_selection_date: "int",
        winner_count: "int",
        only_new_members: "bool" = None,
        has_public_winners: "bool" = None,
        prize_description: "str" = None,
        country_codes: List["str"] = None,
        premium_subscription_month_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.premium_subscription_month_count = premium_subscription_month_count

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["GiveawayCreated"]:
        return (
            GiveawayCreated(
                me=me,
                json=d,
                chats=[Chat._parse(me=me, d=i) for i in d.get("chats")]
                if d.get("chats")
                else None,
                winners_selection_date=d.get("winners_selection_date"),
                winner_count=d.get("winner_count"),
                only_new_members=d.get("only_new_members"),
                has_public_winners=d.get("has_public_winners"),
                prize_description=d.get("prize_description"),
                country_codes=d.get("country_codes"),
                premium_subscription_month_count=d.get(
                    "premium_subscription_month_count"
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Giveaway(Type_):
    """
    This object represents a message about a scheduled giveaway.

    Telegram documentation: https://core.telegram.org/bots/api#giveaway

    :param chats: The list of chats which the user must join to participate in the giveaway
    :type chats: :obj:`list` of :class:`Chat`

    :param winners_selection_date: Point in time (Unix timestamp) when winners of the giveaway will be selected
    :type winners_selection_date: :obj:`int`

    :param winner_count: The number of users which are supposed to be selected as winners of the giveaway
    :type winner_count: :obj:`int`

    :param only_new_members: Optional. True, if only users who join the chats after the giveaway started should be eligible to win
    :type only_new_members: :obj:`bool`

    :param has_public_winners: Optional. True, if the list of giveaway winners will be visible to everyone
    :type has_public_winners: :obj:`bool`

    :param prize_description: Optional. Description of additional giveaway prize
    :type prize_description: :obj:`str`

    :param country_codes: Optional. A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway.
    :type country_codes: :obj:`list` of :obj:`str`

    :param premium_subscription_month_count: Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for
    :type premium_subscription_month_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`Giveaway`
    """

    def __init__(
        self,
        chats: List["Chat"],
        winners_selection_date: "int",
        winner_count: "int",
        only_new_members: "bool" = None,
        has_public_winners: "bool" = None,
        prize_description: "str" = None,
        country_codes: List["str"] = None,
        premium_subscription_month_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.premium_subscription_month_count = premium_subscription_month_count

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Giveaway"]:
        return (
            Giveaway(
                me=me,
                json=d,
                chats=[Chat._parse(me=me, d=i) for i in d.get("chats")]
                if d.get("chats")
                else None,
                winners_selection_date=d.get("winners_selection_date"),
                winner_count=d.get("winner_count"),
                only_new_members=d.get("only_new_members"),
                has_public_winners=d.get("has_public_winners"),
                prize_description=d.get("prize_description"),
                country_codes=d.get("country_codes"),
                premium_subscription_month_count=d.get(
                    "premium_subscription_month_count"
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class GiveawayWinners(Type_):
    """
    This object represents a message about the completion of a giveaway with public winners.

    Telegram documentation: https://core.telegram.org/bots/api#giveawaywinners

    :param chat: The chat that created the giveaway
    :type chat: :class:`Chat`

    :param giveaway_message_id: Identifier of the messsage with the giveaway in the chat
    :type giveaway_message_id: :obj:`int`

    :param winners_selection_date: Point in time (Unix timestamp) when winners of the giveaway were selected
    :type winners_selection_date: :obj:`int`

    :param winner_count: Total number of winners in the giveaway
    :type winner_count: :obj:`int`

    :param winners: List of up to 100 winners of the giveaway
    :type winners: :obj:`list` of :class:`User`

    :param additional_chat_count: Optional. The number of other chats the user had to join in order to be eligible for the giveaway
    :type additional_chat_count: :obj:`int`

    :param premium_subscription_month_count: Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for
    :type premium_subscription_month_count: :obj:`int`

    :param unclaimed_prize_count: Optional. Number of undistributed prizes
    :type unclaimed_prize_count: :obj:`int`

    :param only_new_members: Optional. True, if only users who had joined the chats after the giveaway started were eligible to win
    :type only_new_members: :obj:`bool`

    :param was_refunded: Optional. True, if the giveaway was canceled because the payment for it was refunded
    :type was_refunded: :obj:`bool`

    :param prize_description: Optional. Description of additional giveaway prize
    :type prize_description: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`GiveawayWinners`
    """

    def __init__(
        self,
        chat: "Chat",
        giveaway_message_id: "int",
        winners_selection_date: "int",
        winner_count: "int",
        winners: List["User"],
        additional_chat_count: "int" = None,
        premium_subscription_month_count: "int" = None,
        unclaimed_prize_count: "int" = None,
        only_new_members: "bool" = None,
        was_refunded: "bool" = None,
        prize_description: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.giveaway_message_id = giveaway_message_id
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.winners = winners
        self.additional_chat_count = additional_chat_count
        self.premium_subscription_month_count = premium_subscription_month_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.only_new_members = only_new_members
        self.was_refunded = was_refunded
        self.prize_description = prize_description

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["GiveawayWinners"]:
        return (
            GiveawayWinners(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                giveaway_message_id=d.get("giveaway_message_id"),
                winners_selection_date=d.get("winners_selection_date"),
                winner_count=d.get("winner_count"),
                winners=[User._parse(me=me, d=i) for i in d.get("winners")]
                if d.get("winners")
                else None,
                additional_chat_count=d.get("additional_chat_count"),
                premium_subscription_month_count=d.get(
                    "premium_subscription_month_count"
                ),
                unclaimed_prize_count=d.get("unclaimed_prize_count"),
                only_new_members=d.get("only_new_members"),
                was_refunded=d.get("was_refunded"),
                prize_description=d.get("prize_description"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class GiveawayCompleted(Type_):
    """
    This object represents a service message about the completion of a giveaway without public winners.

    Telegram documentation: https://core.telegram.org/bots/api#giveawaycompleted

    :param winner_count: Number of winners in the giveaway
    :type winner_count: :obj:`int`

    :param unclaimed_prize_count: Optional. Number of undistributed prizes
    :type unclaimed_prize_count: :obj:`int`

    :param giveaway_message: Optional. Message with the giveaway that was completed, if it wasn't deleted
    :type giveaway_message: :class:`Message`

    :return: Instance of the class
    :rtype: :class:`GiveawayCompleted`
    """

    def __init__(
        self,
        winner_count: "int",
        unclaimed_prize_count: "int" = None,
        giveaway_message: "Message" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.winner_count = winner_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.giveaway_message = giveaway_message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["GiveawayCompleted"]:
        return (
            GiveawayCompleted(
                me=me,
                json=d,
                winner_count=d.get("winner_count"),
                unclaimed_prize_count=d.get("unclaimed_prize_count"),
                giveaway_message=Message._parse(me=me, d=d.get("giveaway_message")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class LinkPreviewOptions(Type_):
    """
    Describes the options used for link preview generation.

    Telegram documentation: https://core.telegram.org/bots/api#linkpreviewoptions

    :param is_disabled: Optional. True, if the link preview is disabled
    :type is_disabled: :obj:`bool`

    :param url: Optional. URL to use for the link preview. If empty, then the first URL found in the message text will be used
    :type url: :obj:`str`

    :param prefer_small_media: Optional. True, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
    :type prefer_small_media: :obj:`bool`

    :param prefer_large_media: Optional. True, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
    :type prefer_large_media: :obj:`bool`

    :param show_above_text: Optional. True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text
    :type show_above_text: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`LinkPreviewOptions`
    """

    def __init__(
        self,
        is_disabled: "bool" = None,
        url: "str" = None,
        prefer_small_media: "bool" = None,
        prefer_large_media: "bool" = None,
        show_above_text: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["LinkPreviewOptions"]:
        return (
            LinkPreviewOptions(
                me=me,
                json=d,
                is_disabled=d.get("is_disabled"),
                url=d.get("url"),
                prefer_small_media=d.get("prefer_small_media"),
                prefer_large_media=d.get("prefer_large_media"),
                show_above_text=d.get("show_above_text"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class UserProfilePhotos(Type_):
    """
    This object represent a user's profile pictures.

    Telegram Documentation: https://core.telegram.org/bots/api#userprofilephotos

    :param total_count: Total number of profile pictures the target user has
    :type total_count: :obj:`int`

    :param photos: Requested profile pictures (in up to 4 sizes each)
    :type photos: :obj:`list` of :obj:`list` of :class:`tgram.types.PhotoSize`

    :return: Instance of the class
    :rtype: :class:`tgram.types.UserProfilePhotos`
    """

    def __init__(
        self,
        total_count: "int",
        photos: List[List["PhotoSize"]],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.total_count = total_count
        self.photos = photos

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["UserProfilePhotos"]:
        return (
            UserProfilePhotos(
                me=me,
                json=d,
                total_count=d.get("total_count"),
                photos=[[PhotoSize._parse(None, x) for x in y] for y in d.get("photos")]
                if d.get("photos")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class File(Type_):
    """
    This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.

    Telegram Documentation: https://core.telegram.org/bots/api#file

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param file_size: Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`

    :param file_path: Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the
        file.
    :type file_path: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.File`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        file_size: "int" = None,
        file_path: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["File"]:
        return (
            File(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                file_size=d.get("file_size"),
                file_path=d.get("file_path"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class WebAppInfo(Type_):
    """
    Describes a Web App.

    Telegram Documentation: https://core.telegram.org/bots/api#webappinfo

    :param url: An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps
    :type url: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.WebAppInfo`
    """

    def __init__(self, url: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.url = url

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["WebAppInfo"]:
        return (
            WebAppInfo(
                me=me,
                json=d,
                url=d.get("url"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ReplyKeyboardMarkup(Type_):
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    .. code-block:: python3
        :caption: Example on creating ReplyKeyboardMarkup object

        from tgram.types import ReplyKeyboardMarkup, KeyboardButton

        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton('Text'))
        # or:
        markup.add('Text')

        # display this markup:
        bot.send_message(chat_id, 'Text', reply_markup=markup)

    Telegram Documentation: https://core.telegram.org/bots/api#replykeyboardmarkup

    :param keyboard: :obj:`list` of button rows, each represented by an :obj:`list` of
        :class:`tgram.types.KeyboardButton` objects
    :type keyboard: :obj:`list` of :obj:`list` of :class:`tgram.types.KeyboardButton`

    :param resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make
        the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is
        always of the same height as the app's standard keyboard.
    :type resize_keyboard: :obj:`bool`

    :param one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard
        will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can
        press a special button in the input field to see the custom keyboard again. Defaults to false.
    :type one_time_keyboard: :obj:`bool`

    :param input_field_placeholder: Optional. The placeholder to be shown in the input field when the keyboard is
        active; 1-64 characters
    :type input_field_placeholder: :obj:`str`

    :param selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets:
        1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message
        in the same chat and forum topic, sender of the original message. Example: A user requests to change the bot's
        language, bot replies to the request with a keyboard to select the new language. Other users in the group don't
        see the keyboard.
    :type selective: :obj:`bool`

    :param is_persistent: Optional. Use this parameter if you want to show the keyboard to specific users only.
        Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a
        reply (has reply_to_message_id), sender of the original message.

        Example: A user requests to change the bot's language, bot replies to the request with a keyboard to
        select the new language. Other users in the group don't see the keyboard.

    :return: Instance of the class
    :rtype: :class:`tgram.types.ReplyKeyboardMarkup`
    """

    def __init__(
        self,
        keyboard: List[List["KeyboardButton"]],
        is_persistent: "bool" = None,
        resize_keyboard: "bool" = None,
        one_time_keyboard: "bool" = None,
        input_field_placeholder: "str" = None,
        selective: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ReplyKeyboardMarkup"]:
        return (
            ReplyKeyboardMarkup(
                me=me,
                json=d,
                keyboard=[
                    [KeyboardButton._parse(me=me, d=x) for x in i]
                    for i in d.get("keyboard")
                ]
                if d.get("keyboard")
                else None,
                is_persistent=d.get("is_persistent"),
                resize_keyboard=d.get("resize_keyboard"),
                one_time_keyboard=d.get("one_time_keyboard"),
                input_field_placeholder=d.get("input_field_placeholder"),
                selective=d.get("selective"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class KeyboardButton(Type_):
    """
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive.

    Telegram Documentation: https://core.telegram.org/bots/api#keyboardbutton

    :param text: Text of the button. If none of the optional fields are used, it will be sent as a message when the button is
        pressed
    :type text: :obj:`str`

    :param request_contact: Optional. If True, the user's phone number will be sent as a contact when the button is
        pressed. Available in private chats only.
    :type request_contact: :obj:`bool`

    :param request_location: Optional. If True, the user's current location will be sent when the button is pressed.
        Available in private chats only.
    :type request_location: :obj:`bool`

    :param request_poll: Optional. If specified, the user will be asked to create a poll and send it to the bot when the
        button is pressed. Available in private chats only.
    :type request_poll: :class:`tgram.types.KeyboardButtonPollType`

    :param web_app: Optional. If specified, the described Web App will be launched when the button is pressed. The Web App
        will be able to send a “web_app_data” service message. Available in private chats only.
    :type web_app: :class:`tgram.types.WebAppInfo`

    :param request_user: deprecated
    :type request_user: :class:`tgram.types.KeyboardButtonRequestUser`

    :param request_users: Optional. If specified, pressing the button will open a list of suitable users.
        Identifiers of selected users will be sent to the bot in a “users_shared” service message. Available in private chats only.
    :type request_users: :class:`tgram.types.KeyboardButtonRequestUsers`

    :param request_chat: Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will
        send its identifier to the bot in a “chat_shared” service message. Available in private chats only.
    :type request_chat: :class:`tgram.types.KeyboardButtonRequestChat`

    :return: Instance of the class
    :rtype: :class:`tgram.types.KeyboardButton`
    """

    def __init__(
        self,
        text: "str",
        request_users: "KeyboardButtonRequestUsers" = None,
        request_chat: "KeyboardButtonRequestChat" = None,
        request_contact: "bool" = None,
        request_location: "bool" = None,
        request_poll: "KeyboardButtonPollType" = None,
        web_app: "WebAppInfo" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["KeyboardButton"]:
        return (
            KeyboardButton(
                me=me,
                json=d,
                text=d.get("text"),
                request_users=KeyboardButtonRequestUsers._parse(
                    me=me, d=d.get("request_users")
                ),
                request_chat=KeyboardButtonRequestChat._parse(
                    me=me, d=d.get("request_chat")
                ),
                request_contact=d.get("request_contact"),
                request_location=d.get("request_location"),
                request_poll=KeyboardButtonPollType._parse(
                    me=me, d=d.get("request_poll")
                ),
                web_app=WebAppInfo._parse(me=me, d=d.get("web_app")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class KeyboardButtonRequestUsers(Type_):
    """
    This object defines the criteria used to request a suitable user.
    The identifier of the selected user will be shared with the bot when the corresponding button is pressed.

    Telegram documentation: https://core.telegram.org/bots/api#keyboardbuttonrequestusers

    :param request_id: Signed 32-bit identifier of the request, which will be received back in the UsersShared object.
        Must be unique within the message
    :type request_id: :obj:`int`

    :param user_is_bot: Optional. Pass True to request a bot, pass False to request a regular user.
        If not specified, no additional restrictions are applied.
    :type user_is_bot: :obj:`bool`

    :param user_is_premium: Optional. Pass True to request a premium user, pass False to request a non-premium user.
        If not specified, no additional restrictions are applied.
    :type user_is_premium: :obj:`bool`

    :param max_quantity: Optional. The maximum number of users to be selected; 1-10. Defaults to 1.
    :type max_quantity: :obj:`int`

    :param request_name: Optional. Request name
    :type request_name: :obj:`bool`

    :param request_username: Optional. Request username
    :type request_username: :obj:`bool`

    :param request_photo: Optional. Request photo
    :type request_photo: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.KeyboardButtonRequestUsers`
    """

    def __init__(
        self,
        user_is_bot: "bool" = None,
        user_is_premium: "bool" = None,
        max_quantity: "int" = None,
        request_name: "bool" = None,
        request_username: "bool" = None,
        request_photo: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_id = random.randint(10000, 99999)
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity
        self.request_name = request_name
        self.request_username = request_username
        self.request_photo = request_photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["KeyboardButtonRequestUsers"]:
        return (
            KeyboardButtonRequestUsers(
                me=me,
                json=d,
                user_is_bot=d.get("user_is_bot"),
                user_is_premium=d.get("user_is_premium"),
                max_quantity=d.get("max_quantity"),
                request_name=d.get("request_name"),
                request_username=d.get("request_username"),
                request_photo=d.get("request_photo"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class KeyboardButtonRequestChat(Type_):
    """
    This object defines the criteria used to request a suitable chat. The identifier of the selected chat will
    be shared with the bot when the corresponding button is pressed.

    Telegram documentation: https://core.telegram.org/bots/api#keyboardbuttonrequestchat

    :param request_id: Signed 32-bit identifier of the request, which will be received back in the ChatShared object.
        Must be unique within the message
    :type request_id: :obj:`int`

    :param chat_is_channel: Pass True to request a channel chat, pass False to request a group or a supergroup chat.
    :type chat_is_channel: :obj:`bool`

    :param chat_is_forum: Optional. Pass True to request a forum supergroup, pass False to request a non-forum chat.
        If not specified, no additional restrictions are applied.
    :type chat_is_forum: :obj:`bool`

    :param chat_has_username: Optional. Pass True to request a supergroup or a channel with a username, pass False to request a
        chat without a username. If not specified, no additional restrictions are applied.
    :type chat_has_username: :obj:`bool`

    :param chat_is_created: Optional. Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied.
    :type chat_is_created: :obj:`bool`

    :param user_administrator_rights: Optional. A JSON-serialized object listing the required administrator rights of the user in the chat.
        The rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied.
    :type user_administrator_rights: :class:`tgram.types.ChatAdministratorRights`

    :param bot_administrator_rights: Optional. A JSON-serialized object listing the required administrator rights of the bot in the chat.
        The rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied.
    :type bot_administrator_rights: :class:`tgram.types.ChatAdministratorRights`

    :param bot_is_member: Optional. Pass True to request a chat where the bot is a member. Otherwise, no additional restrictions are applied.
    :type bot_is_member: :obj:`bool`

    :param request_title: Optional. Request title
    :type request_title: :obj:`bool`

    :param request_photo: Optional. Request photo
    :type request_photo: :obj:`bool`

    :param request_username: Optional. Request username
    :type request_username: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.KeyboardButtonRequestChat`
    """

    def __init__(
        self,
        chat_is_channel: "bool",
        chat_is_forum: "bool" = None,
        chat_has_username: "bool" = None,
        chat_is_created: "bool" = None,
        user_administrator_rights: "ChatAdministratorRights" = None,
        bot_administrator_rights: "ChatAdministratorRights" = None,
        bot_is_member: "bool" = None,
        request_title: "bool" = None,
        request_username: "bool" = None,
        request_photo: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_id = random.randint(10000, 99999)
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.chat_is_created = chat_is_created
        self.user_administrator_rights = user_administrator_rights
        self.bot_administrator_rights = bot_administrator_rights
        self.bot_is_member = bot_is_member
        self.request_title = request_title
        self.request_username = request_username
        self.request_photo = request_photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["KeyboardButtonRequestChat"]:
        return (
            KeyboardButtonRequestChat(
                me=me,
                json=d,
                chat_is_channel=d.get("chat_is_channel"),
                chat_is_forum=d.get("chat_is_forum"),
                chat_has_username=d.get("chat_has_username"),
                chat_is_created=d.get("chat_is_created"),
                user_administrator_rights=ChatAdministratorRights._parse(
                    me=me, d=d.get("user_administrator_rights")
                ),
                bot_administrator_rights=ChatAdministratorRights._parse(
                    me=me, d=d.get("bot_administrator_rights")
                ),
                bot_is_member=d.get("bot_is_member"),
                request_title=d.get("request_title"),
                request_username=d.get("request_username"),
                request_photo=d.get("request_photo"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class KeyboardButtonPollType(Type_):
    """
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    Telegram Documentation: https://core.telegram.org/bots/api#keyboardbuttonpolltype

    :param type: Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.KeyboardButtonPollType`
    """

    def __init__(
        self, type: "str" = None, me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["KeyboardButtonPollType"]:
        return (
            KeyboardButtonPollType(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ReplyKeyboardRemove(Type_):
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    Telegram Documentation: https://core.telegram.org/bots/api#replykeyboardremove

    :param remove_keyboard: Requests clients to remove the custom keyboard (user will not be able to summon this
        keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in
        ReplyKeyboardMarkup)
        Note that this parameter is set to True by default by the library. You cannot modify it.
    :type remove_keyboard: :obj:`bool`

    :param selective: Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets:
        1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has
        reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation
        message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options
        to users who haven't voted yet.
    :type selective: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ReplyKeyboardRemove`
    """

    def __init__(
        self,
        remove_keyboard: "bool",
        selective: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.remove_keyboard = remove_keyboard
        self.selective = selective

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ReplyKeyboardRemove"]:
        return (
            ReplyKeyboardRemove(
                me=me,
                json=d,
                remove_keyboard=d.get("remove_keyboard"),
                selective=d.get("selective"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineKeyboardMarkup(Type_):
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinekeyboardmarkup

    :param keyboard: :obj:`list` of button rows, each represented by an :obj:`list` of
        :class:`tgram.types.InlineKeyboardButton` objects
    :type keyboard: :obj:`list` of :obj:`list` of :class:`tgram.types.InlineKeyboardButton`

    :param row_width: number of :class:`tgram.types.InlineKeyboardButton` objects on each row
    :type row_width: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineKeyboardMarkup`
    """

    def __init__(
        self,
        inline_keyboard: List[List["InlineKeyboardButton"]],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.inline_keyboard = inline_keyboard

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineKeyboardMarkup"]:
        return (
            InlineKeyboardMarkup(
                me=me,
                json=d,
                inline_keyboard=[
                    [InlineKeyboardButton._parse(me=me, d=x) for x in i]
                    for i in d.get("inline_keyboard")
                ]
                if d.get("inline_keyboard")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineKeyboardButton(Type_):
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinekeyboardbutton

    :param text: Label text on the button
    :type text: :obj:`str`

    :param url: Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be
        used to mention a user by their ID without using a username, if this is allowed by their privacy settings.
    :type url: :obj:`str`

    :param callback_data: Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    :type callback_data: :obj:`str`

    :param web_app: Optional. Description of the Web App that will be launched when the user presses the button. The Web
        App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only
        in private chats between a user and the bot.
    :type web_app: :class:`tgram.types.WebAppInfo`

    :param login_url: Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for
        the Telegram Login Widget.
    :type login_url: :class:`tgram.types.LoginUrl`

    :param switch_inline_query: Optional. If set, pressing the button will prompt the user to select one of their chats,
        open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which
        case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline
        mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions - in
        this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    :type switch_inline_query: :obj:`str`

    :param switch_inline_query_current_chat: Optional. If set, pressing the button will insert the bot's username
        and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username
        will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting
        something from multiple options.
    :type switch_inline_query_current_chat: :obj:`str`

    :param switch_inline_query_chosen_chat: Optional. If set, pressing the button will prompt the user to select one of their chats of the
        specified type, open that chat and insert the bot's username and the specified inline query in the input field
    :type switch_inline_query_chosen_chat: :class:`tgram.types.SwitchInlineQueryChosenChat`

    :param callback_game: Optional. Description of the game that will be launched when the user presses the
        button. NOTE: This type of button must always be the first button in the first row.
    :type callback_game: :class:`tgram.types.CallbackGame`

    :param pay: Optional. Specify True, to send a Pay button. NOTE: This type of button must always be the first button in
        the first row and can only be used in invoice messages.
    :type pay: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineKeyboardButton`
    """

    def __init__(
        self,
        text: "str",
        url: "str" = None,
        callback_data: "str" = None,
        web_app: "WebAppInfo" = None,
        login_url: "LoginUrl" = None,
        switch_inline_query: "str" = None,
        switch_inline_query_current_chat: "str" = None,
        switch_inline_query_chosen_chat: "SwitchInlineQueryChosenChat" = None,
        callback_game: "CallbackGame" = None,
        pay: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.callback_game = callback_game
        self.pay = pay

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineKeyboardButton"]:
        return (
            InlineKeyboardButton(
                me=me,
                json=d,
                text=d.get("text"),
                url=d.get("url"),
                callback_data=d.get("callback_data"),
                web_app=WebAppInfo._parse(me=me, d=d.get("web_app")),
                login_url=LoginUrl._parse(me=me, d=d.get("login_url")),
                switch_inline_query=d.get("switch_inline_query"),
                switch_inline_query_current_chat=d.get(
                    "switch_inline_query_current_chat"
                ),
                switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat._parse(
                    me=me, d=d.get("switch_inline_query_chosen_chat")
                ),
                callback_game=CallbackGame._parse(me=me, d=d.get("callback_game")),
                pay=d.get("pay"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class LoginUrl(Type_):
    """
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:

    Telegram Documentation: https://core.telegram.org/bots/api#loginurl

    :param url: An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed.
        If the user refuses to provide authorization data, the original URL without information about the user will be
        opened. The data added is the same as described in Receiving authorization data. NOTE: You must always check the hash
        of the received data to verify the authentication and the integrity of the data as described in Checking
        authorization.
    :type url: :obj:`str`

    :param forward_text: Optional. New text of the button in forwarded messages.
    :type forward_text: :obj:`str`

    :param bot_username: Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for
        more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the
        domain linked with the bot. See Linking your domain to the bot for more details.
    :type bot_username: :obj:`str`

    :param request_write_access: Optional. Pass True to request the permission for your bot to send messages to the
        user.
    :type request_write_access: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.LoginUrl`
    """

    def __init__(
        self,
        url: "str",
        forward_text: "str" = None,
        bot_username: "str" = None,
        request_write_access: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["LoginUrl"]:
        return (
            LoginUrl(
                me=me,
                json=d,
                url=d.get("url"),
                forward_text=d.get("forward_text"),
                bot_username=d.get("bot_username"),
                request_write_access=d.get("request_write_access"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class SwitchInlineQueryChosenChat(Type_):
    """
    Represents an inline button that switches the current user to inline mode in a chosen chat,
    with an optional default inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinekeyboardbutton

    :param query: Optional. The default inline query to be inserted in the input field.
                  If left empty, only the bot's username will be inserted
    :type query: :obj:`str`

    :param allow_user_chats: Optional. True, if private chats with users can be chosen
    :type allow_user_chats: :obj:`bool`

    :param allow_bot_chats: Optional. True, if private chats with bots can be chosen
    :type allow_bot_chats: :obj:`bool`

    :param allow_group_chats: Optional. True, if group and supergroup chats can be chosen
    :type allow_group_chats: :obj:`bool`

    :param allow_channel_chats: Optional. True, if channel chats can be chosen
    :type allow_channel_chats: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`SwitchInlineQueryChosenChat`
    """

    def __init__(
        self,
        query: "str" = None,
        allow_user_chats: "bool" = None,
        allow_bot_chats: "bool" = None,
        allow_group_chats: "bool" = None,
        allow_channel_chats: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["SwitchInlineQueryChosenChat"]:
        return (
            SwitchInlineQueryChosenChat(
                me=me,
                json=d,
                query=d.get("query"),
                allow_user_chats=d.get("allow_user_chats"),
                allow_bot_chats=d.get("allow_bot_chats"),
                allow_group_chats=d.get("allow_group_chats"),
                allow_channel_chats=d.get("allow_channel_chats"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class CallbackQuery(Type_, CallbackB):
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    Telegram Documentation: https://core.telegram.org/bots/api#callbackquery

    :param id: Unique identifier for this query
    :type id: :obj:`str`

    :param from_user: Sender
    :type from_user: :class:`tgram.types.User`

    :param message: Optional. Message sent by the bot with the callback button that originated the query
    :type message: :class:`tgram.types.Message` or :class:`tgram.types.InaccessibleMessage`

    :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated the
        query.
    :type inline_message_id: :obj:`str`

    :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback
        button was sent. Useful for high scores in games.
    :type chat_instance: :obj:`str`

    :param data: Optional. Data associated with the callback button. Be aware that the message originated the query can
        contain no callback buttons with this data.
    :type data: :obj:`str`

    :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for the game
    :type game_short_name: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.CallbackQuery`
    """

    def __init__(
        self,
        id: "str",
        from_user: "User",
        chat_instance: "str",
        message: "Message" = None,
        inline_message_id: "str" = None,
        data: "str" = None,
        game_short_name: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["CallbackQuery"]:
        return (
            CallbackQuery(
                me=me,
                json=d,
                id=d.get("id"),
                from_user=User._parse(me=me, d=d.get("from")),
                chat_instance=d.get("chat_instance"),
                message=Message._parse(me=me, d=d.get("message")),
                inline_message_id=d.get("inline_message_id"),
                data=d.get("data"),
                game_short_name=d.get("game_short_name"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ForceReply(Type_):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Telegram Documentation: https://core.telegram.org/bots/api#forcereply

    :param force_reply: Shows reply interface to the user, as if they manually selected the bot's message and tapped
        'Reply'
    :type force_reply: :obj:`bool`

    :param input_field_placeholder: Optional. The placeholder to be shown in the input field when the reply is active;
        1-64 characters
    :type input_field_placeholder: :obj:`str`

    :param selective: Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users
        that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same
        chat and forum topic, sender of the original message.
    :type selective: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ForceReply`
    """

    def __init__(
        self,
        force_reply: "bool",
        input_field_placeholder: "str" = None,
        selective: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ForceReply"]:
        return (
            ForceReply(
                me=me,
                json=d,
                force_reply=d.get("force_reply"),
                input_field_placeholder=d.get("input_field_placeholder"),
                selective=d.get("selective"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatPhoto(Type_):
    """
    This object represents a chat photo.

    Telegram Documentation: https://core.telegram.org/bots/api#chatphoto

    :param small_file_id: File identifier of small (160x160) chat photo. This file_id can be used only for photo
        download and only for as long as the photo is not changed.
    :type small_file_id: :obj:`str`

    :param small_file_unique_id: Unique file identifier of small (160x160) chat photo, which is supposed to be the same
        over time and for different bots. Can't be used to download or reuse the file.
    :type small_file_unique_id: :obj:`str`

    :param big_file_id: File identifier of big (640x640) chat photo. This file_id can be used only for photo download and
        only for as long as the photo is not changed.
    :type big_file_id: :obj:`str`

    :param big_file_unique_id: Unique file identifier of big (640x640) chat photo, which is supposed to be the same over
        time and for different bots. Can't be used to download or reuse the file.
    :type big_file_unique_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatPhoto`
    """

    def __init__(
        self,
        small_file_id: "str",
        small_file_unique_id: "str",
        big_file_id: "str",
        big_file_unique_id: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatPhoto"]:
        return (
            ChatPhoto(
                me=me,
                json=d,
                small_file_id=d.get("small_file_id"),
                small_file_unique_id=d.get("small_file_unique_id"),
                big_file_id=d.get("big_file_id"),
                big_file_unique_id=d.get("big_file_unique_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatInviteLink(Type_):
    """
    Represents an invite link for a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chatinvitelink

    :param invite_link: The invite link. If the link was created by another chat administrator, then the second part of
        the link will be replaced with “…”.
    :type invite_link: :obj:`str`

    :param creator: Creator of the link
    :type creator: :class:`tgram.types.User`

    :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators
    :type creates_join_request: :obj:`bool`

    :param is_primary: True, if the link is primary
    :type is_primary: :obj:`bool`

    :param is_revoked: True, if the link is revoked
    :type is_revoked: :obj:`bool`

    :param name: Optional. Invite link name
    :type name: :obj:`str`

    :param expire_date: Optional. Point in time (Unix timestamp) when the link will expire or has been expired
    :type expire_date: :obj:`int`

    :param member_limit: Optional. The maximum number of users that can be members of the chat simultaneously after
        joining the chat via this invite link; 1-99999
    :type member_limit: :obj:`int`

    :param pending_join_request_count: Optional. Number of pending join requests created using this link
    :type pending_join_request_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatInviteLink`
    """

    def __init__(
        self,
        invite_link: "str",
        creator: "User",
        creates_join_request: "bool",
        is_primary: "bool",
        is_revoked: "bool",
        name: "str" = None,
        expire_date: "int" = None,
        member_limit: "int" = None,
        pending_join_request_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatInviteLink"]:
        return (
            ChatInviteLink(
                me=me,
                json=d,
                invite_link=d.get("invite_link"),
                creator=User._parse(me=me, d=d.get("creator")),
                creates_join_request=d.get("creates_join_request"),
                is_primary=d.get("is_primary"),
                is_revoked=d.get("is_revoked"),
                name=d.get("name"),
                expire_date=d.get("expire_date"),
                member_limit=d.get("member_limit"),
                pending_join_request_count=d.get("pending_join_request_count"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatAdministratorRights(Type_):
    """
    Represents the rights of an administrator in a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chatadministratorrights

    :param is_anonymous: True, if the user's presence in the chat is hidden
    :type is_anonymous: :obj:`bool`

    :param can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message
        statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode.
        Implied by any other administrator privilege
    :type can_manage_chat: :obj:`bool`

    :param can_delete_messages: True, if the administrator can delete messages of other users
    :type can_delete_messages: :obj:`bool`

    :param can_manage_video_chats: True, if the administrator can manage video chats
    :type can_manage_video_chats: :obj:`bool`

    :param can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    :type can_restrict_members: :obj:`bool`

    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own
        privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that
        were appointed by the user)
    :type can_promote_members: :obj:`bool`

    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :type can_change_info: :obj:`bool`

    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :type can_invite_users: :obj:`bool`

    :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only
    :type can_post_messages: :obj:`bool`

    :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin
        messages; channels only
    :type can_edit_messages: :obj:`bool`

    :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only
    :type can_pin_messages: :obj:`bool`

    :param can_manage_topics: Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; supergroups only
    :type can_manage_topics: :obj:`bool`

    :param can_post_stories: Optional. True, if the administrator can post channel stories
    :type can_post_stories: :obj:`bool`

    :param can_edit_stories: Optional. True, if the administrator can edit stories
    :type can_edit_stories: :obj:`bool`

    :param can_delete_stories: Optional. True, if the administrator can delete stories of other users
    :type can_delete_stories: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatAdministratorRights`
    """

    def __init__(
        self,
        is_anonymous: "bool",
        can_manage_chat: "bool",
        can_delete_messages: "bool",
        can_manage_video_chats: "bool",
        can_restrict_members: "bool",
        can_promote_members: "bool",
        can_change_info: "bool",
        can_invite_users: "bool",
        can_post_stories: "bool",
        can_edit_stories: "bool",
        can_delete_stories: "bool",
        can_post_messages: "bool" = None,
        can_edit_messages: "bool" = None,
        can_pin_messages: "bool" = None,
        can_manage_topics: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatAdministratorRights"]:
        return (
            ChatAdministratorRights(
                me=me,
                json=d,
                is_anonymous=d.get("is_anonymous"),
                can_manage_chat=d.get("can_manage_chat"),
                can_delete_messages=d.get("can_delete_messages"),
                can_manage_video_chats=d.get("can_manage_video_chats"),
                can_restrict_members=d.get("can_restrict_members"),
                can_promote_members=d.get("can_promote_members"),
                can_change_info=d.get("can_change_info"),
                can_invite_users=d.get("can_invite_users"),
                can_post_stories=d.get("can_post_stories"),
                can_edit_stories=d.get("can_edit_stories"),
                can_delete_stories=d.get("can_delete_stories"),
                can_post_messages=d.get("can_post_messages"),
                can_edit_messages=d.get("can_edit_messages"),
                can_pin_messages=d.get("can_pin_messages"),
                can_manage_topics=d.get("can_manage_topics"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatMemberUpdated(Type_):
    """
    This object represents changes in the status of a chat member.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberupdated

    :param chat: Chat the user belongs to
    :type chat: :class:`tgram.types.Chat`

    :param from_user: Performer of the action, which resulted in the change
    :type from_user: :class:`tgram.types.User`

    :param date: Date the change was done in Unix time
    :type date: :obj:`int`

    :param old_chat_member: Previous information about the chat member
    :type old_chat_member: :class:`tgram.types.ChatMember`

    :param new_chat_member: New information about the chat member
    :type new_chat_member: :class:`tgram.types.ChatMember`

    :param invite_link: Optional. Chat invite link, which was used by the user to join the chat; for joining by invite
        link events only.
    :type invite_link: :class:`tgram.types.ChatInviteLink`

    :param via_join_request: Optional. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator
    :type via_join_request: :obj:`bool`

    :param via_chat_folder_invite_link: Optional. True, if the user joined the chat via a chat folder invite link
    :type via_chat_folder_invite_link: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberUpdated`
    """

    def __init__(
        self,
        chat: "Chat",
        from_user: "User",
        date: "int",
        old_chat_member: Union[
            "ChatMemberOwner",
            "ChatMemberAdministrator",
            "ChatMemberMember",
            "ChatMemberRestricted",
            "ChatMemberBanned",
            "ChatMemberLeft",
        ],
        new_chat_member: Union[
            "ChatMemberOwner",
            "ChatMemberAdministrator",
            "ChatMemberMember",
            "ChatMemberRestricted",
            "ChatMemberBanned",
            "ChatMemberLeft",
        ],
        invite_link: "ChatInviteLink" = None,
        via_join_request: "bool" = None,
        via_chat_folder_invite_link: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_join_request = via_join_request
        self.via_chat_folder_invite_link = via_chat_folder_invite_link

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatMemberUpdated"]:
        return (
            ChatMemberUpdated(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                from_user=User._parse(me=me, d=d.get("from")),
                date=d.get("date"),
                old_chat_member=ChatMember._parse(me=me, d=d.get("old_chat_member")),
                new_chat_member=ChatMember._parse(me=me, d=d.get("new_chat_member")),
                invite_link=ChatInviteLink._parse(me=me, d=d.get("invite_link")),
                via_join_request=d.get("via_join_request"),
                via_chat_folder_invite_link=d.get("via_chat_folder_invite_link"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatMember(Type_):
    """
    This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are supported:

    * :class:`tgram.types.ChatMemberOwner`
    * :class:`tgram.types.ChatMemberAdministrator`
    * :class:`tgram.types.ChatMemberMember`
    * :class:`tgram.types.ChatMemberRestricted`
    * :class:`tgram.types.ChatMemberLeft`
    * :class:`tgram.types.ChatMemberBanned`

    Telegram Documentation: https://core.telegram.org/bots/api#chatmember
    """

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional[
        Union[
            "ChatMemberOwner",
            "ChatMemberAdministrator",
            "ChatMemberMember",
            "ChatMemberRestricted",
            "ChatMemberBanned",
            "ChatMemberLeft",
        ]
    ]:
        return (
            (
                ChatMemberOwner._parse(me=me, d=d)
                if d.get("status") == "creator"
                else ChatMemberAdministrator._parse(me=me, d=d)
                if d.get("status") == "administrator"
                else ChatMemberMember._parse(me=me, d=d)
                if d.get("status") == "member"
                else ChatMemberRestricted._parse(me=me, d=d)
                if d.get("status") == "restricted"
                else ChatMemberLeft._parse(me=me, d=d)
                if d.get("status") == "left"
                else ChatMemberBanned._parse(me=me, d=d)
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatMemberOwner(Type_):
    """
    Represents a chat member that owns the chat and has all administrator privileges.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberowner

    :param status: The member's status in the chat, always “creator”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param is_anonymous: True, if the user's presence in the chat is hidden
    :type is_anonymous: :obj:`bool`

    :param custom_title: Optional. Custom title for this user
    :type custom_title: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberOwner`
    """

    def __init__(
        self,
        status: "str",
        user: "User",
        is_anonymous: "bool",
        custom_title: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatMemberOwner"]:
        return (
            ChatMemberOwner(
                me=me,
                json=d,
                status=d.get("status"),
                user=User._parse(me=me, d=d.get("user")),
                is_anonymous=d.get("is_anonymous"),
                custom_title=d.get("custom_title"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatMemberAdministrator(Type_):
    """
    Represents a chat member that has some additional privileges.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberadministrator

    :param status: The member's status in the chat, always “administrator”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param can_be_edited: True, if the bot is allowed to edit administrator privileges of that user
    :type can_be_edited: :obj:`bool`

    :param is_anonymous: True, if the user's presence in the chat is hidden
    :type is_anonymous: :obj:`bool`

    :param can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message
        statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode.
        Implied by any other administrator privilege
    :type can_manage_chat: :obj:`bool`

    :param can_delete_messages: True, if the administrator can delete messages of other users
    :type can_delete_messages: :obj:`bool`

    :param can_manage_video_chats: True, if the administrator can manage video chats
    :type can_manage_video_chats: :obj:`bool`

    :param can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    :type can_restrict_members: :obj:`bool`

    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own
        privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that
        were appointed by the user)
    :type can_promote_members: :obj:`bool`

    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :type can_change_info: :obj:`bool`

    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :type can_invite_users: :obj:`bool`

    :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only
    :type can_post_messages: :obj:`bool`

    :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin
        messages; channels only
    :type can_edit_messages: :obj:`bool`

    :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only
    :type can_pin_messages: :obj:`bool`

    :param can_manage_topics: Optional. True, if the user is allowed to create, rename, close, and reopen forum topics;
        supergroups only
    :type can_manage_topics: :obj:`bool`

    :param custom_title: Optional. Custom title for this user
    :type custom_title: :obj:`str`

    :param can_post_stories: Optional. True, if the administrator can post channel stories
    :type can_post_stories: :obj:`bool`

    :param can_edit_stories: Optional. True, if the administrator can edit stories
    :type can_edit_stories: :obj:`bool`

    :param can_delete_stories: Optional. True, if the administrator can delete stories of other users
    :type can_delete_stories: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberAdministrator`
    """

    def __init__(
        self,
        status: "str",
        user: "User",
        can_be_edited: "bool",
        is_anonymous: "bool",
        can_manage_chat: "bool",
        can_delete_messages: "bool",
        can_manage_video_chats: "bool",
        can_restrict_members: "bool",
        can_promote_members: "bool",
        can_change_info: "bool",
        can_invite_users: "bool",
        can_post_stories: "bool",
        can_edit_stories: "bool",
        can_delete_stories: "bool",
        can_post_messages: "bool" = None,
        can_edit_messages: "bool" = None,
        can_pin_messages: "bool" = None,
        can_manage_topics: "bool" = None,
        custom_title: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user
        self.can_be_edited = can_be_edited
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.custom_title = custom_title

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatMemberAdministrator"]:
        return (
            ChatMemberAdministrator(
                me=me,
                json=d,
                status=d.get("status"),
                user=User._parse(me=me, d=d.get("user")),
                can_be_edited=d.get("can_be_edited"),
                is_anonymous=d.get("is_anonymous"),
                can_manage_chat=d.get("can_manage_chat"),
                can_delete_messages=d.get("can_delete_messages"),
                can_manage_video_chats=d.get("can_manage_video_chats"),
                can_restrict_members=d.get("can_restrict_members"),
                can_promote_members=d.get("can_promote_members"),
                can_change_info=d.get("can_change_info"),
                can_invite_users=d.get("can_invite_users"),
                can_post_stories=d.get("can_post_stories"),
                can_edit_stories=d.get("can_edit_stories"),
                can_delete_stories=d.get("can_delete_stories"),
                can_post_messages=d.get("can_post_messages"),
                can_edit_messages=d.get("can_edit_messages"),
                can_pin_messages=d.get("can_pin_messages"),
                can_manage_topics=d.get("can_manage_topics"),
                custom_title=d.get("custom_title"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatMemberMember(Type_):
    """
    Represents a chat member that has no additional privileges or restrictions.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmembermember

    :param status: The member's status in the chat, always “member”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberMember`
    """

    def __init__(
        self, status: "str", user: "User", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatMemberMember"]:
        return (
            ChatMemberMember(
                me=me,
                json=d,
                status=d.get("status"),
                user=User._parse(me=me, d=d.get("user")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatMemberRestricted(Type_):
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberrestricted

    :param status: The member's status in the chat, always “restricted”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param is_member: True, if the user is a member of the chat at the moment of the request
    :type is_member: :obj:`bool`

    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :type can_change_info: :obj:`bool`

    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :type can_invite_users: :obj:`bool`

    :param can_pin_messages: True, if the user is allowed to pin messages
    :type can_pin_messages: :obj:`bool`

    :param can_manage_topics: True, if the user is allowed to create forum topics
    :type can_manage_topics: :obj:`bool`

    :param can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues
    :type can_send_messages: :obj:`bool`

    :param can_send_audios: True, if the user is allowed to send audios
    :type can_send_audios: :obj:`bool`

    :param can_send_documents: True, if the user is allowed to send documents
    :type can_send_documents: :obj:`bool`

    :param can_send_photos: True, if the user is allowed to send photos
    :type can_send_photos: :obj:`bool`

    :param can_send_videos: True, if the user is allowed to send videos
    :type can_send_videos: :obj:`bool`

    :param can_send_video_notes: True, if the user is allowed to send video notes
    :type can_send_video_notes: :obj:`bool`

    :param can_send_voice_notes: True, if the user is allowed to send voice notes
    :type can_send_voice_notes: :obj:`bool`

    :param can_send_polls: True, if the user is allowed to send polls
    :type can_send_polls: :obj:`bool`

    :param can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline
        bots
    :type can_send_other_messages: :obj:`bool`

    :param can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages
    :type can_add_web_page_previews: :obj:`bool`

    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted
        forever
    :type until_date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberRestricted`
    """

    def __init__(
        self,
        status: "str",
        user: "User",
        is_member: "bool",
        can_send_messages: "bool",
        can_send_audios: "bool",
        can_send_documents: "bool",
        can_send_photos: "bool",
        can_send_videos: "bool",
        can_send_video_notes: "bool",
        can_send_voice_notes: "bool",
        can_send_polls: "bool",
        can_send_other_messages: "bool",
        can_add_web_page_previews: "bool",
        can_change_info: "bool",
        can_invite_users: "bool",
        can_pin_messages: "bool",
        can_manage_topics: "bool",
        until_date: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user
        self.is_member = is_member
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.until_date = until_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatMemberRestricted"]:
        return (
            ChatMemberRestricted(
                me=me,
                json=d,
                status=d.get("status"),
                user=User._parse(me=me, d=d.get("user")),
                is_member=d.get("is_member"),
                can_send_messages=d.get("can_send_messages"),
                can_send_audios=d.get("can_send_audios"),
                can_send_documents=d.get("can_send_documents"),
                can_send_photos=d.get("can_send_photos"),
                can_send_videos=d.get("can_send_videos"),
                can_send_video_notes=d.get("can_send_video_notes"),
                can_send_voice_notes=d.get("can_send_voice_notes"),
                can_send_polls=d.get("can_send_polls"),
                can_send_other_messages=d.get("can_send_other_messages"),
                can_add_web_page_previews=d.get("can_add_web_page_previews"),
                can_change_info=d.get("can_change_info"),
                can_invite_users=d.get("can_invite_users"),
                can_pin_messages=d.get("can_pin_messages"),
                can_manage_topics=d.get("can_manage_topics"),
                until_date=d.get("until_date"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatMemberLeft(Type_):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberleft

    :param status: The member's status in the chat, always “left”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberLeft`
    """

    def __init__(
        self, status: "str", user: "User", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatMemberLeft"]:
        return (
            ChatMemberLeft(
                me=me,
                json=d,
                status=d.get("status"),
                user=User._parse(me=me, d=d.get("user")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatMemberBanned(Type_):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberbanned

    :param status: The member's status in the chat, always “kicked”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned
        forever
    :type until_date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberBanned`
    """

    def __init__(
        self,
        status: "str",
        user: "User",
        until_date: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user
        self.until_date = until_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatMemberBanned"]:
        return (
            ChatMemberBanned(
                me=me,
                json=d,
                status=d.get("status"),
                user=User._parse(me=me, d=d.get("user")),
                until_date=d.get("until_date"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatJoinRequest(Type_):
    """
    Represents a join request sent to a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chatjoinrequest

    :param chat: Chat to which the request was sent
    :type chat: :class:`tgram.types.Chat`

    :param from_user: User that sent the join request
    :type from_user: :class:`tgram.types.User`

    :param user_chat_id: Optional. Identifier of a private chat with the user who sent the join request.
        This number may have more than 32 significant bits and some programming languages may have difficulty/silent
        defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision
        float type are safe for storing this identifier. The bot can use this identifier for 24 hours to send messages
        until the join request is processed, assuming no other administrator contacted the user.
    :type user_chat_id: :obj:`int`

    :param date: Date the request was sent in Unix time
    :type date: :obj:`int`

    :param bio: Optional. Bio of the user.
    :type bio: :obj:`str`

    :param invite_link: Optional. Chat invite link that was used by the user to send the join request
    :type invite_link: :class:`tgram.types.ChatInviteLink`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatJoinRequest`
    """

    def __init__(
        self,
        chat: "Chat",
        from_user: "User",
        user_chat_id: "int",
        date: "int",
        bio: "str" = None,
        invite_link: "ChatInviteLink" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatJoinRequest"]:
        return (
            ChatJoinRequest(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                from_user=User._parse(me=me, d=d.get("from")),
                user_chat_id=d.get("user_chat_id"),
                date=d.get("date"),
                bio=d.get("bio"),
                invite_link=ChatInviteLink._parse(me=me, d=d.get("invite_link")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatPermissions(Type_):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chatpermissions

    :param can_send_messages: Optional. True, if the user is allowed to send text messages, contacts, locations and
        venues
    :type can_send_messages: :obj:`bool`

    :param can_send_audios: Optional. True, if the user is allowed to send audios
    :type can_send_audios: :obj:`bool`

    :param can_send_documents: Optional. True, if the user is allowed to send documents
    :type can_send_documents: :obj:`bool`

    :param can_send_photos: Optional. True, if the user is allowed to send photos
    :type can_send_photos: :obj:`bool`

    :param can_send_videos: Optional. True, if the user is allowed to send videos
    :type can_send_videos: :obj:`bool`

    :param can_send_video_notes: Optional. True, if the user is allowed to send video notes
    :type can_send_video_notes: :obj:`bool`

    :param can_send_voice_notes: Optional. True, if the user is allowed to send voice notes
    :type can_send_voice_notes: :obj:`bool`

    :param can_send_polls: Optional. True, if the user is allowed to send polls, implies can_send_messages
    :type can_send_polls: :obj:`bool`

    :param can_send_other_messages: Optional. True, if the user is allowed to send animations, games, stickers and use
        inline bots
    :type can_send_other_messages: :obj:`bool`

    :param can_add_web_page_previews: Optional. True, if the user is allowed to add web page previews to their
        messages
    :type can_add_web_page_previews: :obj:`bool`

    :param can_change_info: Optional. True, if the user is allowed to change the chat title, photo and other settings.
        Ignored in public supergroups
    :type can_change_info: :obj:`bool`

    :param can_invite_users: Optional. True, if the user is allowed to invite new users to the chat
    :type can_invite_users: :obj:`bool`

    :param can_pin_messages: Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
    :type can_pin_messages: :obj:`bool`

    :param can_manage_topics: Optional. True, if the user is allowed to create forum topics. If omitted defaults to the
        value of can_pin_messages
    :type can_manage_topics: :obj:`bool`

    :param can_send_media_messages: deprecated.
    :type can_send_media_messages: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatPermissions`
    """

    def __init__(
        self,
        can_send_messages: "bool" = None,
        can_send_audios: "bool" = None,
        can_send_documents: "bool" = None,
        can_send_photos: "bool" = None,
        can_send_videos: "bool" = None,
        can_send_video_notes: "bool" = None,
        can_send_voice_notes: "bool" = None,
        can_send_polls: "bool" = None,
        can_send_other_messages: "bool" = None,
        can_add_web_page_previews: "bool" = None,
        can_change_info: "bool" = None,
        can_invite_users: "bool" = None,
        can_pin_messages: "bool" = None,
        can_manage_topics: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatPermissions"]:
        return (
            ChatPermissions(
                me=me,
                json=d,
                can_send_messages=d.get("can_send_messages"),
                can_send_audios=d.get("can_send_audios"),
                can_send_documents=d.get("can_send_documents"),
                can_send_photos=d.get("can_send_photos"),
                can_send_videos=d.get("can_send_videos"),
                can_send_video_notes=d.get("can_send_video_notes"),
                can_send_voice_notes=d.get("can_send_voice_notes"),
                can_send_polls=d.get("can_send_polls"),
                can_send_other_messages=d.get("can_send_other_messages"),
                can_add_web_page_previews=d.get("can_add_web_page_previews"),
                can_change_info=d.get("can_change_info"),
                can_invite_users=d.get("can_invite_users"),
                can_pin_messages=d.get("can_pin_messages"),
                can_manage_topics=d.get("can_manage_topics"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Birthdate(Type_):
    """
    This object represents a user's birthdate.

    Telegram documentation: https://core.telegram.org/bots/api#birthdate

    :param day: Day of the user's birth; 1-31
    :type day: :obj:`int`

    :param month: Month of the user's birth; 1-12
    :type month: :obj:`int`

    :param year: Optional. Year of the user's birth
    :type year: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`Birthdate`
    """

    def __init__(
        self,
        day: "int",
        month: "int",
        year: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Birthdate"]:
        return (
            Birthdate(
                me=me,
                json=d,
                day=d.get("day"),
                month=d.get("month"),
                year=d.get("year"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BusinessIntro(Type_):
    """
    This object represents a business intro.

    Telegram documentation: https://core.telegram.org/bots/api#businessintro

    :param title: Optional. Title text of the business intro
    :type title: :obj:`str`

    :param message: Optional. Message text of the business intro
    :type message: :obj:`str`

    :param sticker: Optional. Sticker of the business intro
    :type sticker: :class:`Sticker`

    :return: Instance of the class
    :rtype: :class:`BusinessIntro`
    """

    def __init__(
        self,
        title: "str" = None,
        message: "str" = None,
        sticker: "Sticker" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.message = message
        self.sticker = sticker

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["BusinessIntro"]:
        return (
            BusinessIntro(
                me=me,
                json=d,
                title=d.get("title"),
                message=d.get("message"),
                sticker=Sticker._parse(me=me, d=d.get("sticker")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BusinessLocation(Type_):
    """
    This object represents a business location.

    Telegram documentation: https://core.telegram.org/bots/api#businesslocation

    :param address: Address of the business
    :type address: :obj:`str`

    :param location: Optional. Location of the business
    :type location: :class:`Location`

    :return: Instance of the class
    :rtype: :class:`BusinessLocation`
    """

    def __init__(
        self,
        address: "str",
        location: "Location" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.address = address
        self.location = location

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BusinessLocation"]:
        return (
            BusinessLocation(
                me=me,
                json=d,
                address=d.get("address"),
                location=Location._parse(me=me, d=d.get("location")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BusinessOpeningHoursInterval(Type_):
    """
    This object represents a business opening hours interval.

    Telegram documentation: https://core.telegram.org/bots/api#businessopeninghoursinterval

    :param opening_minute: The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 24 60
    :type opening_minute: :obj:`int`

    :param closing_minute: The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 24 60
    :type closing_minute: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`BusinessOpeningHoursInterval`
    """

    def __init__(
        self,
        opening_minute: "int",
        closing_minute: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.opening_minute = opening_minute
        self.closing_minute = closing_minute

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BusinessOpeningHoursInterval"]:
        return (
            BusinessOpeningHoursInterval(
                me=me,
                json=d,
                opening_minute=d.get("opening_minute"),
                closing_minute=d.get("closing_minute"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BusinessOpeningHours(Type_):
    """

    This object represents business opening hours.

    Telegram documentation: https://core.telegram.org/bots/api#businessopeninghours

    :param time_zone_name: Unique name of the time zone for which the opening hours are defined
    :type time_zone_name: :obj:`str`

    :param opening_hours: List of time intervals describing business opening hours
    :type opening_hours: :obj:`list` of :class:`BusinessOpeningHoursInterval`

    :return: Instance of the class

    :rtype: :class:`BusinessOpeningHours`
    """

    def __init__(
        self,
        time_zone_name: "str",
        opening_hours: List["BusinessOpeningHoursInterval"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.time_zone_name = time_zone_name
        self.opening_hours = opening_hours

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BusinessOpeningHours"]:
        return (
            BusinessOpeningHours(
                me=me,
                json=d,
                time_zone_name=d.get("time_zone_name"),
                opening_hours=[
                    BusinessOpeningHoursInterval._parse(me=me, d=i)
                    for i in d.get("opening_hours")
                ]
                if d.get("opening_hours")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatLocation(Type_):
    """
    Represents a location to which a chat is connected.

    Telegram Documentation: https://core.telegram.org/bots/api#chatlocation

    :param location: The location to which the supergroup is connected. Can't be a live location.
    :type location: :class:`tgram.types.Location`

    :param address: Location address; 1-64 characters, as defined by the chat owner
    :type address: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatLocation`
    """

    def __init__(
        self,
        location: "Location",
        address: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.location = location
        self.address = address

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatLocation"]:
        return (
            ChatLocation(
                me=me,
                json=d,
                location=Location._parse(me=me, d=d.get("location")),
                address=d.get("address"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ReactionType(Type_):
    """
    This object represents a reaction type.

    Telegram documentation: https://core.telegram.org/bots/api#reactiontype

    :param type: Type of the reaction
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`ReactionType`
    """

    def __init__(
        self, type: "str", emoji: "str", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.emoji = emoji

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ReactionType"]:
        return (
            ReactionType(
                me=me,
                json=d,
                type=d.get("type"),
                emoji=d.get("emoji"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ReactionTypeEmoji(Type_):
    """
    This object represents an emoji reaction type.

    Telegram documentation: https://core.telegram.org/bots/api#reactiontypeemoji

    :param type: Type of the reaction, must be emoji
    :type type: :obj:`str`

    :param emoji: Reaction emoji. List is available on the API doc.
    :type emoji: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`ReactionTypeEmoji`
    """

    def __init__(
        self, type: "str", emoji: "str", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.emoji = emoji

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ReactionTypeEmoji"]:
        return (
            ReactionTypeEmoji(
                me=me,
                json=d,
                type=d.get("type"),
                emoji=d.get("emoji"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ReactionTypeCustomEmoji(Type_):
    """
    This object represents a custom emoji reaction type.

    Telegram documentation: https://core.telegram.org/bots/api#reactiontypecustomemoji

    :param type: Type of the reaction, must be custom_emoji
    :type type: :obj:`str`

    :param custom_emoji_id: Identifier of the custom emoji
    :type custom_emoji_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`ReactionTypeCustomEmoji`
    """

    def __init__(
        self,
        type: "str",
        custom_emoji_id: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ReactionTypeCustomEmoji"]:
        return (
            ReactionTypeCustomEmoji(
                me=me,
                json=d,
                type=d.get("type"),
                custom_emoji_id=d.get("custom_emoji_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ReactionCount(Type_):
    """
    This object represents a reaction added to a message along with the number of times it was added.

    Telegram documentation: https://core.telegram.org/bots/api#reactioncount

    :param type: Type of the reaction
    :type type: :class:`ReactionType`

    :param total_count: Number of times the reaction was added
    :type total_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`ReactionCount`
    """

    def __init__(
        self,
        type: "ReactionType",
        total_count: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.total_count = total_count

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ReactionCount"]:
        return (
            ReactionCount(
                me=me,
                json=d,
                type=ReactionType._parse(me=me, d=d.get("type")),
                total_count=d.get("total_count"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MessageReactionUpdated(Type_):
    """
    This object represents a service message about a change in the list of the current user's reactions to a message.

    Telegram documentation: https://core.telegram.org/bots/api#messagereactionupdated

    :param chat: The chat containing the message the user reacted to
    :type chat: :class:`tgram.types.Chat`

    :param message_id: Unique identifier of the message inside the chat
    :type message_id: :obj:`int`

    :param user: Optional. The user that changed the reaction, if the user isn't anonymous
    :type user: :class:`tgram.types.User`

    :param actor_chat: Optional. The chat on behalf of which the reaction was changed, if the user is anonymous
    :type actor_chat: :class:`tgram.types.Chat`

    :param date: Date of the change in Unix time
    :type date: :obj:`int`

    :param old_reaction: Previous list of reaction types that were set by the user
    :type old_reaction: :obj:`list` of :class:`ReactionType`

    :param new_reaction: New list of reaction types that have been set by the user
    :type new_reaction: :obj:`list` of :class:`ReactionType`

    :return: Instance of the class
    :rtype: :class:`MessageReactionUpdated`
    """

    def __init__(
        self,
        chat: "Chat",
        message_id: "int",
        date: "int",
        old_reaction: List["ReactionType"],
        new_reaction: List["ReactionType"],
        user: "User" = None,
        actor_chat: "Chat" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.message_id = message_id
        self.user = user
        self.actor_chat = actor_chat
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MessageReactionUpdated"]:
        return (
            MessageReactionUpdated(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
                date=d.get("date"),
                old_reaction=[
                    ReactionType._parse(me=me, d=i) for i in d.get("old_reaction")
                ]
                if d.get("old_reaction")
                else None,
                new_reaction=[
                    ReactionType._parse(me=me, d=i) for i in d.get("new_reaction")
                ]
                if d.get("new_reaction")
                else None,
                user=User._parse(me=me, d=d.get("user")),
                actor_chat=Chat._parse(me=me, d=d.get("actor_chat")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MessageReactionCountUpdated(Type_):
    """
    This object represents a service message about a change in the list of the current user's reactions to a message.

    Telegram documentation: https://core.telegram.org/bots/api#messagereactioncountupdated

    :param chat: The chat containing the message
    :type chat: :class:`tgram.types.Chat`

    :param message_id: Unique message identifier inside the chat
    :type message_id: :obj:`int`

    :param date: Date of the change in Unix time
    :type date: :obj:`int`

    :param reactions: List of reactions that are present on the message
    :type reactions: :obj:`list` of :class:`ReactionCount`

    :return: Instance of the class
    :rtype: :class:`MessageReactionCountUpdated`
    """

    def __init__(
        self,
        chat: "Chat",
        message_id: "int",
        date: "int",
        reactions: List["ReactionCount"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MessageReactionCountUpdated"]:
        return (
            MessageReactionCountUpdated(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
                date=d.get("date"),
                reactions=[ReactionCount._parse(me=me, d=i) for i in d.get("reactions")]
                if d.get("reactions")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ForumTopic(Type_):
    """
    This object represents a forum topic.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopic

    :param message_thread_id: Unique identifier of the forum topic
    :type message_thread_id: :obj:`int`

    :param name: Name of the topic
    :type name: :obj:`str`

    :param icon_color: Color of the topic icon in RGB format
    :type icon_color: :obj:`int`

    :param icon_custom_emoji_id: Optional. Unique identifier of the custom emoji shown as the topic icon
    :type icon_custom_emoji_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ForumTopic`
    """

    def __init__(
        self,
        message_thread_id: "int",
        name: "str",
        icon_color: "int",
        icon_custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ForumTopic"]:
        return (
            ForumTopic(
                me=me,
                json=d,
                message_thread_id=d.get("message_thread_id"),
                name=d.get("name"),
                icon_color=d.get("icon_color"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommand(Type_):
    """
    This object represents a bot command.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommand

    :param command: Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and
        underscores.
    :type command: :obj:`str`

    :param description: Description of the command; 1-256 characters.
    :type description: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommand`
    """

    def __init__(
        self,
        command: "str",
        description: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.command = command
        self.description = description

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["BotCommand"]:
        return (
            BotCommand(
                me=me,
                json=d,
                command=d.get("command"),
                description=d.get("description"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommandScope(Type_):
    """
    This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:

    * :class:`BotCommandScopeDefault`
    * :class:`BotCommandScopeAllPrivateChats`
    * :class:`BotCommandScopeAllGroupChats`
    * :class:`BotCommandScopeAllChatAdministrators`
    * :class:`BotCommandScopeChat`
    * :class:`BotCommandScopeChatAdministrators`
    * :class:`BotCommandScopeChatMember`

    Determining list of commands
    The following algorithm is used to determine the list of commands for a particular user viewing the bot menu. The first list of commands which is set is returned:

    Commands in the chat with the bot:

    * :class:`BotCommandScopeChat` + language_code
    * :class:`BotCommandScopeChat`
    * :class:`BotCommandScopeAllPrivateChats` + language_code
    * :class:`BotCommandScopeAllPrivateChats`
    * :class:`BotCommandScopeDefault` + language_code
    * :class:`BotCommandScopeDefault`

    Commands in group and supergroup chats:

    * :class:`BotCommandScopeChatMember` + language_code
    * :class:`BotCommandScopeChatMember`
    * :class:`BotCommandScopeChatAdministrators` + language_code (administrators only)
    * :class:`BotCommandScopeChatAdministrators` (administrators only)
    * :class:`BotCommandScopeChat` + language_code
    * :class:`BotCommandScopeChat`
    * :class:`BotCommandScopeAllChatAdministrators` + language_code (administrators only)
    * :class:`BotCommandScopeAllChatAdministrators` (administrators only)
    * :class:`BotCommandScopeAllGroupChats` + language_code
    * :class:`BotCommandScopeAllGroupChats`
    * :class:`BotCommandScopeDefault` + language_code
    * :class:`BotCommandScopeDefault`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScope`
    """

    def __init__(self, type: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["BotCommandScope"]:
        return (
            BotCommandScope(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommandScopeDefault(Type_):
    """
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopedefault

    :param type: Scope type, must be default
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeDefault`
    """

    def __init__(self, type: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BotCommandScopeDefault"]:
        return (
            BotCommandScopeDefault(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommandScopeAllPrivateChats(Type_):
    """
    Represents the scope of bot commands, covering all private chats.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopeallprivatechats

    :param type: Scope type, must be all_private_chats
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeAllPrivateChats`
    """

    def __init__(self, type: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BotCommandScopeAllPrivateChats"]:
        return (
            BotCommandScopeAllPrivateChats(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommandScopeAllGroupChats(Type_):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopeallgroupchats

    :param type: Scope type, must be all_group_chats
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeAllGroupChats`
    """

    def __init__(self, type: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BotCommandScopeAllGroupChats"]:
        return (
            BotCommandScopeAllGroupChats(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommandScopeAllChatAdministrators(Type_):
    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopeallchatadministrators

    :param type: Scope type, must be all_chat_administrators
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeAllChatAdministrators`
    """

    def __init__(self, type: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BotCommandScopeAllChatAdministrators"]:
        return (
            BotCommandScopeAllChatAdministrators(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommandScopeChat(Type_):
    """
    Represents the scope of bot commands, covering a specific chat.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopechat

    :param type: Scope type, must be chat
    :type type: :obj:`str`

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername)
    :type chat_id: :obj:`int` or :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeChat`
    """

    def __init__(
        self,
        type: "str",
        chat_id: Union["int", "str"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.chat_id = chat_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BotCommandScopeChat"]:
        return (
            BotCommandScopeChat(
                me=me,
                json=d,
                type=d.get("type"),
                chat_id=d.get("chat_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommandScopeChatAdministrators(Type_):
    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopechatadministrators

    :param type: Scope type, must be chat_administrators
    :type type: :obj:`str`

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername)
    :type chat_id: :obj:`int` or :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeChatAdministrators`
    """

    def __init__(
        self,
        type: "str",
        chat_id: Union["int", "str"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.chat_id = chat_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BotCommandScopeChatAdministrators"]:
        return (
            BotCommandScopeChatAdministrators(
                me=me,
                json=d,
                type=d.get("type"),
                chat_id=d.get("chat_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotCommandScopeChatMember(Type_):
    """
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopechatmember

    :param type: Scope type, must be chat_member
    :type type: :obj:`str`

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername)
    :type chat_id: :obj:`int` or :obj:`str`

    :param user_id: Unique identifier of the target user
    :type user_id: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeChatMember`
    """

    def __init__(
        self,
        type: "str",
        chat_id: Union["int", "str"],
        user_id: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BotCommandScopeChatMember"]:
        return (
            BotCommandScopeChatMember(
                me=me,
                json=d,
                type=d.get("type"),
                chat_id=d.get("chat_id"),
                user_id=d.get("user_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotName(Type_):
    """
    This object represents a bot name.

    Telegram Documentation: https://core.telegram.org/bots/api#botname

    :param name: The bot name
    :type name: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`BotName`
    """

    def __init__(self, name: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.name = name

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["BotName"]:
        return (
            BotName(
                me=me,
                json=d,
                name=d.get("name"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotDescription(Type_):
    """
    This object represents a bot description.

    Telegram documentation: https://core.telegram.org/bots/api#botdescription

    :param description: Bot description
    :type description: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotDescription`
    """

    def __init__(
        self, description: "str", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.description = description

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["BotDescription"]:
        return (
            BotDescription(
                me=me,
                json=d,
                description=d.get("description"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BotShortDescription(Type_):
    """
    This object represents a bot short description.

    Telegram documentation: https://core.telegram.org/bots/api#botshortdescription

    :param short_description: Bot short description
    :type short_description: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotShortDescription`
    """

    def __init__(
        self, short_description: "str", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.short_description = short_description

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BotShortDescription"]:
        return (
            BotShortDescription(
                me=me,
                json=d,
                short_description=d.get("short_description"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MenuButton(Type_):
    """
    This object describes the bot's menu button in a private chat. It should be one of

    * :class:`MenuButtonCommands`
    * :class:`MenuButtonWebApp`
    * :class:`MenuButtonDefault`

    If a menu button other than MenuButtonDefault is set for a private chat, then it is applied
    in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.
    """

    def __init__(self, type: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["MenuButton"]:
        return (
            MenuButton(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MenuButtonCommands(Type_):
    """
    Represents a menu button, which opens the bot's list of commands.

    Telegram Documentation: https://core.telegram.org/bots/api#menubuttoncommands

    :param type: Type of the button, must be commands
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.MenuButtonCommands`
    """

    def __init__(self, type: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MenuButtonCommands"]:
        return (
            MenuButtonCommands(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MenuButtonWebApp(Type_):
    """
    Represents a menu button, which launches a Web App.

    Telegram Documentation: https://core.telegram.org/bots/api#menubuttonwebapp

    :param type: Type of the button, must be web_app
    :type type: :obj:`str`

    :param text: Text on the button
    :type text: :obj:`str`

    :param web_app: Description of the Web App that will be launched when the user presses the button. The Web App will be
        able to send an arbitrary message on behalf of the user using the method answerWebAppQuery.
    :type web_app: :class:`tgram.types.WebAppInfo`

    :return: Instance of the class
    :rtype: :class:`tgram.types.MenuButtonWebApp`
    """

    def __init__(
        self,
        type: "str",
        text: "str",
        web_app: "WebAppInfo",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.web_app = web_app

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MenuButtonWebApp"]:
        return (
            MenuButtonWebApp(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                web_app=WebAppInfo._parse(me=me, d=d.get("web_app")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MenuButtonDefault(Type_):
    """
    Describes that no specific value for the menu button was set.

    Telegram Documentation: https://core.telegram.org/bots/api#menubuttondefault

    :param type: Type of the button, must be default
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.MenuButtonDefault`
    """

    def __init__(self, type: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["MenuButtonDefault"]:
        return (
            MenuButtonDefault(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBoostSource(Type_):
    """
    This object describes the source of a chat boost. It can be one of
        ChatBoostSourcePremium
        ChatBoostSourceGiftCode
        ChatBoostSourceGiveaway

    Telegram documentation: https://core.telegram.org/bots/api#chatboostsource

    :return: Instance of the class
    :rtype: :class:`ChatBoostSourcePremium` or :class:`ChatBoostSourceGiftCode` or :class:`ChatBoostSourceGiveaway`
    """

    def __init__(
        self, source: "str", user: "User", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.user = user

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatBoostSource"]:
        return (
            ChatBoostSource(
                me=me,
                json=d,
                source=d.get("source"),
                user=User._parse(me=me, d=d.get("user")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBoostSourcePremium(Type_):
    """
    The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostsourcepremium

    :param source: Source of the boost, always “premium”
    :type source: :obj:`str`

    :param user: User that boosted the chat
    :type user: :class:`User`

    :return: Instance of the class
    :rtype: :class:`ChatBoostSourcePremium`
    """

    def __init__(
        self, source: "str", user: "User", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.user = user

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatBoostSourcePremium"]:
        return (
            ChatBoostSourcePremium(
                me=me,
                json=d,
                source=d.get("source"),
                user=User._parse(me=me, d=d.get("user")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBoostSourceGiftCode(Type_):
    """
    The boost was obtained by the creation of Telegram Premium gift codes to boost a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostsourcegiftcode

    :param source: Source of the boost, always “gift_code”
    :type source: :obj:`str`

    :param user: User for which the gift code was created
    :type user: :class:`User`

    :return: Instance of the class
    :rtype: :class:`ChatBoostSourceGiftCode`
    """

    def __init__(
        self, source: "str", user: "User", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.user = user

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatBoostSourceGiftCode"]:
        return (
            ChatBoostSourceGiftCode(
                me=me,
                json=d,
                source=d.get("source"),
                user=User._parse(me=me, d=d.get("user")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBoostSourceGiveaway(Type_):
    """
    The boost was obtained by the creation of a Telegram Premium giveaway.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostsourcegiveaway

    :param source: Source of the boost, always “giveaway”
    :type source: :obj:`str`

    :param giveaway_message_id: Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet.
    :type giveaway_message_id: :obj:`int`

    :param user: User that won the prize in the giveaway if any
    :type user: :class:`User`

    :param is_unclaimed: True, if the giveaway was completed, but there was no user to win the prize
    :type is_unclaimed: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`ChatBoostSourceGiveaway`
    """

    def __init__(
        self,
        source: "str",
        giveaway_message_id: "int",
        user: "User" = None,
        is_unclaimed: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.is_unclaimed = is_unclaimed

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatBoostSourceGiveaway"]:
        return (
            ChatBoostSourceGiveaway(
                me=me,
                json=d,
                source=d.get("source"),
                giveaway_message_id=d.get("giveaway_message_id"),
                user=User._parse(me=me, d=d.get("user")),
                is_unclaimed=d.get("is_unclaimed"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBoost(Type_):
    """
    This object contains information about a chat boost.

    Telegram documentation: https://core.telegram.org/bots/api#chatboost

    :param boost_id: Unique identifier of the boost
    :type boost_id: :obj:`str`

    :param add_date: Point in time (Unix timestamp) when the chat was boosted
    :type add_date: :obj:`int`

    :param expiration_date: Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged
    :type expiration_date: :obj:`int`

    :param source: Optional. Source of the added boost (made Optional for now due to API error)
    :type source: :class:`ChatBoostSource`

    :return: Instance of the class
    :rtype: :class:`ChatBoost`
    """

    def __init__(
        self,
        boost_id: "str",
        add_date: "int",
        expiration_date: "int",
        source: "ChatBoostSource",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ChatBoost"]:
        return (
            ChatBoost(
                me=me,
                json=d,
                boost_id=d.get("boost_id"),
                add_date=d.get("add_date"),
                expiration_date=d.get("expiration_date"),
                source=ChatBoostSource._parse(me=me, d=d.get("source")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBoostUpdated(Type_):
    """
    This object represents a boost added to a chat or changed.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostupdated

    :param chat: Chat which was boosted
    :type chat: :class:`Chat`

    :param boost: Infomation about the chat boost
    :type boost: :class:`ChatBoost`

    :return: Instance of the class
    :rtype: :class:`ChatBoostUpdated`
    """

    def __init__(
        self,
        chat: "Chat",
        boost: "ChatBoost",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.boost = boost

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatBoostUpdated"]:
        return (
            ChatBoostUpdated(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                boost=ChatBoost._parse(me=me, d=d.get("boost")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChatBoostRemoved(Type_):
    """
    This object represents a boost removed from a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostremoved

    :param chat: Chat which was boosted
    :type chat: :class:`Chat`

    :param boost_id: Unique identifier of the boost
    :type boost_id: :obj:`str`

    :param remove_date: Point in time (Unix timestamp) when the boost was removed
    :type remove_date: :obj:`int`

    :param source: Source of the removed boost
    :type source: :class:`ChatBoostSource`

    :return: Instance of the class
    :rtype: :class:`ChatBoostRemoved`
    """

    def __init__(
        self,
        chat: "Chat",
        boost_id: "str",
        remove_date: "int",
        source: "ChatBoostSource",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChatBoostRemoved"]:
        return (
            ChatBoostRemoved(
                me=me,
                json=d,
                chat=Chat._parse(me=me, d=d.get("chat")),
                boost_id=d.get("boost_id"),
                remove_date=d.get("remove_date"),
                source=ChatBoostSource._parse(me=me, d=d.get("source")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class UserChatBoosts(Type_):
    """
    This object represents a list of boosts added to a chat by a user.

    Telegram documentation: https://core.telegram.org/bots/api#userchatboosts

    :param boosts: The list of boosts added to the chat by the user
    :type boosts: :obj:`list` of :class:`ChatBoost`

    :return: Instance of the class
    :rtype: :class:`UserChatBoosts`
    """

    def __init__(
        self, boosts: List["ChatBoost"], me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.boosts = boosts

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["UserChatBoosts"]:
        return (
            UserChatBoosts(
                me=me,
                json=d,
                boosts=[ChatBoost._parse(me=me, d=i) for i in d.get("boosts")]
                if d.get("boosts")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BusinessConnection(Type_):
    """
    This object describes the connection of the bot with a business account.

    Telegram documentation: https://core.telegram.org/bots/api#businessconnection

    :param id: Unique identifier of the business connection
    :type id: :obj:`str`

    :param user: Business account user that created the business connection
    :type user: :class:`User`

    :param user_chat_id: Identifier of a private chat with the user who created the business connection
    :type user_chat_id: :obj:`int`

    :param date: Date the connection was established in Unix time
    :type date: :obj:`int`

    :param can_reply: True, if the bot can act on behalf of the business account in chats that were active in the last 24 hours
    :type can_reply: :obj:`bool`

    :param is_enabled: True, if the connection is active
    :type is_enabled: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`BusinessConnection`
    """

    def __init__(
        self,
        id: "str",
        user: "User",
        user_chat_id: "int",
        date: "int",
        can_reply: "bool",
        is_enabled: "bool",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.user = user
        self.user_chat_id = user_chat_id
        self.date = date
        self.can_reply = can_reply
        self.is_enabled = is_enabled

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BusinessConnection"]:
        return (
            BusinessConnection(
                me=me,
                json=d,
                id=d.get("id"),
                user=User._parse(me=me, d=d.get("user")),
                user_chat_id=d.get("user_chat_id"),
                date=d.get("date"),
                can_reply=d.get("can_reply"),
                is_enabled=d.get("is_enabled"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class BusinessMessagesDeleted(Type_):
    """
    This object is received when messages are deleted from a connected business account.

    Telegram documentation: https://core.telegram.org/bots/api#businessmessagesdeleted

    :param business_connection_id: Unique identifier of the business connection
    :type business_connection_id: :obj:`str`

    :param chat: Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.
    :type chat: :class:`Chat`

    :param message_ids: A JSON-serialized list of identifiers of deleted messages in the chat of the business account
    :type message_ids: :obj:`list` of :obj:`int`

    :return: Instance of the class
    :rtype: :class:`BusinessMessagesDeleted`
    """

    def __init__(
        self,
        business_connection_id: "str",
        chat: "Chat",
        message_ids: List["int"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.message_ids = message_ids

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["BusinessMessagesDeleted"]:
        return (
            BusinessMessagesDeleted(
                me=me,
                json=d,
                business_connection_id=d.get("business_connection_id"),
                chat=Chat._parse(me=me, d=d.get("chat")),
                message_ids=d.get("message_ids"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ResponseParameters(Type_):
    def __init__(
        self,
        migrate_to_chat_id: "int" = None,
        retry_after: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ResponseParameters"]:
        return (
            ResponseParameters(
                me=me,
                json=d,
                migrate_to_chat_id=d.get("migrate_to_chat_id"),
                retry_after=d.get("retry_after"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


InputMedia = Union[
    "InputMediaAudio", "InputMediaDocument", "InputMediaPhoto", "InputMediaVideo"
]


class InputMediaPhoto(Type_):
    """
    Represents a photo to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmediaphoto

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
        HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using
        multipart/form-data under <file_attach_name> name. More information on Sending Files »
    :type media: :obj:`str`

    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param has_spoiler: Optional. True, if the uploaded photo is a spoiler
    :type has_spoiler: :obj:`bool`

    :param show_caption_above_media: Optional. True, if the caption should be shown above the photo
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaPhoto`
    """

    def __init__(
        self,
        media: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        has_spoiler: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "photo"
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["InputMediaPhoto"]:
        return (
            InputMediaPhoto(
                me=me,
                json=d,
                media=d.get("media"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                has_spoiler=d.get("has_spoiler"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputMediaVideo(Type_):
    """
    Represents a video to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmediavideo

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
        HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using
        multipart/form-data under <file_attach_name> name. More information on Sending Files »
    :type media: :obj:`str`

    :param thumbnail: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported
        server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should
        not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
        only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using
        multipart/form-data under <file_attach_name>. More information on Sending Files »
    :type thumbnail: InputFile or :obj:`str`

    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param width: Optional. Video width
    :type width: :obj:`int`

    :param height: Optional. Video height
    :type height: :obj:`int`

    :param duration: Optional. Video duration in seconds
    :type duration: :obj:`int`

    :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
    :type supports_streaming: :obj:`bool`

    :param has_spoiler: Optional. True, if the uploaded video is a spoiler
    :type has_spoiler: :obj:`bool`

    :param show_caption_above_media: Optional. True, if the caption should be shown above the video
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaVideo`
    """

    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        supports_streaming: "bool" = None,
        has_spoiler: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["InputMediaVideo"]:
        return (
            InputMediaVideo(
                me=me,
                json=d,
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                supports_streaming=d.get("supports_streaming"),
                has_spoiler=d.get("has_spoiler"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputMediaAnimation(Type_):
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmediaanimation

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
        HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using
        multipart/form-data under <file_attach_name> name. More information on Sending Files »
    :type media: :obj:`str`

    :param thumbnail: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported
        server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should
        not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
        only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using
        multipart/form-data under <file_attach_name>. More information on Sending Files »
    :type thumbnail: InputFile or :obj:`str`

    :param caption: Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the animation caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param width: Optional. Animation width
    :type width: :obj:`int`

    :param height: Optional. Animation height
    :type height: :obj:`int`

    :param duration: Optional. Animation duration in seconds
    :type duration: :obj:`int`

    :param has_spoiler: Optional. True, if the uploaded animation is a spoiler
    :type has_spoiler: :obj:`bool`

    :param show_caption_above_media: Optional. True, if the caption should be shown above the animation
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaAnimation`
    """

    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        has_spoiler: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "animation"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.has_spoiler = has_spoiler

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputMediaAnimation"]:
        return (
            InputMediaAnimation(
                me=me,
                json=d,
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                has_spoiler=d.get("has_spoiler"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputMediaAudio(Type_):
    """
    Represents an audio file to be treated as music to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmediaaudio

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
        HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using
        multipart/form-data under <file_attach_name> name. More information on Sending Files »
    :type media: :obj:`str`

    :param thumbnail: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported
        server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should
        not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
        only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using
        multipart/form-data under <file_attach_name>. More information on Sending Files »
    :type thumbnail: InputFile or :obj:`str`

    :param caption: Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param duration: Optional. Duration of the audio in seconds
    :type duration: :obj:`int`

    :param performer: Optional. Performer of the audio
    :type performer: :obj:`str`

    :param title: Optional. Title of the audio
    :type title: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaAudio`
    """

    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        duration: "int" = None,
        performer: "str" = None,
        title: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "audio"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["InputMediaAudio"]:
        return (
            InputMediaAudio(
                me=me,
                json=d,
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                duration=d.get("duration"),
                performer=d.get("performer"),
                title=d.get("title"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputMediaDocument(Type_):
    """
    Represents a general file to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmediadocument

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
        HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using
        multipart/form-data under <file_attach_name> name. More information on Sending Files »
    :type media: :obj:`str`

    :param thumbnail: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported
        server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should
        not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
        only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using
        multipart/form-data under <file_attach_name>. More information on Sending Files »
    :type thumbnail: InputFile or :obj:`str`

    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param disable_content_type_detection: Optional. Disables automatic server-side content type detection for
        files uploaded using multipart/form-data. Always True, if the document is sent as part of an album.
    :type disable_content_type_detection: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaDocument`
    """

    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        disable_content_type_detection: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "document"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputMediaDocument"]:
        return (
            InputMediaDocument(
                me=me,
                json=d,
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                disable_content_type_detection=d.get("disable_content_type_detection"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


InputFile = Union[bytes, Path, str]


class Sticker(Type_):
    """
    This object represents a sticker.

    Telegram Documentation: https://core.telegram.org/bots/api#sticker

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param type: Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is
        independent from its format, which is determined by the fields is_animated and is_video.
    :type type: :obj:`str`

    :param width: Sticker width
    :type width: :obj:`int`

    :param height: Sticker height
    :type height: :obj:`int`

    :param is_animated: True, if the sticker is animated
    :type is_animated: :obj:`bool`

    :param is_video: True, if the sticker is a video sticker
    :type is_video: :obj:`bool`

    :param thumbnail: Optional. Sticker thumbnail in the .WEBP or .JPG format
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :param emoji: Optional. Emoji associated with the sticker
    :type emoji: :obj:`str`

    :param set_name: Optional. Name of the sticker set to which the sticker belongs
    :type set_name: :obj:`str`

    :param premium_animation: Optional. Premium animation for the sticker, if the sticker is premium
    :type premium_animation: :class:`tgram.types.File`

    :param mask_position: Optional. For mask stickers, the position where the mask should be placed
    :type mask_position: :class:`tgram.types.MaskPosition`

    :param custom_emoji_id: Optional. For custom emoji stickers, unique identifier of the custom emoji
    :type custom_emoji_id: :obj:`str`

    :param needs_repainting: Optional. True, if the sticker must be repainted to a text color in messages,
        the color of the Telegram Premium badge in emoji status, white color on chat photos, or another
        appropriate color in other places
    :type needs_repainting: :obj:`bool`

    :param file_size: Optional. File size in bytes
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Sticker`
    """

    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        type: "str",
        width: "int",
        height: "int",
        is_animated: "bool",
        is_video: "bool",
        thumbnail: "PhotoSize" = None,
        emoji: "str" = None,
        set_name: "str" = None,
        premium_animation: "File" = None,
        mask_position: "MaskPosition" = None,
        custom_emoji_id: "str" = None,
        needs_repainting: "bool" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.custom_emoji_id = custom_emoji_id
        self.needs_repainting = needs_repainting
        self.file_size = file_size

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Sticker"]:
        return (
            Sticker(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                type=d.get("type"),
                width=d.get("width"),
                height=d.get("height"),
                is_animated=d.get("is_animated"),
                is_video=d.get("is_video"),
                thumbnail=PhotoSize._parse(me=me, d=d.get("thumbnail")),
                emoji=d.get("emoji"),
                set_name=d.get("set_name"),
                premium_animation=File._parse(me=me, d=d.get("premium_animation")),
                mask_position=MaskPosition._parse(me=me, d=d.get("mask_position")),
                custom_emoji_id=d.get("custom_emoji_id"),
                needs_repainting=d.get("needs_repainting"),
                file_size=d.get("file_size"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class StickerSet(Type_):
    """
    This object represents a sticker set.

    Telegram Documentation: https://core.telegram.org/bots/api#stickerset

    :param name: Sticker set name
    :type name: :obj:`str`

    :param title: Sticker set title
    :type title: :obj:`str`

    :param sticker_type: Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”
    :type sticker_type: :obj:`str`

    :param stickers: List of all set stickers
    :type stickers: :obj:`list` of :class:`tgram.types.Sticker`

    :param thumbnail: Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :return: Instance of the class
    :rtype: :class:`tgram.types.StickerSet`
    """

    def __init__(
        self,
        name: "str",
        title: "str",
        sticker_type: "str",
        stickers: List["Sticker"],
        thumbnail: "PhotoSize" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.stickers = stickers
        self.thumbnail = thumbnail

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["StickerSet"]:
        return (
            StickerSet(
                me=me,
                json=d,
                name=d.get("name"),
                title=d.get("title"),
                sticker_type=d.get("sticker_type"),
                stickers=[Sticker._parse(me=me, d=i) for i in d.get("stickers")]
                if d.get("stickers")
                else None,
                thumbnail=PhotoSize._parse(me=me, d=d.get("thumbnail")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class MaskPosition(Type_):
    """
    This object describes the position on faces where a mask should be placed by default.

    Telegram Documentation: https://core.telegram.org/bots/api#maskposition

    :param point: The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or
        “chin”.
    :type point: :obj:`str`

    :param x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example,
        choosing -1.0 will place mask just to the left of the default mask position.
    :type x_shift: :obj:`float` number

    :param y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For
        example, 1.0 will place the mask just below the default mask position.
    :type y_shift: :obj:`float` number

    :param scale: Mask scaling coefficient. For example, 2.0 means double size.
    :type scale: :obj:`float` number

    :return: Instance of the class
    :rtype: :class:`tgram.types.MaskPosition`
    """

    def __init__(
        self,
        point: "str",
        x_shift: "float",
        y_shift: "float",
        scale: "float",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["MaskPosition"]:
        return (
            MaskPosition(
                me=me,
                json=d,
                point=d.get("point"),
                x_shift=d.get("x_shift"),
                y_shift=d.get("y_shift"),
                scale=d.get("scale"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputSticker(Type_):
    """
    This object describes a sticker to be added to a sticker set.

    :param sticker: The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers,
        pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        Animated and video stickers can't be uploaded via HTTP URL.
    :type sticker: :obj:`str` or :obj:`tgram.types.InputFile`

    :param emoji_list: One or more(up to 20) emoji(s) corresponding to the sticker
    :type emoji_list: :obj:`list` of :obj:`str`

    :param mask_position: Optional. Position where the mask should be placed on faces. For “mask” stickers only.
    :type mask_position: :class:`tgram.types.MaskPosition`

    :param keywords: Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters.
        For “regular” and “custom_emoji” stickers only.
    :type keywords: :obj:`list` of :obj:`str`

    :param format: 	Format of the added sticker, must be one of “static” for a .WEBP or .PNG image, “animated” for a .TGS animation, “video” for a WEBM video
    :type format: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputSticker`
    """

    def __init__(
        self,
        sticker: Union["InputFile", "str"],
        format: "str",
        emoji_list: List["str"],
        mask_position: "MaskPosition" = None,
        keywords: List["str"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.sticker = sticker
        self.format = format
        self.emoji_list = emoji_list
        self.mask_position = mask_position
        self.keywords = keywords

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["InputSticker"]:
        return (
            InputSticker(
                me=me,
                json=d,
                sticker=d.get("sticker"),
                format=d.get("format"),
                emoji_list=d.get("emoji_list"),
                mask_position=MaskPosition._parse(me=me, d=d.get("mask_position")),
                keywords=d.get("keywords"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQuery(Type_):
    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequery

    :param id: Unique identifier for this query
    :type id: :obj:`str`

    :param from_user: Sender
    :type from_user: :class:`tgram.types.User`

    :param query: Text of the query (up to 256 characters)
    :type query: :obj:`str`

    :param offset: Offset of the results to be returned, can be controlled by the bot
    :type offset: :obj:`str`

    :param chat_type: Optional. Type of the chat from which the inline query was sent. Can be either “sender” for a private
        chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always
        known for requests sent from official clients and most third-party clients, unless the request was sent from a secret
        chat
    :type chat_type: :obj:`str`

    :param location: Optional. Sender location, only for bots that request user location
    :type location: :class:`tgram.types.Location`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQuery`
    """

    def __init__(
        self,
        id: "str",
        from_user: "User",
        query: "str",
        offset: "str",
        chat_type: "str" = None,
        location: "Location" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["InlineQuery"]:
        return (
            InlineQuery(
                me=me,
                json=d,
                id=d.get("id"),
                from_user=User._parse(me=me, d=d.get("from")),
                query=d.get("query"),
                offset=d.get("offset"),
                chat_type=d.get("chat_type"),
                location=Location._parse(me=me, d=d.get("location")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultsButton(Type_):
    """
    This object represents a button to be shown above inline query results.
    You must use exactly one of the optional fields.

    Telegram documentation: https://core.telegram.org/bots/api#inlinequeryresultsbutton

    :param text: Label text on the button
    :type text: :obj:`str`

    :param web_app: Optional. Description of the Web App that will be launched when the user presses the button.
        The Web App will be able to switch back to the inline mode using the method web_app_switch_inline_query inside the Web App.
    :type web_app: :class:`tgram.types.WebAppInfo`

    :param start_parameter: Optional. Deep-linking parameter for the /start message sent to the bot when a user presses the button.
        1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed.
        Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search
        results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing
        any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs
        the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat
        where they wanted to use the bot's inline capabilities.
    :type start_parameter: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`InlineQueryResultsButton`
    """

    def __init__(
        self,
        text: "str",
        web_app: "WebAppInfo" = None,
        start_parameter: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultsButton"]:
        return (
            InlineQueryResultsButton(
                me=me,
                json=d,
                text=d.get("text"),
                web_app=WebAppInfo._parse(me=me, d=d.get("web_app")),
                start_parameter=d.get("start_parameter"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


InlineQueryResult = Union[
    "InlineQueryResultCachedAudio",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultArticle",
    "InlineQueryResultAudio",
    "InlineQueryResultContact",
    "InlineQueryResultGame",
    "InlineQueryResultDocument",
    "InlineQueryResultGif",
    "InlineQueryResultLocation",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultPhoto",
    "InlineQueryResultVenue",
    "InlineQueryResultVideo",
    "InlineQueryResultVoice",
]


class InlineQueryResultArticle(Type_):
    """
    Represents a link to an article or web page.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultarticle

    :param type: Type of the result, must be article
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 Bytes
    :type id: :obj:`str`

    :param title: Title of the result
    :type title: :obj:`str`

    :param input_message_content: Content of the message to be sent
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param url: Optional. URL of the result
    :type url: :obj:`str`

    :param hide_url: Optional. Pass True, if you don't want the URL to be shown in the message
    :type hide_url: :obj:`bool`

    :param description: Optional. Short description of the result
    :type description: :obj:`str`

    :param thumbnail_url: Optional. Url of the thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_width: Optional. Thumbnail width
    :type thumbnail_width: :obj:`int`

    :param thumbnail_height: Optional. Thumbnail height
    :type thumbnail_height: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultArticle`
    """

    def __init__(
        self,
        title: "str",
        input_message_content: "InputMessageContent",
        reply_markup: "InlineKeyboardMarkup" = None,
        url: "str" = None,
        hide_url: "bool" = None,
        description: "str" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "article"
        self.id = random.randint(10000, 99999)
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultArticle"]:
        return (
            InlineQueryResultArticle(
                me=me,
                json=d,
                title=d.get("title"),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                url=d.get("url"),
                hide_url=d.get("hide_url"),
                description=d.get("description"),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultPhoto(Type_):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultphoto

    :param type: Type of the result, must be photo
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param photo_url: A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB
    :type photo_url: :obj:`str`

    :param thumbnail_url: URL of the thumbnail for the photo
    :type thumbnail_url: :obj:`str`

    :param photo_width: Optional. Width of the photo
    :type photo_width: :obj:`int`

    :param photo_height: Optional. Height of the photo
    :type photo_height: :obj:`int`

    :param title: Optional. Title for the result
    :type title: :obj:`str`

    :param description: Optional. Short description of the result
    :type description: :obj:`str`

    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the photo
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param show_caption_above_media: Optional. If true, a caption is shown over the photo or video
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultPhoto`
    """

    def __init__(
        self,
        photo_url: "str",
        thumbnail_url: "str",
        photo_width: "int" = None,
        photo_height: "int" = None,
        title: "str" = None,
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "photo"
        self.id = random.randint(10000, 99999)
        self.photo_url = photo_url
        self.thumbnail_url = thumbnail_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultPhoto"]:
        return (
            InlineQueryResultPhoto(
                me=me,
                json=d,
                photo_url=d.get("photo_url"),
                thumbnail_url=d.get("thumbnail_url"),
                photo_width=d.get("photo_width"),
                photo_height=d.get("photo_height"),
                title=d.get("title"),
                description=d.get("description"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultGif(Type_):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultgif

    :param type: Type of the result, must be gif
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param gif_url: A valid URL for the GIF file. File size must not exceed 1MB
    :type gif_url: :obj:`str`

    :param gif_width: Optional. Width of the GIF
    :type gif_width: :obj:`int`

    :param gif_height: Optional. Height of the GIF
    :type gif_height: :obj:`int`

    :param gif_duration: Optional. Duration of the GIF in seconds
    :type gif_duration: :obj:`int`

    :param thumbnail_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_mime_type: Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or
        “video/mp4”. Defaults to “image/jpeg”
    :type thumbnail_mime_type: :obj:`str`

    :param title: Optional. Title for the result
    :type title: :obj:`str`

    :param caption: Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the GIF animation
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param show_caption_above_media: Optional. If true, a caption is shown over the photo or video
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultGif`
    """

    def __init__(
        self,
        gif_url: "str",
        thumbnail_url: "str",
        gif_width: "int" = None,
        gif_height: "int" = None,
        gif_duration: "int" = None,
        thumbnail_mime_type: "str" = None,
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "gif"
        self.id = random.randint(10000, 99999)
        self.gif_url = gif_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultGif"]:
        return (
            InlineQueryResultGif(
                me=me,
                json=d,
                gif_url=d.get("gif_url"),
                thumbnail_url=d.get("thumbnail_url"),
                gif_width=d.get("gif_width"),
                gif_height=d.get("gif_height"),
                gif_duration=d.get("gif_duration"),
                thumbnail_mime_type=d.get("thumbnail_mime_type"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultMpeg4Gif(Type_):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif

    :param type: Type of the result, must be mpeg4_gif
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param mpeg4_url: A valid URL for the MPEG4 file. File size must not exceed 1MB
    :type mpeg4_url: :obj:`str`

    :param mpeg4_width: Optional. Video width
    :type mpeg4_width: :obj:`int`

    :param mpeg4_height: Optional. Video height
    :type mpeg4_height: :obj:`int`

    :param mpeg4_duration: Optional. Video duration in seconds
    :type mpeg4_duration: :obj:`int`

    :param thumbnail_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_mime_type: Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or
        “video/mp4”. Defaults to “image/jpeg”
    :type thumbnail_mime_type: :obj:`str`

    :param title: Optional. Title for the result
    :type title: :obj:`str`

    :param caption: Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the video animation
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param show_caption_above_media: Optional. If true, a caption is shown over the photo or video
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultMpeg4Gif`
    """

    def __init__(
        self,
        mpeg4_url: "str",
        thumbnail_url: "str",
        mpeg4_width: "int" = None,
        mpeg4_height: "int" = None,
        mpeg4_duration: "int" = None,
        thumbnail_mime_type: "str" = None,
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "mpeg4gif"
        self.id = random.randint(10000, 99999)
        self.mpeg4_url = mpeg4_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultMpeg4Gif"]:
        return (
            InlineQueryResultMpeg4Gif(
                me=me,
                json=d,
                mpeg4_url=d.get("mpeg4_url"),
                thumbnail_url=d.get("thumbnail_url"),
                mpeg4_width=d.get("mpeg4_width"),
                mpeg4_height=d.get("mpeg4_height"),
                mpeg4_duration=d.get("mpeg4_duration"),
                thumbnail_mime_type=d.get("thumbnail_mime_type"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultVideo(Type_):
    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultvideo

    :param type: Type of the result, must be video
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param video_url: A valid URL for the embedded video player or video file
    :type video_url: :obj:`str`

    :param mime_type: MIME type of the content of the video URL, “text/html” or “video/mp4”
    :type mime_type: :obj:`str`

    :param thumbnail_url: URL of the thumbnail (JPEG only) for the video
    :type thumbnail_url: :obj:`str`

    :param title: Title for the result
    :type title: :obj:`str`

    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param video_width: Optional. Video width
    :type video_width: :obj:`int`

    :param video_height: Optional. Video height
    :type video_height: :obj:`int`

    :param video_duration: Optional. Video duration in seconds
    :type video_duration: :obj:`int`

    :param description: Optional. Short description of the result
    :type description: :obj:`str`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the video. This field is
        required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param show_caption_above_media: Optional. If true, a caption is shown over the video
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultVideo`
    """

    def __init__(
        self,
        video_url: "str",
        mime_type: "str",
        thumbnail_url: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        video_width: "int" = None,
        video_height: "int" = None,
        video_duration: "int" = None,
        description: "str" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.id = random.randint(10000, 99999)
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultVideo"]:
        return (
            InlineQueryResultVideo(
                me=me,
                json=d,
                video_url=d.get("video_url"),
                mime_type=d.get("mime_type"),
                thumbnail_url=d.get("thumbnail_url"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                video_width=d.get("video_width"),
                video_height=d.get("video_height"),
                video_duration=d.get("video_duration"),
                description=d.get("description"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultAudio(Type_):
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultaudio

    :param type: Type of the result, must be audio
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param audio_url: A valid URL for the audio file
    :type audio_url: :obj:`str`

    :param title: Title
    :type title: :obj:`str`

    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param performer: Optional. Performer
    :type performer: :obj:`str`

    :param audio_duration: Optional. Audio duration in seconds
    :type audio_duration: :obj:`int`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the audio
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultAudio`
    """

    def __init__(
        self,
        audio_url: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        performer: "str" = None,
        audio_duration: "int" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "audio"
        self.id = random.randint(10000, 99999)
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultAudio"]:
        return (
            InlineQueryResultAudio(
                me=me,
                json=d,
                audio_url=d.get("audio_url"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                performer=d.get("performer"),
                audio_duration=d.get("audio_duration"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultVoice(Type_):
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultvoice

    :param type: Type of the result, must be voice
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param voice_url: A valid URL for the voice recording
    :type voice_url: :obj:`str`

    :param title: Recording title
    :type title: :obj:`str`

    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the voice message caption. See formatting options for
        more details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param voice_duration: Optional. Recording duration in seconds
    :type voice_duration: :obj:`int`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the voice recording
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        voice_url: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        voice_duration: "int" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "voice"
        self.id = random.randint(10000, 99999)
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultVoice"]:
        return (
            InlineQueryResultVoice(
                me=me,
                json=d,
                voice_url=d.get("voice_url"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                voice_duration=d.get("voice_duration"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultDocument(Type_):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultdocument

    :param type: Type of the result, must be document
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param title: Title for the result
    :type title: :obj:`str`

    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param document_url: A valid URL for the file
    :type document_url: :obj:`str`

    :param mime_type: MIME type of the content of the file, either “application/pdf” or “application/zip”
    :type mime_type: :obj:`str`

    :param description: Optional. Short description of the result
    :type description: :obj:`str`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the file
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param thumbnail_url: Optional. URL of the thumbnail (JPEG only) for the file
    :type thumbnail_url: :obj:`str`

    :param thumbnail_width: Optional. Thumbnail width
    :type thumbnail_width: :obj:`int`

    :param thumbnail_height: Optional. Thumbnail height
    :type thumbnail_height: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultDocument`
    """

    def __init__(
        self,
        title: "str",
        document_url: "str",
        mime_type: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        description: "str" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "document"
        self.id = random.randint(10000, 99999)
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.document_url = document_url
        self.mime_type = mime_type
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultDocument"]:
        return (
            InlineQueryResultDocument(
                me=me,
                json=d,
                title=d.get("title"),
                document_url=d.get("document_url"),
                mime_type=d.get("mime_type"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                description=d.get("description"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultLocation(Type_):
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultlocation

    :param type: Type of the result, must be location
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 Bytes
    :type id: :obj:`str`

    :param latitude: Location latitude in degrees
    :type latitude: :obj:`float` number

    :param longitude: Location longitude in degrees
    :type longitude: :obj:`float` number

    :param title: Location title
    :type title: :obj:`str`

    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :type horizontal_accuracy: :obj:`float` number

    :param live_period: Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
    :type live_period: :obj:`int`

    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :type heading: :obj:`int`

    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :type proximity_alert_radius: :obj:`int`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the location
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param thumbnail_url: Optional. Url of the thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_width: Optional. Thumbnail width
    :type thumbnail_width: :obj:`int`

    :param thumbnail_height: Optional. Thumbnail height
    :type thumbnail_height: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultLocation`
    """

    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        title: "str",
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "location"
        self.id = random.randint(10000, 99999)
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultLocation"]:
        return (
            InlineQueryResultLocation(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                horizontal_accuracy=d.get("horizontal_accuracy"),
                live_period=d.get("live_period"),
                heading=d.get("heading"),
                proximity_alert_radius=d.get("proximity_alert_radius"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultVenue(Type_):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultvenue

    :param type: Type of the result, must be venue
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 Bytes
    :type id: :obj:`str`

    :param latitude: Latitude of the venue location in degrees
    :type latitude: :obj:`float`

    :param longitude: Longitude of the venue location in degrees
    :type longitude: :obj:`float`

    :param title: Title of the venue
    :type title: :obj:`str`

    :param address: Address of the venue
    :type address: :obj:`str`

    :param foursquare_id: Optional. Foursquare identifier of the venue if known
    :type foursquare_id: :obj:`str`

    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example,
        “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :type foursquare_type: :obj:`str`

    :param google_place_id: Optional. Google Places identifier of the venue
    :type google_place_id: :obj:`str`

    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :type google_place_type: :obj:`str`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the venue
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param thumbnail_url: Optional. Url of the thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_width: Optional. Thumbnail width
    :type thumbnail_width: :obj:`int`

    :param thumbnail_height: Optional. Thumbnail height
    :type thumbnail_height: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultVenue`
    """

    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        title: "str",
        address: "str",
        foursquare_id: "str" = None,
        foursquare_type: "str" = None,
        google_place_id: "str" = None,
        google_place_type: "str" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "venue"
        self.id = random.randint(10000, 99999)
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultVenue"]:
        return (
            InlineQueryResultVenue(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                address=d.get("address"),
                foursquare_id=d.get("foursquare_id"),
                foursquare_type=d.get("foursquare_type"),
                google_place_id=d.get("google_place_id"),
                google_place_type=d.get("google_place_type"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultContact(Type_):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcontact

    :param type: Type of the result, must be contact
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 Bytes
    :type id: :obj:`str`

    :param phone_number: Contact's phone number
    :type phone_number: :obj:`str`

    :param first_name: Contact's first name
    :type first_name: :obj:`str`

    :param last_name: Optional. Contact's last name
    :type last_name: :obj:`str`

    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    :type vcard: :obj:`str`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the contact
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param thumbnail_url: Optional. Url of the thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_width: Optional. Thumbnail width
    :type thumbnail_width: :obj:`int`

    :param thumbnail_height: Optional. Thumbnail height
    :type thumbnail_height: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultContact`
    """

    def __init__(
        self,
        phone_number: "str",
        first_name: "str",
        last_name: "str" = None,
        vcard: "str" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "contact"
        self.id = random.randint(10000, 99999)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultContact"]:
        return (
            InlineQueryResultContact(
                me=me,
                json=d,
                phone_number=d.get("phone_number"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                vcard=d.get("vcard"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultGame(Type_):
    """
    Represents a Game.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultgame

    :param type: Type of the result, must be game
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param game_short_name: Short name of the game
    :type game_short_name: :obj:`str`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultGame`
    """

    def __init__(
        self,
        game_short_name: "str",
        reply_markup: "InlineKeyboardMarkup" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "game"
        self.id = random.randint(10000, 99999)
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultGame"]:
        return (
            InlineQueryResultGame(
                me=me,
                json=d,
                game_short_name=d.get("game_short_name"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultCachedPhoto(Type_):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcachedphoto

    :param type: Type of the result, must be photo
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param photo_file_id: A valid file identifier of the photo
    :type photo_file_id: :obj:`str`

    :param title: Optional. Title for the result
    :type title: :obj:`str`

    :param description: Optional. Short description of the result
    :type description: :obj:`str`

    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the photo
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param show_caption_above_media: Optional. Pass True, if a caption is not required for the media
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultCachedPhoto`
    """

    def __init__(
        self,
        photo_file_id: "str",
        title: "str" = None,
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "cachedphoto"
        self.id = random.randint(10000, 99999)
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultCachedPhoto"]:
        return (
            InlineQueryResultCachedPhoto(
                me=me,
                json=d,
                photo_file_id=d.get("photo_file_id"),
                title=d.get("title"),
                description=d.get("description"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultCachedGif(Type_):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcachedgif

    :param type: Type of the result, must be gif
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param gif_file_id: A valid file identifier for the GIF file
    :type gif_file_id: :obj:`str`

    :param title: Optional. Title for the result
    :type title: :obj:`str`

    :param caption: Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the GIF animation
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param show_caption_above_media: Optional. Pass True, if a caption is not required for the media
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultCachedGif`
    """

    def __init__(
        self,
        gif_file_id: "str",
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "cachedgif"
        self.id = random.randint(10000, 99999)
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultCachedGif"]:
        return (
            InlineQueryResultCachedGif(
                me=me,
                json=d,
                gif_file_id=d.get("gif_file_id"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultCachedMpeg4Gif(Type_):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif

    :param type: Type of the result, must be mpeg4_gif
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param mpeg4_file_id: A valid file identifier for the MPEG4 file
    :type mpeg4_file_id: :obj:`str`

    :param title: Optional. Title for the result
    :type title: :obj:`str`

    :param caption: Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the video animation
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param show_caption_above_media: Optional. Pass True, if caption should be shown above the media
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultCachedMpeg4Gif`
    """

    def __init__(
        self,
        mpeg4_file_id: "str",
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "cachedmpeg4gif"
        self.id = random.randint(10000, 99999)
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultCachedMpeg4Gif"]:
        return (
            InlineQueryResultCachedMpeg4Gif(
                me=me,
                json=d,
                mpeg4_file_id=d.get("mpeg4_file_id"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultCachedSticker(Type_):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcachedsticker

    :param type: Type of the result, must be sticker
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param sticker_file_id: A valid file identifier of the sticker
    :type sticker_file_id: :obj:`str`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the sticker
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultCachedSticker`
    """

    def __init__(
        self,
        sticker_file_id: "str",
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "cachedsticker"
        self.id = random.randint(10000, 99999)
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultCachedSticker"]:
        return (
            InlineQueryResultCachedSticker(
                me=me,
                json=d,
                sticker_file_id=d.get("sticker_file_id"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultCachedDocument(Type_):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcacheddocument

    :param type: Type of the result, must be document
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param title: Title for the result
    :type title: :obj:`str`

    :param document_file_id: A valid file identifier for the file
    :type document_file_id: :obj:`str`

    :param description: Optional. Short description of the result
    :type description: :obj:`str`

    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the file
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultCachedDocument`
    """

    def __init__(
        self,
        title: "str",
        document_file_id: "str",
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "cacheddocument"
        self.id = random.randint(10000, 99999)
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultCachedDocument"]:
        return (
            InlineQueryResultCachedDocument(
                me=me,
                json=d,
                title=d.get("title"),
                document_file_id=d.get("document_file_id"),
                description=d.get("description"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultCachedVideo(Type_):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcachedvideo

    :param type: Type of the result, must be video
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param video_file_id: A valid file identifier for the video file
    :type video_file_id: :obj:`str`

    :param title: Title for the result
    :type title: :obj:`str`

    :param description: Optional. Short description of the result
    :type description: :obj:`str`

    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the video
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param show_caption_above_media: Optional. Pass True, if a caption is not required for the media
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultCachedVideo`
    """

    def __init__(
        self,
        video_file_id: "str",
        title: "str",
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "cachedvideo"
        self.id = random.randint(10000, 99999)
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultCachedVideo"]:
        return (
            InlineQueryResultCachedVideo(
                me=me,
                json=d,
                video_file_id=d.get("video_file_id"),
                title=d.get("title"),
                description=d.get("description"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultCachedVoice(Type_):
    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcachedvoice

    :param type: Type of the result, must be voice
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param voice_file_id: A valid file identifier for the voice message
    :type voice_file_id: :obj:`str`

    :param title: Voice message title
    :type title: :obj:`str`

    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the voice message caption. See formatting options for
        more details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the voice message
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultCachedVoice`
    """

    def __init__(
        self,
        voice_file_id: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "cachedvoice"
        self.id = random.randint(10000, 99999)
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultCachedVoice"]:
        return (
            InlineQueryResultCachedVoice(
                me=me,
                json=d,
                voice_file_id=d.get("voice_file_id"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InlineQueryResultCachedAudio(Type_):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultcachedaudio

    :param type: Type of the result, must be audio
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param audio_file_id: A valid file identifier for the audio file
    :type audio_file_id: :obj:`str`

    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the audio
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultCachedAudio`
    """

    def __init__(
        self,
        audio_file_id: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "cachedaudio"
        self.id = random.randint(10000, 99999)
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InlineQueryResultCachedAudio"]:
        return (
            InlineQueryResultCachedAudio(
                me=me,
                json=d,
                audio_file_id=d.get("audio_file_id"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                reply_markup=InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputMessageContent(Type_):
    def __init__(
        self,
        message_text: "str",
        parse_mode: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputMessageContent"]:
        return (
            InputMessageContent(
                me=me,
                json=d,
                message_text=d.get("message_text"),
                parse_mode=d.get("parse_mode"),
                entities=[MessageEntity._parse(me=me, d=i) for i in d.get("entities")]
                if d.get("entities")
                else None,
                link_preview_options=LinkPreviewOptions._parse(
                    me=me, d=d.get("link_preview_options")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputTextMessageContent(Type_):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inputtextmessagecontent

    :param message_text: Text of the message to be sent, 1-4096 characters
    :type message_text: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the message text. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param entities: Optional. List of special entities that appear in message text, which can be specified instead of
        parse_mode
    :type entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param disable_web_page_preview: deprecated
    :type disable_web_page_preview: :obj:`bool`

    :param link_preview_options: Optional. Link preview generation options for the message
    :type link_preview_options: :class:`tgram.types.LinkPreviewOptions`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputTextMessageContent`
    """

    def __init__(
        self,
        message_text: "str",
        parse_mode: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputTextMessageContent"]:
        return (
            InputTextMessageContent(
                me=me,
                json=d,
                message_text=d.get("message_text"),
                parse_mode=d.get("parse_mode"),
                entities=[MessageEntity._parse(me=me, d=i) for i in d.get("entities")]
                if d.get("entities")
                else None,
                link_preview_options=LinkPreviewOptions._parse(
                    me=me, d=d.get("link_preview_options")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputLocationMessageContent(Type_):
    """
    Represents the content of a location message to be sent as the result of an inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inputlocationmessagecontent

    :param latitude: Latitude of the location in degrees
    :type latitude: :obj:`float`

    :param longitude: Longitude of the location in degrees
    :type longitude: :obj:`float`

    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :type horizontal_accuracy: :obj:`float` number

    :param live_period: Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
    :type live_period: :obj:`int`

    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :type heading: :obj:`int`

    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :type proximity_alert_radius: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputLocationMessageContent`
    """

    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputLocationMessageContent"]:
        return (
            InputLocationMessageContent(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                horizontal_accuracy=d.get("horizontal_accuracy"),
                live_period=d.get("live_period"),
                heading=d.get("heading"),
                proximity_alert_radius=d.get("proximity_alert_radius"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputVenueMessageContent(Type_):
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inputvenuemessagecontent

    :param latitude: Latitude of the venue in degrees
    :type latitude: :obj:`float`

    :param longitude: Longitude of the venue in degrees
    :type longitude: :obj:`float`

    :param title: Name of the venue
    :type title: :obj:`str`

    :param address: Address of the venue
    :type address: :obj:`str`

    :param foursquare_id: Optional. Foursquare identifier of the venue, if known
    :type foursquare_id: :obj:`str`

    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example,
        “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :type foursquare_type: :obj:`str`

    :param google_place_id: Optional. Google Places identifier of the venue
    :type google_place_id: :obj:`str`

    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :type google_place_type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputVenueMessageContent`
    """

    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        title: "str",
        address: "str",
        foursquare_id: "str" = None,
        foursquare_type: "str" = None,
        google_place_id: "str" = None,
        google_place_type: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputVenueMessageContent"]:
        return (
            InputVenueMessageContent(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                address=d.get("address"),
                foursquare_id=d.get("foursquare_id"),
                foursquare_type=d.get("foursquare_type"),
                google_place_id=d.get("google_place_id"),
                google_place_type=d.get("google_place_type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputContactMessageContent(Type_):
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inputcontactmessagecontent

    :param phone_number: Contact's phone number
    :type phone_number: :obj:`str`

    :param first_name: Contact's first name
    :type first_name: :obj:`str`

    :param last_name: Optional. Contact's last name
    :type last_name: :obj:`str`

    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    :type vcard: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputContactMessageContent`
    """

    def __init__(
        self,
        phone_number: "str",
        first_name: "str",
        last_name: "str" = None,
        vcard: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputContactMessageContent"]:
        return (
            InputContactMessageContent(
                me=me,
                json=d,
                phone_number=d.get("phone_number"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                vcard=d.get("vcard"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputInvoiceMessageContent(Type_):
    """
    Represents the content of an invoice message to be sent as the result of an inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inputinvoicemessagecontent

    :param title: Product name, 1-32 characters
    :type title: :obj:`str`

    :param description: Product description, 1-255 characters
    :type description: :obj:`str`

    :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your
        internal processes.
    :type payload: :obj:`str`

    :param provider_token: Payment provider token, obtained via @BotFather
    :type provider_token: :obj:`str`

    :param currency: Three-letter ISO 4217 currency code, see more on currencies
    :type currency: :obj:`str`

    :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery
        cost, delivery tax, bonus, etc.)
    :type prices: :obj:`list` of :class:`tgram.types.LabeledPrice`

    :param max_tip_amount: Optional. The maximum accepted amount for tips in the smallest units of the currency
        (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp
        parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the
        majority of currencies). Defaults to 0
    :type max_tip_amount: :obj:`int`

    :param suggested_tip_amounts: Optional. A JSON-serialized array of suggested amounts of tip in the smallest units
        of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip
        amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
    :type suggested_tip_amounts: :obj:`list` of :obj:`int`

    :param provider_data: Optional. A JSON-serialized object for data about the invoice, which will be shared with the
        payment provider. A detailed description of the required fields should be provided by the payment provider.
    :type provider_data: :obj:`str`

    :param photo_url: Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image
        for a service.
    :type photo_url: :obj:`str`

    :param photo_size: Optional. Photo size in bytes
    :type photo_size: :obj:`int`

    :param photo_width: Optional. Photo width
    :type photo_width: :obj:`int`

    :param photo_height: Optional. Photo height
    :type photo_height: :obj:`int`

    :param need_name: Optional. Pass True, if you require the user's full name to complete the order
    :type need_name: :obj:`bool`

    :param need_phone_number: Optional. Pass True, if you require the user's phone number to complete the order
    :type need_phone_number: :obj:`bool`

    :param need_email: Optional. Pass True, if you require the user's email address to complete the order
    :type need_email: :obj:`bool`

    :param need_shipping_address: Optional. Pass True, if you require the user's shipping address to complete the
        order
    :type need_shipping_address: :obj:`bool`

    :param send_phone_number_to_provider: Optional. Pass True, if the user's phone number should be sent to provider
    :type send_phone_number_to_provider: :obj:`bool`

    :param send_email_to_provider: Optional. Pass True, if the user's email address should be sent to provider
    :type send_email_to_provider: :obj:`bool`

    :param is_flexible: Optional. Pass True, if the final price depends on the shipping method
    :type is_flexible: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputInvoiceMessageContent`
    """

    def __init__(
        self,
        title: "str",
        description: "str",
        payload: "str",
        currency: "str",
        prices: List["LabeledPrice"],
        provider_token: "str" = None,
        max_tip_amount: "int" = None,
        suggested_tip_amounts: List["int"] = None,
        provider_data: "str" = None,
        photo_url: "str" = None,
        photo_size: "int" = None,
        photo_width: "int" = None,
        photo_height: "int" = None,
        need_name: "bool" = None,
        need_phone_number: "bool" = None,
        need_email: "bool" = None,
        need_shipping_address: "bool" = None,
        send_phone_number_to_provider: "bool" = None,
        send_email_to_provider: "bool" = None,
        is_flexible: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputInvoiceMessageContent"]:
        return (
            InputInvoiceMessageContent(
                me=me,
                json=d,
                title=d.get("title"),
                description=d.get("description"),
                payload=d.get("payload"),
                currency=d.get("currency"),
                prices=[LabeledPrice._parse(me=me, d=i) for i in d.get("prices")]
                if d.get("prices")
                else None,
                provider_token=d.get("provider_token"),
                max_tip_amount=d.get("max_tip_amount"),
                suggested_tip_amounts=d.get("suggested_tip_amounts"),
                provider_data=d.get("provider_data"),
                photo_url=d.get("photo_url"),
                photo_size=d.get("photo_size"),
                photo_width=d.get("photo_width"),
                photo_height=d.get("photo_height"),
                need_name=d.get("need_name"),
                need_phone_number=d.get("need_phone_number"),
                need_email=d.get("need_email"),
                need_shipping_address=d.get("need_shipping_address"),
                send_phone_number_to_provider=d.get("send_phone_number_to_provider"),
                send_email_to_provider=d.get("send_email_to_provider"),
                is_flexible=d.get("is_flexible"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ChosenInlineResult(Type_):
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.

    Telegram Documentation: https://core.telegram.org/bots/api#choseninlineresult

    :param result_id: The unique identifier for the result that was chosen
    :type result_id: :obj:`str`

    :param from: The user that chose the result
    :type from: :class:`tgram.types.User`

    :param location: Optional. Sender location, only for bots that require user location
    :type location: :class:`tgram.types.Location`

    :param inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline
        keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
    :type inline_message_id: :obj:`str`

    :param query: The query that was used to obtain the result
    :type query: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChosenInlineResult`
    """

    def __init__(
        self,
        result_id: "str",
        from_user: "User",
        query: "str",
        location: "Location" = None,
        inline_message_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.result_id = result_id
        self.from_user = from_user
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["ChosenInlineResult"]:
        return (
            ChosenInlineResult(
                me=me,
                json=d,
                result_id=d.get("result_id"),
                from_user=User._parse(me=me, d=d.get("from")),
                query=d.get("query"),
                location=Location._parse(me=me, d=d.get("location")),
                inline_message_id=d.get("inline_message_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class SentWebAppMessage(Type_):
    """
    Describes an inline message sent by a Web App on behalf of a user.

    Telegram Documentation: https://core.telegram.org/bots/api#sentwebappmessage

    :param inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline
        keyboard attached to the message.
    :type inline_message_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.SentWebAppMessage`
    """

    def __init__(
        self,
        inline_message_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.inline_message_id = inline_message_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["SentWebAppMessage"]:
        return (
            SentWebAppMessage(
                me=me,
                json=d,
                inline_message_id=d.get("inline_message_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class LabeledPrice(Type_):
    """
    This object represents a portion of the price for goods or services.

    Telegram Documentation: https://core.telegram.org/bots/api#labeledprice

    :param label: Portion label
    :type label: :obj:`str`

    :param amount: Price of the product in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past
        the decimal point for each currency (2 for the majority of currencies).
    :type amount: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.LabeledPrice`
    """

    def __init__(
        self, label: "str", amount: "int", me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.label = label
        self.amount = amount

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["LabeledPrice"]:
        return (
            LabeledPrice(
                me=me,
                json=d,
                label=d.get("label"),
                amount=d.get("amount"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Invoice(Type_):
    """
    This object contains basic information about an invoice.

    Telegram Documentation: https://core.telegram.org/bots/api#invoice

    :param title: Product name
    :type title: :obj:`str`

    :param description: Product description
    :type description: :obj:`str`

    :param start_parameter: Unique bot deep-linking parameter that can be used to generate this invoice
    :type start_parameter: :obj:`str`

    :param currency: Three-letter ISO 4217 currency code
    :type currency: :obj:`str`

    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past
        the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Invoice`
    """

    def __init__(
        self,
        title: "str",
        description: "str",
        start_parameter: "str",
        currency: "str",
        total_amount: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Invoice"]:
        return (
            Invoice(
                me=me,
                json=d,
                title=d.get("title"),
                description=d.get("description"),
                start_parameter=d.get("start_parameter"),
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ShippingAddress(Type_):
    """
    This object represents a shipping address.

    Telegram Documentation: https://core.telegram.org/bots/api#shippingaddress

    :param country_code: Two-letter ISO 3166-1 alpha-2 country code
    :type country_code: :obj:`str`

    :param state: State, if applicable
    :type state: :obj:`str`

    :param city: City
    :type city: :obj:`str`

    :param street_line1: First line for the address
    :type street_line1: :obj:`str`

    :param street_line2: Second line for the address
    :type street_line2: :obj:`str`

    :param post_code: Address post code
    :type post_code: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ShippingAddress`
    """

    def __init__(
        self,
        country_code: "str",
        state: "str",
        city: "str",
        street_line1: "str",
        street_line2: "str",
        post_code: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ShippingAddress"]:
        return (
            ShippingAddress(
                me=me,
                json=d,
                country_code=d.get("country_code"),
                state=d.get("state"),
                city=d.get("city"),
                street_line1=d.get("street_line1"),
                street_line2=d.get("street_line2"),
                post_code=d.get("post_code"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class OrderInfo(Type_):
    """
    This object represents information about an order.

    Telegram Documentation: https://core.telegram.org/bots/api#orderinfo

    :param name: Optional. User name
    :type name: :obj:`str`

    :param phone_number: Optional. User's phone number
    :type phone_number: :obj:`str`

    :param email: Optional. User email
    :type email: :obj:`str`

    :param shipping_address: Optional. User shipping address
    :type shipping_address: :class:`tgram.types.ShippingAddress`

    :return: Instance of the class
    :rtype: :class:`tgram.types.OrderInfo`
    """

    def __init__(
        self,
        name: "str" = None,
        phone_number: "str" = None,
        email: "str" = None,
        shipping_address: "ShippingAddress" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["OrderInfo"]:
        return (
            OrderInfo(
                me=me,
                json=d,
                name=d.get("name"),
                phone_number=d.get("phone_number"),
                email=d.get("email"),
                shipping_address=ShippingAddress._parse(
                    me=me, d=d.get("shipping_address")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ShippingOption(Type_):
    """
    This object represents one shipping option.

    Telegram Documentation: https://core.telegram.org/bots/api#shippingoption

    :param id: Shipping option identifier
    :type id: :obj:`str`

    :param title: Option title
    :type title: :obj:`str`

    :param prices: List of price portions
    :type prices: :obj:`list` of :class:`tgram.types.LabeledPrice`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ShippingOption`
    """

    def __init__(
        self,
        id: "str",
        title: "str",
        prices: List["LabeledPrice"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.title = title
        self.prices = prices

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ShippingOption"]:
        return (
            ShippingOption(
                me=me,
                json=d,
                id=d.get("id"),
                title=d.get("title"),
                prices=[LabeledPrice._parse(me=me, d=i) for i in d.get("prices")]
                if d.get("prices")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class SuccessfulPayment(Type_):
    """
    This object contains basic information about a successful payment.

    Telegram Documentation: https://core.telegram.org/bots/api#successfulpayment

    :param currency: Three-letter ISO 4217 currency code
    :type currency: :obj:`str`

    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past
        the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`

    :param invoice_payload: Bot specified invoice payload
    :type invoice_payload: :obj:`str`

    :param shipping_option_id: Optional. Identifier of the shipping option chosen by the user
    :type shipping_option_id: :obj:`str`

    :param order_info: Optional. Order information provided by the user
    :type order_info: :class:`tgram.types.OrderInfo`

    :param telegram_payment_charge_id: Telegram payment identifier
    :type telegram_payment_charge_id: :obj:`str`

    :param provider_payment_charge_id: Provider payment identifier
    :type provider_payment_charge_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.SuccessfulPayment`
    """

    def __init__(
        self,
        currency: "str",
        total_amount: "int",
        invoice_payload: "str",
        telegram_payment_charge_id: "str",
        provider_payment_charge_id: "str",
        shipping_option_id: "str" = None,
        order_info: "OrderInfo" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["SuccessfulPayment"]:
        return (
            SuccessfulPayment(
                me=me,
                json=d,
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
                invoice_payload=d.get("invoice_payload"),
                telegram_payment_charge_id=d.get("telegram_payment_charge_id"),
                provider_payment_charge_id=d.get("provider_payment_charge_id"),
                shipping_option_id=d.get("shipping_option_id"),
                order_info=OrderInfo._parse(me=me, d=d.get("order_info")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class RefundedPayment(Type_):
    def __init__(
        self,
        currency: "str",
        total_amount: "int",
        invoice_payload: "str",
        telegram_payment_charge_id: "str",
        provider_payment_charge_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ) -> None:
        super().__init__(me=me, json=json)
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["RefundedPayment"]:
        return (
            RefundedPayment(
                me=me,
                json=d,
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
                invoice_payload=d.get("invoice_payload"),
                telegram_payment_charge_id=d.get("telegram_payment_charge_id"),
                provider_payment_charge_id=d.get("provider_payment_charge_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class ShippingQuery(Type_):
    """
    This object contains information about an incoming shipping query.

    Telegram Documentation: https://core.telegram.org/bots/api#shippingquery

    :param id: Unique query identifier
    :type id: :obj:`str`

    :param from: User who sent the query
    :type from: :class:`tgram.types.User`

    :param invoice_payload: Bot specified invoice payload
    :type invoice_payload: :obj:`str`

    :param shipping_address: User specified shipping address
    :type shipping_address: :class:`tgram.types.ShippingAddress`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ShippingQuery`
    """

    def __init__(
        self,
        id: "str",
        from_user: "User",
        invoice_payload: "str",
        shipping_address: "ShippingAddress",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["ShippingQuery"]:
        return (
            ShippingQuery(
                me=me,
                json=d,
                id=d.get("id"),
                from_user=User._parse(me=me, d=d.get("from")),
                invoice_payload=d.get("invoice_payload"),
                shipping_address=ShippingAddress._parse(
                    me=me, d=d.get("shipping_address")
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PreCheckoutQuery(Type_):
    """
    This object contains information about an incoming pre-checkout query.

    Telegram Documentation: https://core.telegram.org/bots/api#precheckoutquery

    :param id: Unique query identifier
    :type id: :obj:`str`

    :param from: User who sent the query
    :type from: :class:`tgram.types.User`

    :param currency: Three-letter ISO 4217 currency code
    :type currency: :obj:`str`

    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past
        the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`

    :param invoice_payload: Bot specified invoice payload
    :type invoice_payload: :obj:`str`

    :param shipping_option_id: Optional. Identifier of the shipping option chosen by the user
    :type shipping_option_id: :obj:`str`

    :param order_info: Optional. Order information provided by the user
    :type order_info: :class:`tgram.types.OrderInfo`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PreCheckoutQuery`
    """

    def __init__(
        self,
        id: "str",
        from_user: "User",
        currency: "str",
        total_amount: "int",
        invoice_payload: "str",
        shipping_option_id: "str" = None,
        order_info: "OrderInfo" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PreCheckoutQuery"]:
        return (
            PreCheckoutQuery(
                me=me,
                json=d,
                id=d.get("id"),
                from_user=User._parse(me=me, d=d.get("from")),
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
                invoice_payload=d.get("invoice_payload"),
                shipping_option_id=d.get("shipping_option_id"),
                order_info=OrderInfo._parse(me=me, d=d.get("order_info")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


RevenueWithdrawalState = Union[
    "RevenueWithdrawalStatePending",
    "RevenueWithdrawalStateSucceeded",
    "RevenueWithdrawalStateFailed",
]


class RevenueWithdrawalStatePending(Type_):
    """
    The withdrawal is in progress.

    Telegram documentation: https://core.telegram.org/bots/api#revenuewithdrawalstatepending

    :param type: Type of the state, always “pending”
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`RevenueWithdrawalStatePending`
    """

    def __init__(self, me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = "pending"

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["RevenueWithdrawalStatePending"]:
        return (
            RevenueWithdrawalStatePending(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class RevenueWithdrawalStateSucceeded(Type_):
    """
    The withdrawal succeeded.

    Telegram documentation: https://core.telegram.org/bots/api#revenuewithdrawalstatesucceeded

    :param type: Type of the state, always “succeeded”
    :type type: :obj:`str`

    :param date: Date the withdrawal was completed in Unix time
    :type date: :obj:`int`

    :param url: An HTTPS URL that can be used to see transaction details
    :type url: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`RevenueWithdrawalStateSucceeded`
    """

    def __init__(
        self,
        date: "int",
        url: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "succeeded"
        self.date = date
        self.url = url

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["RevenueWithdrawalStateSucceeded"]:
        return (
            RevenueWithdrawalStateSucceeded(
                me=me,
                json=d,
                type=d.get("type"),
                date=d.get("date"),
                url=d.get("url"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class RevenueWithdrawalStateFailed(Type_):
    """
    The withdrawal failed and the transaction was refunded.

    Telegram documentation: https://core.telegram.org/bots/api#revenuewithdrawalstatefailed

    :param type: Type of the state, always “failed”
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`RevenueWithdrawalStateFailed`
    """

    def __init__(self, me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = "faield"

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["RevenueWithdrawalStateFailed"]:
        return (
            RevenueWithdrawalStateFailed(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


TransactionPartner = Union[
    "TransactionPartnerFragment",
    "TransactionPartnerUser",
    "TransactionPartnerOther",
    "TransactionPartnerTelegramAds",
]


class TransactionPartnerFragment(Type_):
    """
    Describes a withdrawal transaction with Fragment.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartnerfragment

    :param type: Type of the transaction partner, always “fragment”
    :type type: :obj:`str`

    :param withdrawal_state: Optional. State of the transaction if the transaction is outgoing
    :type withdrawal_state: :class:`RevenueWithdrawalState`

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerFragment`

    """

    def __init__(
        self,
        withdrawal_state: "RevenueWithdrawalState" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "fragment"
        self.withdrawal_state = withdrawal_state

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["TransactionPartnerFragment"]:
        return (
            TransactionPartnerFragment(
                me=me,
                json=d,
                type=d.get("type"),
                withdrawal_state=None
                if not d.get("withdrawal_state")
                else (
                    RevenueWithdrawalStateSucceeded._parse(
                        me=me, d=d.get("withdrawal_state")
                    )
                    if d["type"] == "succeeded"
                    else RevenueWithdrawalStateFailed._parse(
                        me=me, d=d.get("withdrawal_state")
                    )
                    if d["type"] == "failed"
                    else RevenueWithdrawalStatePending._parse(
                        me=me, d=d.get("withdrawal_state")
                    )
                ),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class TransactionPartnerUser(Type_):
    """
    Describes a transaction with a user.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartneruser

    :param type: Type of the transaction partner, always “user”
    :type type: :obj:`str`

    :param user: Information about the user
    :type user: :class:`User`

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerUser`
    """

    def __init__(
        self,
        user: "User",
        invoice_payload: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "user"
        self.user = user
        self.invoice_payload = invoice_payload

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["TransactionPartnerUser"]:
        return (
            TransactionPartnerUser(
                me=me,
                json=d,
                type=d.get("type"),
                user=User._parse(me=me, d=d.get("user")),
                invoice_payload=d.get("invoice_payload"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class TransactionPartnerOther(Type_):
    """
    Describes a transaction with an unknown source or recipient.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartnerother

    :param type: Type of the transaction partner, always “other”
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerOther`
    """

    def __init__(self, me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = "other"

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["TransactionPartnerOther"]:
        return (
            TransactionPartnerOther(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class StarTransaction(Type_):
    """
    Describes a Telegram Star transaction.

    Telegram documentation: https://core.telegram.org/bots/api#startransaction

    :param id: Unique identifier of the transaction. Coincides with the identifer of the original transaction for refund transactions. Coincides with SuccessfulPayment.telegram_payment_charge_id for successful incoming payments from users.
    :type id: :obj:`str`

    :param amount: Number of Telegram Stars transferred by the transaction
    :type amount: :obj:`int`

    :param date: Date the transaction was created in Unix time
    :type date: :obj:`int`

    :param source: Optional. Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions
    :type source: :class:`TransactionPartner`

    :param receiver: Optional. Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions
    :type receiver: :class:`TransactionPartner`

    :return: Instance of the class
    :rtype: :class:`StarTransaction`
    """

    def __init__(
        self,
        id: "str",
        amount: "int",
        date: "int",
        source: "TransactionPartner" = None,
        receiver: "TransactionPartner" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.amount = amount
        self.date = date
        self.source = source
        self.receiver = receiver

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["StarTransaction"]:
        return (
            StarTransaction(
                me=me,
                json=d,
                id=d.get("id"),
                amount=d.get("amount"),
                date=d.get("date"),
                source=TransactionPartner._parse(me=me, d=d.get("source")),
                receiver=TransactionPartner._parse(me=me, d=d.get("receiver")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class TransactionPartnerTelegramAds(Type_):
    def __init__(self, me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = "telegram_ads"

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["TransactionPartnerTelegramAds"]:
        return (
            TransactionPartnerTelegramAds(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class StarTransactions(Type_):
    """
    Contains a list of Telegram Star transactions.

    Telegram documentation: https://core.telegram.org/bots/api#startransactions

    :param transactions: The list of transactions
    :type transactions: :obj:`list` of :class:`StarTransaction`

    :return: Instance of the class
    :rtype: :class:`StarTransactions`

    """

    def __init__(
        self,
        transactions: List["StarTransaction"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.transactions = transactions

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["StarTransactions"]:
        return (
            StarTransactions(
                me=me,
                json=d,
                transactions=[
                    StarTransaction._parse(me=me, d=i) for i in d.get("transactions")
                ]
                if d.get("transactions")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportData(Type_):
    def __init__(
        self,
        data: List["EncryptedPassportElement"],
        credentials: "EncryptedCredentials",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.data = data
        self.credentials = credentials

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["PassportData"]:
        return (
            PassportData(
                me=me,
                json=d,
                data=[
                    EncryptedPassportElement._parse(me=me, d=i) for i in d.get("data")
                ]
                if d.get("data")
                else None,
                credentials=EncryptedCredentials._parse(me=me, d=d.get("credentials")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportFile(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        file_size: "int",
        file_date: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["PassportFile"]:
        return (
            PassportFile(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                file_size=d.get("file_size"),
                file_date=d.get("file_date"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class EncryptedPassportElement(Type_):
    def __init__(
        self,
        type: "str",
        hash: "str",
        data: "str" = None,
        phone_number: "str" = None,
        email: "str" = None,
        files: List["PassportFile"] = None,
        front_side: "PassportFile" = None,
        reverse_side: "PassportFile" = None,
        selfie: "PassportFile" = None,
        translation: List["PassportFile"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.hash = hash

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["EncryptedPassportElement"]:
        return (
            EncryptedPassportElement(
                me=me,
                json=d,
                type=d.get("type"),
                hash=d.get("hash"),
                data=d.get("data"),
                phone_number=d.get("phone_number"),
                email=d.get("email"),
                files=[PassportFile._parse(me=me, d=i) for i in d.get("files")]
                if d.get("files")
                else None,
                front_side=PassportFile._parse(me=me, d=d.get("front_side")),
                reverse_side=PassportFile._parse(me=me, d=d.get("reverse_side")),
                selfie=PassportFile._parse(me=me, d=d.get("selfie")),
                translation=[
                    PassportFile._parse(me=me, d=i) for i in d.get("translation")
                ]
                if d.get("translation")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class EncryptedCredentials(Type_):
    def __init__(
        self,
        data: "str",
        hash: "str",
        secret: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.data = data
        self.hash = hash
        self.secret = secret

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["EncryptedCredentials"]:
        return (
            EncryptedCredentials(
                me=me,
                json=d,
                data=d.get("data"),
                hash=d.get("hash"),
                secret=d.get("secret"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementError(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        field_name: "str",
        data_hash: "str",
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementError"]:
        return (
            PassportElementError(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                field_name=d.get("field_name"),
                data_hash=d.get("data_hash"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorDataField(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        field_name: "str",
        data_hash: "str",
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorDataField"]:
        return (
            PassportElementErrorDataField(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                field_name=d.get("field_name"),
                data_hash=d.get("data_hash"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorFrontSide(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorFrontSide"]:
        return (
            PassportElementErrorFrontSide(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorReverseSide(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorReverseSide"]:
        return (
            PassportElementErrorReverseSide(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorSelfie(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorSelfie"]:
        return (
            PassportElementErrorSelfie(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorFile(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorFile"]:
        return (
            PassportElementErrorFile(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorFiles(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hashes: List["str"],
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorFiles"]:
        return (
            PassportElementErrorFiles(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hashes=d.get("file_hashes"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorTranslationFile(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorTranslationFile"]:
        return (
            PassportElementErrorTranslationFile(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorTranslationFiles(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hashes: List["str"],
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorTranslationFiles"]:
        return (
            PassportElementErrorTranslationFiles(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hashes=d.get("file_hashes"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PassportElementErrorUnspecified(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        element_hash: "str",
        message: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PassportElementErrorUnspecified"]:
        return (
            PassportElementErrorUnspecified(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                element_hash=d.get("element_hash"),
                message=d.get("message"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class Game(Type_):
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Telegram Documentation: https://core.telegram.org/bots/api#game

    :param title: Title of the game
    :type title: :obj:`str`

    :param description: Description of the game
    :type description: :obj:`str`

    :param photo: Photo that will be displayed in the game message in chats.
    :type photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param text: Optional. Brief description of the game or high scores included in the game message. Can be
        automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited
        using editMessageText. 0-4096 characters.
    :type text: :obj:`str`

    :param text_entities: Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    :type text_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param animation: Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
    :type animation: :class:`tgram.types.Animation`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Game`
    """

    def __init__(
        self,
        title: "str",
        description: "str",
        photo: List["PhotoSize"],
        text: "str" = None,
        text_entities: List["MessageEntity"] = None,
        animation: "Animation" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["Game"]:
        return (
            Game(
                me=me,
                json=d,
                title=d.get("title"),
                description=d.get("description"),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
                text=d.get("text"),
                text_entities=[
                    MessageEntity._parse(me=me, d=i) for i in d.get("text_entities")
                ]
                if d.get("text_entities")
                else None,
                animation=Animation._parse(me=me, d=d.get("animation")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class CallbackGame(Type_):
    def __init__(
        self,
        user_id: "int",
        score: "int",
        force: "bool" = None,
        disable_edit_message: "bool" = None,
        chat_id: "int" = None,
        message_id: "int" = None,
        inline_message_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.user_id = user_id
        self.score = score
        self.force = force
        self.disable_edit_message = disable_edit_message
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["CallbackGame"]:
        return (
            CallbackGame(
                me=me,
                json=d,
                user_id=d.get("user_id"),
                score=d.get("score"),
                force=d.get("force"),
                disable_edit_message=d.get("disable_edit_message"),
                chat_id=d.get("chat_id"),
                message_id=d.get("message_id"),
                inline_message_id=d.get("inline_message_id"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class GameHighScore(Type_):
    """
    This object represents one row of the high scores table for a game.

    Telegram Documentation: https://core.telegram.org/bots/api#gamehighscore

    :param position: Position in high score table for the game
    :type position: :obj:`int`

    :param user: User
    :type user: :class:`tgram.types.User`

    :param score: Score
    :type score: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.GameHighScore`
    """

    def __init__(
        self,
        position: "int",
        user: "User",
        score: "int",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.position = position
        self.user = user
        self.score = score

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["GameHighScore"]:
        return (
            GameHighScore(
                me=me,
                json=d,
                position=d.get("position"),
                user=User._parse(me=me, d=d.get("user")),
                score=d.get("score"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PaidMediaInfo(Type_):
    def __init__(
        self,
        star_count: "int",
        paid_media: List["PaidMedia"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.star_count = star_count
        self.paid_media = paid_media

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["PaidMediaInfo"]:
        return (
            PaidMediaInfo(
                me=me,
                json=d,
                star_count=d.get("star_count"),
                paid_media=[
                    PaidMediaPreview._parse(me=me, d=i)
                    if i["type"] == "preview"
                    else PaidMediaPhoto._parse(me=me, d=i)
                    if i["type"] == "photo"
                    else PaidMediaVideo._parse(me=me, d=i)
                    for i in d.get("paid_media")
                ]
                if d.get("paid_media")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


PaidMedia = Union["PaidMediaPreview", "PaidMediaPhoto", "PaidMediaVideo"]


class PaidMediaPreview(Type_):
    def __init__(
        self,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "preview"
        self.width = width
        self.height = height
        self.duration = duration

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["PaidMediaPreview"]:
        return (
            PaidMediaPreview(
                me=me,
                json=d,
                type=d.get("type"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PaidMediaPhoto(Type_):
    def __init__(
        self,
        photo: List["PhotoSize"],
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "photo"
        self.photo = photo

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["PaidMediaPhoto"]:
        return (
            PaidMediaPhoto(
                me=me,
                json=d,
                type=d.get("type"),
                photo=[PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class PaidMediaVideo(Type_):
    def __init__(self, video: "Video", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.video = video

    @staticmethod
    def _parse(me: "tgram.TgBot" = None, d: dict = None) -> Optional["PaidMediaVideo"]:
        return (
            PaidMediaVideo(
                me=me,
                json=d,
                type=d.get("type"),
                video=Video._parse(me=me, d=d.get("video")),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


InputPaidMedia = Union["InputPaidMediaPhoto", "InputPaidMediaVideo"]


class InputPaidMediaPhoto(Type_):
    def __init__(self, media: "str", me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = "photo"
        self.media = media

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputPaidMediaPhoto"]:
        return (
            InputPaidMediaPhoto(
                me=me,
                json=d,
                type=d.get("type"),
                media=d.get("media"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )


class InputPaidMediaVideo(Type_):
    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        supports_streaming: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.media = media
        self.thumbnail = thumbnail
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None
    ) -> Optional["InputPaidMediaVideo"]:
        return (
            InputPaidMediaVideo(
                me=me,
                json=d,
                type=d.get("type"),
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                supports_streaming=d.get("supports_streaming"),
            )
            if d and me and __class__.__name__ not in me._custom_types
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d), me._custom_types.get(__class__.__name__)
            )
        )
