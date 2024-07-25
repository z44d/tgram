import tgram
from .type_ import Type_

from typing import Optional


class MessageOriginChannel(Type_):
    """
    The message was originally sent to a channel chat.

    :param chat: Channel chat to which the message was originally sent
    :type chat: :class:`Chat`

    :param message_id: Unique message identifier inside the chat
    :type message_id: :obj:`int`

    :param author_signature: Optional. Signature of the original post author
    :type author_signature: :obj:`str`
    """

    def __init__(
        self,
        type: "str" = None,
        date: "int" = None,
        chat: "tgram.types.Chat" = None,
        message_id: "int" = None,
        author_signature: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.date = date
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MessageOriginChannel"]:
        return (
            MessageOriginChannel(
                me=me,
                json=d,
                type=d.get("type"),
                date=d.get("date"),
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
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
