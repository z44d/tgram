import tgram
from .type_ import Type_

from typing import Optional


class PollOptionAdded(Type_):
    """
    This object represents a service message about a new poll option added to a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#polloptionadded

    :param poll_option: The poll option that was added.
    :type poll_option: :class:`tgram.types.PollOption`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollOptionAdded`
    """

    def __init__(
        self,
        poll_option: "tgram.types.PollOption" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.poll_option = poll_option

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PollOptionAdded"]:
        return (
            PollOptionAdded(
                me=me,
                json=d,
                poll_option=tgram.types.PollOption._parse(
                    me=me, d=d.get("poll_option")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
