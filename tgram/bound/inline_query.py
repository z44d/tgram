import tgram

from typing import List


class InlineQueryB:
    async def answer(
        self: "tgram.types.InlineQuery",
        results: List["tgram.types.InlineQueryResult"],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        button: "tgram.types.InlineQueryResultsButton" = None,
    ) -> bool:
        return await self._me.answer_inline_query(
            inline_query_id=self.id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            button=button,
        )
