import tgram
from typing import Union


class LeaveChat:
    async def leave_chat(self: "tgram.TgBot", chat_id: Union[int, str]) -> bool:
        """
        Use this method for your bot to leave a group, supergroup or channel. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#leavechat

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: :obj:`bool`
        """

        result = await self(
            "leaveChat",
            chat_id=chat_id,
        )
        return result["result"]
