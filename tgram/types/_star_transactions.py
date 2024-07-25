import tgram
from .type_ import Type_

from typing import List, Optional


class StarTransactions(Type_):
    """
    Contains a list of Telegram Star transactions.

    Telegram documentation: https://core.telegram.org/bots/api#startransactions

    :param transactions: The list of transactions
    :type transactions: :obj:`list` of :class:`StarTransaction`

    :return: Instance of the class
    :rtype: :class:`StarTransactions`

    """

    def __init__(
        self,
        transactions: List["tgram.types.StarTransaction"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.transactions = transactions

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.StarTransactions"]:
        return (
            StarTransactions(
                me=me,
                json=d,
                transactions=[
                    tgram.types.StarTransaction._parse(me=me, d=i)
                    for i in d.get("transactions")
                ]
                if d.get("transactions")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
