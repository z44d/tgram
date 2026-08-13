from typing import Optional

import tgram

from .type_ import Type_


class InputMediaLocation(Type_):
    """
    Represents a location to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmedialocation

    :param type: Type of the media, must be location
    :type type: :obj:`str`

    :param latitude: Latitude of the location
    :type latitude: :obj:`float`

    :param longitude: Longitude of the location
    :type longitude: :obj:`float`

    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :type horizontal_accuracy: :obj:`float`

    :param live_period: Optional. Period in seconds for which the location will be updated
    :type live_period: :obj:`int`

    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees; 1-360
    :type heading: :obj:`int`

    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters
    :type proximity_alert_radius: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaLocation`
    """

    def __init__(
        self,
        latitude: "float | None" = None,
        longitude: "float | None" = None,
        horizontal_accuracy: "float | None" = None,
        live_period: "int | None" = None,
        heading: "int | None" = None,
        proximity_alert_radius: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "location"
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputMediaLocation"]:
        return (
            InputMediaLocation(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                horizontal_accuracy=d.get("horizontal_accuracy"),
                live_period=d.get("live_period"),
                heading=d.get("heading"),
                proximity_alert_radius=d.get("proximity_alert_radius"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
