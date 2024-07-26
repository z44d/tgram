import tgram
from .type_ import Type_

from typing import Optional, Union


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

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional[
        Union[
            "tgram.types.BackgroundTypeFill",
            "tgram.types.BackgroundTypeWallpaper",
            "tgram.types.BackgroundTypePattern",
            "tgram.types.BackgroundTypeChatTheme",
        ]
    ]:
        return (
            None
            if not d
            else tgram.types.BackgroundTypeFill._parse(me, d, force)
            if d["type"] == "fill"
            else tgram.types.BackgroundTypeWallpaper._parse(me, d, force)
            if d["type"] == "wallpaper"
            else tgram.types.BackgroundTypePattern._parse(me, d, force)
            if d["type"] == "pattern"
            else tgram.types.BackgroundTypeChatTheme._parse(me, d, force)
        )
