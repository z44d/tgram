import tgram
from .type_ import Type_

from typing import Optional


class TransactionPartnerUser(Type_):
    """
    Describes a transaction with a user.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartneruser

    :param type: Type of the transaction partner, always “user”
    :type type: :obj:`str`

    :param user: Information about the user
    :type user: :class:`User`

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerUser`
    """

    def __init__(
        self,
        user: "tgram.types.User" = None,
        invoice_payload: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "user"
        self.user = user
        self.invoice_payload = invoice_payload

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.TransactionPartnerUser"]:
        return (
            TransactionPartnerUser(
                me=me,
                json=d,
                type=d.get("type"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                invoice_payload=d.get("invoice_payload"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
