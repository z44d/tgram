import tgram
from .type_ import Type_

from typing import Optional


class UniqueGiftColors(Type_):
    """
    This object describes the color scheme for a user's name, replies to messages
    and link previews based on a unique gift.

    Telegram Documentation: https://core.telegram.org/bots/api#uniquegiftcolors

    :param background_color: The background color for the area where the unique gift colors are displayed in RGB format
    :type background_color: :obj:`int`

    :param frame_color: The frame color around the area where the unique gift colors are displayed in RGB format
    :type frame_color: :obj:`int`

    :param symbol_color: The color of the symbol on the area where the unique gift colors are displayed in RGB format
    :type symbol_color: :obj:`int`

    :param text_color: The text color on the area where the unique gift colors are displayed in RGB format
    :type text_color: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.UniqueGiftColors`
    """

    def __init__(
        self,
        background_color: "int" = None,
        frame_color: "int" = None,
        symbol_color: "int" = None,
        text_color: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.background_color = background_color
        self.frame_color = frame_color
        self.symbol_color = symbol_color
        self.text_color = text_color

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.UniqueGiftColors"]:
        return (
            UniqueGiftColors(
                background_color=d.get("background_color"),
                frame_color=d.get("frame_color"),
                symbol_color=d.get("symbol_color"),
                text_color=d.get("text_color"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
