import tgram
from .type_ import Type_
from typing import Optional


class DirectMessagesTopic(Type_):
    """
    Describes a topic of a direct messages chat.

    Telegram Documentation: https://core.telegram.org/bots/api#directmessagestopic

    :param topic_id: Unique identifier of the topic. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type topic_id: :obj:`int`

    :param user: Optional. Information about the user that created the topic. Currently, it is always present.
    :type user: :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.DirectMessagesTopic`
    """

    def __init__(
        self,
        topic_id: "int" = None,
        user: "tgram.types.User" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.topic_id = topic_id
        self.user = user

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.DirectMessagesTopic"]:
        return (
            DirectMessagesTopic(
                me=me,
                json=d,
                topic_id=d.get("topic_id"),
                user=tgram.types.User._parse(me=me, d=d.get("user"))
                if d.get("user")
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
