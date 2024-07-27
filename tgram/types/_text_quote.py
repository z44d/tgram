import tgram
from .type_ import Type_

from typing import List, Optional
from tgram.utils import String


class TextQuote(Type_):
    """
    This object contains information about the quoted part of a message that is replied to by the given message.

    Telegram documentation: https://core.telegram.org/bots/api#textquote

    :param text: Text of the quoted part of a message that is replied to by the given message
    :type text: :class:`tgram.utils.String`

    :param entities: Optional. Special entities that appear in the quote. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes.
    :type entities: :obj:`list` of :class:`MessageEntity`

    :param position: Approximate quote position in the original message in UTF-16 code units as specified by the sender
    :type position: :obj:`int`

    :param is_manual: Optional. True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server.
    :type is_manual: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`TextQuote`
    """

    def __init__(
        self,
        text: "String" = None,
        position: "int" = None,
        entities: List["tgram.types.MessageEntity"] = None,
        is_manual: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = String(text).put(entities)
        self.entities = entities
        self.position = position
        self.is_manual = is_manual

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.TextQuote"]:
        return (
            TextQuote(
                me=me,
                json=d,
                text=d.get("text"),
                position=d.get("position"),
                entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("entities")
                ]
                if d.get("entities")
                else None,
                is_manual=d.get("is_manual"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
