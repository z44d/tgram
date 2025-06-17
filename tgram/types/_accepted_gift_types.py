import tgram
from .type_ import Type_
from typing import Optional


class AcceptedGiftTypes(Type_):
    """
    This object describes the types of gifts that can be gifted to a user or a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#acceptedgifttypes

    :param unlimited_gifts: True, if unlimited regular gifts are accepted
    :type unlimited_gifts: :obj:`bool`

    :param limited_gifts: True, if limited regular gifts are accepted
    :type limited_gifts: :obj:`bool`

    :param unique_gifts: True, if unique gifts or gifts that can be upgraded to unique for free are accepted
    :type unique_gifts: :obj:`bool`

    :param premium_subscription: True, if a Telegram Premium subscription is accepted
    :type premium_subscription: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.AcceptedGiftTypes`
    """

    def __init__(
        self,
        unlimited_gifts: bool = None,
        limited_gifts: bool = None,
        unique_gifts: bool = None,
        premium_subscription: bool = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.unlimited_gifts = unlimited_gifts
        self.limited_gifts = limited_gifts
        self.unique_gifts = unique_gifts
        self.premium_subscription = premium_subscription

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.AcceptedGiftTypes"]:
        return (
            AcceptedGiftTypes(
                me=me,
                json=d,
                unlimited_gifts=d.get("unlimited_gifts"),
                limited_gifts=d.get("limited_gifts"),
                unique_gifts=d.get("unique_gifts"),
                premium_subscription=d.get("premium_subscription"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
