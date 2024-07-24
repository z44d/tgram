import tgram
from typing import Union


class EditForumTopic:
    async def edit_forum_topic(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_thread_id: int,
        name: str = None,
        icon_custom_emoji_id: str = None,
    ) -> bool:
        """
        Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an
        administrator in the chat for this to work and must have can_manage_topics administrator rights,
        unless it is the creator of the topic. Returns True on success.

        Telegram Documentation: https://core.telegram.org/bots/api#editforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_thread_id: Identifier of the topic to edit
        :type message_thread_id: :obj:`int`

        :param name: Optional, New name of the topic, 1-128 characters. If not specififed or empty,
            the current name of the topic will be kept
        :type name: :obj:`str`

        :param icon_custom_emoji_id: Optional, New unique identifier of the custom emoji shown as the topic icon.
            Use getForumTopicIconStickers to get all allowed custom emoji identifiers. Pass an empty string to remove the
            icon. If not specified, the current icon will be kept
        :type icon_custom_emoji_id: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "editForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
            name=name,
            icon_custom_emoji_id=icon_custom_emoji_id,
        )
        return result["result"]
