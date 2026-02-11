import tgram
from .type_ import Type_

from typing import List, Optional


class UserProfileAudios(Type_):
    """
    This object represent a user's profile audios.

    Telegram Documentation: https://core.telegram.org/bots/api#userprofileaudios

    :param total_count: Total number of profile audios the target user has
    :type total_count: :obj:`int`

    :param audios: Requested profile audios
    :type audios: :obj:`list` of :class:`tgram.types.Audio`

    :return: Instance of the class
    :rtype: :class:`tgram.types.UserProfileAudios`
    """

    def __init__(
        self,
        total_count: "int" = None,
        audios: List["tgram.types.Audio"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.total_count = total_count
        self.audios = audios

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.UserProfileAudios"]:
        return (
            UserProfileAudios(
                me=me,
                json=d,
                total_count=d.get("total_count"),
                audios=[
                    tgram.types.Audio._parse(me=me, d=i) for i in d.get("audios")
                ]
                if d.get("audios")
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
