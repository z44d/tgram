import tgram

from typing import Optional


class PreCheckoutQueryB:
    async def answer(
        self: "tgram.types.PreCheckoutQuery",
        ok: "bool" = True,
        error_message: "str" = None,
    ) -> bool:
        return await self._me.answer_pre_checkout_query(
            pre_checkout_query_id=self.id, ok=ok, error_message=error_message
        )

    @property
    def user(self: "tgram.types.PreCheckoutQuery") -> Optional["tgram.types.User"]:
        return self.from_user

    sender_user = user
