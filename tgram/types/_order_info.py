import tgram
from .type_ import Type_

from typing import Optional


class OrderInfo(Type_):
    """
    This object represents information about an order.

    Telegram Documentation: https://core.telegram.org/bots/api#orderinfo

    :param name: Optional. User name
    :type name: :obj:`str`

    :param phone_number: Optional. User's phone number
    :type phone_number: :obj:`str`

    :param email: Optional. User email
    :type email: :obj:`str`

    :param shipping_address: Optional. User shipping address
    :type shipping_address: :class:`tgram.types.ShippingAddress`

    :return: Instance of the class
    :rtype: :class:`tgram.types.OrderInfo`
    """

    def __init__(
        self,
        name: "str" = None,
        phone_number: "str" = None,
        email: "str" = None,
        shipping_address: "tgram.types.ShippingAddress" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.OrderInfo"]:
        return (
            OrderInfo(
                me=me,
                json=d,
                name=d.get("name"),
                phone_number=d.get("phone_number"),
                email=d.get("email"),
                shipping_address=tgram.types.ShippingAddress._parse(
                    me=me, d=d.get("shipping_address")
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
