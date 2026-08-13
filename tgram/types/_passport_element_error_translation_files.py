from typing import Optional

import tgram

from .type_ import Type_


class PassportElementErrorTranslationFiles(Type_):
    def __init__(
        self,
        source: "str | None" = None,
        type: "str | None" = None,
        file_hashes: list["str"] | None = None,
        message: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.PassportElementErrorTranslationFiles"]:
        return (
            PassportElementErrorTranslationFiles(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                file_hashes=d.get("file_hashes"),
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
