import tgram
from typing import List


class SetStickerEmojiList:
    async def set_sticker_emoji_list(
        self: "tgram.TgBot", sticker: str, emoji_list: List[str]
    ) -> bool:
        """
        Use this method to set the emoji list of a sticker set.
        Returns True on success.

        :param name: Sticker set name
        :type name: :obj:`str`

        :param emoji_list: List of emojis
        :type emoji_list: :obj:`list` of :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setStickerEmojiList",
            sticker=sticker,
            emoji_list=emoji_list,
        )
        return result.get("result", {})
