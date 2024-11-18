import tgram
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import InputMedia
from tgram.types import Message

from tgram.utils import convert_input_media, convert_to_inline_keyboard_markup


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
        """
        Use this method to edit animation, audio, document, photo, or video messages, or to add media to text messages.
        If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise.
        When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL.
        On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.
        """
        converted, file = convert_input_media([media])
        result = await self._send_request(
            "editMessageMedia",
            media=converted[0],
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
            **file,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )
