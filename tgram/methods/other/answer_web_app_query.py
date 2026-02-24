import tgram
from tgram.types import InlineQueryResult
from tgram.types import SentWebAppMessage


class AnswerWebAppQuery:
    async def answer_web_app_query(
        self: "tgram.TgBot", web_app_query_id: str, result: InlineQueryResult
    ) -> SentWebAppMessage:
        """
        Use this method to set the result of an interaction with a Web App and
        send a corresponding message on behalf of the user to the chat from which
        the query originated.
        On success, a SentWebAppMessage object is returned.

        Telegram Documentation: https://core.telegram.org/bots/api#answerwebappquery

        :param web_app_query_id: Unique identifier for the query to be answered
        :type web_app_query_id: :obj:`str`

        :param result: A JSON-serialized object describing the message to be sent
        :type result: :class:`tgram.types.InlineQueryResultBase`

        :return: On success, a SentWebAppMessage object is returned.
        :rtype: :class:`tgram.types.SentWebAppMessage`
        """

        result = await self(
            "answerWebAppQuery",
            web_app_query_id=web_app_query_id,
            result=result,
        )
        return SentWebAppMessage._parse(me=self, d=result.get("result", {}))
