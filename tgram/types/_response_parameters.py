import tgram
from .type_ import Type_

from typing import Optional


class ResponseParameters(Type_):
    def __init__(
        self,
        migrate_to_chat_id: "int" = None,
        retry_after: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ResponseParameters"]:
        return (
            ResponseParameters(
                me=me,
                json=d,
                migrate_to_chat_id=d.get("migrate_to_chat_id"),
                retry_after=d.get("retry_after"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
