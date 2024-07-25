import tgram
from .type_ import Type_

from typing import List, Optional


class MessageReactionCountUpdated(Type_):
    """
    This object represents a service message about a change in the list of the current user's reactions to a message.

    Telegram documentation: https://core.telegram.org/bots/api#messagereactioncountupdated

    :param chat: The chat containing the message
    :type chat: :class:`tgram.types.Chat`

    :param message_id: Unique message identifier inside the chat
    :type message_id: :obj:`int`

    :param date: Date of the change in Unix time
    :type date: :obj:`int`

    :param reactions: List of reactions that are present on the message
    :type reactions: :obj:`list` of :class:`ReactionCount`

    :return: Instance of the class
    :rtype: :class:`MessageReactionCountUpdated`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        message_id: "int" = None,
        date: "int" = None,
        reactions: List["tgram.types.ReactionCount"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MessageReactionCountUpdated"]:
        return (
            MessageReactionCountUpdated(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
                date=d.get("date"),
                reactions=[
                    tgram.types.ReactionCount._parse(me=me, d=i)
                    for i in d.get("reactions")
                ]
                if d.get("reactions")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
