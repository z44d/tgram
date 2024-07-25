import tgram
from .type_ import Type_

from typing import Optional


class MessageAutoDeleteTimerChanged(Type_):
    """
    This object represents a service message about a change in auto-delete timer settings.

    Telegram Documentation: https://core.telegram.org/bots/api#messageautodeletetimerchanged

    :param message_auto_delete_time: New auto-delete time for messages in the chat; in seconds
    :type message_auto_delete_time: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.MessageAutoDeleteTimerChanged`
    """

    def __init__(
        self,
        message_auto_delete_time: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_auto_delete_time = message_auto_delete_time

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MessageAutoDeleteTimerChanged"]:
        return (
            MessageAutoDeleteTimerChanged(
                me=me,
                json=d,
                message_auto_delete_time=d.get("message_auto_delete_time"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
