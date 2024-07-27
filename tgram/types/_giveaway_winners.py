import tgram
from .type_ import Type_

from typing import List, Optional


class GiveawayWinners(Type_):
    """
    This object represents a message about the completion of a giveaway with public winners.

    Telegram documentation: https://core.telegram.org/bots/api#giveawaywinners

    :param chat: The chat that created the giveaway
    :type chat: :class:`Chat`

    :param giveaway_message_id: Identifier of the messsage with the giveaway in the chat
    :type giveaway_message_id: :obj:`int`

    :param winners_selection_date: Point in time (Unix timestamp) when winners of the giveaway were selected
    :type winners_selection_date: :obj:`int`

    :param winner_count: Total number of winners in the giveaway
    :type winner_count: :obj:`int`

    :param winners: List of up to 100 winners of the giveaway
    :type winners: :obj:`list` of :class:`User`

    :param additional_chat_count: Optional. The number of other chats the user had to join in order to be eligible for the giveaway
    :type additional_chat_count: :obj:`int`

    :param premium_subscription_month_count: Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for
    :type premium_subscription_month_count: :obj:`int`

    :param unclaimed_prize_count: Optional. Number of undistributed prizes
    :type unclaimed_prize_count: :obj:`int`

    :param only_new_members: Optional. True, if only users who had joined the chats after the giveaway started were eligible to win
    :type only_new_members: :obj:`bool`

    :param was_refunded: Optional. True, if the giveaway was canceled because the payment for it was refunded
    :type was_refunded: :obj:`bool`

    :param prize_description: Optional. Description of additional giveaway prize
    :type prize_description: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`GiveawayWinners`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        giveaway_message_id: "int" = None,
        winners_selection_date: "int" = None,
        winner_count: "int" = None,
        winners: List["tgram.types.User"] = None,
        additional_chat_count: "int" = None,
        premium_subscription_month_count: "int" = None,
        unclaimed_prize_count: "int" = None,
        only_new_members: "bool" = None,
        was_refunded: "bool" = None,
        prize_description: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.giveaway_message_id = giveaway_message_id
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.winners = winners
        self.additional_chat_count = additional_chat_count
        self.premium_subscription_month_count = premium_subscription_month_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.only_new_members = only_new_members
        self.was_refunded = was_refunded
        self.prize_description = prize_description

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.GiveawayWinners"]:
        return (
            GiveawayWinners(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                giveaway_message_id=d.get("giveaway_message_id"),
                winners_selection_date=d.get("winners_selection_date"),
                winner_count=d.get("winner_count"),
                winners=[tgram.types.User._parse(me=me, d=i) for i in d.get("winners")]
                if d.get("winners")
                else None,
                additional_chat_count=d.get("additional_chat_count"),
                premium_subscription_month_count=d.get(
                    "premium_subscription_month_count"
                ),
                unclaimed_prize_count=d.get("unclaimed_prize_count"),
                only_new_members=d.get("only_new_members"),
                was_refunded=d.get("was_refunded"),
                prize_description=d.get("prize_description"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
