import tgram


class SetStickerSetTitle:
    async def set_sticker_set_title(self: "tgram.TgBot", name: str, title: str) -> bool:
        """
        Use this method to set the title of a created sticker set.
        Returns True on success.

        :param name: Sticker set name
        :type name: :obj:`str`

        :param title: New sticker set title
        :type title: :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setStickerSetTitle",
            name=name,
            title=title,
        )
        return result["result"]
