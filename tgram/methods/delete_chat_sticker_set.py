import tgram
from typing import Union


class DeleteChatStickerSet:
    async def delete_chat_sticker_set(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat
        for this to work and must have the appropriate admin rights. Use the field can_set_sticker_set
        optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletechatstickerset

        :param chat_id:	Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteChatStickerSet",
            chat_id=chat_id,
        )
        return result["result"]
