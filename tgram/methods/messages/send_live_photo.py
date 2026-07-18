import tgram
from typing import List, Union
from tgram.types import ForceReply
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message
from tgram.types import MessageEntity
from tgram.types import ReplyKeyboardMarkup
from tgram.types import ReplyKeyboardRemove
from tgram.types import ReplyParameters, ParseMode

from tgram.utils import convert_to_inline_keyboard_markup


class SendLivePhoto:
    async def send_live_photo(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        live_photo: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: ParseMode = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
        allow_paid_broadcast: bool = None,
    ) -> Message:
        """
        Use this method to send a live photo.
        On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendlivephoto

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` | :obj:`str`

        :param live_photo: Live photo to send. Pass a file_id to send a file that exists on the Telegram servers
        :type live_photo: :obj:`str`

        :param business_connection_id: Identifier of the business connection to send the message through
        :type business_connection_id: :obj:`str`

        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum
        :type message_thread_id: :obj:`int`

        :param caption: Live photo caption, 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param parse_mode: Mode for parsing entities in the live photo caption
        :type parse_mode: :obj:`str`

        :param caption_entities: List of special entities that appear in the caption
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param show_caption_above_media: True, if the caption must be shown above the message media
        :type show_caption_above_media: :obj:`bool`

        :param has_spoiler: True, if the live photo needs to be covered with a spoiler animation
        :type has_spoiler: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param reply_markup: Additional interface options.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` | :class:`tgram.types.ReplyKeyboardMarkup` | :class:`tgram.types.ReplyKeyboardRemove` | :class:`tgram.types.ForceReply`

        :param allow_paid_broadcast: Pass True to allow up to 1000 messages per second
        :type allow_paid_broadcast: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self(
            "sendLivePhoto",
            chat_id=chat_id,
            live_photo=live_photo,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
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
