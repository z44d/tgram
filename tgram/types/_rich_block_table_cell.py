from typing import Optional

import tgram

from .type_ import Type_


class RichBlockTableCell(Type_):
    """
    This object represents a table cell in a rich block table.

    Telegram Documentation: https://core.telegram.org/bots/api#richblocktablecell

    :param text: Rich text
    :type text: :class:`tgram.types.RichText`

    :param colspan: Optional. Column span
    :type colspan: :obj:`int`

    :param rowspan: Optional. Row span
    :type rowspan: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockTableCell`
    """

    def __init__(
        self,
        text: "tgram.types.RichText" = None,
        colspan: "int | None" = None,
        rowspan: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.colspan = colspan
        self.rowspan = rowspan

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichBlockTableCell"]:
        return (
            RichBlockTableCell(
                me=me,
                json=d,
                text=tgram.utils.rich_text_parse(me, d.get("text"))
                if d.get("text")
                else None,
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
