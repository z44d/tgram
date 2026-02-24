import tgram
from typing import Union


class EditGeneralForumTopic:
    async def edit_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], name: str
    ) -> bool:
        """
        Use this method to edit the name of the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#editgeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param name: New topic name, 1-128 characters
        :type name: :obj:`str`
        """

        result = await self(
            "editGeneralForumTopic",
            chat_id=chat_id,
            name=name,
        )
        return result.get("result", {})
