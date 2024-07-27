import tgram
from .type_ import Type_

from typing import Union, Optional

from pathlib import Path


class InputPaidMediaVideo(Type_):
    """
    The paid media to send is a video.

    Telegram documentation: https://core.telegram.org/bots/api#inputpaidmediavideo

    :param type: Type of the media, must be video
    :type type: :obj:`str`

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for
        Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data
        under <file_attach_name> name. More information on Sending Files »
    :type media: :obj:`str`

    :param thumbnail: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
        The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
        Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,
        so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.
        More information on Sending Files »
    :type thumbnail: :class:`InputFile`

    :param width: Optional. Video width
    :type width: :obj:`int`

    :param height: Optional. Video height
    :type height: :obj:`int`

    :param duration: Optional. Video duration in seconds
    :type duration: :obj:`int`

    :param supports_streaming: Optional. Pass True if the uploaded video is suitable for streaming
    :type supports_streaming: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`InputPaidMediaVideo`

    """

    def __init__(
        self,
        media: Union["Path", "str"] = None,
        thumbnail: Union["tgram.types.InputFile", "str"] = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        supports_streaming: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.media = media
        self.thumbnail = thumbnail
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputPaidMediaVideo"]:
        return (
            InputPaidMediaVideo(
                me=me,
                json=d,
                type=d.get("type"),
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                supports_streaming=d.get("supports_streaming"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
