from typing import Optional

import tgram

from .type_ import Type_


class InputRichBlockDetails(Type_):
    def __init__(
        self,
        type: "str" = "details",
        text: "str | None" = None,
        blocks: list["tgram.types.InputRichBlock"] | None = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.blocks = blocks

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputRichBlockDetails"]:
        return (
            InputRichBlockDetails(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
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
