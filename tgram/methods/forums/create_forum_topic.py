import tgram
from typing import Union
from tgram.types import ForumTopic


class CreateForumTopic:
    async def create_forum_topic(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        name: str,
        icon_color: int = None,
        icon_custom_emoji_id: str = None,
    ) -> ForumTopic:
        """
        Use this method to create a topic in a forum supergroup chat. The bot must be an administrator
        in the chat for this to work and must have the can_manage_topics administrator rights.
        Returns information about the created topic as a ForumTopic object.

        Telegram documentation: https://core.telegram.org/bots/api#createforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param name: Name of the topic, 1-128 characters
        :type name: :obj:`str`

        :param icon_color: Color of the topic icon in RGB format. Currently, must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F
        :type icon_color: :obj:`int`

        :param icon_custom_emoji_id: Custom emoji for the topic icon. Must be an emoji of type “tgs” and must be exactly 1 character long
        :type icon_custom_emoji_id: :obj:`str`

        :return: On success, information about the created topic is returned as a ForumTopic object.
        :rtype: :class:`tgram.types.ForumTopic`
        """

        result = await self(
            "createForumTopic",
            chat_id=chat_id,
            name=name,
            icon_color=icon_color,
            icon_custom_emoji_id=icon_custom_emoji_id,
        )
        return ForumTopic._parse(me=self, d=result["result"])
