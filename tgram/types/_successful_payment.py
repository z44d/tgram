import tgram
from .type_ import Type_

from typing import Optional


class SuccessfulPayment(Type_):
    """
    This object contains basic information about a successful payment.

    Telegram Documentation: https://core.telegram.org/bots/api#successfulpayment

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

    :param telegram_payment_charge_id: Telegram payment identifier
    :type telegram_payment_charge_id: :obj:`str`

    :param provider_payment_charge_id: Provider payment identifier
    :type provider_payment_charge_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.SuccessfulPayment`
    """

    def __init__(
        self,
        currency: "str" = None,
        total_amount: "int" = None,
        invoice_payload: "str" = None,
        subscription_expiration_date: int = None,
        is_recurring: bool = None,
        is_first_recurring: bool = None,
        telegram_payment_charge_id: "str" = None,
        provider_payment_charge_id: "str" = None,
        shipping_option_id: "str" = None,
        order_info: "tgram.types.OrderInfo" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.subscription_expiration_date = subscription_expiration_date
        self.is_recurring = is_recurring
        self.is_first_recurring = is_first_recurring
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuccessfulPayment"]:
        return (
            SuccessfulPayment(
                me=me,
                json=d,
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
                invoice_payload=d.get("invoice_payload"),
                subscription_expiration_date=d.get("subscription_expiration_date"),
                is_recurring=d.get("is_recurring"),
                is_first_recurring=d.get("is_first_recurring"),
                telegram_payment_charge_id=d.get("telegram_payment_charge_id"),
                provider_payment_charge_id=d.get("provider_payment_charge_id"),
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
