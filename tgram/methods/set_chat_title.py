import tgram
from typing import Union


class SetChatTitle:
    async def set_chat_title(
        self: "tgram.TgBot", chat_id: Union[int, str], title: str
    ) -> bool:
        """
        Use this method to change the title of a chat. Titles can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.
        Note: In regular groups (non-supergroups), this method will only work if the ‘All Members Are Admins’
        setting is off in the target group.

        Telegram documentation: https://core.telegram.org/bots/api#setchattitle

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param title: New chat title, 1-255 characters
        :type title: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setChatTitle",
            chat_id=chat_id,
            title=title,
        )
        return result["result"]
