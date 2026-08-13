from typing import Optional

import tgram

from .type_ import Type_


class Dice(Type_):
    """
    This object represents an animated emoji that displays a random value.

    Telegram Documentation: https://core.telegram.org/bots/api#dice

    :param emoji: Emoji on which the dice throw animation is based
    :type emoji: :obj:`str`

    :param value: Value of the dice, 1-6 for “🎲”, “🎯” and “🎳” base emoji, 1-5 for “🏀” and “⚽” base emoji, 1-64 for “🎰” base emoji
    :type value: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Dice`
    """

    def __init__(
        self,
        emoji: "str | None" = None,
        value: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.emoji = emoji
        self.value = value

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.Dice"]:
        return (
            Dice(me=me, json=d, emoji=d.get("emoji"), value=d.get("value"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
