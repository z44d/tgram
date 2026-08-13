from typing import Optional

import tgram

from .type_ import Type_


class PassportElementErrorUnspecified(Type_):
    def __init__(
        self,
        source: "str | None" = None,
        type: "str | None" = None,
        element_hash: "str | None" = None,
        message: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.PassportElementErrorUnspecified"]:
        return (
            PassportElementErrorUnspecified(
                me=me,
                json=d,
                source=d.get("source"),
                type=d.get("type"),
                element_hash=d.get("element_hash"),
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
