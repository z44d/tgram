import tgram
from .type_ import Type_

from typing import Optional


class BotDescription(Type_):
    """
    This object represents a bot description.

    Telegram documentation: https://core.telegram.org/bots/api#botdescription

    :param description: Bot description
    :type description: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotDescription`
    """

    def __init__(
        self,
        description: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.description = description

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BotDescription"]:
        return (
            BotDescription(me=me, json=d, description=d.get("description"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
