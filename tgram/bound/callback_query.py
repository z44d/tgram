import tgram


class CallbackB:
    async def answer(
        self: "tgram.types.CallbackQuery",
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> bool:
        return await self._me.answer_callback_query(
            self.id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )
