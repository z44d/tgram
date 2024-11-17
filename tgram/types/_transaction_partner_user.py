import tgram
from .type_ import Type_

from typing import Optional, List


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
        subscription_period: "int" = None,
        paid_media: List["tgram.types.PaidMedia"] = None,
        paid_media_payload: "str" = None,
        gift: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "user"
        self.user = user
        self.invoice_payload = invoice_payload
        self.subscription_period = subscription_period
        self.paid_media = paid_media
        self.paid_media_payload = paid_media_payload
        self.gift = gift

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
                gift=d.get("gift"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
