import tgram


class SetStickerPositionInSet:
    async def set_sticker_position_in_set(
        self: "tgram.TgBot", sticker: str, position: int
    ) -> bool:
        """
        Use this method to move a sticker in a set created by the bot to a specific position . Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setstickerpositioninset

        :param sticker: File identifier of the sticker
        :type sticker: :obj:`str`

        :param position: New sticker position in the set, zero-based
        :type position: :obj:`int`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setStickerPositionInSet",
            sticker=sticker,
            position=position,
        )
        return result["result"]
