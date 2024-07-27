import tgram
from .type_ import Type_

from typing import Optional


class BackgroundTypeChatTheme(Type_):
    """
    The background is taken directly from a built-in chat theme.

    Telegram documentation: https://core.telegram.org/bots/api#backgroundtypechattheme

    :param type: Type of the background, always “chat_theme”
    :type type: :obj:`str`

    :param theme_name: Intensity of the pattern when it is shown above the filled background; 0-100
    :type theme_name: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`BackgroundTypeChatTheme`
    """

    def __init__(
        self,
        type: "str" = None,
        theme_name: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.theme_name = theme_name

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BackgroundTypeChatTheme"]:
        return (
            BackgroundTypeChatTheme(
                me=me, json=d, type=d.get("type"), theme_name=d.get("theme_name")
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
