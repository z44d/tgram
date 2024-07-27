import tgram
from .type_ import Type_

from typing import Optional


class MenuButton(Type_):
    """
    This object describes the bot's menu button in a private chat. It should be one of

    * :class:`MenuButtonCommands`
    * :class:`MenuButtonWebApp`
    * :class:`MenuButtonDefault`

    If a menu button other than MenuButtonDefault is set for a private chat, then it is applied
    in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.
    """

    def __init__(
        self, type: "str" = None, me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MenuButton"]:
        return (
            MenuButton(me=me, json=d, type=d.get("type"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
