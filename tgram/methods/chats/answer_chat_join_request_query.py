import tgram
from typing import Union


class AnswerChatJoinRequestQuery:
    async def answer_chat_join_request_query(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        query_id: str,
        text: str = None,
        show_alert: bool = None,
        url: str = None,
    ) -> bool:
        """
        Use this method to answer a chat join request query.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#answerchatjoinrequestquery

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param query_id: Unique identifier of the query to be answered
        :type query_id: :obj:`str`

        :param text: Optional. Text of the answer
        :type text: :obj:`str`

        :param show_alert: Optional. If True, an alert will be shown to the user
        :type show_alert: :obj:`bool`

        :param url: Optional. URL that will be opened by the user
        :type url: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "answerChatJoinRequestQuery",
            chat_id=chat_id,
            user_id=user_id,
            query_id=query_id,
            text=text,
            show_alert=show_alert,
            url=url,
        )
        return result.get("result", {})
