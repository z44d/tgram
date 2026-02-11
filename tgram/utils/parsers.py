import html
import tgram
import re

from typing import List, Union, Pattern, Match, Optional
from struct import unpack


class String(str):
    def __init__(self, *args) -> None:
        self._entities: List["tgram.types.MessageEntity"] = None
        super().__init__()

    def put(self, e: List["tgram.types.MessageEntity"] = None) -> "String":
        self._entities = e
        if e:
            text = add_surrogates(self)
            for entity in e:
                entity._content = remove_surrogates(
                    text[entity.offset : entity.offset + entity.length]
                )

        return self

    def match(
        self, pattern: Union[str, Pattern[str]], flags: Union[int, re.RegexFlag] = 0
    ) -> Optional[Match[str]]:
        return re.match(pattern=pattern, string=self, flags=flags)

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
            start_tag = f"<{name}{' expandable' if expandable else ''}>"
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
            start_tag = f"<tg-emoji emoji-id='{custom_emoji_id}'>"
            end_tag = "</tg-emoji>"
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
