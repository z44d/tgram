import tgram
from typing import Union


class UnpinAllForumTopicMessages:
    async def unpin_all_forum_topic_messages(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the
        chat for this to work and must have the can_pin_messages administrator right in the supergroup.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unpinallforumtopicmessages

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_thread_id: Identifier of the topic
        :type message_thread_id: :obj:`int`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self(
            "unpinAllForumTopicMessages",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]
