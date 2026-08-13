import tgram
from tgram.types import (
    InlineKeyboardMarkup,
    InputRichMessage,
    LinkPreviewOptions,
    Message,
    MessageEntity,
    ParseMode,
)
from tgram.utils import convert_to_inline_keyboard_markup, get_parse_mode


class EditMessageText:
    async def edit_message_text(
        self: "tgram.TgBot",
        text: str | None = None,
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        parse_mode: ParseMode = None,
        entities: list[MessageEntity] | None = None,
        link_preview_options: LinkPreviewOptions = None,
        reply_markup: InlineKeyboardMarkup = None,
        rich_message: InputRichMessage = None,
    ) -> Message | bool:
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
            rich_message=rich_message,
        )
        return (
            Message._parse(me=self, d=result.get("result", {}))
            if isinstance(result.get("result", {}), dict)
            else result.get("result", {})
        )
