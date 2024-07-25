import tgram
from .type_ import Type_

from typing import Optional


class VideoChatScheduled(Type_):
    """
    This object represents a service message about a video chat scheduled in the chat.

    Telegram Documentation: https://core.telegram.org/bots/api#videochatscheduled

    :param start_date: Point in time (Unix timestamp) when the video chat is supposed to be started by a chat
        administrator
    :type start_date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoChatScheduled`
    """

    def __init__(
        self,
        start_date: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.start_date = start_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.VideoChatScheduled"]:
        return (
            VideoChatScheduled(me=me, json=d, start_date=d.get("start_date"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
