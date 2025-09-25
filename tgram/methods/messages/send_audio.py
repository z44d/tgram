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
)
from tgram.utils import get_file_path, get_parse_mode, convert_to_inline_keyboard_markup

from pathlib import Path
from typing import Union, List


class SendAudio:
    async def send_audio(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        audio: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: ParseMode = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        performer: str = None,
        title: str = None,
        thumbnail: Union[Path, bytes, str] = None,
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
        Use this method to send audio files, if you want Telegram clients to display them in the music player.
        Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size,
        this limit may be changed in the future.

        For sending voice messages, use the send_voice method instead.

        Telegram documentation: https://core.telegram.org/bots/api#sendaudio

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param audio: Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended),
            pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data.
            Audio must be in the .MP3 or .M4A format.
        :type audio: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption: Audio caption, 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param duration: Duration of the audio in seconds
        :type duration: :obj:`int`

        :param performer: Performer
        :type performer: :obj:`str`

        :param title: Track name
        :type title: :obj:`str`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup:
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.
        :type parse_mode: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
            The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,
            so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>
        :type thumbnail: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param thumb: Deprecated. Use thumbnail instead
        :type thumb: :obj:`str` or :class:`tgram.types.InputFile`

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
            "sendAudio",
            chat_id=chat_id,
            audio=get_file_path(audio),
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=get_parse_mode(self, parse_mode),
            caption_entities=caption_entities,
            duration=duration,
            performer=performer,
            title=title,
            thumbnail=get_file_path(thumbnail),
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
        return Message._parse(me=self, d=result["result"])
