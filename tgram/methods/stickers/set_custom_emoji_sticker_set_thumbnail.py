import tgram


class SetCustomEmojiStickerSetThumbnail:
    async def set_custom_emoji_sticker_set_thumbnail(
        self: "tgram.TgBot", name: str, custom_emoji_id: str = None
    ) -> bool:
        """
        Use this method to set the thumbnail of a custom emoji sticker set.
        Returns True on success.

        :param name: Sticker set name
        :type name: :obj:`str`

        :param custom_emoji_id: Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.
        :type custom_emoji_id: :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setCustomEmojiStickerSetThumbnail",
            name=name,
            custom_emoji_id=custom_emoji_id,
        )
        return result["result"]
