import tgram
from .type_ import Type_

from typing import Optional


class VideoNote(Type_):
    """
    This object represents a video message (available in Telegram apps as of v.4.0).

    Telegram Documentation: https://core.telegram.org/bots/api#videonote

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param length: Video width and height (diameter of the video message) as defined by sender
    :type length: :obj:`int`

    :param duration: Duration of the video in seconds as defined by sender
    :type duration: :obj:`int`

    :param thumbnail: Optional. Video thumbnail
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :param file_size: Optional. File size in bytes
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoNote`
    """

    def __init__(
        self,
        file_id: "str" = None,
        file_unique_id: "str" = None,
        length: "int" = None,
        duration: "int" = None,
        thumbnail: "tgram.types.PhotoSize" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.VideoNote"]:
        return (
            VideoNote(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                length=d.get("length"),
                duration=d.get("duration"),
                thumbnail=tgram.types.PhotoSize._parse(me=me, d=d.get("thumbnail")),
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
