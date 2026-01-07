import tgram
from .type_ import Type_

from typing import Optional


class UserRating(Type_):
    """
    This object describes the rating of a user.

    Telegram Documentation: https://core.telegram.org/bots/api#userrating

    :param trust_score: The trust score of the user, ranging from 0 to 5
    :type trust_score: :obj:`float`

    :param ratings_count: The number of ratings the user has received
    :type ratings_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.UserRating`
    """

    def __init__(
        self,
        trust_score: "float" = None,
        ratings_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.trust_score = trust_score
        self.ratings_count = ratings_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.UserRating"]:
        return (
            UserRating(
                trust_score=d.get("trust_score"),
                ratings_count=d.get("ratings_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
