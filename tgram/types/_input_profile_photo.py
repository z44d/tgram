import tgram
from .type_ import Type_

from typing import Optional, Union
from pathlib import Path


class InputProfilePhotoStatic(Type_):
    """
    A static profile photo in the .JPG format.

    Telegram Documentation: https://core.telegram.org/bots/api#inputprofilephotostatic

    :param photo: The static profile photo. Profile photos can't be reused and can only be uploaded as a new file,
        so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>.
        More information on Sending Files »
    :type photo: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputProfilePhotoStatic`
    """

    def __init__(
        self,
        photo: Union["Path", "str"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "static"
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputProfilePhotoStatic"]:
        return (
            InputProfilePhotoStatic(
                me=me,
                json=d,
                photo=d.get("photo"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class InputProfilePhotoAnimated(Type_):
    """
    An animated profile photo in the MPEG4 format.

    Telegram Documentation: https://core.telegram.org/bots/api#inputprofilephotoanimated

    :param animation: The animated profile photo. Profile photos can't be reused and can only be uploaded as a new file,
        so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>.
        More information on Sending Files »
    :type animation: :obj:`str`
    :param main_frame_timestamp: Optional. Timestamp in seconds of the frame that will be used as the static profile photo. Defaults to 0.0.
    :type main_frame_timestamp: :obj:`float`, optional

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputProfilePhotoAnimated`
    """

    def __init__(
        self,
        animation: Union["Path", "str"] = None,
        main_frame_timestamp: Optional[float] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "animated"
        self.animation = animation
        self.main_frame_timestamp = main_frame_timestamp

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputProfilePhotoAnimated"]:
        return (
            InputProfilePhotoAnimated(
                me=me,
                json=d,
                animation=d.get("animation"),
                main_frame_timestamp=d.get("main_frame_timestamp"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
