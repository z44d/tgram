from typing import Optional

import tgram

from .type_ import Type_


class InputRichBlockTable(Type_):
    def __init__(
        self,
        type: "str" = "table",
        cells: list[list["tgram.types.InputRichBlockTableCell"]] | None = None,
        column_count: "int | None" = None,
        row_count: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.cells = cells
        self.column_count = column_count
        self.row_count = row_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
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
