import tgram
from .type_ import Type_

from typing import List, Optional


class PassportData(Type_):
    def __init__(
        self,
        data: List["tgram.types.EncryptedPassportElement"] = None,
        credentials: "tgram.types.EncryptedCredentials" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.data = data
        self.credentials = credentials

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PassportData"]:
        return (
            PassportData(
                me=me,
                json=d,
                data=[
                    tgram.types.EncryptedPassportElement._parse(me=me, d=i)
                    for i in d.get("data")
                ]
                if d.get("data")
                else None,
                credentials=tgram.types.EncryptedCredentials._parse(
                    me=me, d=d.get("credentials")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
