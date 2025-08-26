import tgram
from .type_ import Type_

from typing import List, Union, Optional


class ReplyParameters(Type_):
    """
    Describes reply parameters for the message that is being sent.

    Telegram documentation: https://core.telegram.org/bots/api#replyparameters

    :param message_id: Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified
    :type message_id: :obj:`int`

    :param chat_id: Optional. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername). Not supported for messages sent on behalf of a business account and messages from channel direct messages chats.
    :type chat_id: :obj:`int` or :obj:`str`

    :param allow_sending_without_reply: Optional. Pass True if the message should be sent even if the specified message to be replied to is not found. Always False for replies in another chat or forum topic. Always True for messages sent on behalf of a business account.
    :type allow_sending_without_reply: :obj:`bool`

    :param quote: Optional. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold, italic, underline, strikethrough, spoiler, and custom_emoji entities. The message will fail to send if the quote isn't found in the original message.
    :type quote: :obj:`str`

    :param quote_parse_mode: Optional. Mode for parsing entities in the quote. See formatting options for more details.
    :type quote_parse_mode: :obj:`str`

    :param quote_entities: Optional. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of quote_parse_mode.
    :type quote_entities: :obj:`list` of :class:`MessageEntity`

    :param quote_position: Optional. Position of the quote in the original message in UTF-16 code units
    :type quote_position: :obj:`int`

    :param checklist_task_id: Optional. Identifier of the specific checklist task to be replied to
    :type checklist_task_id: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`ReplyParameters`
    """

    def __init__(
        self,
        message_id: "int" = None,
        chat_id: Union["int", "str"] = None,
        allow_sending_without_reply: "bool" = None,
        quote: "str" = None,
        quote_parse_mode: "str" = None,
        quote_entities: List["tgram.types.MessageEntity"] = None,
        quote_position: "int" = None,
        checklist_task_id: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities
        self.quote_position = quote_position
        self.checklist_task_id = checklist_task_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ReplyParameters"]:
        return (
            ReplyParameters(
                me=me,
                json=d,
                message_id=d.get("message_id"),
                chat_id=d.get("chat_id"),
                allow_sending_without_reply=d.get("allow_sending_without_reply"),
                quote=d.get("quote"),
                quote_parse_mode=d.get("quote_parse_mode"),
                quote_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("quote_entities")
                ]
                if d.get("quote_entities")
                else None,
                quote_position=d.get("quote_position"),
                checklist_task_id=d.get("checklist_task_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
