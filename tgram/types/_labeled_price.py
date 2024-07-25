import tgram
from .type_ import Type_

from typing import Optional


class LabeledPrice(Type_):
    """
    This object represents a portion of the price for goods or services.

    Telegram Documentation: https://core.telegram.org/bots/api#labeledprice

    :param label: Portion label
    :type label: :obj:`str`

    :param amount: Price of the product in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past
        the decimal point for each currency (2 for the majority of currencies).
    :type amount: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.LabeledPrice`
    """

    def __init__(
        self,
        label: "str" = None,
        amount: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.label = label
        self.amount = amount

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.LabeledPrice"]:
        return (
            LabeledPrice(me=me, json=d, label=d.get("label"), amount=d.get("amount"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
