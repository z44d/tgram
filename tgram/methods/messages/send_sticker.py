import tgram

from tgram.types import (
    ReplyParameters,
    SuggestedPostParameters,
    Message,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
)
from tgram.utils import (
    convert_to_inline_keyboard_markup,
)

from pathlib import Path
from typing import Union


class SendSticker:
    async def send_sticker(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        sticker: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        emoji: str = None,
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
        Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers.
        On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendsticker

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param sticker: Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL
            as a String for Telegram to get a .webp file from the Internet, or upload a new one using multipart/form-data.
        :type sticker: :obj:`str` or :class:`tgram.types.InputFile`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param disable_notification: to disable the notification
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param data: function typo miss compatibility: do not use it
        :type data: :obj:`str`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param emoji: Emoji associated with the sticker; only for just uploaded stickers
        :type emoji: :obj:`str`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

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
            "sendSticker",
            chat_id=chat_id,
            sticker=sticker,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            emoji=emoji,
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
