from typing import Optional

import tgram

from .type_ import Type_


class RichBlockPhoto(Type_):
    """
    This object represents a photo rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockphoto

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param photo: Optional. Photo
    :type photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param media: Optional. Input media photo
    :type media: :class:`tgram.types.InputMediaPhoto`

    :param caption: Optional. Caption
    :type caption: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockPhoto`
    """

    def __init__(
        self,
        type: "str" = "photo",
        photo: list["tgram.types.PhotoSize"] | None = None,
        media: "tgram.types.InputMediaPhoto" = None,
        caption: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.photo = photo
        self.media = media
        self.caption = caption

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichBlockPhoto"]:
        return (
            RichBlockPhoto(
                me=me,
                json=d,
                type=d.get("type"),
                photo=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
                media=tgram.types.InputMediaPhoto._parse(me=me, d=d.get("media"))
                if d.get("media")
                else None,
                caption=d.get("caption"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
