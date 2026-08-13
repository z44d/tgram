import tgram
from .type_ import Type_

from typing import List, Optional


class InputRichBlockSlideshow(Type_):
    def __init__(
        self,
        type: "str" = "slideshow",
        blocks: List["tgram.types.InputRichBlock"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.blocks = blocks

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputRichBlockSlideshow"]:
        return (
            InputRichBlockSlideshow(
                me=me,
                json=d,
                type=d.get("type"),
                blocks=[
                    tgram.utils.input_rich_block_parse(me, i) for i in d.get("blocks")
                ]
                if d.get("blocks")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
