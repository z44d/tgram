import tgram
from .type_ import Type_

from typing import Optional


class ReactionCount(Type_):
    """
    This object represents a reaction added to a message along with the number of times it was added.

    Telegram documentation: https://core.telegram.org/bots/api#reactioncount

    :param type: Type of the reaction
    :type type: :class:`ReactionType`

    :param total_count: Number of times the reaction was added
    :type total_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`ReactionCount`
    """

    def __init__(
        self,
        type: "tgram.types.ReactionType" = None,
        total_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.total_count = total_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ReactionCount"]:
        return (
            ReactionCount(
                me=me,
                json=d,
                type=(
                    tgram.types.ReactionTypeCustomEmoji._parse(me, d.get("type"))
                    if d["type"]["type"] == "custom_emoji"
                    else tgram.types.ReactionTypeEmoji._parse(me, d.get("type"))
                    if d["type"]["type"] == "emoji"
                    else tgram.types.ReactionTypePaid._parse(me, d.get("type"))
                )
                if d.get("type")
                else None,
                total_count=d.get("total_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
