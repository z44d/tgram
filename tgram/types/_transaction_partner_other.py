import tgram
from .type_ import Type_

from typing import Optional


class TransactionPartnerOther(Type_):
    """
    Describes a transaction with an unknown source or recipient.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartnerother

    :param type: Type of the transaction partner, always “other”
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerOther`
    """

    def __init__(self, me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = "other"

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.TransactionPartnerOther"]:
        return (
            TransactionPartnerOther(me=me, json=d, type=d.get("type"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
