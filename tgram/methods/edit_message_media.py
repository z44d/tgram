import tgram
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import InputMedia
from tgram.types import Message


class EditMessageMedia:
    async def edit_message_media(
        self: "tgram.TgBot",
        media: InputMedia,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageMedia",
            media=media,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )
