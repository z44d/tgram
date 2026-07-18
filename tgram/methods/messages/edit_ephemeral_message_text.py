import tgram
from typing import List
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import LinkPreviewOptions
from tgram.types import Message
from tgram.types import MessageEntity, ParseMode

from tgram.utils import get_parse_mode, convert_to_inline_keyboard_markup


class EditEphemeralMessageText:
    async def edit_ephemeral_message_text(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        text: str,
        parse_mode: ParseMode = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        result = await self(
            "editEphemeralMessageText",
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            parse_mode=get_parse_mode(self, parse_mode),
            entities=entities,
            link_preview_options=link_preview_options or self.link_preview_options,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return Message._parse(me=self, d=result.get("result", {}))
