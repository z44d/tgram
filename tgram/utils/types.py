import tgram
import os

from typing import Optional, List, Union
from pathlib import Path
from io import BytesIO

from tgram import utils


def message_origin_parse(
    d: Optional[dict] = None, me: Optional["tgram.TgBot"] = None
) -> Optional["tgram.types.MessageOrigin"]:
    if d is None:
        return None

    origin_type = d["type"]

    return (
        tgram.types.MessageOriginUser._parse(me=me, d=d)
        if origin_type == "user"
        else tgram.types.MessageOriginHiddenUser._parse(me=me, d=d)
        if origin_type == "hidden_user"
        else tgram.types.MessageOriginChat._parse(me=me, d=d)
        if origin_type == "chat"
        else tgram.types.MessageOriginChannel._parse(me=me, d=d)
    )


def convert_input_media(
    x: List[Union["tgram.types.InputMedia", "tgram.types.InputPaidMedia"]],
):
    files = {}
    count = 1
    for y in x:
        if (
            isinstance(y.media, (Path, str))
            and os.path.isfile(y.media)
            or isinstance(y.media, (bytes, BytesIO))
        ):
            files[f"file_{count}"] = utils.get_file_path(y.media)
            y.media = f"attach://file_{count}"
            count += 1

            if hasattr(y, "thumbnail") and getattr(y, "thumbnail"):
                if (
                    isinstance(y.thumbnail, (Path, str)) and os.path.isfile(y.thumbnail)
                ) or isinstance(y.thumbnail, (bytes, BytesIO)):
                    files[f"file_{count}"] = utils.get_file_path(y.thumbnail)
                    y.thumbnail = f"attach://file_{count}"
                    count += 1

    return x, files
