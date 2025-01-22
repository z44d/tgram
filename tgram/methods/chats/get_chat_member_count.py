import tgram
from typing import Union


class GetChatMemberCount:
    async def get_chat_member_count(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> int:
        """
        Use this method to get the number of members in a chat.

        Telegram documentation: https://core.telegram.org/bots/api#getchatmembercount

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: Number of members in the chat.
        :rtype: :obj:`int`
        """

        result = await self(
            "getChatMemberCount",
            chat_id=chat_id,
        )
        return result["result"]
