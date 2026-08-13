import os
import re
from io import BytesIO
from pathlib import Path
from typing import Optional, Union

import tgram
from tgram import utils


def message_origin_parse(
    d: dict | None = None, me: Optional["tgram.TgBot"] = None
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
    x: list[
        Union[
            "tgram.types.InputMedia",
            "tgram.types.InputPaidMedia",
            "tgram.types.InputProfilePhotoAnimated",
            "tgram.types.InputProfilePhotoStatic",
        ]
    ],
):
    files = {}
    count = 1

    def attach_file(obj, attr):
        nonlocal count
        media = getattr(obj, attr, None)
        if media is None:
            return
        is_path = isinstance(media, (Path, str)) and os.path.isfile(media)
        is_bytes = isinstance(media, (bytes, BytesIO))
        if is_path or is_bytes:
            files[f"file_{count}"] = utils.get_file_path(media)
            setattr(obj, attr, f"attach://file_{count}")
            count += 1

    for y in x:
        # Handle profile photos
        if isinstance(
            y,
            (
                tgram.types.InputProfilePhotoAnimated,
                tgram.types.InputProfilePhotoStatic,
            ),
        ):
            attr_name = "animation" if hasattr(y, "animation") else "photo"
            attach_file(y, attr_name)
        else:
            # Handle main media
            attach_file(y, "media")
            # Optionally handle thumbnail and cover
            if hasattr(y, "thumbnail") and getattr(y, "thumbnail", None):
                attach_file(y, "thumbnail")
            if hasattr(y, "cover") and getattr(y, "cover", None):
                attach_file(y, "cover")

    return x, files


def reaction_type_parse(
    bot: "tgram.TgBot",
    x: list[dict] | dict | None,
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


def rich_text_parse(
    me: Optional["tgram.TgBot"] = None, d: dict | None = None
) -> Optional["tgram.types.RichText"]:
    if d is None:
        return None

    rich_text_type = d.get("type")

    return (
        tgram.types.RichTextBold._parse(me=me, d=d)
        if rich_text_type == "bold"
        else tgram.types.RichTextItalic._parse(me=me, d=d)
        if rich_text_type == "italic"
        else tgram.types.RichTextUnderline._parse(me=me, d=d)
        if rich_text_type == "underline"
        else tgram.types.RichTextStrikethrough._parse(me=me, d=d)
        if rich_text_type == "strikethrough"
        else tgram.types.RichTextSpoiler._parse(me=me, d=d)
        if rich_text_type == "spoiler"
        else tgram.types.RichTextDateTime._parse(me=me, d=d)
        if rich_text_type == "date_time"
        else tgram.types.RichTextTextMention._parse(me=me, d=d)
        if rich_text_type == "text_mention"
        else tgram.types.RichTextSubscript._parse(me=me, d=d)
        if rich_text_type == "subscript"
        else tgram.types.RichTextSuperscript._parse(me=me, d=d)
        if rich_text_type == "superscript"
        else tgram.types.RichTextMarked._parse(me=me, d=d)
        if rich_text_type == "marked"
        else tgram.types.RichTextCode._parse(me=me, d=d)
        if rich_text_type == "code"
        else tgram.types.RichTextCustomEmoji._parse(me=me, d=d)
        if rich_text_type == "custom_emoji"
        else tgram.types.RichTextMathematicalExpression._parse(me=me, d=d)
        if rich_text_type == "mathematical_expression"
        else tgram.types.RichTextUrl._parse(me=me, d=d)
        if rich_text_type == "url"
        else tgram.types.RichTextEmailAddress._parse(me=me, d=d)
        if rich_text_type == "email_address"
        else tgram.types.RichTextPhoneNumber._parse(me=me, d=d)
        if rich_text_type == "phone_number"
        else tgram.types.RichTextBankCardNumber._parse(me=me, d=d)
        if rich_text_type == "bank_card_number"
        else tgram.types.RichTextMention._parse(me=me, d=d)
        if rich_text_type == "mention"
        else tgram.types.RichTextHashtag._parse(me=me, d=d)
        if rich_text_type == "hashtag"
        else tgram.types.RichTextCashtag._parse(me=me, d=d)
        if rich_text_type == "cashtag"
        else tgram.types.RichTextBotCommand._parse(me=me, d=d)
        if rich_text_type == "bot_command"
        else tgram.types.RichTextAnchor._parse(me=me, d=d)
        if rich_text_type == "anchor"
        else tgram.types.RichTextAnchorLink._parse(me=me, d=d)
        if rich_text_type == "anchor_link"
        else tgram.types.RichTextReference._parse(me=me, d=d)
        if rich_text_type == "reference"
        else tgram.types.RichTextReferenceLink._parse(me=me, d=d)
        if rich_text_type == "reference_link"
        else None
    )


def rich_block_parse(
    me: Optional["tgram.TgBot"] = None, d: dict | None = None
) -> Optional["tgram.types.RichBlock"]:
    if d is None:
        return None

    block_type = d.get("type")

    return (
        tgram.types.RichBlockParagraph._parse(me=me, d=d)
        if block_type == "paragraph"
        else tgram.types.RichBlockSectionHeading._parse(me=me, d=d)
        if block_type == "section_heading"
        else tgram.types.RichBlockPreformatted._parse(me=me, d=d)
        if block_type == "preformatted"
        else tgram.types.RichBlockFooter._parse(me=me, d=d)
        if block_type == "footer"
        else tgram.types.RichBlockDivider._parse(me=me, d=d)
        if block_type == "divider"
        else tgram.types.RichBlockMathematicalExpression._parse(me=me, d=d)
        if block_type == "mathematical_expression"
        else tgram.types.RichBlockAnchor._parse(me=me, d=d)
        if block_type == "anchor"
        else tgram.types.RichBlockList._parse(me=me, d=d)
        if block_type == "list"
        else tgram.types.RichBlockBlockQuotation._parse(me=me, d=d)
        if block_type == "block_quotation"
        else tgram.types.RichBlockPullQuotation._parse(me=me, d=d)
        if block_type == "pull_quotation"
        else tgram.types.RichBlockCollage._parse(me=me, d=d)
        if block_type == "collage"
        else tgram.types.RichBlockSlideshow._parse(me=me, d=d)
        if block_type == "slideshow"
        else tgram.types.RichBlockTable._parse(me=me, d=d)
        if block_type == "table"
        else tgram.types.RichBlockDetails._parse(me=me, d=d)
        if block_type == "details"
        else tgram.types.RichBlockMap._parse(me=me, d=d)
        if block_type == "map"
        else tgram.types.RichBlockAnimation._parse(me=me, d=d)
        if block_type == "animation"
        else tgram.types.RichBlockAudio._parse(me=me, d=d)
        if block_type == "audio"
        else tgram.types.RichBlockPhoto._parse(me=me, d=d)
        if block_type == "photo"
        else tgram.types.RichBlockVideo._parse(me=me, d=d)
        if block_type == "video"
        else tgram.types.RichBlockVoiceNote._parse(me=me, d=d)
        if block_type == "voice_note"
        else tgram.types.RichBlockThinking._parse(me=me, d=d)
        if block_type == "thinking"
        else None
    )


def input_rich_block_parse(
    me: Optional["tgram.TgBot"] = None, d: dict | None = None
) -> Optional["tgram.types.InputRichBlock"]:
    if d is None:
        return None

    block_type = d.get("type")

    return (
        tgram.types.InputRichBlockParagraph._parse(me=me, d=d)
        if block_type == "paragraph"
        else tgram.types.InputRichBlockSectionHeading._parse(me=me, d=d)
        if block_type == "section_heading"
        else tgram.types.InputRichBlockPreformatted._parse(me=me, d=d)
        if block_type == "preformatted"
        else tgram.types.InputRichBlockFooter._parse(me=me, d=d)
        if block_type == "footer"
        else tgram.types.InputRichBlockDivider._parse(me=me, d=d)
        if block_type == "divider"
        else tgram.types.InputRichBlockMathematicalExpression._parse(me=me, d=d)
        if block_type == "mathematical_expression"
        else tgram.types.InputRichBlockAnchor._parse(me=me, d=d)
        if block_type == "anchor"
        else tgram.types.InputRichBlockList._parse(me=me, d=d)
        if block_type == "list"
        else tgram.types.InputRichBlockBlockQuotation._parse(me=me, d=d)
        if block_type == "block_quotation"
        else tgram.types.InputRichBlockPullQuotation._parse(me=me, d=d)
        if block_type == "pull_quotation"
        else tgram.types.InputRichBlockCollage._parse(me=me, d=d)
        if block_type == "collage"
        else tgram.types.InputRichBlockSlideshow._parse(me=me, d=d)
        if block_type == "slideshow"
        else tgram.types.InputRichBlockTable._parse(me=me, d=d)
        if block_type == "table"
        else tgram.types.InputRichBlockDetails._parse(me=me, d=d)
        if block_type == "details"
        else tgram.types.InputRichBlockMap._parse(me=me, d=d)
        if block_type == "map"
        else tgram.types.InputRichBlockAnimation._parse(me=me, d=d)
        if block_type == "animation"
        else tgram.types.InputRichBlockAudio._parse(me=me, d=d)
        if block_type == "audio"
        else tgram.types.InputRichBlockPhoto._parse(me=me, d=d)
        if block_type == "photo"
        else tgram.types.InputRichBlockVideo._parse(me=me, d=d)
        if block_type == "video"
        else tgram.types.InputRichBlockVoiceNote._parse(me=me, d=d)
        if block_type == "voice_note"
        else tgram.types.InputRichBlockThinking._parse(me=me, d=d)
        if block_type == "thinking"
        else None
    )


pattern = re.compile(
    r"^(https?):\/\/" r"([a-zA-Z0-9.-]+)" r"(\.[a-zA-Z]{2,})" r"(\/[^\s]*)?$"
)


def convert_to_inline_keyboard_markup(v: list[list[tuple]]):
    return tgram.types.InlineKeyboardMarkup(
        [
            [
                tgram.types.InlineKeyboardButton(
                    x,
                    callback_data=y if not re.match(pattern, y) else None,
                    url=y if re.match(pattern, y) else None,
                    user_id=y if isinstance(y, int) else None,
                )
                for x, y in z
            ]
            for z in v
        ]
    )
