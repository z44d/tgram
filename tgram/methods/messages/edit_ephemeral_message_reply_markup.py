
import tgram
from tgram.types import InlineKeyboardMarkup, Message
from tgram.utils import convert_to_inline_keyboard_markup


class EditEphemeralMessageReplyMarkup:
    async def edit_ephemeral_message_reply_markup(
        self: "tgram.TgBot",
        chat_id: int | str,
        message_id: int,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        result = await self(
            "editEphemeralMessageReplyMarkup",
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return Message._parse(me=self, d=result.get("result", {}))
