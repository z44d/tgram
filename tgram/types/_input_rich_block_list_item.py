from typing import Optional

import tgram

from .type_ import Type_


class InputRichBlockListItem(Type_):
    def __init__(
        self,
        text: "str | None" = None,
        num: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.num = num

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputRichBlockListItem"]:
        return (
            InputRichBlockListItem(
                me=me,
                json=d,
                text=d.get("text"),
                num=d.get("num"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
