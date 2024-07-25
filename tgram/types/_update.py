import tgram
from .type_ import Type_

from typing import Optional


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
        update_id: "int" = None,
        message: "tgram.types.Message" = None,
        edited_message: "tgram.types.Message" = None,
        channel_post: "tgram.types.Message" = None,
        edited_channel_post: "tgram.types.Message" = None,
        business_connection: "tgram.types.BusinessConnection" = None,
        business_message: "tgram.types.Message" = None,
        edited_business_message: "tgram.types.Message" = None,
        deleted_business_messages: "tgram.types.BusinessMessagesDeleted" = None,
        message_reaction: "tgram.types.MessageReactionUpdated" = None,
        message_reaction_count: "tgram.types.MessageReactionCountUpdated" = None,
        inline_query: "tgram.types.InlineQuery" = None,
        chosen_inline_result: "tgram.types.ChosenInlineResult" = None,
        callback_query: "tgram.types.CallbackQuery" = None,
        shipping_query: "tgram.types.ShippingQuery" = None,
        pre_checkout_query: "tgram.types.PreCheckoutQuery" = None,
        poll: "tgram.types.Poll" = None,
        poll_answer: "tgram.types.PollAnswer" = None,
        my_chat_member: "tgram.types.ChatMemberUpdated" = None,
        chat_member: "tgram.types.ChatMemberUpdated" = None,
        chat_join_request: "tgram.types.ChatJoinRequest" = None,
        chat_boost: "tgram.types.ChatBoostUpdated" = None,
        removed_chat_boost: "tgram.types.ChatBoostRemoved" = None,
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
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Update"]:
        return (
            Update(
                me=me,
                json=d,
                update_id=d.get("update_id"),
                message=tgram.types.Message._parse(me=me, d=d.get("message")),
                edited_message=tgram.types.Message._parse(
                    me=me, d=d.get("edited_message")
                ),
                channel_post=tgram.types.Message._parse(me=me, d=d.get("channel_post")),
                edited_channel_post=tgram.types.Message._parse(
                    me=me, d=d.get("edited_channel_post")
                ),
                business_connection=tgram.types.BusinessConnection._parse(
                    me=me, d=d.get("business_connection")
                ),
                business_message=tgram.types.Message._parse(
                    me=me, d=d.get("business_message")
                ),
                edited_business_message=tgram.types.Message._parse(
                    me=me, d=d.get("edited_business_message")
                ),
                deleted_business_messages=tgram.types.BusinessMessagesDeleted._parse(
                    me=me, d=d.get("deleted_business_messages")
                ),
                message_reaction=tgram.types.MessageReactionUpdated._parse(
                    me=me, d=d.get("message_reaction")
                ),
                message_reaction_count=tgram.types.MessageReactionCountUpdated._parse(
                    me=me, d=d.get("message_reaction_count")
                ),
                inline_query=tgram.types.InlineQuery._parse(
                    me=me, d=d.get("inline_query")
                ),
                chosen_inline_result=tgram.types.ChosenInlineResult._parse(
                    me=me, d=d.get("chosen_inline_result")
                ),
                callback_query=tgram.types.CallbackQuery._parse(
                    me=me, d=d.get("callback_query")
                ),
                shipping_query=tgram.types.ShippingQuery._parse(
                    me=me, d=d.get("shipping_query")
                ),
                pre_checkout_query=tgram.types.PreCheckoutQuery._parse(
                    me=me, d=d.get("pre_checkout_query")
                ),
                poll=tgram.types.Poll._parse(me=me, d=d.get("poll")),
                poll_answer=tgram.types.PollAnswer._parse(
                    me=me, d=d.get("poll_answer")
                ),
                my_chat_member=tgram.types.ChatMemberUpdated._parse(
                    me=me, d=d.get("my_chat_member")
                ),
                chat_member=tgram.types.ChatMemberUpdated._parse(
                    me=me, d=d.get("chat_member")
                ),
                chat_join_request=tgram.types.ChatJoinRequest._parse(
                    me=me, d=d.get("chat_join_request")
                ),
                chat_boost=tgram.types.ChatBoostUpdated._parse(
                    me=me, d=d.get("chat_boost")
                ),
                removed_chat_boost=tgram.types.ChatBoostRemoved._parse(
                    me=me, d=d.get("removed_chat_boost")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
