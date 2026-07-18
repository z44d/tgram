import tgram
from .type_ import Type_

from typing import Optional


class InputRichBlockMap(Type_):
    def __init__(
        self,
        type: "str" = "map",
        latitude: "float" = None,
        longitude: "float" = None,
        heading: "int" = None,
        zoom: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.heading = heading
        self.zoom = zoom

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputRichBlockMap"]:
        return (
            InputRichBlockMap(
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
