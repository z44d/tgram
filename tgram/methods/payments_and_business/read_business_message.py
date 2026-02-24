import tgram


class ReadBusinessMessage:
    async def read_business_message(
        self: "tgram.TgBot",
        business_connection_id: str,
        chat_id: int,
        message_id: int,
    ) -> bool:
        """
        Marks an incoming message as read on behalf of a business account.
        Requires the can_read_messages business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#readbusinessmessage

        :param business_connection_id: Unique identifier of the business connection on behalf of which to read the message
        :type business_connection_id: :obj:`str`

        :param chat_id: Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours.
        :type chat_id: :obj:`int`

        :param message_id: Unique identifier of the message to mark as read
        :type message_id: :obj:`int`

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """

        result = await self(
            "readBusinessMessage",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
        )
        return result.get("result", {})
