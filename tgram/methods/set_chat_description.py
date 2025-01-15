import tgram
from typing import Union


class SetChatDescription:
    async def set_chat_description(
        self: "tgram.TgBot", chat_id: Union[int, str], description: str = None
    ) -> bool:
        """
        Use this method to change the description of a supergroup or a channel.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#setchatdescription

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param description: Str: New chat description, 0-255 characters
        :type description: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setChatDescription",
            chat_id=chat_id,
            description=description,
        )
        return result["result"]
