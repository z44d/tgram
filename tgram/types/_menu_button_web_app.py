import tgram
from .type_ import Type_

from typing import Optional


class MenuButtonWebApp(Type_):
    """
    Represents a menu button, which launches a Web App.

    Telegram Documentation: https://core.telegram.org/bots/api#menubuttonwebapp

    :param type: Type of the button, must be web_app
    :type type: :obj:`str`

    :param text: Text on the button
    :type text: :obj:`str`

    :param web_app: Description of the Web App that will be launched when the user presses the button. The Web App will be
        able to send an arbitrary message on behalf of the user using the method answerWebAppQuery.
    :type web_app: :class:`tgram.types.WebAppInfo`

    :return: Instance of the class
    :rtype: :class:`tgram.types.MenuButtonWebApp`
    """

    def __init__(
        self,
        type: "str" = None,
        text: "str" = None,
        web_app: "tgram.types.WebAppInfo" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.web_app = web_app

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MenuButtonWebApp"]:
        return (
            MenuButtonWebApp(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                web_app=tgram.types.WebAppInfo._parse(me=me, d=d.get("web_app")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
