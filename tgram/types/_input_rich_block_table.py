import tgram
from .type_ import Type_

from typing import List, Optional


class InputRichBlockTable(Type_):
    def __init__(
        self,
        type: "str" = "table",
        cells: List[List["tgram.types.InputRichBlockTableCell"]] = None,
        column_count: "int" = None,
        row_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.cells = cells
        self.column_count = column_count
        self.row_count = row_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputRichBlockTable"]:
        return (
            InputRichBlockTable(
                me=me,
                json=d,
                type=d.get("type"),
                cells=[
                    [tgram.types.InputRichBlockTableCell._parse(me=me, d=j) for j in i]
                    for i in d.get("cells")
                ]
                if d.get("cells")
                else None,
                column_count=d.get("column_count"),
                row_count=d.get("row_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
