import tgram
from .type_ import Type_

from typing import Optional


class GiveawayCompleted(Type_):
    """
    This object represents a service message about the completion of a giveaway without public winners.

    Telegram documentation: https://core.telegram.org/bots/api#giveawaycompleted

    :param winner_count: Number of winners in the giveaway
    :type winner_count: :obj:`int`

    :param unclaimed_prize_count: Optional. Number of undistributed prizes
    :type unclaimed_prize_count: :obj:`int`

    :param giveaway_message: Optional. Message with the giveaway that was completed, if it wasn't deleted
    :type giveaway_message: :class:`Message`

    :param is_star_giveaway: Optional. True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.
    :type is_star_giveaway: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`GiveawayCompleted`
    """

    def __init__(
        self,
        winner_count: "int" = None,
        unclaimed_prize_count: "int" = None,
        giveaway_message: "tgram.types.Message" = None,
        is_star_giveaway: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.winner_count = winner_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.giveaway_message = giveaway_message
        self.is_star_giveaway = is_star_giveaway

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.GiveawayCompleted"]:
        return (
            GiveawayCompleted(
                me=me,
                json=d,
                winner_count=d.get("winner_count"),
                unclaimed_prize_count=d.get("unclaimed_prize_count"),
                giveaway_message=tgram.types.Message._parse(
                    me=me, d=d.get("giveaway_message")
                ),
                is_star_giveaway=d.get("is_star_giveaway"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
