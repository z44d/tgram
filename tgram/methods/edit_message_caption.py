import tgram
from typing import List
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message
from tgram.types import MessageEntity


class EditMessageCaption:
    async def edit_message_caption(
        self: "tgram.TgBot",
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageCaption",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )
