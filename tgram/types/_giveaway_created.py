import tgram
from .type_ import Type_

from typing import List, Optional


class GiveawayCreated(Type_):
    """
    This object represents a service message about the creation of a scheduled giveaway. Currently holds no information.
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
        self.premium_subscription_month_count = premium_subscription_month_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.GiveawayCreated"]:
        return (
            GiveawayCreated(
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
