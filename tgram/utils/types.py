import tgram
import os
import re

from typing import Optional, List, Union, Tuple
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

            if hasattr(y, "cover") and getattr(y, "cover"):
                if (
                    isinstance(y.cover, (Path, str)) and os.path.isfile(y.cover)
                ) or isinstance(y.cover, (bytes, BytesIO)):
                    files[f"file_{count}"] = utils.get_file_path(y.cover)
                    y.thumbnail = f"attach://file_{count}"
                    count += 1

    return x, files


def reaction_type_parse(
    bot: "tgram.TgBot",
    x: Optional[Union[List[dict], dict]],
) -> "tgram.types.ReactionType":
    if x is None:
        return None

    x = x if isinstance(x, list) else [x]

    return [
        (
            tgram.types.ReactionTypeCustomEmoji._parse(bot, i)
            if i["type"] == "custom_emoji"
            else tgram.types.ReactionTypeEmoji._parse(bot, i)
            if i["type"] == "emoji"
            else tgram.types.ReactionTypePaid._parse(bot, i)
        )
        for i in x
    ]


pattern = re.compile(
    r"^(https?):\/\/" r"([a-zA-Z0-9.-]+)" r"(\.[a-zA-Z]{2,})" r"(\/[^\s]*)?$"
)


def convert_to_inline_keyboard_markup(v: List[List[Tuple]]):
    return tgram.types.InlineKeyboardMarkup(
        [
            [
                tgram.types.InlineKeyboardButton(
                    x,
                    callback_data=y if not re.match(pattern, y) else None,
                    url=y if re.match(pattern, y) else None,
                )
                for x, y in z
            ]
            for z in v
        ]
    )
