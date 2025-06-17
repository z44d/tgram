import tgram
from .type_ import Type_

from typing import Optional, List


class TransactionPartnerUser(Type_):
    """
    Describes a transaction with a user.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartneruser

    :param type: Type of the transaction partner, always “user”
    :type type: :obj:`str`

    :param transaction_type: Type of the transaction, currently one of “invoice_payment”, “paid_media_payment”, “gift_purchase”, “premium_purchase”, “business_account_transfer”
    :type transaction_type: :obj:`str`

    :param user: Information about the user
    :type user: :class:`User`

    :param affiliate: Optional. Information about the affiliate that received a commission via this transaction. Can be available only for “invoice_payment” and “paid_media_payment” transactions.
    :type affiliate: :class:`AffiliateInfo`, optional

    :param invoice_payload: Optional. Bot-specified invoice payload. Can be available only for “invoice_payment” transactions.
    :type invoice_payload: :obj:`str`, optional

    :param subscription_period: Optional. The duration of the paid subscription. Can be available only for “invoice_payment” transactions.
    :type subscription_period: :obj:`int`, optional

    :param paid_media: Optional. Information about the paid media bought by the user; for “paid_media_payment” transactions only
    :type paid_media: List[:class:`PaidMedia`], optional

    :param paid_media_payload: Optional. Bot-specified paid media payload. Can be available only for “paid_media_payment” transactions.
    :type paid_media_payload: :obj:`str`, optional

    :param gift: Optional. The gift sent to the user by the bot; for “gift_purchase” transactions only
    :type gift: :class:`Gift`, optional

    :param premium_subscription_duration: Optional. Number of months the gifted Telegram Premium subscription will be active for; for “premium_purchase” transactions only
    :type premium_subscription_duration: :obj:`int`, optional

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerUser`
    """

    def __init__(
        self,
        user: "tgram.types.User" = None,
        transaction_type: str = None,
        affiliate: "tgram.types.AffiliateInfo" = None,
        invoice_payload: str = None,
        subscription_period: int = None,
        paid_media: List["tgram.types.PaidMedia"] = None,
        paid_media_payload: str = None,
        gift: "tgram.types.Gift" = None,
        premium_subscription_duration: int = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "user"
        self.transaction_type = transaction_type
        self.user = user
        self.affiliate = affiliate
        self.invoice_payload = invoice_payload
        self.subscription_period = subscription_period
        self.paid_media = paid_media
        self.paid_media_payload = paid_media_payload
        self.gift = gift
        self.premium_subscription_duration = premium_subscription_duration

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.TransactionPartnerUser"]:
        return (
            TransactionPartnerUser(
                me=me,
                json=d,
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                transaction_type=d.get("transaction_type"),
                affiliate=tgram.types.AffiliateInfo._parse(me=me, d=d.get("affiliate")),
                invoice_payload=d.get("invoice_payload"),
                subscription_period=d.get("subscription_period"),
                paid_media=[
                    (
                        tgram.types.PaidMediaPreview._parse(me=me, d=i)
                        if i["type"] == "preview"
                        else tgram.types.PaidMediaPhoto._parse(me=me, d=i)
                        if i["type"] == "photo"
                        else tgram.types.PaidMediaVideo._parse(me=me, d=i)
                    )
                    for i in d.get("paid_media")
                ]
                if d.get("paid_media")
                else None,
                paid_media_payload=d.get("paid_media_payload"),
                gift=tgram.types.Gift._parse(me=me, d=d.get("gift")),
                premium_subscription_duration=d.get("premium_subscription_duration"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
