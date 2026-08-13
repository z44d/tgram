from typing import Union as _Union

from ._rich_block_anchor import RichBlockAnchor
from ._rich_block_animation import RichBlockAnimation
from ._rich_block_audio import RichBlockAudio
from ._rich_block_block_quotation import RichBlockBlockQuotation
from ._rich_block_collage import RichBlockCollage
from ._rich_block_details import RichBlockDetails
from ._rich_block_divider import RichBlockDivider
from ._rich_block_footer import RichBlockFooter
from ._rich_block_list import RichBlockList
from ._rich_block_map import RichBlockMap
from ._rich_block_mathematical_expression import RichBlockMathematicalExpression
from ._rich_block_paragraph import RichBlockParagraph
from ._rich_block_photo import RichBlockPhoto
from ._rich_block_preformatted import RichBlockPreformatted
from ._rich_block_pull_quotation import RichBlockPullQuotation
from ._rich_block_section_heading import RichBlockSectionHeading
from ._rich_block_slideshow import RichBlockSlideshow
from ._rich_block_table import RichBlockTable
from ._rich_block_thinking import RichBlockThinking
from ._rich_block_video import RichBlockVideo
from ._rich_block_voice_note import RichBlockVoiceNote

RichBlock = _Union[
    "RichBlockParagraph",
    "RichBlockSectionHeading",
    "RichBlockPreformatted",
    "RichBlockFooter",
    "RichBlockDivider",
    "RichBlockMathematicalExpression",
    "RichBlockAnchor",
    "RichBlockList",
    "RichBlockBlockQuotation",
    "RichBlockPullQuotation",
    "RichBlockCollage",
    "RichBlockSlideshow",
    "RichBlockTable",
    "RichBlockDetails",
    "RichBlockMap",
    "RichBlockAnimation",
    "RichBlockAudio",
    "RichBlockPhoto",
    "RichBlockVideo",
    "RichBlockVoiceNote",
    "RichBlockThinking",
]
