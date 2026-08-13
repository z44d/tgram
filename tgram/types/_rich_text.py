from typing import Union as _Union

from ._rich_text_anchor import RichTextAnchor
from ._rich_text_anchor_link import RichTextAnchorLink
from ._rich_text_bank_card_number import RichTextBankCardNumber
from ._rich_text_bold import RichTextBold
from ._rich_text_bot_command import RichTextBotCommand
from ._rich_text_cashtag import RichTextCashtag
from ._rich_text_code import RichTextCode
from ._rich_text_custom_emoji import RichTextCustomEmoji
from ._rich_text_date_time import RichTextDateTime
from ._rich_text_email_address import RichTextEmailAddress
from ._rich_text_hashtag import RichTextHashtag
from ._rich_text_italic import RichTextItalic
from ._rich_text_marked import RichTextMarked
from ._rich_text_mathematical_expression import RichTextMathematicalExpression
from ._rich_text_mention import RichTextMention
from ._rich_text_phone_number import RichTextPhoneNumber
from ._rich_text_reference import RichTextReference
from ._rich_text_reference_link import RichTextReferenceLink
from ._rich_text_spoiler import RichTextSpoiler
from ._rich_text_strikethrough import RichTextStrikethrough
from ._rich_text_subscript import RichTextSubscript
from ._rich_text_superscript import RichTextSuperscript
from ._rich_text_text_mention import RichTextTextMention
from ._rich_text_underline import RichTextUnderline
from ._rich_text_url import RichTextUrl

RichText = _Union[
    "RichTextBold",
    "RichTextItalic",
    "RichTextUnderline",
    "RichTextStrikethrough",
    "RichTextSpoiler",
    "RichTextDateTime",
    "RichTextTextMention",
    "RichTextSubscript",
    "RichTextSuperscript",
    "RichTextMarked",
    "RichTextCode",
    "RichTextCustomEmoji",
    "RichTextMathematicalExpression",
    "RichTextUrl",
    "RichTextEmailAddress",
    "RichTextPhoneNumber",
    "RichTextBankCardNumber",
    "RichTextMention",
    "RichTextHashtag",
    "RichTextCashtag",
    "RichTextBotCommand",
    "RichTextAnchor",
    "RichTextAnchorLink",
    "RichTextReference",
    "RichTextReferenceLink",
]
