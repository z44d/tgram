from pathlib import Path
from typing import Optional, Union

import tgram

from .type_ import Type_


class InputPaidMediaLivePhoto(Type_):
    """
    The paid media to send is a live photo.

    Telegram Documentation: https://core.telegram.org/bots/api#inputpaidmedialivephoto

    :param type: Type of the media, must be live_photo
    :type type: :obj:`str`

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
        HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one
    :type media: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputPaidMediaLivePhoto`
    """

    def __init__(
        self,
        media: Union["Path", "str"] | None = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "live_photo"
        self.media = media

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputPaidMediaLivePhoto"]:
        return (
            InputPaidMediaLivePhoto(
                me=me,
                json=d,
                media=d.get("media"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
