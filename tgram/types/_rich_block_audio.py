import tgram
from .type_ import Type_

from typing import Optional


class RichBlockAudio(Type_):
    """
    This object represents an audio rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockaudio

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param audio: Optional. Audio
    :type audio: :class:`tgram.types.Audio`

    :param media: Optional. Input media audio
    :type media: :class:`tgram.types.InputMediaAudio`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockAudio`
    """

    def __init__(
        self,
        type: "str" = "audio",
        audio: "tgram.types.Audio" = None,
        media: "tgram.types.InputMediaAudio" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.audio = audio
        self.media = media

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockAudio"]:
        return (
            RichBlockAudio(
                me=me,
                json=d,
                type=d.get("type"),
                audio=tgram.types.Audio._parse(me=me, d=d.get("audio"))
                if d.get("audio")
                else None,
                media=tgram.types.InputMediaAudio._parse(me=me, d=d.get("media"))
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
