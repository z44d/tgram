import tgram
from .type_ import Type_

from typing import Optional


class PollMedia(Type_):
    """
    This object represents a media file in a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#pollmedia

    :param type: Type of the media
    :type type: :obj:`str`

    :param media: File identifier
    :type media: :obj:`str`

    :param width: Optional. Media width
    :type width: :obj:`int`

    :param height: Optional. Media height
    :type height: :obj:`int`

    :param duration: Optional. Media duration in seconds
    :type duration: :obj:`int`

    :param link: Optional. Link
    :type link: :class:`tgram.types.Link`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollMedia`
    """

    def __init__(
        self,
        type: "str" = None,
        media: "str" = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        link: "tgram.types.Link" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.media = media
        self.width = width
        self.height = height
        self.duration = duration
        self.link = link

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PollMedia"]:
        return (
            PollMedia(
                me=me,
                json=d,
                type=d.get("type"),
                media=d.get("media"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                link=tgram.types.Link._parse(me=me, d=d.get("link"))
                if d.get("link")
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
