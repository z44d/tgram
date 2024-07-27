import tgram
from .type_ import Type_

from typing import Optional


class InputContactMessageContent(Type_):
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inputcontactmessagecontent

    :param phone_number: Contact's phone number
    :type phone_number: :obj:`str`

    :param first_name: Contact's first name
    :type first_name: :obj:`str`

    :param last_name: Optional. Contact's last name
    :type last_name: :obj:`str`

    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    :type vcard: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputContactMessageContent`
    """

    def __init__(
        self,
        phone_number: "str" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        vcard: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputContactMessageContent"]:
        return (
            InputContactMessageContent(
                me=me,
                json=d,
                phone_number=d.get("phone_number"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                vcard=d.get("vcard"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
