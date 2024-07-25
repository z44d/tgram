import tgram
from .type_ import Type_

from typing import Optional


class Audio(Type_):
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    Telegram Documentation: https://core.telegram.org/bots/api#audio

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type file_id: :obj:`str`

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different
        bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`

    :param duration: Duration of the audio in seconds as defined by sender
    :type duration: :obj:`int`

    :param performer: Optional. Performer of the audio as defined by sender or by audio tags
    :type performer: :obj:`str`

    :param title: Optional. Title of the audio as defined by sender or by audio tags
    :type title: :obj:`str`

    :param file_name: Optional. Original filename as defined by sender
    :type file_name: :obj:`str`

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type mime_type: :obj:`str`

    :param file_size: Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`

    :param thumbnail: Optional. Thumbnail of the album cover to which the music file belongs
    :type thumbnail: :class:`tgram.types.PhotoSize`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Audio`
    """

    def __init__(
        self,
        file_id: "str" = None,
        file_unique_id: "str" = None,
        duration: "int" = None,
        performer: "str" = None,
        title: "str" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
        thumbnail: "tgram.types.PhotoSize" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Audio"]:
        return (
            Audio(
                me=me,
                json=d,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                duration=d.get("duration"),
                performer=d.get("performer"),
                title=d.get("title"),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
                thumbnail=tgram.types.PhotoSize._parse(me=me, d=d.get("thumbnail")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
