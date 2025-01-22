import tgram
from tgram.types import StickerSet


class GetStickerSet:
    async def get_sticker_set(self: "tgram.TgBot", name: str) -> StickerSet:
        """
        Use this method to get a sticker set. On success, a StickerSet object is returned.

        Telegram documentation: https://core.telegram.org/bots/api#getstickerset

        :param name: Sticker set name
        :type name: :obj:`str`

        :return: On success, a StickerSet object is returned.
        :rtype: :class:`tgram.types.StickerSet`
        """

        result = await self(
            "getStickerSet",
            name=name,
        )
        return StickerSet._parse(me=self, d=result["result"])
