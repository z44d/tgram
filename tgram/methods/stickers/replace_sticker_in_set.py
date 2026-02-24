import tgram
from tgram.types import InputSticker


class ReplaceStickerInSet:
    async def replace_sticker_in_set(
        self: "tgram.TgBot",
        user_id: int,
        name: str,
        old_sticker: str,
        sticker: InputSticker,
    ) -> bool:
        """
        Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling deleteStickerFromSet, then addStickerToSet,
            then setStickerPositionInSet. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#replaceStickerInSet

        :param user_id: User identifier of the sticker set owner
        :type user_id: :obj:`int`

        :param name: Sticker set name
        :type name: :obj:`str`

        :param old_sticker: File identifier of the replaced sticker
        :type old_sticker: :obj:`str`

        :param sticker: A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.
        :type sticker: :class:`tgram.types.InputSticker`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "replaceStickerInSet",
            user_id=user_id,
            name=name,
            old_sticker=old_sticker,
            sticker=sticker,
        )
        return result.get("result", {})
