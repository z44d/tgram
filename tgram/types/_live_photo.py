from typing import Optional

import tgram

from .type_ import Type_


class LivePhoto(Type_):
    """
    This object represents a live photo (photo with a short video).

    Telegram Documentation: https://core.telegram.org/bots/api#livephoto

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots
    :type file_unique_id: :obj:`str`

    :param width: Photo width
    :type width: :obj:`int`

    :param height: Photo height
    :type height: :obj:`int`

    :param file_size: Optional. File size in bytes
    :type file_size: :obj:`int`

    :param video_file_id: Optional. File identifier of the accompanying video
    :type video_file_id: :obj:`str`

    :param video_file_unique_id: Optional. Unique identifier of the accompanying video
    :type video_file_unique_id: :obj:`str`

    :param video_width: Optional. Video width
    :type video_width: :obj:`int`

    :param video_height: Optional. Video height
    :type video_height: :obj:`int`

    :param video_duration: Optional. Video duration in seconds
    :type video_duration: :obj:`int`

    :param thumbnail: Optional. Photo thumbnail
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :return: Instance of the class
    :rtype: :class:`tgram.types.LivePhoto`
    """

    def __init__(
        self,
        file_id: "str | None" = None,
        file_unique_id: "str | None" = None,
        width: "int | None" = None,
        height: "int | None" = None,
        file_size: "int | None" = None,
        video_file_id: "str | None" = None,
        video_file_unique_id: "str | None" = None,
        video_width: "int | None" = None,
        video_height: "int | None" = None,
        video_duration: "int | None" = None,
        thumbnail: "tgram.types.PhotoSize" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size
        self.video_file_id = video_file_id
        self.video_file_unique_id = video_file_unique_id
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.thumbnail = thumbnail

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.LivePhoto"]:
        return (
            LivePhoto(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                file_size=d.get("file_size"),
                video_file_id=d.get("video_file_id"),
                video_file_unique_id=d.get("video_file_unique_id"),
                video_width=d.get("video_width"),
                video_height=d.get("video_height"),
                video_duration=d.get("video_duration"),
                thumbnail=tgram.types.PhotoSize._parse(me=me, d=d.get("thumbnail")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
