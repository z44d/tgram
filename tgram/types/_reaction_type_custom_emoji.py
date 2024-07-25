import tgram
from .type_ import Type_

from typing import Optional


class ReactionTypeCustomEmoji(Type_):
    """
    This object represents a custom emoji reaction type.

    Telegram documentation: https://core.telegram.org/bots/api#reactiontypecustomemoji

    :param type: Type of the reaction, must be custom_emoji
    :type type: :obj:`str`

    :param custom_emoji_id: Identifier of the custom emoji
    :type custom_emoji_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`ReactionTypeCustomEmoji`
    """

    def __init__(
        self,
        type: "str" = None,
        custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ReactionTypeCustomEmoji"]:
        return (
            ReactionTypeCustomEmoji(
                me=me,
                json=d,
                type=d.get("type"),
                custom_emoji_id=d.get("custom_emoji_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
