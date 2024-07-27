import tgram
from typing import List
from typing import Union
from tgram.types import ForceReply
from tgram.types import InlineKeyboardMarkup
from tgram.types import InputPaidMedia
from tgram.types import Message
from tgram.types import MessageEntity
from tgram.types import ReplyKeyboardMarkup
from tgram.types import ReplyKeyboardRemove
from tgram.types import ReplyParameters


class SendPaidMedia:
    async def send_paid_media(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        star_count: int,
        media: List[InputPaidMedia],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        result = await self._send_request(
            "sendPaidMedia",
            chat_id=chat_id,
            star_count=star_count,
            media=media,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])
