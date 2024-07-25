import tgram
from .type_ import Type_

from typing import List, Optional


class ShippingOption(Type_):
    """
    This object represents one shipping option.

    Telegram Documentation: https://core.telegram.org/bots/api#shippingoption

    :param id: Shipping option identifier
    :type id: :obj:`str`

    :param title: Option title
    :type title: :obj:`str`

    :param prices: List of price portions
    :type prices: :obj:`list` of :class:`tgram.types.LabeledPrice`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ShippingOption`
    """

    def __init__(
        self,
        id: "str" = None,
        title: "str" = None,
        prices: List["tgram.types.LabeledPrice"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.title = title
        self.prices = prices

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ShippingOption"]:
        return (
            ShippingOption(
                me=me,
                json=d,
                id=d.get("id"),
                title=d.get("title"),
                prices=[
                    tgram.types.LabeledPrice._parse(me=me, d=i) for i in d.get("prices")
                ]
                if d.get("prices")
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
