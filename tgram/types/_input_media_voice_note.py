from pathlib import Path
from typing import Optional, Union

import tgram

from .type_ import Type_


class InputMediaVoiceNote(Type_):
    def __init__(
        self,
        media: Union["Path", "str"] | None = None,
        thumbnail: Union["tgram.types.InputFile", "str"] = None,
        duration: "int | None" = None,
        waveform: "bytes | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "voice_note"
        self.media = media
        self.thumbnail = thumbnail
        self.duration = duration
        self.waveform = waveform

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputMediaVoiceNote"]:
        return (
            InputMediaVoiceNote(
                me=me,
                json=d,
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                duration=d.get("duration"),
                waveform=d.get("waveform"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
