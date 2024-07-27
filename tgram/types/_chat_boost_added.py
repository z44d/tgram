import tgram
from .type_ import Type_

from typing import Optional


class ChatBoostAdded(Type_):
    """
    This object represents a service message about a user boosting a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostadded

    :param boost_count: Number of boosts added by the user
    :type boost_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`ChatBoostAdded`
    """

    def __init__(
        self,
        boost_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.boost_count = boost_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatBoostAdded"]:
        return (
            ChatBoostAdded(me=me, json=d, boost_count=d.get("boost_count"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
