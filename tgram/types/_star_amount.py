import tgram
from .type_ import Type_
from typing import Optional


class StarAmount(Type_):
    """
    Describes an amount of Telegram Stars.

    Telegram documentation: https://core.telegram.org/bots/api#staramount

    :param amount: Integer amount of Telegram Stars, rounded to 0; can be negative
    :type amount: :obj:`int`

    :param nanostar_amount: Optional. The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999; can be negative if and only if amount is non-positive
    :type nanostar_amount: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`StarAmount`
    """

    def __init__(
        self,
        amount: "int" = None,
        nanostar_amount: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.amount = amount
        self.nanostar_amount = nanostar_amount

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["StarAmount"]:
        return (
            StarAmount(
                me=me,
                json=d,
                amount=d.get("amount"),
                nanostar_amount=d.get("nanostar_amount"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
