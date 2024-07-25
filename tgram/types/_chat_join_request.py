import tgram
from .type_ import Type_

from typing import Optional


class ChatJoinRequest(Type_):
    """
    Represents a join request sent to a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chatjoinrequest

    :param chat: Chat to which the request was sent
    :type chat: :class:`tgram.types.Chat`

    :param from_user: User that sent the join request
    :type from_user: :class:`tgram.types.User`

    :param user_chat_id: Optional. Identifier of a private chat with the user who sent the join request.
        This number may have more than 32 significant bits and some programming languages may have difficulty/silent
        defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision
        float type are safe for storing this identifier. The bot can use this identifier for 24 hours to send messages
        until the join request is processed, assuming no other administrator contacted the user.
    :type user_chat_id: :obj:`int`

    :param date: Date the request was sent in Unix time
    :type date: :obj:`int`

    :param bio: Optional. Bio of the user.
    :type bio: :obj:`str`

    :param invite_link: Optional. Chat invite link that was used by the user to send the join request
    :type invite_link: :class:`tgram.types.ChatInviteLink`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatJoinRequest`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        from_user: "tgram.types.User" = None,
        user_chat_id: "int" = None,
        date: "int" = None,
        bio: "str" = None,
        invite_link: "tgram.types.ChatInviteLink" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatJoinRequest"]:
        return (
            ChatJoinRequest(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                user_chat_id=d.get("user_chat_id"),
                date=d.get("date"),
                bio=d.get("bio"),
                invite_link=tgram.types.ChatInviteLink._parse(
                    me=me, d=d.get("invite_link")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
