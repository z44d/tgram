from typing import Optional

import tgram

from .type_ import Type_


class BackgroundFillSolid(Type_):
    """
    The background is filled using the selected color.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundfillsolid

    :param type: Type of the background fill, always “solid”
    :type type: :obj:`str`

    :param color: The color of the background fill in the RGB24 format
    :type color: :class:`int`

    :return: Instance of the class
    :rtype: :class:`BackgroundFillSolid`
    """

    def __init__(
        self,
        type: "str | None" = None,
        color: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.color = color

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.BackgroundFillSolid"]:
        return (
            BackgroundFillSolid(me=me, json=d, type=d.get("type"), color=d.get("color"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
