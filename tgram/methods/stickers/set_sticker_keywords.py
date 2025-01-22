import tgram
from typing import List


class SetStickerKeywords:
    async def set_sticker_keywords(
        self: "tgram.TgBot", sticker: str, keywords: List[str] = None
    ) -> bool:
        """
        Use this method to change search keywords assigned to a regular or custom emoji sticker.
        The sticker must belong to a sticker set created by the bot.
        Returns True on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`

        :param keywords: A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters
        :type keywords: :obj:`list` of :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setStickerKeywords",
            sticker=sticker,
            keywords=keywords,
        )
        return result["result"]
