import random
from typing import Optional

import tgram

from .type_ import Type_


class InlineQueryResultGame(Type_):
    """
    Represents a Game.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultgame

    :param type: Type of the result, must be game
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 bytes
    :type id: :obj:`str`

    :param game_short_name: Short name of the game
    :type game_short_name: :obj:`str`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultGame`
    """

    def __init__(
        self,
        game_short_name: "str | None" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "game"
        self.id = random.randint(10000, 99999)
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InlineQueryResultGame"]:
        return (
            InlineQueryResultGame(
                me=me,
                json=d,
                game_short_name=d.get("game_short_name"),
                reply_markup=tgram.types.InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
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
