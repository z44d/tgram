import tgram
from .type_ import Type_

from typing import Optional


class RichBlockSectionHeading(Type_):
    """
    This object represents a section heading rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblocksectionheading

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param text: Rich text
    :type text: :class:`tgram.types.RichText`

    :param level: Heading level
    :type level: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockSectionHeading`
    """

    def __init__(
        self,
        type: "str" = "section_heading",
        text: "tgram.types.RichText" = None,
        level: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.level = level

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockSectionHeading"]:
        return (
            RichBlockSectionHeading(
                me=me,
                json=d,
                type=d.get("type"),
                text=tgram.utils.rich_text_parse(me, d.get("text"))
                if d.get("text")
                else None,
                level=d.get("level"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
