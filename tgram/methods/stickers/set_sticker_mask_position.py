import tgram
from tgram.types import MaskPosition


class SetStickerMaskPosition:
    async def set_sticker_mask_position(
        self: "tgram.TgBot", sticker: str, mask_position: MaskPosition = None
    ) -> bool:
        """
        Use this method to change the mask position of a mask sticker.
        The sticker must belong to a sticker set that was created by the bot.
        Returns True on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`

        :param mask_position: A JSON-serialized object for position where the mask should be placed on faces.
        :type mask_position: :class:`tgram.types.MaskPosition`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setStickerMaskPosition",
            sticker=sticker,
            mask_position=mask_position,
        )
        return result.get("result", {})
