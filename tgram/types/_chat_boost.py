import tgram
from .type_ import Type_

from typing import Optional


class ChatBoost(Type_):
    """
    This object contains information about a chat boost.

    Telegram documentation: https://core.telegram.org/bots/api#chatboost

    :param boost_id: Unique identifier of the boost
    :type boost_id: :obj:`str`

    :param add_date: Point in time (Unix timestamp) when the chat was boosted
    :type add_date: :obj:`int`

    :param expiration_date: Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged
    :type expiration_date: :obj:`int`

    :param source: Optional. Source of the added boost (made Optional for now due to API error)
    :type source: :class:`ChatBoostSource`

    :return: Instance of the class
    :rtype: :class:`ChatBoost`
    """

    def __init__(
        self,
        boost_id: "str" = None,
        add_date: "int" = None,
        expiration_date: "int" = None,
        source: "tgram.types.ChatBoostSource" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatBoost"]:
        return (
            ChatBoost(
                me=me,
                json=d,
                boost_id=d.get("boost_id"),
                add_date=d.get("add_date"),
                expiration_date=d.get("expiration_date"),
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
