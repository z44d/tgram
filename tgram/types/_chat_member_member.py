import tgram
from .type_ import Type_

from typing import Optional


class ChatMemberMember(Type_):
    """
    Represents a chat member that has no additional privileges or restrictions.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmembermember

    :param status: The member's status in the chat, always “member”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param until_date: Optional. Date when the user's subscription will expire; Unix time
    :type status: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberMember`
    """

    def __init__(
        self,
        status: "tgram.types.ChatMemberStatus" = None,
        user: "tgram.types.User" = None,
        until_date: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user
        self.until_date = until_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatMemberMember"]:
        return (
            ChatMemberMember(
                me=me,
                json=d,
                status=d.get("status"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                until_date=d.get("until_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
