import tgram
from .type_ import Type_

from typing import Optional, List


class Video(Type_):
    """
    This object represents a video file.

    Telegram Documentation: https://core.telegram.org/bots/api#video

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param width: Video width as defined by sender
    :type width: :obj:`int`

    :param height: Video height as defined by sender
    :type height: :obj:`int`

    :param duration: Duration of the video in seconds as defined by sender
    :type duration: :obj:`int`

    :param thumbnail: Optional. Video thumbnail
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :param cover: Optional. Video thumbnail
    :type cover: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param start_timestamp: Optional. Timestamp in seconds from which the video will play in the message
    :type start_timestamp: :obj:`int`

    :param file_name: Optional. Original filename as defined by sender
    :type file_name: :obj:`str`

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type mime_type: :obj:`str`

    :param file_size: Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Video`
    """

    def __init__(
        self,
        file_id: "str" = None,
        file_unique_id: "str" = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        thumbnail: "tgram.types.PhotoSize" = None,
        cover: List["tgram.types.PhotoSize"] = None,
        start_timestamp: "int" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.cover = cover
        self.start_timestamp = start_timestamp
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Video"]:
        return (
            Video(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                thumbnail=tgram.types.PhotoSize._parse(me=me, d=d.get("thumbnail")),
                cover=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("cover")]
                if d.get("cover")
                else None,
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
