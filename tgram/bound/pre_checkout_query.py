import tgram


class PreCheckoutQueryB:
    async def answer(
        self: "tgram.types.PreCheckoutQuery",
        ok: "bool" = True,
        error_message: "str" = None,
    ) -> bool:
        return await self._me.answer_pre_checkout_query(
            pre_checkout_query_id=self.id, ok=ok, error_message=error_message
        )
