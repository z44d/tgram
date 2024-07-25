import tgram
from .type_ import Type_

from typing import Optional


class InaccessibleMessage(Type_):
    """
    This object describes a message that was deleted or is otherwise inaccessible to the bot.

    Telegram documentation: https://core.telegram.org/bots/api#inaccessiblemessage

    :param chat: Chat the message belonged to
    :type chat: :class:`Chat`

    :param message_id: Unique message identifier inside the chat
    :type message_id: :obj:`int`

    :param date: Always 0. The field can be used to differentiate regular and inaccessible messages.
    :type date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`InaccessibleMessage`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        message_id: "int" = None,
        date: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.message_id = message_id
        self.date = date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InaccessibleMessage"]:
        return (
            InaccessibleMessage(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
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
