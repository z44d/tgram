import os
import tgram
import re
import html
import asyncio
import logging
import base64
import struct

from pathlib import Path
from typing import List, Union, TypedDict
from struct import unpack
from io import BytesIO
from json import dumps

from .handlers import Handlers

API_URL = "https://api.telegram.org/"
ALL_UPDATES: List[str] = [
    getattr(Handlers, i)
    for i in filter(lambda x: not x.startswith("_"), Handlers.__dict__)
]

log = logging.getLogger(__name__)

HTML_MENTION = '<a href="tg://user?id={user_id}">{name}</a>'
MARKDOWN_MENTION = "[{name}](tg://user?id={user_id})"


class Mention:
    def __init__(self, name: str, user_id: int) -> None:
        self.name = name
        self.user_id = user_id

    @property
    def markdown(self) -> str:
        return MARKDOWN_MENTION.format(name=self.name, user_id=self.user_id)

    @property
    def html(self) -> str:
        return HTML_MENTION.format(name=self.name, user_id=self.user_id)

    def __str__(self) -> str:
        log.warning("Make sure to use Mention.markdown or Mention.html.")
        return self.name


class Json(dict):
    def __str__(self) -> str:
        return dumps(
            self,
            ensure_ascii=False,
            indent=2,
            default=lambda obj: repr(obj) if not isinstance(obj, dict) else obj,
        )


def get_file_name(obj):
    name = getattr(obj, "name", None)
    if name and isinstance(name, str) and name[0] != "<" and name[-1] != ">":
        return os.path.basename(name)


def get_file_path(file):
    return Path(file) if isinstance(file, str) and os.path.isfile(file) else file


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
            files[f"file_{count}"] = get_file_path(y.media)
            y.media = f"attach://file_{count}"
            count += 1

            if hasattr(y, "thumbnail") and getattr(y, "thumbnail"):
                if (
                    isinstance(y.thumbnail, (Path, str)) and os.path.isfile(y.thumbnail)
                ) or isinstance(y.thumbnail, (bytes, BytesIO)):
                    files[f"file_{count}"] = get_file_path(y.thumbnail)
                    y.thumbnail = f"attach://file_{count}"
                    count += 1

    return x, files


class async_property:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, *args):
        return self.f(obj)


tgram.sync.async_to_sync(async_property, "__get__")


class String(str):
    def __init__(self, *args) -> None:
        self._entities: List["tgram.types.MessageEntity"] = None
        super().__init__()

    def put(self, e: List["tgram.types.MessageEntity"] = None) -> "String":
        self._entities = e

        return self

    @property
    def markdown(self) -> str:
        return self if not self._entities else markdown_unparse(self, self._entities)

    @property
    def html(self) -> str:
        return self if not self._entities else html_unparse(self, self._entities)


SMP_RE = re.compile(r"[\U00010000-\U0010FFFF]")

BOLD_DELIM = "**"
ITALIC_DELIM = "__"
UNDERLINE_DELIM = "--"
STRIKE_DELIM = "~~"
SPOILER_DELIM = "||"
CODE_DELIM = "`"
PRE_DELIM = "```"
BLOCKQUOTE_DELIM = ">"

MARKDOWN_RE = re.compile(
    r"({d})|(!?)\[(.+?)\]\((.+?)\)".format(
        d="|".join(
            [
                "".join(i)
                for i in [
                    [rf"\{j}" for j in i]
                    for i in [
                        PRE_DELIM,
                        CODE_DELIM,
                        STRIKE_DELIM,
                        UNDERLINE_DELIM,
                        ITALIC_DELIM,
                        BOLD_DELIM,
                        SPOILER_DELIM,
                    ]
                ]
            ]
        )
    )
)

OPENING_TAG = "<{}>"
CLOSING_TAG = "</{}>"
URL_MARKUP = '<a href="{}">{}</a>'
EMOJI_MARKUP = "<emoji id={}>{}</emoji>"
FIXED_WIDTH_DELIMS = [CODE_DELIM, PRE_DELIM]


def add_surrogates(text: str) -> str:
    # Replace each SMP code point with a surrogate pair
    return SMP_RE.sub(
        lambda match:  # Split SMP in two surrogates
        "".join(chr(i) for i in unpack("<HH", match.group().encode("utf-16le"))),
        text,
    )


def remove_surrogates(text: str) -> str:
    # Replace each surrogate pair with a SMP code point
    return text.encode("utf-16", "surrogatepass").decode("utf-16")


def markdown_unparse(text: str, entities: List["tgram.types.MessageEntity"]):
    text = add_surrogates(text)

    entities_offsets = []

    for entity in entities:
        entity_type = entity.type.lower()
        start = entity.offset
        end = start + entity.length

        if entity_type == "bold":
            start_tag = end_tag = BOLD_DELIM
        elif entity_type == "italic":
            start_tag = end_tag = ITALIC_DELIM
        elif entity_type == "underline":
            start_tag = end_tag = UNDERLINE_DELIM
        elif entity_type == "strikethrough":
            start_tag = end_tag = STRIKE_DELIM
        elif entity_type == "code":
            start_tag = end_tag = CODE_DELIM
        elif entity_type == "pre":
            language = getattr(entity, "language", "") or ""
            start_tag = f"{PRE_DELIM}{language}\n"
            end_tag = f"\n{PRE_DELIM}"
        elif entity_type == "blockquote":
            start_tag = BLOCKQUOTE_DELIM + " "
            end_tag = ""
            blockquote_text = text[start:end]
            lines = blockquote_text.split("\n")
            last_length = 0
            for line in lines:
                if len(line) == 0 and last_length == end:
                    continue
                start_offset = start + last_length
                last_length = last_length + len(line)
                end_offset = start_offset + last_length
                entities_offsets.append(
                    (
                        start_tag,
                        start_offset,
                    )
                )
                entities_offsets.append(
                    (
                        end_tag,
                        end_offset,
                    )
                )
                last_length = last_length + 1
            continue
        elif entity_type == "spoiler":
            start_tag = end_tag = SPOILER_DELIM
        elif entity_type == "text_link":
            url = entity.url
            start_tag = "["
            end_tag = f"]({url})"
        elif entity_type == "text_mention":
            user = entity.user
            start_tag = "["
            end_tag = f"](tg://user?id={user.id})"
        elif entity_type == "custom_emoji":
            emoji_id = entity.custom_emoji_id
            start_tag = "!["
            end_tag = f"](tg://emoji?id={emoji_id})"
        else:
            continue

        entities_offsets.append(
            (
                start_tag,
                start,
            )
        )
        entities_offsets.append(
            (
                end_tag,
                end,
            )
        )

    entities_offsets = map(
        lambda x: x[1],
        sorted(
            enumerate(entities_offsets), key=lambda x: (x[1][1], x[0]), reverse=True
        ),
    )

    for entity, offset in entities_offsets:
        text = text[:offset] + entity + text[offset:]

    return remove_surrogates(text)


def html_unparse(text: str, entities: List["tgram.types.MessageEntity"]) -> str:
    def parse_one(entity: "tgram.types.MessageEntity"):
        """
        Parses a single entity and returns (start_tag, start), (end_tag, end)
        """
        entity_type = entity.type.lower()
        start = entity.offset
        end = start + entity.length

        if entity_type in (
            "bold",
            "italic",
            "underline",
            "strikethrough",
        ):
            name = entity_type[0]
            start_tag = f"<{name}>"
            end_tag = f"</{name}>"
        elif entity_type == "pre":
            name = entity_type
            language = getattr(entity, "language", "") or ""
            start_tag = f'<{name} language="{language}">' if language else f"<{name}>"
            end_tag = f"</{name}>"
        elif entity_type == "blockquote":
            name = entity_type
            expandable = getattr(entity, "expandable", False)
            start_tag = f'<{name}{" expandable" if expandable else ""}>'
            end_tag = f"</{name}>"
        elif entity_type in (
            "code",
            "spoiler",
        ):
            name = entity_type if entity_type == "code" else "tg-spoiler"
            start_tag = f"<{name}>"
            end_tag = f"</{name}>"
        elif entity_type == "text_link":
            url = entity.url
            start_tag = f'<a href="{url}">'
            end_tag = "</a>"
        elif entity_type == "text_mention":
            user = entity.user
            start_tag = f'<a href="tg://user?id={user.id}">'
            end_tag = "</a>"
        elif entity_type == "custom_emoji":
            custom_emoji_id = entity.custom_emoji_id
            start_tag = f'<emoji id="{custom_emoji_id}">'
            end_tag = "</emoji>"
        else:
            return

        return (start_tag, start), (end_tag, end)

    def recursive(entity_i: int) -> int:
        """
        Takes the index of the entity to start parsing from, returns the number of parsed entities inside it.
        Uses entities_offsets as a stack, pushing (start_tag, start) first, then parsing nested entities,
        and finally pushing (end_tag, end) to the stack.
        No need to sort at the end.
        """
        this = parse_one(entities[entity_i])
        if this is None:
            return 1
        (start_tag, start), (end_tag, end) = this
        entities_offsets.append((start_tag, start))
        internal_i = entity_i + 1
        # while the next entity is inside the current one, keep parsing
        while internal_i < len(entities) and entities[internal_i].offset < end:
            internal_i += recursive(internal_i)
        entities_offsets.append((end_tag, end))
        return internal_i - entity_i

    text = add_surrogates(text)

    entities_offsets = []

    # probably useless because entities are already sorted by telegram
    entities.sort(key=lambda e: (e.offset, -e.length))

    # main loop for first-level entities
    i = 0
    while i < len(entities):
        i += recursive(i)

    if entities_offsets:
        last_offset = entities_offsets[-1][1]
        # no need to sort, but still add entities starting from the end
        for entity, offset in reversed(entities_offsets):
            text = (
                text[:offset]
                + entity
                + html.escape(text[offset:last_offset])
                + text[last_offset:]
            )
            last_offset = offset

    return remove_surrogates(text)


async def compose(bots: List["tgram.TgBot"]):
    tasks = [asyncio.create_task(bot.run_for_updates()) for bot in bots]

    return await asyncio.wait(tasks)


def b64_decode(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def rle_decode(s: bytes) -> bytes:
    r: List[int] = []
    z: bool = False

    for b in s:
        if not b:
            z = True
            continue

        if z:
            r.extend((0,) * b)
            z = False
        else:
            r.append(b)

    return bytes(r)


FILE_TYPES = {
    0: "Thumbnail",
    1: "ChatPhoto",
    2: "Photo",
    3: "Voice",
    4: "Video",
    5: "Document",
    8: "Sticker",
    9: "Audio",
    10: "Animation",
    13: "VideoNote",
    17: "Document",
}

SUPPORTED_FILE_TYPES_TO_SEND = (2, 3, 4, 5, 8, 9, 10, 13, 17)

WEB_LOCATION_FLAG = 1 << 24
FILE_REFERENCE_FLAG = 1 << 25


class DecodedFileId(TypedDict):
    file_type_int: int
    file_type: str
    dc_id: int
    file_id: str


def decode_file_id(file_id: str) -> DecodedFileId:
    decoded = rle_decode(b64_decode(file_id))
    major = decoded[-1]

    if major < 4:
        buffer = BytesIO(decoded[:-1])
    else:
        buffer = BytesIO(decoded[:-2])

    file_type_int, dc_id = struct.unpack("<ii", buffer.read(8))

    file_type_int &= ~WEB_LOCATION_FLAG
    file_type_int &= ~FILE_REFERENCE_FLAG

    try:
        file_type = FILE_TYPES[file_type_int]
    except ValueError:
        raise ValueError(f"Unknown file_type {file_type} of file_id {file_id}")

    return Json(
        {
            "file_type_int": file_type_int,
            "file_type": file_type,
            "dc_id": dc_id,
            "file_id": file_id,
        }
    )
