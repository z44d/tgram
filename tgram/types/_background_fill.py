import tgram
from .type_ import Type_

from typing import Optional


class BackgroundFill(Type_):
    """
    This object describes the way a background is filled based on the selected colors. Currently, it can be one of
        BackgroundFillSolid
        BackgroundFillGradient
        BackgroundFillFreeformGradient

    Telegram documentation: https://core.telegram.org/bots/api#backgroundfill

    :return: Instance of the class
    :rtype: :class:`BackgroundFillSolid` or :class:`BackgroundFillGradient` or :class:`BackgroundFillFreeformGradient`
    """

    def __init__(
        self,
        type: "str" = None,
        color: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.color = color

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BackgroundFill"]:
        return (
            BackgroundFill(me=me, json=d, type=d.get("type"), color=d.get("color"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
