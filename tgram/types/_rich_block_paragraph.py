import tgram
from .type_ import Type_

from typing import Optional


class RichBlockParagraph(Type_):
    """
    This object represents a paragraph rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockparagraph

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param text: Rich text
    :type text: :class:`tgram.types.RichText`

    :param fallback: Optional. Fallback text
    :type fallback: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockParagraph`
    """

    def __init__(
        self,
        type: "str" = "paragraph",
        text: "tgram.types.RichText" = None,
        fallback: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.fallback = fallback

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockParagraph"]:
        return (
            RichBlockParagraph(
                me=me,
                json=d,
                type=d.get("type"),
                text=tgram.utils.rich_text_parse(me, d.get("text"))
                if d.get("text")
                else None,
                fallback=d.get("fallback"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
