import tgram
from typing import Union


class DeleteForumTopic:
    async def delete_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """
        Use this method to delete a topic in a forum supergroup chat. The bot must be an administrator in the chat for this
        to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True
        on success.

        Telegram documentation: https://core.telegram.org/bots/api#deleteforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_thread_id: Identifier of the topic to delete
        :type message_thread_id: :obj:`int`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]
