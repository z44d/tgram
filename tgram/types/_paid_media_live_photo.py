from typing import Optional

import tgram

from .type_ import Type_


class PaidMediaLivePhoto(Type_):
    """
    The paid media to send is a live photo.

    Telegram Documentation: https://core.telegram.org/bots/api#paidmedialivephoto

    :param type: Type of the media, must be live_photo
    :type type: :obj:`str`

    :param live_photo: The live photo
    :type live_photo: :class:`tgram.types.LivePhoto`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PaidMediaLivePhoto`
    """

    def __init__(
        self,
        type: "str | None" = None,
        live_photo: "tgram.types.LivePhoto" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.live_photo = live_photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.PaidMediaLivePhoto"]:
        return (
            PaidMediaLivePhoto(
                me=me,
                json=d,
                type=d.get("type"),
                live_photo=tgram.types.LivePhoto._parse(me=me, d=d.get("live_photo")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
