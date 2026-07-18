import tgram
from .type_ import Type_

from typing import List, Optional


class Community(Type_):
    def __init__(
        self,
        id: "str" = None,
        title: "str" = None,
        description: "str" = None,
        photo: "tgram.types.ChatPhoto" = None,
        member_count: "int" = None,
        linked_chat_ids: List["int"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.title = title
        self.description = description
        self.photo = photo
        self.member_count = member_count
        self.linked_chat_ids = linked_chat_ids

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Community"]:
        return (
            Community(
                me=me,
                json=d,
                id=d.get("id"),
                title=d.get("title"),
                description=d.get("description"),
                photo=tgram.types.ChatPhoto._parse(me=me, d=d.get("photo")),
                member_count=d.get("member_count"),
                linked_chat_ids=d.get("linked_chat_ids"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
