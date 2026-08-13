from typing import Optional

import tgram

from .type_ import Type_


class RichTextPhoneNumber(Type_):
    """
    This object represents a phone number rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtextphonenumber

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :param phone_number: Phone number
    :type phone_number: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextPhoneNumber`
    """

    def __init__(
        self,
        type: "str" = "phone_number",
        text: "str | None" = None,
        phone_number: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.phone_number = phone_number

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichTextPhoneNumber"]:
        return (
            RichTextPhoneNumber(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                phone_number=d.get("phone_number"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
