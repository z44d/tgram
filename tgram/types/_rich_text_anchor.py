from typing import Optional

import tgram

from .type_ import Type_


class RichTextAnchor(Type_):
    """
    This object represents an anchor rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtextanchor

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :param name: Anchor name
    :type name: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextAnchor`
    """

    def __init__(
        self,
        type: "str" = "anchor",
        text: "str | None" = None,
        name: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.name = name

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichTextAnchor"]:
        return (
            RichTextAnchor(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                name=d.get("name"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
