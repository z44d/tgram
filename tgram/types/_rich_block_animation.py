import tgram
from .type_ import Type_

from typing import Optional


class RichBlockAnimation(Type_):
    """
    This object represents an animation rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockanimation

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param animation: Optional. Animation
    :type animation: :class:`tgram.types.Animation`

    :param media: Optional. Input media animation
    :type media: :class:`tgram.types.InputMediaAnimation`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockAnimation`
    """

    def __init__(
        self,
        type: "str" = "animation",
        animation: "tgram.types.Animation" = None,
        media: "tgram.types.InputMediaAnimation" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.animation = animation
        self.media = media

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockAnimation"]:
        return (
            RichBlockAnimation(
                me=me,
                json=d,
                type=d.get("type"),
                animation=tgram.types.Animation._parse(me=me, d=d.get("animation"))
                if d.get("animation")
                else None,
                media=tgram.types.InputMediaAnimation._parse(me=me, d=d.get("media"))
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
