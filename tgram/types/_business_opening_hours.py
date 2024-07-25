import tgram
from .type_ import Type_

from typing import List, Optional


class BusinessOpeningHours(Type_):
    """

    This object represents business opening hours.

    Telegram documentation: https://core.telegram.org/bots/api#businessopeninghours

    :param time_zone_name: Unique name of the time zone for which the opening hours are defined
    :type time_zone_name: :obj:`str`

    :param opening_hours: List of time intervals describing business opening hours
    :type opening_hours: :obj:`list` of :class:`BusinessOpeningHoursInterval`

    :return: Instance of the class

    :rtype: :class:`BusinessOpeningHours`
    """

    def __init__(
        self,
        time_zone_name: "str" = None,
        opening_hours: List["tgram.types.BusinessOpeningHoursInterval"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.time_zone_name = time_zone_name
        self.opening_hours = opening_hours

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BusinessOpeningHours"]:
        return (
            BusinessOpeningHours(
                me=me,
                json=d,
                time_zone_name=d.get("time_zone_name"),
                opening_hours=[
                    tgram.types.BusinessOpeningHoursInterval._parse(me=me, d=i)
                    for i in d.get("opening_hours")
                ]
                if d.get("opening_hours")
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
