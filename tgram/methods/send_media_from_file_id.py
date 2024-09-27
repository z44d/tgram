import tgram
from typing import List
from typing import Union
from tgram.types import ForceReply
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message
from tgram.types import MessageEntity
from tgram.types import ReplyKeyboardMarkup
from tgram.types import ReplyKeyboardRemove
from tgram.types import ReplyParameters, ParseMode

from tgram import utils


class SendMediaFromFileId:
    async def send_media_from_file_id(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        file_id: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: ParseMode = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        decoded_file_id = utils.decode_file_id(file_id)

        if decoded_file_id["file_type_int"] not in utils.SUPPORTED_FILE_TYPES_TO_SEND:
            raise ValueError(
                f"Unsupported file type to send {decoded_file_id['file_type']}, You have to download it first."
            )

        result = await self._send_request(
            "send" + decoded_file_id["file_type"],
            **{
                "chat_id": chat_id,
                decoded_file_id["file_type"].lower(): file_id,
                "business_connection_id": business_connection_id,
                "message_thread_id": message_thread_id,
                "caption": caption,
                "parse_mode": parse_mode or self.parse_mode,
                "caption_entities": caption_entities,
                "show_caption_above_media": show_caption_above_media,
                "disable_notification": disable_notification,
                "protect_content": protect_content
                if protect_content is not None
                else self.protect_content,
                "message_effect_id": message_effect_id,
                "reply_parameters": reply_parameters,
                "reply_markup": reply_markup,
            },
        )

        return Message._parse(me=self, d=result["result"])
