import tgram
from typing import List, Union, Optional


class CallbackB:
    async def answer(
        self: "tgram.types.CallbackQuery",
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> bool:
        """
        Answer the callback query.

        Args:
            text (str, optional): Notification text.
            show_alert (bool, optional): If True, an alert will be shown.
            url (str, optional): URL to be opened.
            cache_time (int, optional): The maximum amount of time in seconds that the result of the callback query may be cached client-side.

        Returns:
            bool: True on success.
        """
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
        parse_mode: "tgram.types.ParseMode" = None,
        entities: List["tgram.types.MessageEntity"] = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        """
        Edit the text of the message.

        Args:
            text (str): New text of the message.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the message text.
            entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in message text.
            link_preview_options (tgram.types.LinkPreviewOptions, optional): Options for link previews.
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): New inline keyboard.

        Returns:
            Union[tgram.types.Message, bool]: The edited message or True on success.
        """
        return await self._me.edit_message_text(
            text=text,
            chat_id=self.message.chat.id
            if (self.message and self.message.chat)
            else None,
            message_id=self.message.id if self.message else None,
            inline_message_id=self.inline_message_id,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options,
            reply_markup=reply_markup,
        )

    async def edit_message_caption(
        self: "tgram.types.CallbackQuery",
        caption: str = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        """
        Edit the caption of the message.

        Args:
            caption (str, optional): New caption of the message.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the message caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in message caption.
            show_caption_above_media (bool, optional): If True, the caption will be shown above the media.
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): New inline keyboard.

        Returns:
            Union[tgram.types.Message, bool]: The edited message or True on success.
        """
        return await self._me.edit_message_caption(
            chat_id=self.message.chat.id
            if (self.message and self.message.chat)
            else None,
            message_id=self.message.id if self.message else None,
            inline_message_id=self.inline_message_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )

    async def edit_message_reply_markup(
        self: "tgram.types.CallbackQuery",
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        """
        Edit the reply markup of the message.

        Args:
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): New inline keyboard.

        Returns:
            Union[tgram.types.Message, bool]: The edited message or True on success.
        """
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
        """
        Edit the media of the message.

        Args:
            media (tgram.types.InputMedia): New media of the message.
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): New inline keyboard.

        Returns:
            Union[tgram.types.Message, bool]: The edited message or True on success.
        """
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
        live_period: int,
    ) -> Union["tgram.types.Message", "bool"]:
        """
        Edit the live location of the message.

        Args:
            latitude (float): Latitude of the new location.
            longitude (float): Longitude of the new location.
            live_period (int): Period in seconds for which the location will be updated.

        Returns:
            Union[tgram.types.Message, bool]: The edited message or True on success.
        """
        return await self._me.edit_message_live_location(
            latitude=latitude,
            longitude=longitude,
            chat_id=self.message.chat.id
            if (self.message and self.message.chat)
            else None,
            message_id=self.message.id if self.message else None,
            inline_message_id=self.inline_message_id,
            live_period=live_period,
        )

    @property
    def user(self: "tgram.types.CallbackQuery") -> Optional["tgram.types.User"]:
        """
        Get the user who sent the callback query.

        Returns:
            Optional[tgram.types.User]: The user who sent the callback query.
        """
        return self.from_user

    sender_user = user
