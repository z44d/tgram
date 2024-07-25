import tgram
from .type_ import Type_

from typing import Optional


class VideoChatEnded(Type_):
    """
    This object represents a service message about a video chat ended in the chat.

    Telegram Documentation: https://core.telegram.org/bots/api#videochatended

    :param duration: Video chat duration in seconds
    :type duration: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoChatEnded`
    """

    def __init__(
        self, duration: "int" = None, me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.duration = duration

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.VideoChatEnded"]:
        return (
            VideoChatEnded(me=me, json=d, duration=d.get("duration"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
