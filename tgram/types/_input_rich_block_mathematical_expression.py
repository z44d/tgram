from typing import Optional

import tgram

from .type_ import Type_


class InputRichBlockMathematicalExpression(Type_):
    def __init__(
        self,
        type: "str" = "mathematical_expression",
        text: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputRichBlockMathematicalExpression"]:
        return (
            InputRichBlockMathematicalExpression(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
