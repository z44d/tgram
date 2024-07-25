import tgram
from .type_ import Type_

from typing import Optional


class MaskPosition(Type_):
    """
    This object describes the position on faces where a mask should be placed by default.

    Telegram Documentation: https://core.telegram.org/bots/api#maskposition

    :param point: The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or
        “chin”.
    :type point: :obj:`str`

    :param x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example,
        choosing -1.0 will place mask just to the left of the default mask position.
    :type x_shift: :obj:`float` number

    :param y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For
        example, 1.0 will place the mask just below the default mask position.
    :type y_shift: :obj:`float` number

    :param scale: Mask scaling coefficient. For example, 2.0 means double size.
    :type scale: :obj:`float` number

    :return: Instance of the class
    :rtype: :class:`tgram.types.MaskPosition`
    """

    def __init__(
        self,
        point: "str" = None,
        x_shift: "float" = None,
        y_shift: "float" = None,
        scale: "float" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MaskPosition"]:
        return (
            MaskPosition(
                me=me,
                json=d,
                point=d.get("point"),
                x_shift=d.get("x_shift"),
                y_shift=d.get("y_shift"),
                scale=d.get("scale"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
