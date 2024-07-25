import tgram
from .type_ import Type_

from typing import Optional


class GameHighScore(Type_):
    """
    This object represents one row of the high scores table for a game.

    Telegram Documentation: https://core.telegram.org/bots/api#gamehighscore

    :param position: Position in high score table for the game
    :type position: :obj:`int`

    :param user: User
    :type user: :class:`tgram.types.User`

    :param score: Score
    :type score: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.GameHighScore`
    """

    def __init__(
        self,
        position: "int" = None,
        user: "tgram.types.User" = None,
        score: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.position = position
        self.user = user
        self.score = score

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.GameHighScore"]:
        return (
            GameHighScore(
                me=me,
                json=d,
                position=d.get("position"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                score=d.get("score"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
