import tgram
from .type_ import Type_

from typing import Optional


class InlineQuery(Type_):
    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequery

    :param id: Unique identifier for this query
    :type id: :obj:`str`

    :param from_user: Sender
    :type from_user: :class:`tgram.types.User`

    :param query: Text of the query (up to 256 characters)
    :type query: :obj:`str`

    :param offset: Offset of the results to be returned, can be controlled by the bot
    :type offset: :obj:`str`

    :param chat_type: Optional. Type of the chat from which the inline query was sent. Can be either “sender” for a private
        chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always
        known for requests sent from official clients and most third-party clients, unless the request was sent from a secret
        chat
    :type chat_type: :obj:`str`

    :param location: Optional. Sender location, only for bots that request user location
    :type location: :class:`tgram.types.Location`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQuery`
    """

    def __init__(
        self,
        id: "str" = None,
        from_user: "tgram.types.User" = None,
        query: "str" = None,
        offset: "str" = None,
        chat_type: "str" = None,
        location: "tgram.types.Location" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InlineQuery"]:
        return (
            InlineQuery(
                me=me,
                json=d,
                id=d.get("id"),
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                query=d.get("query"),
                offset=d.get("offset"),
                chat_type=d.get("chat_type"),
                location=tgram.types.Location._parse(me=me, d=d.get("location")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
