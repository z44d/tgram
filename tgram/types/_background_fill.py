import tgram
from .type_ import Type_

from typing import Optional, Union


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

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional[
        Union[
            "tgram.types.BackgroundFillSolid",
            "tgram.types.BackgroundFillGradient",
            "tgram.types.BackgroundFillFreeformGradient",
        ]
    ]:
        return (
            None
            if not d
            else tgram.types.BackgroundFillSolid._parse(me, d, force)
            if d["type"] == "solid"
            else tgram.types.BackgroundFillGradient._parse(me, d, force)
            if d["type"] == "gradient"
            else tgram.types.BackgroundFillFreeformGradient._parse(me, d, force)
        )
