import tgram

from .type_ import Type_

from typing import Optional


class PaidMediaPurchased(Type_):
    """
    This object contains information about a paid media purchase.

    Telegram documentation: https://core.telegram.org/bots/api#paidmediapurchased

    :param from_user: User who purchased the media
    :type from_user: :class:`tgram.types.User`

    :param paid_media_payload: Bot-specified paid media payload
    :type paid_media_payload: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`PaidMediaPurchased`
    """

    def __init__(
        self,
        from_user: "tgram.types.User" = None,
        paid_media_payload: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.from_user = from_user
        self.paid_media_payload = paid_media_payload

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PaidMediaPurchased"]:
        return (
            PaidMediaPurchased(
                me=me,
                json=d,
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                paid_media_payload=d.get("paid_media_payload"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
