import tgram
from typing import List
from typing import Union
from tgram.types import ForceReply
from tgram.types import InlineKeyboardMarkup
from tgram.types import InputPaidMedia
from tgram.types import Message
from tgram.types import MessageEntity
from tgram.types import ReplyKeyboardMarkup
from tgram.types import ReplyKeyboardRemove
from tgram.types import ReplyParameters, ParseMode

from tgram.utils import convert_input_media, get_parse_mode


class SendPaidMedia:
    async def send_paid_media(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        star_count: int,
        media: List[InputPaidMedia],
        payload: str = None,
        caption: str = None,
        parse_mode: ParseMode = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
        business_connection_id: str = None,
    ) -> Message:
        """
        Use this method to send paid media to channel chats. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendpaidmedia

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param star_count: The number of Telegram Stars that must be paid to buy access to the media
        :type star_count: :obj:`int`

        :param media: A JSON-serialized array describing the media to be sent; up to 10 items
        :type media: :obj:`list` of :class:`tgram.types.InputPaidMedia`

        :param caption: Media caption, 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param payload: Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes.
        :type payload: :obj:`str`

        :param parse_mode: Mode for parsing entities in the media caption
        :type parse_mode: :obj:`str`

        :param caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param show_caption_above_media: Pass True, if the caption must be shown above the message media
        :type show_caption_above_media: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param reply_parameters: Description of the message to reply to
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove` or :class:`tgram.types.ForceReply`

        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent
        :type protect_content: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """
        arr, files = convert_input_media(media)
        result = await self._send_request(
            "sendPaidMedia",
            chat_id=chat_id,
            star_count=star_count,
            media=arr,
            payload=payload,
            caption=caption,
            parse_mode=get_parse_mode(self, parse_mode),
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
            business_connection_id=business_connection_id,
            **files,
        )
        return Message._parse(me=self, d=result["result"])
