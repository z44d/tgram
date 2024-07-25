import tgram
from .type_ import Type_

from typing import Optional


class ShippingAddress(Type_):
    """
    This object represents a shipping address.

    Telegram Documentation: https://core.telegram.org/bots/api#shippingaddress

    :param country_code: Two-letter ISO 3166-1 alpha-2 country code
    :type country_code: :obj:`str`

    :param state: State, if applicable
    :type state: :obj:`str`

    :param city: City
    :type city: :obj:`str`

    :param street_line1: First line for the address
    :type street_line1: :obj:`str`

    :param street_line2: Second line for the address
    :type street_line2: :obj:`str`

    :param post_code: Address post code
    :type post_code: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ShippingAddress`
    """

    def __init__(
        self,
        country_code: "str" = None,
        state: "str" = None,
        city: "str" = None,
        street_line1: "str" = None,
        street_line2: "str" = None,
        post_code: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ShippingAddress"]:
        return (
            ShippingAddress(
                me=me,
                json=d,
                country_code=d.get("country_code"),
                state=d.get("state"),
                city=d.get("city"),
                street_line1=d.get("street_line1"),
                street_line2=d.get("street_line2"),
                post_code=d.get("post_code"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
