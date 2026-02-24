import tgram
from typing import Union


class ReopenGeneralForumTopic:
    async def reopen_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to reopen the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#reopengeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`
        """

        result = await self(
            "reopenGeneralForumTopic",
            chat_id=chat_id,
        )
        return result.get("result", {})
