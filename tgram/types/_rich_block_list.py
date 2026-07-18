import tgram
from .type_ import Type_

from typing import List, Optional


class RichBlockList(Type_):
    """
    This object represents a list rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblocklist

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param items: List items
    :type items: :obj:`list` of :class:`tgram.types.RichBlockListItem`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockList`
    """

    def __init__(
        self,
        type: "str" = "list",
        items: List["tgram.types.RichBlockListItem"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.items = items

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockList"]:
        return (
            RichBlockList(
                me=me,
                json=d,
                type=d.get("type"),
                items=[
                    tgram.types.RichBlockListItem._parse(me=me, d=i)
                    for i in d.get("items")
                ]
                if d.get("items")
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
