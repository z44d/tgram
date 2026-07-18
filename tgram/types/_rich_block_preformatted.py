import tgram
from .type_ import Type_

from typing import Optional


class RichBlockPreformatted(Type_):
    """
    This object represents a preformatted rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockpreformatted

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param text: Rich text
    :type text: :class:`tgram.types.RichText`

    :param language: Optional. Language
    :type language: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockPreformatted`
    """

    def __init__(
        self,
        type: "str" = "preformatted",
        text: "tgram.types.RichText" = None,
        language: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.language = language

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockPreformatted"]:
        return (
            RichBlockPreformatted(
                me=me,
                json=d,
                type=d.get("type"),
                text=tgram.utils.rich_text_parse(me, d.get("text"))
                if d.get("text")
                else None,
                language=d.get("language"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
