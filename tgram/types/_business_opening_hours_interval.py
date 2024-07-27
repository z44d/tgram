import tgram
from .type_ import Type_

from typing import Optional


class BusinessOpeningHoursInterval(Type_):
    """
    This object represents a business opening hours interval.

    Telegram documentation: https://core.telegram.org/bots/api#businessopeninghoursinterval

    :param opening_minute: The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 24 60
    :type opening_minute: :obj:`int`

    :param closing_minute: The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 24 60
    :type closing_minute: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`BusinessOpeningHoursInterval`
    """

    def __init__(
        self,
        opening_minute: "int" = None,
        closing_minute: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.opening_minute = opening_minute
        self.closing_minute = closing_minute

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BusinessOpeningHoursInterval"]:
        return (
            BusinessOpeningHoursInterval(
                me=me,
                json=d,
                opening_minute=d.get("opening_minute"),
                closing_minute=d.get("closing_minute"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
