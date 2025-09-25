import tgram
from .type_ import Type_

from typing import Optional
from tgram import bound


class Chat(Type_, bound.ChatB):
    """
    This object represents a chat.

    Telegram documentation: https://core.telegram.org/bots/api#Chat

    :param id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :type id: :obj:`int`

    :param type: Type of the chat, can be either “private”, “group”, “supergroup” or “channel”.
    :type type: :obj:`str`

    :param title: Optional. Title, for supergroups, channels and group chats.
    :type title: :obj:`str`, optional

    :param username: Optional. Username, for private chats, supergroups and channels if available.
    :type username: :obj:`str`, optional

    :param first_name: Optional. First name of the other party in a private chat.
    :type first_name: :obj:`str`, optional

    :param last_name: Optional. Last name of the other party in a private chat.
    :type last_name: :obj:`str`, optional

    :param is_forum: Optional. True, if the supergroup chat is a forum (has topics enabled).
    :type is_forum: :obj:`bool`, optional

    :param is_direct_messages: Optional. True, if the chat is the direct messages chat of a channel.
    :type is_direct_messages: :obj:`bool`, optional

    :return: Instance of the class
    :rtype: :class:`tgram.types.Chat`
    """

    def __init__(
        self,
        id: int,
        type: str,
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        is_forum: Optional[bool] = None,
        is_direct_messages: Optional[bool] = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.is_direct_messages = is_direct_messages

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Chat"]:
        return (
            Chat(
                me=me,
                json=d,
                id=d.get("id"),
                type=d.get("type"),
                title=d.get("title"),
                username=d.get("username"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                is_forum=d.get("is_forum"),
                is_direct_messages=d.get("is_direct_messages"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
