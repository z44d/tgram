from typing import Optional

import tgram

from .type_ import Type_


class ManagedBotCreated(Type_):
    """
    This object represents a service message about the creation of a managed bot by a user.

    Telegram Documentation: https://core.telegram.org/bots/api#managedbotcreated

    :param managed_bot: The user that was created as a managed bot.
    :type managed_bot: :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ManagedBotCreated`
    """

    def __init__(
        self,
        managed_bot: "tgram.types.User" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.managed_bot = managed_bot

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.ManagedBotCreated"]:
        return (
            ManagedBotCreated(
                me=me,
                json=d,
                managed_bot=tgram.types.User._parse(me=me, d=d.get("managed_bot"))
                if d.get("managed_bot")
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
