import tgram
from .type_ import Type_

from typing import Optional


class ChatBoostSourcePremium(Type_):
    """
    The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostsourcepremium

    :param source: Source of the boost, always “premium”
    :type source: :obj:`str`

    :param user: User that boosted the chat
    :type user: :class:`User`

    :return: Instance of the class
    :rtype: :class:`ChatBoostSourcePremium`
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
    ) -> Optional["tgram.types.ChatBoostSourcePremium"]:
        return (
            ChatBoostSourcePremium(
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
