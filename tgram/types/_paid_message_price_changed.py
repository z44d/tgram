import tgram
from .type_ import Type_

from typing import Optional


class PaidMessagePriceChanged(Type_):
    """
    Describes a service message about a change in the price of paid messages within a chat.

    :param paid_message_star_count: The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message
    :type paid_message_star_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PaidMessagePriceChanged`
    """

    def __init__(
        self,
        paid_message_star_count: int = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.paid_message_star_count = paid_message_star_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["PaidMessagePriceChanged"]:
        return (
            PaidMessagePriceChanged(
                me=me,
                json=d,
                paid_message_star_count=d.get("paid_message_star_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
