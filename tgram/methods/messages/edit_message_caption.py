
import tgram
from tgram.types import InlineKeyboardMarkup, Message, MessageEntity, ParseMode
from tgram.utils import convert_to_inline_keyboard_markup, get_parse_mode


class EditMessageCaption:
    async def edit_message_caption(
        self: "tgram.TgBot",
        business_connection_id: str | None = None,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        caption: str | None = None,
        parse_mode: ParseMode = None,
        caption_entities: list[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message | bool:
        """
        Use this method to edit captions of messages.
        On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.
        """
        result = await self(
            "editMessageCaption",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            caption=caption,
            parse_mode=get_parse_mode(self, parse_mode),
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return (
            Message._parse(me=self, d=result.get("result", {}))
            if isinstance(result.get("result", {}), dict)
            else result.get("result", {})
        )
