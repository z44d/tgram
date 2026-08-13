from typing import Optional

import tgram

from .type_ import Type_


class InputRichBlockSectionHeading(Type_):
    def __init__(
        self,
        type: "str" = "section_heading",
        text: "str | None" = None,
        level: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.level = level

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputRichBlockSectionHeading"]:
        return (
            InputRichBlockSectionHeading(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                level=d.get("level"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
