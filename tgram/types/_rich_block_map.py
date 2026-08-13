from typing import Optional

import tgram

from .type_ import Type_


class RichBlockMap(Type_):
    """
    This object represents a map rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockmap

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param latitude: Latitude
    :type latitude: :obj:`float`

    :param longitude: Longitude
    :type longitude: :obj:`float`

    :param heading: Optional. Heading
    :type heading: :obj:`int`

    :param zoom: Optional. Zoom level
    :type zoom: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockMap`
    """

    def __init__(
        self,
        type: "str" = "map",
        latitude: "float | None" = None,
        longitude: "float | None" = None,
        heading: "int | None" = None,
        zoom: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.heading = heading
        self.zoom = zoom

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichBlockMap"]:
        return (
            RichBlockMap(
                me=me,
                json=d,
                type=d.get("type"),
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                heading=d.get("heading"),
                zoom=d.get("zoom"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
