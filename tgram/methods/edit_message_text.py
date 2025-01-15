import tgram
from typing import List
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import LinkPreviewOptions
from tgram.types import Message
from tgram.types import MessageEntity, ParseMode

from tgram.utils import get_parse_mode, convert_to_inline_keyboard_markup


class EditMessageText:
    async def edit_message_text(
        self: "tgram.TgBot",
        text: str,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        parse_mode: ParseMode = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """
        Use this method to edit text and game messages.
        On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.
        """
        result = await self(
            "editMessageText",
            text=text,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            parse_mode=get_parse_mode(self, parse_mode),
            entities=entities,
            link_preview_options=link_preview_options or self.link_preview_options,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )
