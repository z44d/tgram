import tgram
from .type_ import Type_

from typing import List, Optional


class RichBlockTable(Type_):
    """
    This object represents a table rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblocktable

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param cells: Table cells
    :type cells: :obj:`list` of :obj:`list` of :class:`tgram.types.RichBlockTableCell`

    :param column_count: Column count
    :type column_count: :obj:`int`

    :param row_count: Row count
    :type row_count: :obj:`int`

    :param title: Optional. Title
    :type title: :class:`tgram.types.RichText`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockTable`
    """

    def __init__(
        self,
        type: "str" = "table",
        cells: List[List["tgram.types.RichBlockTableCell"]] = None,
        column_count: "int" = None,
        row_count: "int" = None,
        title: "tgram.types.RichText" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.cells = cells
        self.column_count = column_count
        self.row_count = row_count
        self.title = title

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockTable"]:
        return (
            RichBlockTable(
                me=me,
                json=d,
                type=d.get("type"),
                cells=[
                    [tgram.types.RichBlockTableCell._parse(me=me, d=j) for j in i]
                    for i in d.get("cells")
                ]
                if d.get("cells")
                else None,
                column_count=d.get("column_count"),
                row_count=d.get("row_count"),
                title=tgram.utils.rich_text_parse(me, d.get("title"))
                if d.get("title")
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
