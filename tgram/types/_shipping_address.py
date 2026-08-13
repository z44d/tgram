from typing import Optional

import tgram

from .type_ import Type_


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
        country_code: "str | None" = None,
        state: "str | None" = None,
        city: "str | None" = None,
        street_line1: "str | None" = None,
        street_line2: "str | None" = None,
        post_code: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
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
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
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
