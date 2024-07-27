import tgram
from .type_ import Type_

from typing import Optional


class ChatBoostUpdated(Type_):
    """
    This object represents a boost added to a chat or changed.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostupdated

    :param chat: Chat which was boosted
    :type chat: :class:`Chat`

    :param boost: Infomation about the chat boost
    :type boost: :class:`ChatBoost`

    :return: Instance of the class
    :rtype: :class:`ChatBoostUpdated`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        boost: "tgram.types.ChatBoost" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.boost = boost

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatBoostUpdated"]:
        return (
            ChatBoostUpdated(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                boost=tgram.types.ChatBoost._parse(me=me, d=d.get("boost")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
