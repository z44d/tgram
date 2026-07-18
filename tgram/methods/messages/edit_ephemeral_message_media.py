import tgram
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import InputMedia
from tgram.types import Message

from tgram.utils import convert_input_media, convert_to_inline_keyboard_markup


class EditEphemeralMessageMedia:
    async def edit_ephemeral_message_media(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        media: InputMedia,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        converted, file = convert_input_media([media])
        result = await self(
            "editEphemeralMessageMedia",
            chat_id=chat_id,
            message_id=message_id,
            media=converted[0],
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
            **file,
        )
        return Message._parse(me=self, d=result.get("result", {}))
