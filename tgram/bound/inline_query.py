import tgram

from typing import List, Optional


class InlineQueryB:
    async def answer(
        self: "tgram.types.InlineQuery",
        results: List["tgram.types.InlineQueryResult"],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        button: "tgram.types.InlineQueryResultsButton" = None,
    ) -> bool:
        """
        Sends answers to an inline query.

        Parameters:
        - results (List[tgram.types.InlineQueryResult]): A list of results for the inline query.
        - cache_time (int, optional): The maximum amount of time in seconds that the result of the inline query may be cached on the server.
        - is_personal (bool, optional): Pass True if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query.
        - next_offset (str, optional): Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don’t support pagination. Offset length can’t exceed 64 bytes.
        - button (tgram.types.InlineQueryResultsButton, optional): A button to be shown above inline query results.

        Returns:
        - bool: True on success.
        """
        return await self._me.answer_inline_query(
            inline_query_id=self.id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            button=button,
        )

    @property
    def user(self: "tgram.types.InlineQuery") -> Optional["tgram.types.User"]:
        """
        Returns the user who sent the inline query.

        Returns:
        - Optional[tgram.types.User]: The user who sent the inline query.
        """
        return self.from_user

    sender_user = user
