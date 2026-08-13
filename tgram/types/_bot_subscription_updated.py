from typing import Optional

import tgram

from .type_ import Type_


class BotSubscriptionUpdated(Type_):
    def __init__(
        self,
        user: "tgram.types.User" = None,
        chat: "tgram.types.Chat" = None,
        subscription_period: "int | None" = None,
        total_count: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.user = user
        self.chat = chat
        self.subscription_period = subscription_period
        self.total_count = total_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.BotSubscriptionUpdated"]:
        return (
            BotSubscriptionUpdated(
                me=me,
                json=d,
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                subscription_period=d.get("subscription_period"),
                total_count=d.get("total_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
