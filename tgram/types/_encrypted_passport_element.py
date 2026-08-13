from typing import Optional

import tgram

from .type_ import Type_


class EncryptedPassportElement(Type_):
    def __init__(
        self,
        type: "str | None" = None,
        hash: "str | None" = None,
        data: "str | None" = None,
        phone_number: "str | None" = None,
        email: "str | None" = None,
        files: list["tgram.types.PassportFile"] | None = None,
        front_side: "tgram.types.PassportFile" = None,
        reverse_side: "tgram.types.PassportFile" = None,
        selfie: "tgram.types.PassportFile" = None,
        translation: list["tgram.types.PassportFile"] | None = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.hash = hash

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.EncryptedPassportElement"]:
        return (
            EncryptedPassportElement(
                me=me,
                json=d,
                type=d.get("type"),
                hash=d.get("hash"),
                data=d.get("data"),
                phone_number=d.get("phone_number"),
                email=d.get("email"),
                files=[
                    tgram.types.PassportFile._parse(me=me, d=i) for i in d.get("files")
                ]
                if d.get("files")
                else None,
                front_side=tgram.types.PassportFile._parse(
                    me=me, d=d.get("front_side")
                ),
                reverse_side=tgram.types.PassportFile._parse(
                    me=me, d=d.get("reverse_side")
                ),
                selfie=tgram.types.PassportFile._parse(me=me, d=d.get("selfie")),
                translation=[
                    tgram.types.PassportFile._parse(me=me, d=i)
                    for i in d.get("translation")
                ]
                if d.get("translation")
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
