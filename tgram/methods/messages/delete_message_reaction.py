import tgram


class DeleteMessageReaction:
    async def delete_message_reaction(
        self: "tgram.TgBot",
        chat_id: int | str,
        message_id: int,
    ) -> bool:
        """
        Use this method to delete a reaction from a message.
        Returns True on success.

        Telegram Documentation: https://core.telegram.org/bots/api#deletemessagereaction

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` | :obj:`str`

        :param message_id: Identifier of the message
        :type message_id: :obj:`int`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "deleteMessageReaction",
            chat_id=chat_id,
            message_id=message_id,
        )
        return result.get("result", {})
