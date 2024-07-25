import tgram
from .type_ import Type_

from typing import Optional


class MessageOriginChat(Type_):
    """
    The message was originally sent on behalf of a chat to a group chat.

    :param sender_chat: Chat that sent the message originally
    :type sender_chat: :class:`Chat`

    :param author_signature: Optional. For messages originally sent by an anonymous chat administrator, original message author signature
    :type author_signature: :obj:`str`
    """

    def __init__(
        self,
        type: "str" = None,
        date: "int" = None,
        sender_chat: "tgram.types.Chat" = None,
        author_signature: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.date = date
        self.sender_chat = sender_chat
        self.author_signature = author_signature

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MessageOriginChat"]:
        return (
            MessageOriginChat(
                me=me,
                json=d,
                type=d.get("type"),
                date=d.get("date"),
                sender_chat=tgram.types.Chat._parse(me=me, d=d.get("sender_chat")),
                author_signature=d.get("author_signature"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
