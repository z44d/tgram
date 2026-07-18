import tgram
from .type_ import Type_

from typing import Optional


class InputRichBlockTableCell(Type_):
    def __init__(
        self,
        text: "str" = None,
        colspan: "int" = None,
        rowspan: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.colspan = colspan
        self.rowspan = rowspan

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputRichBlockTableCell"]:
        return (
            InputRichBlockTableCell(
                me=me,
                json=d,
                text=d.get("text"),
                colspan=d.get("colspan"),
                rowspan=d.get("rowspan"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
