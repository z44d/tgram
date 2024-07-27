import tgram
from .type_ import Type_

from typing import Optional


class MessageOriginHiddenUser(Type_):
    """
    The message was originally sent by an unknown user.

    :param sender_user_name: Name of the user that sent the message originally
    :type sender_user_name: :obj:`str`
    """

    def __init__(
        self,
        type: "str" = None,
        date: "int" = None,
        sender_user_name: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.date = date
        self.sender_user_name = sender_user_name

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MessageOriginHiddenUser"]:
        return (
            MessageOriginHiddenUser(
                me=me,
                json=d,
                type=d.get("type"),
                date=d.get("date"),
                sender_user_name=d.get("sender_user_name"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
