from typing import Optional

import tgram

from .type_ import Type_


class PollOptionDeleted(Type_):
    """
    This object represents a service message about a poll option deleted from a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#polloptiondeleted

    :param persistent_id: The persistent identifier of the deleted poll option.
    :type persistent_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollOptionDeleted`
    """

    def __init__(
        self,
        persistent_id: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.persistent_id = persistent_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.PollOptionDeleted"]:
        return (
            PollOptionDeleted(
                me=me,
                json=d,
                persistent_id=d.get("persistent_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
