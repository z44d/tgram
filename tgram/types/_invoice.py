import tgram
from .type_ import Type_

from typing import Optional


class Invoice(Type_):
    """
    This object contains basic information about an invoice.

    Telegram Documentation: https://core.telegram.org/bots/api#invoice

    :param title: Product name
    :type title: :obj:`str`

    :param description: Product description
    :type description: :obj:`str`

    :param start_parameter: Unique bot deep-linking parameter that can be used to generate this invoice
    :type start_parameter: :obj:`str`

    :param currency: Three-letter ISO 4217 currency code
    :type currency: :obj:`str`

    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past
        the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Invoice`
    """

    def __init__(
        self,
        title: "str" = None,
        description: "str" = None,
        start_parameter: "str" = None,
        currency: "str" = None,
        total_amount: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Invoice"]:
        return (
            Invoice(
                me=me,
                json=d,
                title=d.get("title"),
                description=d.get("description"),
                start_parameter=d.get("start_parameter"),
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
