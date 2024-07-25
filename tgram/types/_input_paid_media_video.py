import tgram
from .type_ import Type_

from typing import Union, Optional


class InputPaidMediaVideo(Type_):
    def __init__(
        self,
        media: "str" = None,
        thumbnail: Union["tgram.types.InputFile", "str"] = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        supports_streaming: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.media = media
        self.thumbnail = thumbnail
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputPaidMediaVideo"]:
        return (
            InputPaidMediaVideo(
                me=me,
                json=d,
                type=d.get("type"),
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                supports_streaming=d.get("supports_streaming"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
