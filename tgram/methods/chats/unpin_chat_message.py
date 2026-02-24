import tgram
from typing import Union


class UnpinChatMessage:
    async def unpin_chat_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int = None,
        business_connection_id: str = None,
    ) -> bool:
        """
        Use this method to unpin specific pinned message in a supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unpinchatmessage

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Int: Identifier of a message to unpin
        :type message_id: :obj:`int`

        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be pinned
        :type business_connection_id: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "unpinChatMessage",
            chat_id=chat_id,
            message_id=message_id,
            business_connection_id=business_connection_id,
        )
        return result.get("result", {})
