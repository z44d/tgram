import tgram
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message


class EditMessageReplyMarkup:
    async def edit_message_reply_markup(
        self: "tgram.TgBot",
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageReplyMarkup",
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
