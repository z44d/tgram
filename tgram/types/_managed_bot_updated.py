import tgram
from .type_ import Type_

from typing import Optional


class ManagedBotUpdated(Type_):
    """
    This object represents a service message about a change of a managed bot's token.

    Telegram Documentation: https://core.telegram.org/bots/api#managedbotupdated

    :param managed_bot: The user that was created as a managed bot.
    :type managed_bot: :class:`tgram.types.User`

    :param token: Optional. The new token of the managed bot.
    :type token: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ManagedBotUpdated`
    """

    def __init__(
        self,
        managed_bot: "tgram.types.User" = None,
        token: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.managed_bot = managed_bot
        self.token = token

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ManagedBotUpdated"]:
        return (
            ManagedBotUpdated(
                me=me,
                json=d,
                managed_bot=tgram.types.User._parse(me=me, d=d.get("managed_bot"))
                if d.get("managed_bot")
                else None,
                token=d.get("token"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
