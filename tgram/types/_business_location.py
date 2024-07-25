import tgram
from .type_ import Type_

from typing import Optional


class BusinessLocation(Type_):
    """
    This object represents a business location.

    Telegram documentation: https://core.telegram.org/bots/api#businesslocation

    :param address: Address of the business
    :type address: :obj:`str`

    :param location: Optional. Location of the business
    :type location: :class:`Location`

    :return: Instance of the class
    :rtype: :class:`BusinessLocation`
    """

    def __init__(
        self,
        address: "str" = None,
        location: "tgram.types.Location" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.address = address
        self.location = location

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BusinessLocation"]:
        return (
            BusinessLocation(
                me=me,
                json=d,
                address=d.get("address"),
                location=tgram.types.Location._parse(me=me, d=d.get("location")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
