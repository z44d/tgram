import tgram
from .type_ import Type_

from typing import Optional


class RefundedPayment(Type_):
    def __init__(
        self,
        currency: "str" = None,
        total_amount: "int" = None,
        invoice_payload: "str" = None,
        telegram_payment_charge_id: "str" = None,
        provider_payment_charge_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ) -> None:
        super().__init__(me=me, json=json)
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RefundedPayment"]:
        return (
            RefundedPayment(
                me=me,
                json=d,
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
                invoice_payload=d.get("invoice_payload"),
                telegram_payment_charge_id=d.get("telegram_payment_charge_id"),
                provider_payment_charge_id=d.get("provider_payment_charge_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
