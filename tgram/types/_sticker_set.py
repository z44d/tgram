import tgram
from .type_ import Type_

from typing import List, Optional


class StickerSet(Type_):
    """
    This object represents a sticker set.

    Telegram Documentation: https://core.telegram.org/bots/api#stickerset

    :param name: Sticker set name
    :type name: :obj:`str`

    :param title: Sticker set title
    :type title: :obj:`str`

    :param sticker_type: Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”
    :type sticker_type: :obj:`str`

    :param stickers: List of all set stickers
    :type stickers: :obj:`list` of :class:`tgram.types.Sticker`

    :param thumbnail: Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :return: Instance of the class
    :rtype: :class:`tgram.types.StickerSet`
    """

    def __init__(
        self,
        name: "str" = None,
        title: "str" = None,
        sticker_type: "str" = None,
        stickers: List["tgram.types.Sticker"] = None,
        thumbnail: "tgram.types.PhotoSize" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.stickers = stickers
        self.thumbnail = thumbnail

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.StickerSet"]:
        return (
            StickerSet(
                me=me,
                json=d,
                name=d.get("name"),
                title=d.get("title"),
                sticker_type=d.get("sticker_type"),
                stickers=[
                    tgram.types.Sticker._parse(me=me, d=i) for i in d.get("stickers")
                ]
                if d.get("stickers")
                else None,
                thumbnail=tgram.types.PhotoSize._parse(me=me, d=d.get("thumbnail")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
