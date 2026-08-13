from typing import Optional

import tgram

from .type_ import Type_


class ChatOwnerLeft(Type_):
    """
    This object represents a service message about the current owner of a chat that left.

    Telegram Documentation: https://core.telegram.org/bots/api#chatownerleft

    :param new_owner: Optional. The user which will be the new owner of the chat if the previous owner
        does not return to the chat.
    :type new_owner: :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatOwnerLeft`
    """

    def __init__(
        self,
        new_owner: "tgram.types.User" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.new_owner = new_owner

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.ChatOwnerLeft"]:
        return (
            ChatOwnerLeft(
                me=me,
                json=d,
                new_owner=tgram.types.User._parse(me=me, d=d.get("new_owner"))
                if d.get("new_owner")
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
