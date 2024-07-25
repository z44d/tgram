import tgram
from .type_ import Type_

from typing import Optional


class BackgroundTypePattern(Type_):
    """
    The background is a wallpaper in the JPEG format.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtypepattern

    :param type: Type of the background, always “pattern”
    :type type: :obj:`str`

    :param document: Document with the pattern
    :type document: :class:`Document`

    :param fill: The background fill that is combined with the pattern
    :type fill: :class:`BackgroundFill`

    :param intensity: Intensity of the pattern when it is shown above the filled background; 0-100
    :type intensity: :obj:`int`

    :param is_inverted: Optional. True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only
    :type is_inverted: :obj:`bool`

    :param is_moving: Optional. True, if the background moves slightly when the device is tilted
    :type is_moving: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`BackgroundTypePattern`
    """

    def __init__(
        self,
        type: "str" = None,
        document: "tgram.types.Document" = None,
        fill: "tgram.types.BackgroundFill" = None,
        intensity: "int" = None,
        is_inverted: "bool" = None,
        is_moving: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.document = document
        self.fill = fill
        self.intensity = intensity
        self.is_inverted = is_inverted
        self.is_moving = is_moving

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BackgroundTypePattern"]:
        return (
            BackgroundTypePattern(
                me=me,
                json=d,
                type=d.get("type"),
                document=tgram.types.Document._parse(me=me, d=d.get("document")),
                fill=tgram.types.BackgroundFill._parse(me=me, d=d.get("fill")),
                intensity=d.get("intensity"),
                is_inverted=d.get("is_inverted"),
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
