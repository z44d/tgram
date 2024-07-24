import tgram
from typing import Union


class SetChatStickerSet:
    async def set_chat_sticker_set(
        self: "tgram.TgBot", chat_id: Union[int, str], sticker_set_name: str
    ) -> bool:
        """
        Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat
        for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned
        in getChat requests to check if the bot can use this method. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setchatstickerset

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param sticker_set_name: Name of the sticker set to be set as the group sticker set
        :type sticker_set_name: :obj:`str`

        :return: StickerSet object
        :rtype: :class:`tgram.types.StickerSet`
        """

        result = await self._send_request(
            "setChatStickerSet",
            chat_id=chat_id,
            sticker_set_name=sticker_set_name,
        )
        return result["result"]
