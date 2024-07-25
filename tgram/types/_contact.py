import tgram
from .type_ import Type_

from typing import Optional


class Contact(Type_):
    """
    This object represents a phone contact.

    Telegram Documentation: https://core.telegram.org/bots/api#contact

    :param phone_number: Contact's phone number
    :type phone_number: :obj:`str`

    :param first_name: Contact's first name
    :type first_name: :obj:`str`

    :param last_name: Optional. Contact's last name
    :type last_name: :obj:`str`

    :param user_id: Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits
        and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52
        significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type user_id: :obj:`int`

    :param vcard: Optional. Additional data about the contact in the form of a vCard
    :type vcard: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Contact`
    """

    def __init__(
        self,
        phone_number: "str" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        user_id: "int" = None,
        vcard: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Contact"]:
        return (
            Contact(
                me=me,
                json=d,
                phone_number=d.get("phone_number"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                user_id=d.get("user_id"),
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
