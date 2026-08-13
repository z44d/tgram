from typing import Optional

import tgram

from .type_ import Type_


class CommunityChatAdded(Type_):
    def __init__(
        self,
        community: "tgram.types.Community" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.community = community

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.CommunityChatAdded"]:
        return (
            CommunityChatAdded(
                me=me,
                json=d,
                community=tgram.types.Community._parse(me=me, d=d.get("community")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
