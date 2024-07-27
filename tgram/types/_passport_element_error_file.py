import tgram
from .type_ import Type_

from typing import Optional


class PassportElementErrorFile(Type_):
    def __init__(
        self,
        source: "str" = None,
        type: "str" = None,
        file_hash: "str" = None,
        message: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PassportElementErrorFile"]:
        return (
            PassportElementErrorFile(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
