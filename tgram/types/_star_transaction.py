import tgram
from .type_ import Type_

from typing import Optional


class StarTransaction(Type_):
    """
    Describes a Telegram Star transaction.

    Telegram documentation: https://core.telegram.org/bots/api#startransaction

    :param id: Unique identifier of the transaction. Coincides with the identifer of the original transaction for refund transactions. Coincides with SuccessfulPayment.telegram_payment_charge_id for successful incoming payments from users.
    :type id: :obj:`str`

    :param amount: Number of Telegram Stars transferred by the transaction
    :type amount: :obj:`int`

    :param date: Date the transaction was created in Unix time
    :type date: :obj:`int`

    :param source: Optional. Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions
    :type source: :class:`TransactionPartner`

    :param receiver: Optional. Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions
    :type receiver: :class:`TransactionPartner`

    :return: Instance of the class
    :rtype: :class:`StarTransaction`
    """

    def __init__(
        self,
        id: "str" = None,
        amount: "int" = None,
        date: "int" = None,
        source: "tgram.types.TransactionPartner" = None,
        receiver: "tgram.types.TransactionPartner" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.amount = amount
        self.date = date
        self.source = source
        self.receiver = receiver

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.StarTransaction"]:
        return (
            StarTransaction(
                me=me,
                json=d,
                id=d.get("id"),
                amount=d.get("amount"),
                date=d.get("date"),
                source=tgram.types.TransactionPartner._parse(me=me, d=d.get("source")),
                receiver=tgram.types.TransactionPartner._parse(
                    me=me, d=d.get("receiver")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
