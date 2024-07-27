import tgram
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import InputMedia
from tgram.types import Message

from tgram.utils import convert_input_media


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
        converted, file = convert_input_media([media])
        result = await self._send_request(
            "editMessageMedia",
            media=converted[0],
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup,
            **file,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )
