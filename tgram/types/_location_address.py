from typing import Optional

import tgram

from .type_ import Type_


class LocationAddress(Type_):
    """
    Describes the physical address of a location.

    :param country_code: The two-letter ISO 3166-1 alpha-2 country code of the country where the location is located
    :type country_code: :obj:`str`
    :param state: Optional. State of the location
    :type state: :obj:`str`
    :param city: Optional. City of the location
    :type city: :obj:`str`
    :param street: Optional. Street address of the location
    :type street: :obj:`str`
    """

    def __init__(
        self,
        country_code: str | None = None,
        state: str | None = None,
        city: str | None = None,
        street: str | None = None,
        me: "tgram.TgBot" = None,
        json: dict | None = None,
    ):
        super().__init__(me=me, json=json)
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street = street

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["LocationAddress"]:
        return (
            LocationAddress(
                country_code=d.get("country_code"),
                state=d.get("state"),
                city=d.get("city"),
                street=d.get("street"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
