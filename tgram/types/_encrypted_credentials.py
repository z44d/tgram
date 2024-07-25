import tgram
from .type_ import Type_

from typing import Optional


class EncryptedCredentials(Type_):
    def __init__(
        self,
        data: "str" = None,
        hash: "str" = None,
        secret: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.data = data
        self.hash = hash
        self.secret = secret

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.EncryptedCredentials"]:
        return (
            EncryptedCredentials(
                me=me,
                json=d,
                data=d.get("data"),
                hash=d.get("hash"),
                secret=d.get("secret"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
