from typing import Optional

import tgram

from .type_ import Type_


class InputMediaVenue(Type_):
    """
    Represents a venue to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmediavenue

    :param type: Type of the media, must be venue
    :type type: :obj:`str`

    :param latitude: Latitude of the venue
    :type latitude: :obj:`float`

    :param longitude: Longitude of the venue
    :type longitude: :obj:`float`

    :param title: Name of the venue
    :type title: :obj:`str`

    :param address: Address of the venue
    :type address: :obj:`str`

    :param foursquare_id: Optional. Foursquare identifier of the venue
    :type foursquare_id: :obj:`str`

    :param foursquare_type: Optional. Foursquare type of the venue, if known
    :type foursquare_type: :obj:`str`

    :param google_place_id: Optional. Google Places identifier of the venue
    :type google_place_id: :obj:`str`

    :param google_place_type: Optional. Google Places type of the venue
    :type google_place_type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaVenue`
    """

    def __init__(
        self,
        latitude: "float | None" = None,
        longitude: "float | None" = None,
        title: "str | None" = None,
        address: "str | None" = None,
        foursquare_id: "str | None" = None,
        foursquare_type: "str | None" = None,
        google_place_id: "str | None" = None,
        google_place_type: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "venue"
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputMediaVenue"]:
        return (
            InputMediaVenue(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                address=d.get("address"),
                foursquare_id=d.get("foursquare_id"),
                foursquare_type=d.get("foursquare_type"),
                google_place_id=d.get("google_place_id"),
                google_place_type=d.get("google_place_type"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
