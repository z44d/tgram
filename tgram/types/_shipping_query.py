import tgram
from .type_ import Type_

from typing import Optional


class ShippingQuery(Type_):
    """
    This object contains information about an incoming shipping query.

    Telegram Documentation: https://core.telegram.org/bots/api#shippingquery

    :param id: Unique query identifier
    :type id: :obj:`str`

    :param from: User who sent the query
    :type from: :class:`tgram.types.User`

    :param invoice_payload: Bot specified invoice payload
    :type invoice_payload: :obj:`str`

    :param shipping_address: User specified shipping address
    :type shipping_address: :class:`tgram.types.ShippingAddress`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ShippingQuery`
    """

    def __init__(
        self,
        id: "str" = None,
        from_user: "tgram.types.User" = None,
        invoice_payload: "str" = None,
        shipping_address: "tgram.types.ShippingAddress" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ShippingQuery"]:
        return (
            ShippingQuery(
                me=me,
                json=d,
                id=d.get("id"),
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                invoice_payload=d.get("invoice_payload"),
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
