import tgram
from .type_ import Type_

from typing import List, Union, Optional

from pathlib import Path


class InputMediaVideo(Type_):
    """
    Represents a video to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmediavideo

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

    :param cover: Optional. Cover for the video in the message.
        Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet,
        or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
    :type cover: :class:`InputFile` of :obj:`str`

    :param start_timestamp: Optional. Start timestamp for the video in the message
    :type start_timestamp: :obj:`int`

    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :type caption: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param width: Optional. Video width
    :type width: :obj:`int`

    :param height: Optional. Video height
    :type height: :obj:`int`

    :param duration: Optional. Video duration in seconds
    :type duration: :obj:`int`

    :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
    :type supports_streaming: :obj:`bool`

    :param has_spoiler: Optional. True, if the uploaded video is a spoiler
    :type has_spoiler: :obj:`bool`

    :param show_caption_above_media: Optional. True, if the caption should be shown above the video
    :type show_caption_above_media: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaVideo`
    """

    def __init__(
        self,
        media: Union["Path", "str"] = None,
        thumbnail: "tgram.types.InputFile" = None,
        cover: "tgram.types.InputFile" = None,
        start_timestamp: int = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        supports_streaming: "bool" = None,
        has_spoiler: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.media = media
        self.thumbnail = thumbnail
        self.cover = cover
        self.start_timestamp = start_timestamp
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputMediaVideo"]:
        return (
            InputMediaVideo(
                me=me,
                json=d,
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                cover=d.get("cover"),
                start_timestamp=d.get("start_timestamp"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                supports_streaming=d.get("supports_streaming"),
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
