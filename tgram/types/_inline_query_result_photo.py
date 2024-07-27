import tgram
import random
from .type_ import Type_

from typing import List, Optional


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
        photo_url: "str" = None,
        thumbnail_url: "str" = None,
        photo_width: "int" = None,
        photo_height: "int" = None,
        title: "str" = None,
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
        input_message_content: "tgram.types.InputMessageContent" = None,
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
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InlineQueryResultPhoto"]:
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
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=tgram.types.InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=tgram.types.InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
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
