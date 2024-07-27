import tgram
from .type_ import Type_

from typing import Optional


class TransactionPartnerFragment(Type_):
    """
    Describes a withdrawal transaction with Fragment.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartnerfragment

    :param type: Type of the transaction partner, always “fragment”
    :type type: :obj:`str`

    :param withdrawal_state: Optional. State of the transaction if the transaction is outgoing
    :type withdrawal_state: :class:`RevenueWithdrawalState`

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerFragment`

    """

    def __init__(
        self,
        withdrawal_state: "tgram.types.RevenueWithdrawalState" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "fragment"
        self.withdrawal_state = withdrawal_state

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.TransactionPartnerFragment"]:
        return (
            TransactionPartnerFragment(
                me=me,
                json=d,
                type=d.get("type"),
                withdrawal_state=None
                if not d.get("withdrawal_state")
                else tgram.types.RevenueWithdrawalStateSucceeded._parse(
                    me=me, d=d.get("withdrawal_state")
                )
                if d["type"] == "succeeded"
                else tgram.types.RevenueWithdrawalStateFailed._parse(
                    me=me, d=d.get("withdrawal_state")
                )
                if d["type"] == "failed"
                else tgram.types.RevenueWithdrawalStatePending._parse(
                    me=me, d=d.get("withdrawal_state")
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
