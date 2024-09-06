import tgram
from .type_ import Type_

from typing import Optional


class GiveawayCreated(Type_):
    """
    This object represents a service message about the creation of a scheduled giveaway.

    Telegram documentation: https://core.telegram.org/bots/api#giveawaycreated

    :param prize_star_count: Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only
    :type prize_star_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`GiveawayCreated`
    """

    def __init__(
        self,
        prize_star_count: int = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.prize_star_count = prize_star_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.GiveawayCreated"]:
        return (
            GiveawayCreated(me=me, json=d, prize_star_count=d.get("prize_star_count"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
