import tgram
from .type_ import Type_

from tgram import bound

from typing import Optional


class PreCheckoutQuery(Type_, bound.PreCheckoutQueryB):
    """
    This object contains information about an incoming pre-checkout query.

    Telegram Documentation: https://core.telegram.org/bots/api#precheckoutquery

    :param id: Unique query identifier
    :type id: :obj:`str`

    :param from: User who sent the query
    :type from: :class:`tgram.types.User`

    :param currency: Three-letter ISO 4217 currency code
    :type currency: :obj:`str`

    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past
        the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`

    :param invoice_payload: Bot specified invoice payload
    :type invoice_payload: :obj:`str`

    :param shipping_option_id: Optional. Identifier of the shipping option chosen by the user
    :type shipping_option_id: :obj:`str`

    :param order_info: Optional. Order information provided by the user
    :type order_info: :class:`tgram.types.OrderInfo`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PreCheckoutQuery`
    """

    def __init__(
        self,
        id: "str" = None,
        from_user: "tgram.types.User" = None,
        currency: "str" = None,
        total_amount: "int" = None,
        invoice_payload: "str" = None,
        shipping_option_id: "str" = None,
        order_info: "tgram.types.OrderInfo" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PreCheckoutQuery"]:
        return (
            PreCheckoutQuery(
                me=me,
                json=d,
                id=d.get("id"),
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
                invoice_payload=d.get("invoice_payload"),
                shipping_option_id=d.get("shipping_option_id"),
                order_info=tgram.types.OrderInfo._parse(me=me, d=d.get("order_info")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
