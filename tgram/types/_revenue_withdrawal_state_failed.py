import tgram
from .type_ import Type_

from typing import Optional


class RevenueWithdrawalStateFailed(Type_):
    """
    The withdrawal failed and the transaction was refunded.

    Telegram documentation: https://core.telegram.org/bots/api#revenuewithdrawalstatefailed

    :param type: Type of the state, always “failed”
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`RevenueWithdrawalStateFailed`
    """

    def __init__(self, me: "tgram.TgBot" = None, json: "dict" = None):
        super().__init__(me=me, json=json)
        self.type = "faield"

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RevenueWithdrawalStateFailed"]:
        return (
            RevenueWithdrawalStateFailed(me=me, json=d, type=d.get("type"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
