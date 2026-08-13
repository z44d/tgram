from typing import Union as _Union

from ._input_rich_block_anchor import InputRichBlockAnchor
from ._input_rich_block_animation import InputRichBlockAnimation
from ._input_rich_block_audio import InputRichBlockAudio
from ._input_rich_block_block_quotation import InputRichBlockBlockQuotation
from ._input_rich_block_collage import InputRichBlockCollage
from ._input_rich_block_details import InputRichBlockDetails
from ._input_rich_block_divider import InputRichBlockDivider
from ._input_rich_block_footer import InputRichBlockFooter
from ._input_rich_block_list import InputRichBlockList
from ._input_rich_block_map import InputRichBlockMap
from ._input_rich_block_mathematical_expression import (
    InputRichBlockMathematicalExpression,
)
from ._input_rich_block_paragraph import InputRichBlockParagraph
from ._input_rich_block_photo import InputRichBlockPhoto
from ._input_rich_block_preformatted import InputRichBlockPreformatted
from ._input_rich_block_pull_quotation import InputRichBlockPullQuotation
from ._input_rich_block_section_heading import InputRichBlockSectionHeading
from ._input_rich_block_slideshow import InputRichBlockSlideshow
from ._input_rich_block_table import InputRichBlockTable
from ._input_rich_block_thinking import InputRichBlockThinking
from ._input_rich_block_video import InputRichBlockVideo
from ._input_rich_block_voice_note import InputRichBlockVoiceNote

InputRichBlock = _Union[
    "InputRichBlockParagraph",
    "InputRichBlockSectionHeading",
    "InputRichBlockPreformatted",
    "InputRichBlockFooter",
    "InputRichBlockDivider",
    "InputRichBlockMathematicalExpression",
    "InputRichBlockAnchor",
    "InputRichBlockList",
    "InputRichBlockBlockQuotation",
    "InputRichBlockPullQuotation",
    "InputRichBlockCollage",
    "InputRichBlockSlideshow",
    "InputRichBlockTable",
    "InputRichBlockDetails",
    "InputRichBlockMap",
    "InputRichBlockAnimation",
    "InputRichBlockAudio",
    "InputRichBlockPhoto",
    "InputRichBlockVideo",
    "InputRichBlockVoiceNote",
    "InputRichBlockThinking",
]
