import tgram
from .type_ import Type_

from typing import List, Optional, Union

from pathlib import Path


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
        media: Union["Path", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
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
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputMediaPhoto"]:
        return (
            InputMediaPhoto(
                me=me,
                json=d,
                media=d.get("media"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                has_spoiler=d.get("has_spoiler"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
