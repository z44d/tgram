from typing import Optional

import tgram

from .type_ import Type_


class KeyboardButtonRequestManagedBot(Type_):
    """
    This object defines the criteria used to request a suitable managed bot. The identifier of the selected managed bot will be shared with the bot when the button is pressed.

    Telegram Documentation: https://core.telegram.org/bots/api#keyboardbuttonrequestmanagedbot

    :param managed_bot_username: Optional. The username of the managed bot to request. If not specified, the user can select any managed bot.
    :type managed_bot_username: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.KeyboardButtonRequestManagedBot`
    """

    def __init__(
        self,
        managed_bot_username: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.managed_bot_username = managed_bot_username

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.KeyboardButtonRequestManagedBot"]:
        return (
            KeyboardButtonRequestManagedBot(
                me=me,
                json=d,
                managed_bot_username=d.get("managed_bot_username"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
