import tgram
from typing import Union


class CloseGeneralForumTopic:
    async def close_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to close the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#closegeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`
        """

        result = await self._send_request(
            "closeGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]
