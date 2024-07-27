import tgram
from .type_ import Type_

from typing import Optional


class ChatBoostRemoved(Type_):
    """
    This object represents a boost removed from a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostremoved

    :param chat: Chat which was boosted
    :type chat: :class:`Chat`

    :param boost_id: Unique identifier of the boost
    :type boost_id: :obj:`str`

    :param remove_date: Point in time (Unix timestamp) when the boost was removed
    :type remove_date: :obj:`int`

    :param source: Source of the removed boost
    :type source: :class:`ChatBoostSource`

    :return: Instance of the class
    :rtype: :class:`ChatBoostRemoved`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        boost_id: "str" = None,
        remove_date: "int" = None,
        source: "tgram.types.ChatBoostSource" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatBoostRemoved"]:
        return (
            ChatBoostRemoved(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                boost_id=d.get("boost_id"),
                remove_date=d.get("remove_date"),
                source=tgram.types.ChatBoostSource._parse(me=me, d=d.get("source")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
