import tgram
from .type_ import Type_

from typing import List, Optional


class PaidMediaInfo(Type_):
    """
    Describes the paid media added to a message.

    Telegram documentation: https://core.telegram.org/bots/api#paidmediainfo

    :param star_count: The number of Telegram Stars that must be paid to buy access to the media
    :type star_count: :obj:`int`

    :param paid_media: Information about the paid media
    :type paid_media: :obj:`list` of :class:`PaidMedia`

    :return: Instance of the class
    :rtype: :class:`PaidMediaInfo`
    """

    def __init__(
        self,
        star_count: "int" = None,
        paid_media: List["tgram.types.PaidMedia"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.star_count = star_count
        self.paid_media = paid_media

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PaidMediaInfo"]:
        return (
            PaidMediaInfo(
                me=me,
                json=d,
                star_count=d.get("star_count"),
                paid_media=[
                    (
                        tgram.types.PaidMediaPreview._parse(me=me, d=i)
                        if i["type"] == "preview"
                        else tgram.types.PaidMediaPhoto._parse(me=me, d=i)
                        if i["type"] == "photo"
                        else tgram.types.PaidMediaVideo._parse(me=me, d=i)
                    )
                    for i in d.get("paid_media")
                ]
                if d.get("paid_media")
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
