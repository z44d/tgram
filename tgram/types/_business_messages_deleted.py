import tgram
from .type_ import Type_

from typing import List, Optional


class BusinessMessagesDeleted(Type_):
    """
    This object is received when messages are deleted from a connected business account.

    Telegram documentation: https://core.telegram.org/bots/api#businessmessagesdeleted

    :param business_connection_id: Unique identifier of the business connection
    :type business_connection_id: :obj:`str`

    :param chat: Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.
    :type chat: :class:`Chat`

    :param message_ids: A JSON-serialized list of identifiers of deleted messages in the chat of the business account
    :type message_ids: :obj:`list` of :obj:`int`

    :return: Instance of the class
    :rtype: :class:`BusinessMessagesDeleted`
    """

    def __init__(
        self,
        business_connection_id: "str" = None,
        chat: "tgram.types.Chat" = None,
        message_ids: List["int"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.message_ids = message_ids

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BusinessMessagesDeleted"]:
        return (
            BusinessMessagesDeleted(
                me=me,
                json=d,
                business_connection_id=d.get("business_connection_id"),
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                message_ids=d.get("message_ids"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
