import tgram
from .type_ import Type_

from typing import List, Optional


class UserChatBoosts(Type_):
    """
    This object represents a list of boosts added to a chat by a user.

    Telegram documentation: https://core.telegram.org/bots/api#userchatboosts

    :param boosts: The list of boosts added to the chat by the user
    :type boosts: :obj:`list` of :class:`ChatBoost`

    :return: Instance of the class
    :rtype: :class:`UserChatBoosts`
    """

    def __init__(
        self,
        boosts: List["tgram.types.ChatBoost"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.boosts = boosts

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.UserChatBoosts"]:
        return (
            UserChatBoosts(
                me=me,
                json=d,
                boosts=[
                    tgram.types.ChatBoost._parse(me=me, d=i) for i in d.get("boosts")
                ]
                if d.get("boosts")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
