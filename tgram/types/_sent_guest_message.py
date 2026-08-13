from typing import Optional

import tgram

from .type_ import Type_


class SentGuestMessage(Type_):
    """
    Describes a sent guest message.

    Telegram Documentation: https://core.telegram.org/bots/api#sentguestmessage

    :param message_id: Unique identifier of the sent message
    :type message_id: :obj:`int`

    :param sender_chat: Optional. The chat from which the message was sent
    :type sender_chat: :class:`tgram.types.Chat`

    :param date: Date the message was sent in Unix time
    :type date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.SentGuestMessage`
    """

    def __init__(
        self,
        message_id: "int | None" = None,
        sender_chat: "tgram.types.Chat" = None,
        date: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_id = message_id
        self.sender_chat = sender_chat
        self.date = date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.SentGuestMessage"]:
        return (
            SentGuestMessage(
                me=me,
                json=d,
                message_id=d.get("message_id"),
                sender_chat=tgram.types.Chat._parse(me=me, d=d.get("sender_chat")),
                date=d.get("date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
