import tgram
from .type_ import Type_

from typing import List, Optional


class SharedUser(Type_):
    """
    This object contains information about a user that was shared with the bot using a KeyboardButtonRequestUser button.

    Telegram documentation: https://core.telegram.org/bots/api#shareduser

    :param user_id: Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.
    :type user_id: :obj:`int`

    :param first_name: Optional. First name of the user, if the name was requested by the bot
    :type first_name: :obj:`str`

    :param last_name: Optional. Last name of the user, if the name was requested by the bot
    :type last_name: :obj:`str`

    :param username: Optional. Username of the user, if the username was requested by the bot
    :type username: :obj:`str`

    :param photo: Optional. Available sizes of the chat photo, if the photo was requested by the bot
    :type photo: :obj:`list` of :class:`PhotoSize`

    :return: Instance of the class
    :rtype: :class:`SharedUser`
    """

    def __init__(
        self,
        user_id: "int" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["tgram.types.PhotoSize"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SharedUser"]:
        return (
            SharedUser(
                me=me,
                json=d,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
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
