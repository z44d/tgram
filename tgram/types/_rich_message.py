import tgram
from .type_ import Type_

from typing import List, Optional


class RichMessage(Type_):
    """
    This object represents a rich message.

    Telegram Documentation: https://core.telegram.org/bots/api#richmessage

    :param blocks: Blocks
    :type blocks: :obj:`list` of :class:`tgram.types.RichBlock`

    :param caption: Optional. Caption
    :type caption: :class:`tgram.types.RichBlockCaption`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichMessage`
    """

    def __init__(
        self,
        blocks: List["tgram.types.RichBlock"] = None,
        caption: "tgram.types.RichBlockCaption" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.blocks = blocks
        self.caption = caption

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichMessage"]:
        return (
            RichMessage(
                me=me,
                json=d,
                blocks=[
                    tgram.utils.rich_block_parse(me, i)
                    for i in d.get("blocks")
                ]
                if d.get("blocks")
                else None,
                caption=tgram.types.RichBlockCaption._parse(
                    me=me, d=d.get("caption")
                )
                if d.get("caption")
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
