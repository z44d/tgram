import tgram

from tgram.types import (
    ReplyParameters,
    ParseMode,
    SuggestedPostParameters,
    Message,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    MessageEntity,
    LinkPreviewOptions,
)
from tgram.utils import (
    get_parse_mode,
    convert_to_inline_keyboard_markup,
)

from typing import Union, List


class SendMessage:
    async def send_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        text: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        parse_mode: ParseMode = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
        allow_paid_broadcast: bool = None,
        direct_messages_topic_id: int = None,
        suggested_post_parameters: SuggestedPostParameters = None,
    ) -> Message:
        """
        Use this method to send text messages.

        Warning: Do not send more than about 4096 characters each message, otherwise you'll risk an HTTP 414 error.
        If you must send more than 4096 characters,
        use the `split_string` or `smart_split` function in util.py.

        Telegram documentation: https://core.telegram.org/bots/api#sendmessage

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param text: Text of the message to be sent
        :type text: :obj:`str`

        :param parse_mode: Mode for parsing entities in the message text.
        :type parse_mode: :obj:`str`

        :param entities: List of special entities that appear in message text, which can be specified instead of parse_mode
        :type entities: Array of :class:`tgram.types.MessageEntity`

        :param disable_web_page_preview: Deprecated - Use link_preview_options instead.
        :type disable_web_page_preview: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: If True, the message content will be hidden for all users except for the target user
        :type protect_content: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param link_preview_options: Options for previewing links.
        :type link_preview_options: :class:`tgram.types.LinkPreviewOptions`

        :param business_connection_id: Unique identifier for the target business connection
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :param allow_paid_broadcast: Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
            The relevant Stars will be withdrawn from the bot's balance
        :type allow_paid_broadcast: :obj:`bool`

        :param direct_messages_topic_id: Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
        :type direct_messages_topic_id: :obj:`int`

        :param suggested_post_parameters: A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.
        :type suggested_post_parameters: :class:`tgram.types.SuggestedPostParameters`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self(
            "sendMessage",
            chat_id=chat_id,
            text=text,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            parse_mode=get_parse_mode(self, parse_mode),
            entities=entities,
            link_preview_options=link_preview_options or self.link_preview_options,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
            allow_paid_broadcast=allow_paid_broadcast,
            direct_messages_topic_id=direct_messages_topic_id,
            suggested_post_parameters=suggested_post_parameters,
        )
        return Message._parse(me=self, d=result.get("result", {}))
