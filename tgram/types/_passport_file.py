from typing import Optional

import tgram

from .type_ import Type_


class PassportFile(Type_):
    def __init__(
        self,
        file_id: "str | None" = None,
        file_unique_id: "str | None" = None,
        file_size: "int | None" = None,
        file_date: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.PassportFile"]:
        return (
            PassportFile(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                file_size=d.get("file_size"),
                file_date=d.get("file_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
