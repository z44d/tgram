import tgram
from .type_ import Type_

from typing import Optional


class BotShortDescription(Type_):
    """
    This object represents a bot short description.

    Telegram documentation: https://core.telegram.org/bots/api#botshortdescription

    :param short_description: Bot short description
    :type short_description: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotShortDescription`
    """

    def __init__(
        self,
        short_description: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.short_description = short_description

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BotShortDescription"]:
        return (
            BotShortDescription(
                me=me, json=d, short_description=d.get("short_description")
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
