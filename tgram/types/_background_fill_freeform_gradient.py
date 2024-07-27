import tgram
from .type_ import Type_

from typing import List, Optional


class BackgroundFillFreeformGradient(Type_):
    """
    The background is a freeform gradient that rotates after every message in the chat.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundfillfreeformgradient

    :param type: Type of the background fill, always “freeform_gradient”
    :type type: :obj:`str`

    :param colors: A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format
    :type colors: :obj:`list` of :class:`int`

    :return: Instance of the class
    :rtype: :class:`BackgroundFillFreeformGradient`
    """

    def __init__(
        self,
        type: "str" = None,
        colors: List["int"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.colors = colors

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BackgroundFillFreeformGradient"]:
        return (
            BackgroundFillFreeformGradient(
                me=me, json=d, type=d.get("type"), colors=d.get("colors")
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
