import tgram
from .type_ import Type_

from typing import Union, Optional


class BotCommandScopeChat(Type_):
    """
    Represents the scope of bot commands, covering a specific chat.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopechat

    :param type: Scope type, must be chat
    :type type: :obj:`str`

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername)
    :type chat_id: :obj:`int` or :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeChat`
    """

    def __init__(
        self,
        type: "str" = None,
        chat_id: Union["int", "str"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.chat_id = chat_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BotCommandScopeChat"]:
        return (
            BotCommandScopeChat(
                me=me, json=d, type=d.get("type"), chat_id=d.get("chat_id")
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
