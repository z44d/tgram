import tgram
from .type_ import Type_

from typing import Optional


class ChatPhoto(Type_):
    """
    This object represents a chat photo.

    Telegram Documentation: https://core.telegram.org/bots/api#chatphoto

    :param small_file_id: File identifier of small (160x160) chat photo. This file_id can be used only for photo
        download and only for as long as the photo is not changed.
    :type small_file_id: :obj:`str`

    :param small_file_unique_id: Unique file identifier of small (160x160) chat photo, which is supposed to be the same
        over time and for different bots. Can't be used to download or reuse the file.
    :type small_file_unique_id: :obj:`str`

    :param big_file_id: File identifier of big (640x640) chat photo. This file_id can be used only for photo download and
        only for as long as the photo is not changed.
    :type big_file_id: :obj:`str`

    :param big_file_unique_id: Unique file identifier of big (640x640) chat photo, which is supposed to be the same over
        time and for different bots. Can't be used to download or reuse the file.
    :type big_file_unique_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatPhoto`
    """

    def __init__(
        self,
        small_file_id: "str" = None,
        small_file_unique_id: "str" = None,
        big_file_id: "str" = None,
        big_file_unique_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatPhoto"]:
        return (
            ChatPhoto(
                me=me,
                json=d,
                small_file_id=d.get("small_file_id"),
                small_file_unique_id=d.get("small_file_unique_id"),
                big_file_id=d.get("big_file_id"),
                big_file_unique_id=d.get("big_file_unique_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
