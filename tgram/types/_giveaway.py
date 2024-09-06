import tgram
from .type_ import Type_

from typing import List, Optional


class Giveaway(Type_):
    """
    This object represents a message about a scheduled giveaway.

    Telegram documentation: https://core.telegram.org/bots/api#giveaway

    :param chats: The list of chats which the user must join to participate in the giveaway
    :type chats: :obj:`list` of :class:`Chat`

    :param winners_selection_date: Point in time (Unix timestamp) when winners of the giveaway will be selected
    :type winners_selection_date: :obj:`int`

    :param winner_count: The number of users which are supposed to be selected as winners of the giveaway
    :type winner_count: :obj:`int`

    :param only_new_members: Optional. True, if only users who join the chats after the giveaway started should be eligible to win
    :type only_new_members: :obj:`bool`

    :param has_public_winners: Optional. True, if the list of giveaway winners will be visible to everyone
    :type has_public_winners: :obj:`bool`

    :param prize_description: Optional. Description of additional giveaway prize
    :type prize_description: :obj:`str`

    :param country_codes: Optional. A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway.
    :type country_codes: :obj:`list` of :obj:`str`

    :param prize_star_count: Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only
    :type prize_star_count: :obj:`int`

    :param premium_subscription_month_count: Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for
    :type premium_subscription_month_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`Giveaway`
    """

    def __init__(
        self,
        chats: List["tgram.types.Chat"] = None,
        winners_selection_date: "int" = None,
        winner_count: "int" = None,
        only_new_members: "bool" = None,
        has_public_winners: "bool" = None,
        prize_description: "str" = None,
        country_codes: List["str"] = None,
        prize_star_count: "int" = None,
        premium_subscription_month_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.prize_star_count = prize_star_count
        self.premium_subscription_month_count = premium_subscription_month_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Giveaway"]:
        return (
            Giveaway(
                me=me,
                json=d,
                chats=[tgram.types.Chat._parse(me=me, d=i) for i in d.get("chats")]
                if d.get("chats")
                else None,
                winners_selection_date=d.get("winners_selection_date"),
                winner_count=d.get("winner_count"),
                only_new_members=d.get("only_new_members"),
                has_public_winners=d.get("has_public_winners"),
                prize_description=d.get("prize_description"),
                country_codes=d.get("country_codes"),
                prize_star_count=d.get("prize_star_count"),
                premium_subscription_month_count=d.get(
                    "premium_subscription_month_count"
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
