import tgram
from typing import Union


class UnpinAllGeneralForumTopicMessages:
    async def unpin_all_general_forum_topic_messages(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a General forum topic.
        The bot must be an administrator in the chat for this to work and must have the
        can_pin_messages administrator right in the supergroup.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unpinAllGeneralForumTopicMessages

        :param chat_id: Unique identifier for the target chat or username of chat
        :type chat_id: :obj:`int` | :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self(
            "unpinAllGeneralForumTopicMessages",
            chat_id=chat_id,
        )
        return result.get("result", {})
