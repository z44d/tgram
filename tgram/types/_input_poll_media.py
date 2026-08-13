from pathlib import Path
from typing import Optional, Union

import tgram

from .type_ import Type_


class InputPollMedia(Type_):
    """
    Represents a media to be added to a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#inputpollmedia

    :param type: Type of the media
    :type type: :obj:`str`

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
        HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one
    :type media: :obj:`str`

    :param width: Optional. Media width
    :type width: :obj:`int`

    :param height: Optional. Media height
    :type height: :obj:`int`

    :param duration: Optional. Media duration in seconds
    :type duration: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputPollMedia`
    """

    def __init__(
        self,
        type: "str | None" = None,
        media: Union["Path", "str"] | None = None,
        width: "int | None" = None,
        height: "int | None" = None,
        duration: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.media = media
        self.width = width
        self.height = height
        self.duration = duration

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputPollMedia"]:
        return (
            InputPollMedia(
                me=me,
                json=d,
                type=d.get("type"),
                media=d.get("media"),
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
