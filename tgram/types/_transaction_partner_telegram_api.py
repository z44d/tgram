import tgram
from .type_ import Type_

from typing import Optional


class TransactionPartnerTelegramApi(Type_):
    def __init__(
        self, request_count: int, me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = "telegram_api"
        self.request_count = request_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.TransactionPartnerTelegramApi"]:
        return (
            TransactionPartnerTelegramApi(
                me=me, json=d, request_count=d.get("request_count")
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
