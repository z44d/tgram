import tgram
from .type_ import Type_

from typing import List, Union, Optional


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
        media: "str" = None,
        thumbnail: Union["tgram.types.InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
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
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputMediaDocument"]:
        return (
            InputMediaDocument(
                me=me,
                json=d,
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                disable_content_type_detection=d.get("disable_content_type_detection"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
