import tgram
from .type_ import Type_

from typing import Optional


class ChatMemberBanned(Type_):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberbanned

    :param status: The member's status in the chat, always “kicked”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned
        forever
    :type until_date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberBanned`
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
    ) -> Optional["tgram.types.ChatMemberBanned"]:
        return (
            ChatMemberBanned(
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
