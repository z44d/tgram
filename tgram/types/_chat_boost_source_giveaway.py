import tgram
from .type_ import Type_

from typing import Optional


class ChatBoostSourceGiveaway(Type_):
    """
    The boost was obtained by the creation of a Telegram Premium giveaway.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostsourcegiveaway

    :param source: Source of the boost, always “giveaway”
    :type source: :obj:`str`

    :param giveaway_message_id: Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet.
    :type giveaway_message_id: :obj:`int`

    :param user: User that won the prize in the giveaway if any
    :type user: :class:`User`

    :param prize_star_count: Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only
    :type prize_star_count: :obj:`int`

    :param is_unclaimed: True, if the giveaway was completed, but there was no user to win the prize
    :type is_unclaimed: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`ChatBoostSourceGiveaway`
    """

    def __init__(
        self,
        source: "str" = None,
        giveaway_message_id: "int" = None,
        user: "tgram.types.User" = None,
        prize_star_count: "int" = None,
        is_unclaimed: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.prize_star_count = prize_star_count
        self.is_unclaimed = is_unclaimed

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatBoostSourceGiveaway"]:
        return (
            ChatBoostSourceGiveaway(
                me=me,
                json=d,
                source=d.get("source"),
                giveaway_message_id=d.get("giveaway_message_id"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                prize_star_count=d.get("prize_star_count"),
                is_unclaimed=d.get("is_unclaimed"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
