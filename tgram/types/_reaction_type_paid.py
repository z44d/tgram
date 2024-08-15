import tgram
from .type_ import Type_

from typing import Optional


class ReactionTypePaid(Type_):
    """
    The reaction is paid.

    Telegram documentation: https://core.telegram.org/bots/api#reactiontypepaid

    :param type: Type of the reaction, must be paid
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`ReactionTypePaid`
    """

    def __init__(
        self,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "paid"

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ReactionTypePaid"]:
        return (
            ReactionTypePaid(me=me, json=d)
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
