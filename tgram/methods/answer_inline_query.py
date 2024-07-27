import tgram
from typing import List
from tgram.types import InlineQueryResult
from tgram.types import InlineQueryResultsButton


class AnswerInlineQuery:
    async def answer_inline_query(
        self: "tgram.TgBot",
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        button: InlineQueryResultsButton = None,
    ) -> bool:
        """
        Use this method to send answers to an inline query. On success, True is returned.
        No more than 50 results per query are allowed.

        Telegram documentation: https://core.telegram.org/bots/api#answerinlinequery

        :param inline_query_id: Unique identifier for the answered query
        :type inline_query_id: :obj:`str`

        :param results: Array of results for the inline query
        :type results: :obj:`list` of :obj:`tgram.types.InlineQueryResult`

        :param cache_time: The maximum amount of time in seconds that the result of the inline query
            may be cached on the server.
        :type cache_time: :obj:`int`

        :param is_personal: Pass True, if results may be cached on the server side only for
            the user that sent the query.
        :type is_personal: :obj:`bool`

        :param next_offset: Pass the offset that a client should send in the next query with the same text
            to receive more results.
        :type next_offset: :obj:`str`

        :param switch_pm_parameter: Deep-linking parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters,
            only A-Z, a-z, 0-9, _ and - are allowed.
            Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly.
            To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a
            private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline
            button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.
        :type switch_pm_parameter: :obj:`str`

        :param switch_pm_text: Parameter for the start message sent to the bot when user presses the switch button
        :type switch_pm_text: :obj:`str`

        :param button: A JSON-serialized object describing a button to be shown above inline query results
        :type button: :obj:`tgram.types.InlineQueryResultsButton`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "answerInlineQuery",
            inline_query_id=inline_query_id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            button=button,
        )
        return result["result"]
