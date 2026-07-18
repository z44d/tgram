import tgram
from tgram.types import InlineQueryResult
from tgram.types import SentGuestMessage


class AnswerGuestQuery:
    async def answer_guest_query(
        self: "tgram.TgBot",
        guest_query_id: str,
        result: InlineQueryResult,
    ) -> SentGuestMessage:
        """
        Use this method to reply to a received guest message.
        On success, a SentGuestMessage object is returned.

        Telegram Documentation: https://core.telegram.org/bots/api#answerguestquery

        :param guest_query_id: Unique identifier for the query to be answered
        :type guest_query_id: :obj:`str`

        :param result: A JSON-serialized object describing the message to be sent
        :type result: :class:`tgram.types.InlineQueryResult`

        :return: On success, a SentGuestMessage object is returned.
        :rtype: :class:`tgram.types.SentGuestMessage`
        """

        result = await self(
            "answerGuestQuery",
            guest_query_id=guest_query_id,
            result=result,
        )
        return SentGuestMessage._parse(me=self, d=result.get("result", {}))
