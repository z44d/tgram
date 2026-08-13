from typing import Optional

import tgram

from .type_ import Type_


class CommunityChatRemoved(Type_):
    def __init__(
        self,
        community_id: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.community_id = community_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.CommunityChatRemoved"]:
        return (
            CommunityChatRemoved(
                me=me,
                json=d,
                community_id=d.get("community_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
