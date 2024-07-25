import tgram
from .type_ import Type_

from typing import List, Optional


class ForumTopicReopened(Type_):
    """
    This object represents a service message about a forum topic reopened in the chat. Currently holds no information.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopicreopened
    """

    def __init__(
        self,
        user_id: "int" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["tgram.types.PhotoSize"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ForumTopicReopened"]:
        return (
            ForumTopicReopened(
                me=me,
                json=d,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
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
