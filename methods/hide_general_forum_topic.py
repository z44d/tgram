import tgram
from typing import Union


class HideGeneralForumTopic:
    async def hide_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to hide the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#hidegeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`
        """

        result = await self._send_request(
            "hideGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]
