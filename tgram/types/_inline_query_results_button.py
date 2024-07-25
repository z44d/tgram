import tgram
from .type_ import Type_

from typing import Optional


class InlineQueryResultsButton(Type_):
    """
    This object represents a button to be shown above inline query results.
    You must use exactly one of the optional fields.

    Telegram documentation: https://core.telegram.org/bots/api#inlinequeryresultsbutton

    :param text: Label text on the button
    :type text: :obj:`str`

    :param web_app: Optional. Description of the Web App that will be launched when the user presses the button.
        The Web App will be able to switch back to the inline mode using the method web_app_switch_inline_query inside the Web App.
    :type web_app: :class:`tgram.types.WebAppInfo`

    :param start_parameter: Optional. Deep-linking parameter for the /start message sent to the bot when a user presses the button.
        1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed.
        Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search
        results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing
        any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs
        the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat
        where they wanted to use the bot's inline capabilities.
    :type start_parameter: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`InlineQueryResultsButton`
    """

    def __init__(
        self,
        text: "str" = None,
        web_app: "tgram.types.WebAppInfo" = None,
        start_parameter: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InlineQueryResultsButton"]:
        return (
            InlineQueryResultsButton(
                me=me,
                json=d,
                text=d.get("text"),
                web_app=tgram.types.WebAppInfo._parse(me=me, d=d.get("web_app")),
                start_parameter=d.get("start_parameter"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
