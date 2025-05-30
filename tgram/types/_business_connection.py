import tgram
from .type_ import Type_

from typing import Optional


class BusinessConnection(Type_):
    """
    This object describes the connection of the bot with a business account.

    Telegram documentation: https://core.telegram.org/bots/api#businessconnection

    :param id: Unique identifier of the business connection
    :type id: :obj:`str`

    :param user: Business account user that created the business connection
    :type user: :class:`User`

    :param user_chat_id: Identifier of a private chat with the user who created the business connection
    :type user_chat_id: :obj:`int`

    :param date: Date the connection was established in Unix time
    :type date: :obj:`int`

    :param rights: Optional. Rights of the business bot
    :type rights: :class:`tgram.types.BusinessBotRights`

    :param is_enabled: True, if the connection is active
    :type is_enabled: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`BusinessConnection`
    """

    def __init__(
        self,
        id: "str" = None,
        user: "tgram.types.User" = None,
        user_chat_id: "int" = None,
        date: "int" = None,
        rights: "tgram.types.BusinessBotRights" = None,
        is_enabled: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.user = user
        self.user_chat_id = user_chat_id
        self.date = date
        self.rights = rights
        self.is_enabled = is_enabled

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BusinessConnection"]:
        return (
            BusinessConnection(
                me=me,
                json=d,
                id=d.get("id"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                user_chat_id=d.get("user_chat_id"),
                date=d.get("date"),
                rights=tgram.types.BusinessBotRights._parse(me=me, d=d.get("rights")),
                is_enabled=d.get("is_enabled"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
