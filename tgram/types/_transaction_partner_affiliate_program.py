import tgram
from .type_ import Type_

from typing import Optional


class TransactionPartnerAffiliateProgram(Type_):
    """
    Describes the affiliate program that issued the affiliate commission received via this transaction.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartneraffiliateprogram

    :param type: Type of the transaction partner, always “affiliate_program”
    :type type: :obj:`str`

    :param sponsor_user: Optional. Information about the bot that sponsored the affiliate program
    :type sponsor_user: :class:`User`

    :param commission_per_mille: The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users
    :type commission_per_mille: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerAffiliateProgram`
    """

    def __init__(
        self,
        sponsor_user: "tgram.types.User" = None,
        commission_per_mille: int = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "affiliate_program"
        self.sponsor_user = sponsor_user
        self.commission_per_mille = commission_per_mille

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.TransactionPartnerAffiliateProgram"]:
        return (
            TransactionPartnerAffiliateProgram(
                me=me,
                json=d,
                type=d.get("type"),
                sponsor_user=tgram.types.User._parse(me=me, d=d.get("sponsor_user")),
                commission_per_mille=d.get("commission_per_mille"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
