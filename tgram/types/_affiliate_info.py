import tgram
from .type_ import Type_

from typing import Optional


class AffiliateInfo(Type_):
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    Telegram Documentation: https://core.telegram.org/bots/api#affiliateinfo

    :param affiliate_user: Optional. The bot or the user that received an affiliate commission if it was received by a bot or a user
    :type affiliate_user: :class:`User`

    :param affiliate_chat: Optional. The chat that received an affiliate commission if it was received by a chat
    :type affiliate_chat: :class:`Chat`

    :param commission_per_mille: The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users
    :type commission_per_mille: :obj:`int`

    :param amount: Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds
    :type amount: :obj:`int`

    :param nanostar_amount: Optional. The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds
    :type nanostar_amount: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.AffiliateInfo`
    """

    def __init__(
        self,
        affiliate_user: "tgram.types.User" = None,
        affiliate_chat: "tgram.types.Chat" = None,
        commission_per_mille: int = None,
        amount: int = None,
        nanostar_amount: int = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.affiliate_user = affiliate_user
        self.affiliate_chat = affiliate_chat
        self.commission_per_mille = commission_per_mille
        self.amount = amount
        self.nanostar_amount = nanostar_amount

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.AffiliateInfo"]:
        return (
            AffiliateInfo(
                me=me,
                json=d,
                affiliate_user=tgram.types.User._parse(
                    me=me, d=d.get("affiliate_user")
                ),
                affiliate_chat=tgram.types.Chat._parse(
                    me=me, d=d.get("affiliate_chat")
                ),
                commission_per_mille=d.get("commission_per_mille"),
                amount=d.get("amount"),
                nanostar_amount=d.get("nanostar_amount"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
