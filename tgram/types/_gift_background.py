import tgram
from .type_ import Type_

from typing import Optional, List


class GiftBackground(Type_):
    """
    This object describes the background of a gift.

    Telegram Documentation: https://core.telegram.org/bots/api#giftbackground

    :param type: Type of the background, either "solid" or "gradient"
    :type type: :obj:`str`

    :param color: Optional. The color of the background in RGB format (for solid backgrounds)
    :type color: :obj:`int`

    :param pattern_color: Optional. The color of the pattern on the background in RGB format
    :type pattern_color: :obj:`int`

    :param colors: Optional. A list of colors in RGB format for the gradient background
    :type colors: :obj:`list` of :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.GiftBackground`
    """

    def __init__(
        self,
        type: "str" = None,
        color: "int" = None,
        pattern_color: "int" = None,
        colors: List["int"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.color = color
        self.pattern_color = pattern_color
        self.colors = colors

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.GiftBackground"]:
        return (
            GiftBackground(
                type=d.get("type"),
                color=d.get("color"),
                pattern_color=d.get("pattern_color"),
                colors=d.get("colors"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
