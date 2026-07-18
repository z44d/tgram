import tgram
from .type_ import Type_

from typing import Optional


class RichBlockVideo(Type_):
    """
    This object represents a video rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockvideo

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param video: Optional. Video
    :type video: :class:`tgram.types.Video`

    :param media: Optional. Input media video
    :type media: :class:`tgram.types.InputMediaVideo`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockVideo`
    """

    def __init__(
        self,
        type: "str" = "video",
        video: "tgram.types.Video" = None,
        media: "tgram.types.InputMediaVideo" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.video = video
        self.media = media

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockVideo"]:
        return (
            RichBlockVideo(
                me=me,
                json=d,
                type=d.get("type"),
                video=tgram.types.Video._parse(me=me, d=d.get("video"))
                if d.get("video")
                else None,
                media=tgram.types.InputMediaVideo._parse(me=me, d=d.get("media"))
                if d.get("media")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
