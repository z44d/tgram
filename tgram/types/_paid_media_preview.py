import tgram
from .type_ import Type_

from typing import Optional


class PaidMediaPreview(Type_):
    def __init__(
        self,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "preview"
        self.width = width
        self.height = height
        self.duration = duration

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PaidMediaPreview"]:
        return (
            PaidMediaPreview(
                me=me,
                json=d,
                type=d.get("type"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
