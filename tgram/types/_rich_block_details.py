import tgram
from .type_ import Type_

from typing import List, Optional


class RichBlockDetails(Type_):
    """
    This object represents a details rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockdetails

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param text: Rich text
    :type text: :class:`tgram.types.RichText`

    :param blocks: Blocks
    :type blocks: :obj:`list` of :class:`tgram.types.RichBlock`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockDetails`
    """

    def __init__(
        self,
        type: "str" = "details",
        text: "tgram.types.RichText" = None,
        blocks: List["tgram.types.RichBlock"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.blocks = blocks

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockDetails"]:
        return (
            RichBlockDetails(
                me=me,
                json=d,
                type=d.get("type"),
                text=tgram.utils.rich_text_parse(me, d.get("text"))
                if d.get("text")
                else None,
                blocks=[tgram.utils.rich_block_parse(me, i) for i in d.get("blocks")]
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
