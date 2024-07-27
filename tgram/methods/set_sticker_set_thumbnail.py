import tgram
from typing import Union
from pathlib import Path
from tgram.utils import get_file_path


class SetStickerSetThumbnail:
    async def set_sticker_set_thumbnail(
        self: "tgram.TgBot",
        name: str,
        user_id: int,
        format: str,
        thumbnail: Union[Path, bytes, str] = None,
    ) -> bool:
        """
        Use this method to set the thumbnail of a sticker set.
        Animated thumbnails can be set for animated sticker sets only. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setstickersetthumbnail

        :param name: Sticker set name
        :type name: :obj:`str`

        :param user_id: User identifier
        :type user_id: :obj:`int`

        :param thumbnail: A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a .TGS animation
            with a thumbnail up to 32 kilobytes in size (see https://core.telegram.org/stickers#animated-sticker-requirements for animated sticker technical requirements),
            or a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-sticker-requirements for video sticker technical
            requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from
            the Internet, or upload a new one using multipart/form-data. More information on Sending Files ». Animated and video sticker set thumbnails can't be uploaded via
            HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.
        :type thumbnail: :obj:`filelike object`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setStickerSetThumbnail",
            name=name,
            user_id=user_id,
            format=format,
            thumbnail=get_file_path(thumbnail),
        )
        return result["result"]
