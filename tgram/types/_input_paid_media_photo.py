import tgram
from .type_ import Type_

from typing import Optional, Union

from pathlib import Path


class InputPaidMediaPhoto(Type_):
    """
    The paid media to send is a photo.

    Telegram documentation: https://core.telegram.org/bots/api#inputpaidmediaphoto

    :param type: Type of the media, must be photo
    :type type: :obj:`str`

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for
        Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data
        under <file_attach_name> name. More information on Sending Files »
    :type media: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`InputPaidMediaPhoto`
    """

    def __init__(
        self,
        media: Union["Path", "str"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "photo"
        self.media = media

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputPaidMediaPhoto"]:
        return (
            InputPaidMediaPhoto(me=me, json=d, type=d.get("type"), media=d.get("media"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
