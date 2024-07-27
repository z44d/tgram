import tgram
from typing import List
from tgram.types import InputSticker


class CreateNewStickerSet:
    async def create_new_sticker_set(
        self: "tgram.TgBot",
        user_id: int,
        name: str,
        title: str,
        stickers: List[InputSticker],
        sticker_type: str = None,
        needs_repainting: bool = None,
    ) -> bool:
        """
        Use this method to create new sticker set owned by a user.
        The bot will be able to edit the created sticker set.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#createnewstickerset

        .. note::
            Fields *_sticker are deprecated, pass a list of stickers to stickers parameter instead.

        :param user_id: User identifier of created sticker set owner
        :type user_id: :obj:`int`

        :param name: Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only English letters,
            digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>".
            <bot_username> is case insensitive. 1-64 characters.
        :type name: :obj:`str`

        :param title: Sticker set title, 1-64 characters
        :type title: :obj:`str`

        :param emojis: One or more emoji corresponding to the sticker
        :type emojis: :obj:`str`

        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width
            or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL
            as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        :type png_sticker: :obj:`str`

        :param tgs_sticker: TGS animation with the sticker, uploaded using multipart/form-data.
        :type tgs_sticker: :obj:`str`

        :param webm_sticker: WebM animation with the sticker, uploaded using multipart/form-data.
        :type webm_sticker: :obj:`str`

        :param contains_masks: Pass True, if a set of mask stickers should be created. Deprecated since Bot API 6.2,
            use sticker_type instead.
        :type contains_masks: :obj:`bool`

        :param sticker_type: Type of stickers in the set, pass “regular”, “mask”, or “custom_emoji”. By default, a regular sticker set is created.
        :type sticker_type: :obj:`str`

        :param mask_position: A JSON-serialized object for position where the mask should be placed on faces
        :type mask_position: :class:`tgram.types.MaskPosition`

        :param needs_repainting: Pass True if stickers in the sticker set must be repainted to the color of text when used in messages,
            the accent color if used as emoji status, white on chat photos, or another appropriate color based on context;
            for custom emoji sticker sets only
        :type needs_repainting: :obj:`bool`

        :param stickers: List of stickers to be added to the set
        :type stickers: :obj:`list` of :class:`tgram.types.InputSticker`

        :param sticker_format: deprecated
        :type sticker_format: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "createNewStickerSet",
            user_id=user_id,
            name=name,
            title=title,
            stickers=stickers,
            sticker_type=sticker_type,
            needs_repainting=needs_repainting,
        )
        return result["result"]
