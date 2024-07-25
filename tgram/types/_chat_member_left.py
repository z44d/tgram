import tgram
from .type_ import Type_

from typing import Optional


class ChatMemberLeft(Type_):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberleft

    :param status: The member's status in the chat, always “left”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberLeft`
    """

    def __init__(
        self,
        status: "str" = None,
        user: "tgram.types.User" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatMemberLeft"]:
        return (
            ChatMemberLeft(
                me=me,
                json=d,
                status=d.get("status"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
