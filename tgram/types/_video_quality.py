from typing import Optional

import tgram

from .type_ import Type_


class VideoQuality(Type_):
    """
    This object represents a video file of a specific quality.

    Telegram Documentation: https://core.telegram.org/bots/api#videoquality

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param width: Video width
    :type width: :obj:`int`

    :param height: Video height
    :type height: :obj:`int`

    :param codec: Codec used to encode the video, e.g. "h264", "h265", or "av01"
    :type codec: :obj:`str`

    :param file_size: Optional. File size in bytes
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoQuality`
    """

    def __init__(
        self,
        file_id: "str | None" = None,
        file_unique_id: "str | None" = None,
        width: "int | None" = None,
        height: "int | None" = None,
        codec: "str | None" = None,
        file_size: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.codec = codec
        self.file_size = file_size

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.VideoQuality"]:
        return (
            VideoQuality(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                codec=d.get("codec"),
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
