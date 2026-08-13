
import tgram
from tgram import utils
from tgram.types import (
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    MessageEntity,
    ParseMode,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
)


class SendMediaFromFileId:
    async def send_media_from_file_id(
        self: "tgram.TgBot",
        chat_id: int | str,
        file_id: str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: ParseMode = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,
        allow_paid_broadcast: bool | None = None,
    ) -> Message:
        decoded_file_id = utils.decode_file_id(file_id)

        if decoded_file_id["file_type_int"] not in utils.SUPPORTED_FILE_TYPES_TO_SEND:
            raise ValueError(
                f"Unsupported file type to send {decoded_file_id['file_type']}, You have to download it first."
            )

        result = await self(
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
                "reply_markup": utils.convert_to_inline_keyboard_markup(reply_markup)
                if isinstance(reply_markup, list)
                else reply_markup,
                "allow_paid_broadcast": allow_paid_broadcast,
            },
        )

        return Message._parse(me=self, d=result.get("result", {}))
