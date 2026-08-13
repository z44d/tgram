from typing import Optional

import tgram

from .type_ import Type_


class BotAccessSettings(Type_):
    """
    This object describes the access settings of a bot.

    Telegram Documentation: https://core.telegram.org/bots/api#botaccesssettings

    :param is_access_restricted: True, if only selected users can access the bot. The bot's owner can always access it.
    :type is_access_restricted: :obj:`bool`

    :param added_users: Optional. The list of other users who have access to the bot if the access is restricted.
    :type added_users: :obj:`list` of :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotAccessSettings`
    """

    def __init__(
        self,
        is_access_restricted: "bool | None" = None,
        added_users: list["tgram.types.User"] | None = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.is_access_restricted = is_access_restricted
        self.added_users = added_users

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.BotAccessSettings"]:
        return (
            BotAccessSettings(
                me=me,
                json=d,
                is_access_restricted=d.get("is_access_restricted"),
                added_users=[
                    tgram.types.User._parse(me=me, d=i) for i in d.get("added_users")
                ]
                if d.get("added_users")
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
