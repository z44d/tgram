import tgram
from .type_ import Type_

from typing import Optional


class PaidMediaVideo(Type_):
    def __init__(
        self,
        video: "tgram.types.Video" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.video = video

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PaidMediaVideo"]:
        return (
            PaidMediaVideo(
                me=me,
                json=d,
                type=d.get("type"),
                video=tgram.types.Video._parse(me=me, d=d.get("video")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
