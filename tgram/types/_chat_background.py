import tgram
from .type_ import Type_

from typing import Optional


class ChatBackground(Type_):
    """
    This object represents a chat background.

    Telegram documentation: https://core.telegram.org/bots/api#chatbackground

    :param type: Type of the background
    :type type: :class:`BackgroundType`

    :return: Instance of the class
    :rtype: :class:`ChatBackground`
    """

    def __init__(
        self,
        type: "tgram.types.BackgroundType" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatBackground"]:
        return (
            ChatBackground(
                me=me,
                json=d,
                type=tgram.types.BackgroundType._parse(me=me, d=d.get("type")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
