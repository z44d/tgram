import tgram


class AnswerCallbackQuery:
    async def answer_callback_query(
        self: "tgram.TgBot",
        callback_query_id: str,
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> bool:
        """
        Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to
        the user as a notification at the top of the chat screen or as an alert.

        Telegram documentation: https://core.telegram.org/bots/api#answercallbackquery

        :param callback_query_id: Unique identifier for the query to be answered
        :type callback_query_id: :obj:`int`

        :param text: Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
        :type text: :obj:`str`

        :param show_alert: If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
        :type show_alert: :obj:`bool`

        :param url: URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your
            game - note that this will only work if the query comes from a callback_game button.
        :type url: :obj:`str`

        :param cache_time: The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching
            starting in version 3.14. Defaults to 0.

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self(
            "answerCallbackQuery",
            callback_query_id=callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )
        return result["result"]
