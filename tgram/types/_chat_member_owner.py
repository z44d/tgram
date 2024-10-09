import tgram
from .type_ import Type_

from typing import Optional


class ChatMemberOwner(Type_):
    """
    Represents a chat member that owns the chat and has all administrator privileges.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberowner

    :param status: The member's status in the chat, always “creator”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param is_anonymous: True, if the user's presence in the chat is hidden
    :type is_anonymous: :obj:`bool`

    :param custom_title: Optional. Custom title for this user
    :type custom_title: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberOwner`
    """

    def __init__(
        self,
        status: "tgram.types.ChatMemberStatus" = None,
        user: "tgram.types.User" = None,
        is_anonymous: "bool" = None,
        custom_title: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatMemberOwner"]:
        return (
            ChatMemberOwner(
                me=me,
                json=d,
                status=d.get("status"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                is_anonymous=d.get("is_anonymous"),
                custom_title=d.get("custom_title"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
