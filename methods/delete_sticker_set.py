import tgram


class DeleteStickerSet:
    async def delete_sticker_set(self: "tgram.TgBot", name: str) -> bool:
        """
        Use this method to delete a sticker set. Returns True on success.

        :param name: Sticker set name
        :type name: :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteStickerSet",
            name=name,
        )
        return result["result"]
