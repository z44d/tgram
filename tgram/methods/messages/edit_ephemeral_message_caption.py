
import tgram
from tgram.types import InlineKeyboardMarkup, Message, MessageEntity, ParseMode
from tgram.utils import convert_to_inline_keyboard_markup, get_parse_mode


class EditEphemeralMessageCaption:
    async def edit_ephemeral_message_caption(
        self: "tgram.TgBot",
        chat_id: int | str,
        message_id: int,
        caption: str | None = None,
        parse_mode: ParseMode = None,
        caption_entities: list[MessageEntity] | None = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        result = await self(
            "editEphemeralMessageCaption",
            chat_id=chat_id,
            message_id=message_id,
            caption=caption,
            parse_mode=get_parse_mode(self, parse_mode),
            caption_entities=caption_entities,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return Message._parse(me=self, d=result.get("result", {}))
