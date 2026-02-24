import tgram
from typing import Union


class DeleteMessage:
    async def delete_message(
        self: "tgram.TgBot", chat_id: Union[int, str], message_id: int
    ) -> bool:
        """
        Use this method to delete a message, including service messages, with the following limitations:
        - A message can only be deleted if it was sent less than 48 hours ago.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted can_post_messages permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletemessage

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Identifier of the message to delete
        :type message_id: :obj:`int`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "deleteMessage",
            chat_id=chat_id,
            message_id=message_id,
        )
        return result.get("result", {})
