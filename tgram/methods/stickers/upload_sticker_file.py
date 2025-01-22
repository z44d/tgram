import tgram
from typing import Union
from tgram.types import File
from pathlib import Path


class UploadStickerFile:
    async def upload_sticker_file(
        self: "tgram.TgBot",
        user_id: int,
        sticker: Union[Path, bytes, str],
        sticker_format: str,
    ) -> File:
        """
        Use this method to upload a .png file with a sticker for later use in createNewStickerSet and addStickerToSet
        methods (can be used multiple times). Returns the uploaded File on success.

        Telegram documentation: https://core.telegram.org/bots/api#uploadstickerfile

        :param user_id: User identifier of sticker set owner
        :type user_id: :obj:`int`

        :param png_sticker: DEPRECATED: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px,
            and either width or height must be exactly 512px.
        :type png_sticker: :obj:`filelike object`

        :param sticker: A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format.
            See https://core.telegram.org/stickers for technical requirements. More information on Sending Files »
        :type sticker: :class:`tgram.types.InputFile`

        :param sticker_format: One of "static", "animated", "video".
        :type sticker_format: :obj:`str`

        :return: On success, the sent file is returned.
        :rtype: :class:`tgram.types.File`
        """

        result = await self(
            "uploadStickerFile",
            user_id=user_id,
            sticker=sticker,
            sticker_format=sticker_format,
        )
        return File._parse(me=self, d=result["result"])
