import tgram
from tgram.types import InputSticker


class AddStickerToSet:
    async def add_sticker_to_set(
        self: "tgram.TgBot", user_id: int, name: str, sticker: InputSticker
    ) -> bool:
        """
        Use this method to add a new sticker to a set created by the bot.
        The format of the added sticker must match the format of the other stickers in the set.
        Emoji sticker sets can have up to 200 stickers. Animated and video sticker sets can have up to 50 stickers.
        Static sticker sets can have up to 120 stickers.
        Returns True on success.

        .. note::
            **_sticker, mask_position, emojis parameters are deprecated, use stickers instead

        Telegram documentation: https://core.telegram.org/bots/api#addstickertoset

        :param user_id: User identifier of created sticker set owner
        :type user_id: :obj:`int`

        :param name: Sticker set name
        :type name: :obj:`str`

        :param emojis: One or more emoji corresponding to the sticker
        :type emojis: :obj:`str`

        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either
            width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers,
            pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        :type png_sticker: :obj:`str` or :obj:`filelike object`

        :param tgs_sticker: TGS animation with the sticker, uploaded using multipart/form-data.
        :type tgs_sticker: :obj:`str` or :obj:`filelike object`

        :param webm_sticker: WebM animation with the sticker, uploaded using multipart/form-data.
        :type webm_sticker: :obj:`str` or :obj:`filelike object`

        :param mask_position: A JSON-serialized object for position where the mask should be placed on faces
        :type mask_position: :class:`tgram.types.MaskPosition`

        :param sticker: A JSON-serialized object for sticker to be added to the sticker set
        :type sticker: :class:`tgram.types.InputSticker`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self(
            "addStickerToSet",
            user_id=user_id,
            name=name,
            sticker=sticker,
        )
        return result["result"]
