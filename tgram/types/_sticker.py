import tgram
from .type_ import Type_

from typing import Optional


class Sticker(Type_):
    """
    This object represents a sticker.

    Telegram Documentation: https://core.telegram.org/bots/api#sticker

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param type: Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is
        independent from its format, which is determined by the fields is_animated and is_video.
    :type type: :obj:`str`

    :param width: Sticker width
    :type width: :obj:`int`

    :param height: Sticker height
    :type height: :obj:`int`

    :param is_animated: True, if the sticker is animated
    :type is_animated: :obj:`bool`

    :param is_video: True, if the sticker is a video sticker
    :type is_video: :obj:`bool`

    :param thumbnail: Optional. Sticker thumbnail in the .WEBP or .JPG format
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :param emoji: Optional. Emoji associated with the sticker
    :type emoji: :obj:`str`

    :param set_name: Optional. Name of the sticker set to which the sticker belongs
    :type set_name: :obj:`str`

    :param premium_animation: Optional. Premium animation for the sticker, if the sticker is premium
    :type premium_animation: :class:`tgram.types.File`

    :param mask_position: Optional. For mask stickers, the position where the mask should be placed
    :type mask_position: :class:`tgram.types.MaskPosition`

    :param custom_emoji_id: Optional. For custom emoji stickers, unique identifier of the custom emoji
    :type custom_emoji_id: :obj:`str`

    :param needs_repainting: Optional. True, if the sticker must be repainted to a text color in messages,
        the color of the Telegram Premium badge in emoji status, white color on chat photos, or another
        appropriate color in other places
    :type needs_repainting: :obj:`bool`

    :param file_size: Optional. File size in bytes
    :type file_size: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Sticker`
    """

    def __init__(
        self,
        file_id: "str" = None,
        file_unique_id: "str" = None,
        type: "str" = None,
        width: "int" = None,
        height: "int" = None,
        is_animated: "bool" = None,
        is_video: "bool" = None,
        thumbnail: "tgram.types.PhotoSize" = None,
        emoji: "str" = None,
        set_name: "str" = None,
        premium_animation: "tgram.types.File" = None,
        mask_position: "tgram.types.MaskPosition" = None,
        custom_emoji_id: "str" = None,
        needs_repainting: "bool" = None,
        file_size: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.custom_emoji_id = custom_emoji_id
        self.needs_repainting = needs_repainting
        self.file_size = file_size

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Sticker"]:
        return (
            Sticker(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                type=d.get("type"),
                width=d.get("width"),
                height=d.get("height"),
                is_animated=d.get("is_animated"),
                is_video=d.get("is_video"),
                thumbnail=tgram.types.PhotoSize._parse(me=me, d=d.get("thumbnail")),
                emoji=d.get("emoji"),
                set_name=d.get("set_name"),
                premium_animation=tgram.types.File._parse(
                    me=me, d=d.get("premium_animation")
                ),
                mask_position=tgram.types.MaskPosition._parse(
                    me=me, d=d.get("mask_position")
                ),
                custom_emoji_id=d.get("custom_emoji_id"),
                needs_repainting=d.get("needs_repainting"),
                file_size=d.get("file_size"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
