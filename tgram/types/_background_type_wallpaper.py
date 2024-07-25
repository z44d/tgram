import tgram
from .type_ import Type_

from typing import Optional


class BackgroundTypeWallpaper(Type_):
    """
    The background is a wallpaper in the JPEG format.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtypewallpaper

    :param type: Type of the background, always “wallpaper”
    :type type: :obj:`str`

    :param document: Document with the wallpaper
    :type document: :class:`Document`

    :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100
    :type dark_theme_dimming: :obj:`int`

    :param is_blurred: Optional. True, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12
    :type is_blurred: :obj:`bool`

    :param is_moving: Optional. True, if the background moves slightly when the device is tilted
    :type is_moving: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`BackgroundTypeWallpaper`
    """

    def __init__(
        self,
        type: "str" = None,
        document: "tgram.types.Document" = None,
        dark_theme_dimming: "int" = None,
        is_blurred: "bool" = None,
        is_moving: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.document = document
        self.dark_theme_dimming = dark_theme_dimming
        self.is_blurred = is_blurred
        self.is_moving = is_moving

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BackgroundTypeWallpaper"]:
        return (
            BackgroundTypeWallpaper(
                me=me,
                json=d,
                type=d.get("type"),
                document=tgram.types.Document._parse(me=me, d=d.get("document")),
                dark_theme_dimming=d.get("dark_theme_dimming"),
                is_blurred=d.get("is_blurred"),
                is_moving=d.get("is_moving"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
