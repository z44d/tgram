import tgram
from .type_ import Type_

from typing import Optional


class BackgroundType(Type_):
    """
    This object describes the type of a background. Currently, it can be one of
        BackgroundTypeFill
        BackgroundTypeWallpaper
        BackgroundTypePattern
        BackgroundTypeChatTheme

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtype

    :return: Instance of the class
    :rtype: :class:`BackgroundTypeFill` or :class:`BackgroundTypeWallpaper` or :class:`BackgroundTypePattern` or :class:`BackgroundTypeChatTheme`
    """

    def __init__(
        self,
        type: "str" = None,
        fill: "tgram.types.BackgroundFill" = None,
        dark_theme_dimming: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BackgroundType"]:
        return (
            BackgroundType(
                me=me,
                json=d,
                type=d.get("type"),
                fill=tgram.types.BackgroundFill._parse(me=me, d=d.get("fill")),
                dark_theme_dimming=d.get("dark_theme_dimming"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
