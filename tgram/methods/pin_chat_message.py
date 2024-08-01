import tgram
from typing import Union


class PinChatMessage:
    async def pin_chat_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: bool = None,
        business_connection_id: str = None,
    ) -> bool:
        """
        Use this method to pin a message in a supergroup.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#pinchatmessage

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Identifier of a message to pin
        :type message_id: :obj:`int`

        :param disable_notification: Pass True, if it is not necessary to send a notification
            to all group members about the new pinned message
        :type disable_notification: :obj:`bool`

        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be pinned
        :type business_connection_id: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "pinChatMessage",
            chat_id=chat_id,
            message_id=message_id,
            disable_notification=disable_notification,
            business_connection_id=business_connection_id,
        )
        return result["result"]
