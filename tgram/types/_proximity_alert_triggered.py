import tgram
from .type_ import Type_

from typing import Optional


class ProximityAlertTriggered(Type_):
    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    Telegram Documentation: https://core.telegram.org/bots/api#proximityalerttriggered

    :param traveler: User that triggered the alert
    :type traveler: :class:`tgram.types.User`

    :param watcher: User that set the alert
    :type watcher: :class:`tgram.types.User`

    :param distance: The distance between the users
    :type distance: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ProximityAlertTriggered`
    """

    def __init__(
        self,
        traveler: "tgram.types.User" = None,
        watcher: "tgram.types.User" = None,
        distance: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ProximityAlertTriggered"]:
        return (
            ProximityAlertTriggered(
                me=me,
                json=d,
                traveler=tgram.types.User._parse(me=me, d=d.get("traveler")),
                watcher=tgram.types.User._parse(me=me, d=d.get("watcher")),
                distance=d.get("distance"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
