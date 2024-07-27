import tgram
from .type_ import Type_

from typing import Optional


class PaidMediaPreview(Type_):
    """
    The paid media isn't available before the payment.

    Telegram documentation: https://core.telegram.org/bots/api#paidmediapreview

    :param type: Type of the paid media, always “preview”
    :type type: :obj:`str`

    :param width: Optional. Media width as defined by the sender
    :type width: :obj:`int`

    :param height: Optional. Media height as defined by the sender
    :type height: :obj:`int`

    :param duration: Optional. Duration of the media in seconds as defined by the sender
    :type duration: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`PaidMediaPreview`
    """

    def __init__(
        self,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "preview"
        self.width = width
        self.height = height
        self.duration = duration

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PaidMediaPreview"]:
        return (
            PaidMediaPreview(
                me=me,
                json=d,
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
