import tgram
from .type_ import Type_

from typing import Optional


class RichTextMention(Type_):
    """
    This object represents a mention rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtextmention

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextMention`
    """

    def __init__(
        self,
        type: "str" = "mention",
        text: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichTextMention"]:
        return (
            RichTextMention(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
