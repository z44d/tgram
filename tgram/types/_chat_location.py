import tgram
from .type_ import Type_

from typing import Optional


class ChatLocation(Type_):
    """
    Represents a location to which a chat is connected.

    Telegram Documentation: https://core.telegram.org/bots/api#chatlocation

    :param location: The location to which the supergroup is connected. Can't be a live location.
    :type location: :class:`tgram.types.Location`

    :param address: Location address; 1-64 characters, as defined by the chat owner
    :type address: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatLocation`
    """

    def __init__(
        self,
        location: "tgram.types.Location" = None,
        address: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.location = location
        self.address = address

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatLocation"]:
        return (
            ChatLocation(
                me=me,
                json=d,
                location=tgram.types.Location._parse(me=me, d=d.get("location")),
                address=d.get("address"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
