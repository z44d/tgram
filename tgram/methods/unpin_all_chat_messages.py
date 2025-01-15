import tgram
from typing import Union


class UnpinAllChatMessages:
    async def unpin_all_chat_messages(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to unpin a all pinned messages in a supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unpinallchatmessages

        :param chat_id: Int or Str: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "unpinAllChatMessages",
            chat_id=chat_id,
        )
        return result["result"]
