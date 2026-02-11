import tgram
from .type_ import Type_

from typing import Optional


class ChatOwnerChanged(Type_):
    """
    This object represents a service message about the new owner of a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chatownerchanged

    :param new_owner: The new owner of the chat
    :type new_owner: :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatOwnerChanged`
    """

    def __init__(
        self,
        new_owner: "tgram.types.User" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.new_owner = new_owner

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatOwnerChanged"]:
        return (
            ChatOwnerChanged(
                me=me,
                json=d,
                new_owner=tgram.types.User._parse(me=me, d=d.get("new_owner")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
