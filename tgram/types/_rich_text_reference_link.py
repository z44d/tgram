import tgram
from .type_ import Type_

from typing import Optional


class RichTextReferenceLink(Type_):
    """
    This object represents a reference link rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtextreferencelink

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :param reference_id: Reference ID
    :type reference_id: :obj:`str`

    :param url: URL
    :type url: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextReferenceLink`
    """

    def __init__(
        self,
        type: "str" = "reference_link",
        text: "str" = None,
        reference_id: "str" = None,
        url: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.reference_id = reference_id
        self.url = url

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichTextReferenceLink"]:
        return (
            RichTextReferenceLink(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                reference_id=d.get("reference_id"),
                url=d.get("url"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
