from typing import Optional

import tgram

from .type_ import Type_


class RichTextEmailAddress(Type_):
    """
    This object represents an email address rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtextemailaddress

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :param email_address: Email address
    :type email_address: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextEmailAddress`
    """

    def __init__(
        self,
        type: "str" = "email_address",
        text: "str | None" = None,
        email_address: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.email_address = email_address

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichTextEmailAddress"]:
        return (
            RichTextEmailAddress(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                email_address=d.get("email_address"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
