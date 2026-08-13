from typing import Optional

import tgram

from .type_ import Type_


class RichTextTextMention(Type_):
    """
    This object represents a text mention rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtexttextmention

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :param user: User
    :type user: :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextTextMention`
    """

    def __init__(
        self,
        type: "str" = "text_mention",
        text: "str | None" = None,
        user: "tgram.types.User" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.user = user

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichTextTextMention"]:
        return (
            RichTextTextMention(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                user=tgram.types.User._parse(me=me, d=d.get("user"))
                if d.get("user")
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
