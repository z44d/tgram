import tgram

from typing import List, Union


class CallbackB:
    async def answer(
        self: "tgram.types.CallbackQuery",
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> bool:
        return await self._me.answer_callback_query(
            self.id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )

    async def edit_message_text(
        self: "tgram.types.CallbackQuery",
        text: str,
        parse_mode: str = None,
        entities: List["tgram.types.MessageEntity"] = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_text(
            text=text,
            chat_id=self.message.chat.id
            if (self.message and self.message.chat)
            else None,
            message_id=self.message.id if self.message else None,
            inline_message_id=self.inline_message_id,
            parse_mode=parse_mode or self._me.parse_mode,
            entities=entities,
            link_preview_options=link_preview_options,
            reply_markup=reply_markup,
        )

    async def edit_message_caption(
        self: "tgram.types.CallbackQuery",
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_caption(
            chat_id=self.message.chat.id
            if (self.message and self.message.chat)
            else None,
            message_id=self.message.id if self.message else None,
            inline_message_id=self.inline_message_id,
            caption=caption,
            parse_mode=parse_mode or self._me.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )

    async def edit_message_reply_markup(
        self: "tgram.types.CallbackQuery",
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_reply_markup(
            chat_id=self.message.chat.id
            if (self.message and self.message.chat)
            else None,
            message_id=self.message.id if self.message else None,
            inline_message_id=self.inline_message_id,
            reply_markup=reply_markup,
        )

    async def edit_message_media(
        self: "tgram.types.CallbackQuery",
        media: "tgram.types.InputMedia",
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_media(
            media=media,
            inline_message_id=self.inline_message_id,
            chat_id=self.message.chat.id
            if (self.message and self.message.chat)
            else None,
            message_id=self.message.id if self.message else None,
            reply_markup=reply_markup,
        )

    async def edit_message_live_location(
        self: "tgram.types.CallbackQuery",
        latitude: float,
        longitude: float,
        live_period: int = None,
        horizontal_accuracy: float = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_live_location(
            latitude=latitude,
            longitude=longitude,
            chat_id=self.message.chat.id
            if (self.message and self.message.chat)
            else None,
            message_id=self.message.id if self.message else None,
            inline_message_id=self.inline_message_id,
            live_period=live_period,
            horizontal_accuracy=horizontal_accuracy,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            reply_markup=reply_markup,
        )
