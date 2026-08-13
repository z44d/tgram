import tgram
from tgram.types import InlineKeyboardMarkup, Message
from tgram.utils import convert_to_inline_keyboard_markup


class StopMessageLiveLocation:
    async def stop_message_live_location(
        self: "tgram.TgBot",
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message | bool:
        result = await self(
            "stopMessageLiveLocation",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return (
            Message._parse(me=self, d=result.get("result", {}))
            if isinstance(result.get("result", {}), dict)
            else result.get("result", {})
        )
