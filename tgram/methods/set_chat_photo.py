import tgram
from typing import Union
from pathlib import Path


class SetChatPhoto:
    async def set_chat_photo(
        self: "tgram.TgBot", chat_id: Union[int, str], photo: Union[Path, bytes, str]
    ) -> bool:
        """
        Use this method to set a new profile photo for the chat. Photos can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.
        Note: In regular groups (non-supergroups), this method will only work if the ‘All Members Are Admins’
        setting is off in the target group.

        Telegram documentation: https://core.telegram.org/bots/api#setchatphoto

        :param chat_id: Int or Str: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param photo: InputFile: New chat photo, uploaded using multipart/form-data
        :type photo: :obj:`typing.Union[file_like, str]`
        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setChatPhoto",
            chat_id=chat_id,
            photo=photo,
        )
        return result["result"]
