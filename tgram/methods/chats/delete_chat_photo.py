import tgram
from typing import Union


class DeleteChatPhoto:
    async def delete_chat_photo(self: "tgram.TgBot", chat_id: Union[int, str]) -> bool:
        """
        Use this method to delete a chat photo. Photos can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.
        Note: In regular groups (non-supergroups), this method will only work if the ‘All Members Are Admins’ setting is off in the target group.

        Telegram documentation: https://core.telegram.org/bots/api#deletechatphoto

        :param chat_id: Int or Str: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "deleteChatPhoto",
            chat_id=chat_id,
        )
        return result.get("result", {})
