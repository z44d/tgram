import tgram
from .type_ import Type_

from typing import Optional


class BotName(Type_):
    """
    This object represents a bot name.

    Telegram Documentation: https://core.telegram.org/bots/api#botname

    :param name: The bot name
    :type name: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`BotName`
    """

    def __init__(
        self, name: "str" = None, me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.name = name

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BotName"]:
        return (
            BotName(me=me, json=d, name=d.get("name"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
