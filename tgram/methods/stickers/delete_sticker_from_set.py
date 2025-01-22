import tgram


class DeleteStickerFromSet:
    async def delete_sticker_from_set(self: "tgram.TgBot", sticker: str) -> bool:
        """
        Use this method to delete a sticker from a set created by the bot. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletestickerfromset

        :param sticker: File identifier of the sticker
        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self(
            "deleteStickerFromSet",
            sticker=sticker,
        )
        return result["result"]
