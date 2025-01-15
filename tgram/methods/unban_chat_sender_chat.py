import tgram
from typing import Union


class UnbanChatSenderChat:
    async def unban_chat_sender_chat(
        self: "tgram.TgBot", chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """
        Use this method to unban a previously banned channel chat in a supergroup or channel.
        The bot must be an administrator for this to work and must have the appropriate
        administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unbanchatsenderchat

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param sender_chat_id: Unique identifier of the target sender chat.
        :type sender_chat_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "unbanChatSenderChat",
            chat_id=chat_id,
            sender_chat_id=sender_chat_id,
        )
        return result["result"]
