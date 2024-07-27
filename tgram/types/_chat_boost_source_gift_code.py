import tgram
from .type_ import Type_

from typing import Optional


class ChatBoostSourceGiftCode(Type_):
    """
    The boost was obtained by the creation of Telegram Premium gift codes to boost a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostsourcegiftcode

    :param source: Source of the boost, always “gift_code”
    :type source: :obj:`str`

    :param user: User for which the gift code was created
    :type user: :class:`User`

    :return: Instance of the class
    :rtype: :class:`ChatBoostSourceGiftCode`
    """

    def __init__(
        self,
        source: "str" = None,
        user: "tgram.types.User" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.user = user

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatBoostSourceGiftCode"]:
        return (
            ChatBoostSourceGiftCode(
                me=me,
                json=d,
                source=d.get("source"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
