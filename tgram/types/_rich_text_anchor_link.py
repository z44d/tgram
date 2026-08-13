from typing import Optional

import tgram

from .type_ import Type_


class RichTextAnchorLink(Type_):
    """
    This object represents an anchor link rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtextanchorlink

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :param anchor_name: Anchor name
    :type anchor_name: :obj:`str`

    :param url: Optional. URL
    :type url: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextAnchorLink`
    """

    def __init__(
        self,
        type: "str" = "anchor_link",
        text: "str | None" = None,
        anchor_name: "str | None" = None,
        url: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.anchor_name = anchor_name
        self.url = url

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichTextAnchorLink"]:
        return (
            RichTextAnchorLink(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                anchor_name=d.get("anchor_name"),
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
