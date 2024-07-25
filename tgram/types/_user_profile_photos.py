import tgram
from .type_ import Type_

from typing import List, Optional


class UserProfilePhotos(Type_):
    """
    This object represent a user's profile pictures.

    Telegram Documentation: https://core.telegram.org/bots/api#userprofilephotos

    :param total_count: Total number of profile pictures the target user has
    :type total_count: :obj:`int`

    :param photos: Requested profile pictures (in up to 4 sizes each)
    :type photos: :obj:`list` of :obj:`list` of :class:`tgram.types.PhotoSize`

    :return: Instance of the class
    :rtype: :class:`tgram.types.UserProfilePhotos`
    """

    def __init__(
        self,
        total_count: "int" = None,
        photos: List[List["tgram.types.PhotoSize"]] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.total_count = total_count
        self.photos = photos

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.UserProfilePhotos"]:
        return (
            UserProfilePhotos(
                me=me,
                json=d,
                total_count=d.get("total_count"),
                photos=[
                    [tgram.types.PhotoSize._parse(me, x) for x in y]
                    for y in d.get("photos")
                ]
                if d.get("photos")
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
