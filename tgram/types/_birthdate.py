import tgram
from .type_ import Type_

from typing import Optional


class Birthdate(Type_):
    """
    This object represents a user's birthdate.

    Telegram documentation: https://core.telegram.org/bots/api#birthdate

    :param day: Day of the user's birth; 1-31
    :type day: :obj:`int`

    :param month: Month of the user's birth; 1-12
    :type month: :obj:`int`

    :param year: Optional. Year of the user's birth
    :type year: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`Birthdate`
    """

    def __init__(
        self,
        day: "int" = None,
        month: "int" = None,
        year: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Birthdate"]:
        return (
            Birthdate(
                me=me,
                json=d,
                day=d.get("day"),
                month=d.get("month"),
                year=d.get("year"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
