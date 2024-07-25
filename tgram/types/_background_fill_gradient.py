import tgram
from .type_ import Type_

from typing import Optional


class BackgroundFillGradient(Type_):
    """
    The background is a gradient fill.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundfillgradient

    :param type: Type of the background fill, always “gradient”
    :type type: :obj:`str`

    :param top_color: Top color of the gradient in the RGB24 format
    :type top_color: :class:`int`

    :param bottom_color: Bottom color of the gradient in the RGB24 format
    :type bottom_color: :class:`int`

    :param rotation_angle: Clockwise rotation angle of the background fill in degrees; 0-359
    :type rotation_angle: :class:`int`

    :return: Instance of the class
    :rtype: :class:`BackgroundFillGradient`
    """

    def __init__(
        self,
        type: "str" = None,
        top_color: "int" = None,
        bottom_color: "int" = None,
        rotation_angle: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.rotation_angle = rotation_angle

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BackgroundFillGradient"]:
        return (
            BackgroundFillGradient(
                me=me,
                json=d,
                type=d.get("type"),
                top_color=d.get("top_color"),
                bottom_color=d.get("bottom_color"),
                rotation_angle=d.get("rotation_angle"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
