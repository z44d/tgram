from typing import Optional

import tgram

from .type_ import Type_


class PaidMediaPhoto(Type_):
    """
    The paid media is a photo.

    Telegram documentation: https://core.telegram.org/bots/api#paidmediaphoto

    :param type: Type of the paid media, always “photo”
    :type type: :obj:`str`

    :param photo: The photo
    :type photo: :obj:`list` of :class:`PhotoSize`

    :return: Instance of the class
    :rtype: :class:`PaidMediaPhoto`

    """

    def __init__(
        self,
        photo: list["tgram.types.PhotoSize"] | None = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "photo"
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.PaidMediaPhoto"]:
        return (
            PaidMediaPhoto(
                me=me,
                json=d,
                photo=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
