import tgram
from .type_ import Type_

from typing import List, Optional


class RichBlockSlideshow(Type_):
    """
    This object represents a slideshow rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockslideshow

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param blocks: Blocks
    :type blocks: :obj:`list` of :class:`tgram.types.RichBlock`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockSlideshow`
    """

    def __init__(
        self,
        type: "str" = "slideshow",
        blocks: List["tgram.types.RichBlock"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.blocks = blocks

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockSlideshow"]:
        return (
            RichBlockSlideshow(
                me=me,
                json=d,
                type=d.get("type"),
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
