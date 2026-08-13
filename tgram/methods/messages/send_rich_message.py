import tgram
from tgram.types import (
    ForceReply,
    InlineKeyboardMarkup,
    InputRichMessage,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
)
from tgram.utils import convert_to_inline_keyboard_markup


class SendRichMessage:
    async def send_rich_message(
        self: "tgram.TgBot",
        chat_id: int | str,
        rich_message: InputRichMessage,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply = None,
        allow_paid_broadcast: bool | None = None,
    ) -> Message:
        """
        Use this method to send a rich message.

        Telegram documentation: https://core.telegram.org/bots/api#sendrichmessage

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param rich_message: Rich message to send
        :type rich_message: :class:`tgram.types.InputRichMessage`

        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :type message_thread_id: :obj:`int`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: If True, the message content will be hidden for all users except for the target user
        :type protect_content: :obj:`bool`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param reply_markup: Additional interface options.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup`
            or :class:`tgram.types.ReplyKeyboardRemove` or :class:`tgram.types.ForceReply`

        :param allow_paid_broadcast: Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
        :type allow_paid_broadcast: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self(
            "sendRichMessage",
            chat_id=chat_id,
            rich_message=rich_message,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
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
        )
        return Message._parse(me=self, d=result.get("result", {}))
