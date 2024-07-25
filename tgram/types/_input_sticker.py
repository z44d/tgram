import tgram
from .type_ import Type_

from typing import List, Union, Optional


class InputSticker(Type_):
    """
    This object describes a sticker to be added to a sticker set.

    :param sticker: The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers,
        pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        Animated and video stickers can't be uploaded via HTTP URL.
    :type sticker: :obj:`str` or :obj:`tgram.types.InputFile`

    :param emoji_list: One or more(up to 20) emoji(s) corresponding to the sticker
    :type emoji_list: :obj:`list` of :obj:`str`

    :param mask_position: Optional. Position where the mask should be placed on faces. For “mask” stickers only.
    :type mask_position: :class:`tgram.types.MaskPosition`

    :param keywords: Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters.
        For “regular” and “custom_emoji” stickers only.
    :type keywords: :obj:`list` of :obj:`str`

    :param format: 	Format of the added sticker, must be one of “static” for a .WEBP or .PNG image, “animated” for a .TGS animation, “video” for a WEBM video
    :type format: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputSticker`
    """

    def __init__(
        self,
        sticker: Union["tgram.types.InputFile", "str"] = None,
        format: "str" = None,
        emoji_list: List["str"] = None,
        mask_position: "tgram.types.MaskPosition" = None,
        keywords: List["str"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.sticker = sticker
        self.format = format
        self.emoji_list = emoji_list
        self.mask_position = mask_position
        self.keywords = keywords

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputSticker"]:
        return (
            InputSticker(
                me=me,
                json=d,
                sticker=d.get("sticker"),
                format=d.get("format"),
                emoji_list=d.get("emoji_list"),
                mask_position=tgram.types.MaskPosition._parse(
                    me=me, d=d.get("mask_position")
                ),
                keywords=d.get("keywords"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
