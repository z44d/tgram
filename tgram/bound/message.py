import tgram

from typing import Union, List, Optional, Literal

from io import BytesIO
from pathlib import Path


MEDIA_TYPES = {
    "audio",
    "video",
    "photo",
    "animation",
    "voice",
    "video_note",
    "sticker",
    "document",
}

SERVICE_TYPES = {
    "video_chat_participants_invited",
    "video_chat_ended",
    "video_chat_started",
    "video_chat_scheduled",
    "giveaway_completed",
    "general_forum_topic_unhidden",
    "general_forum_topic_hidden",
    "forum_topic_reopened",
    "forum_topic_closed",
    "forum_topic_edited",
    "forum_topic_created",
    "chat_background_set",
    "boost_added",
    "proximity_alert_triggered",
    "write_access_allowed",
    "successful_payment",
    "refunded_payment",
    "users_shared",
    "chat_shared",
    "pinned_message",
    "message_auto_delete_timer_changed",
    "channel_chat_created",
    "supergroup_chat_created",
    "group_chat_created",
    "delete_chat_photo",
    "new_chat_photo",
    "new_chat_title",
    "left_chat_member",
    "new_chat_members",
}


class MessageB:
    async def reply_text(
        self: "tgram.types.Message",
        text: str,
        message_thread_id: int = None,
        parse_mode: "tgram.types.ParseMode" = None,
        entities: List["tgram.types.MessageEntity"] = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_message(
            chat_id=self.chat.id,
            text=text,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options or self._me.link_preview_options,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_markup=reply_markup,
            reply_parameters=self.__reply_param,
        )

    reply = reply_text

    async def reply_photo(
        self: "tgram.types.Message",
        photo: Union[Path, bytes, str],
        caption: str = None,
        message_thread_id: int = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_photo(
            self.chat.id,
            photo=photo,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_audio(
        self: "tgram.types.Message",
        audio: Union[Path, bytes, str],
        caption: str = None,
        message_thread_id: int = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        duration: int = None,
        performer: str = None,
        title: str = None,
        thumbnail: Union[Path, bytes, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_audio(
            self.chat.id,
            audio=audio,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            performer=performer,
            title=title,
            thumbnail=thumbnail,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_document(
        self: "tgram.types.Message",
        document: Union[Path, bytes, str],
        message_thread_id: int = None,
        thumbnail: Union[Path, bytes, str] = None,
        caption: str = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        disable_content_type_detection: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_document(
            self.chat.id,
            document=document,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_content_type_detection=disable_content_type_detection,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_video(
        self: "tgram.types.Message",
        video: Union[Path, bytes, str],
        message_thread_id: int = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[Path, bytes, str] = None,
        caption: str = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        supports_streaming: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_video(
            self.chat.id,
            video=video,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            supports_streaming=supports_streaming,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_animation(
        self: "tgram.types.Message",
        animation: Union[Path, bytes, str],
        message_thread_id: int = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[Path, bytes, str] = None,
        caption: str = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_animation(
            self.chat.id,
            animation=animation,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_voice(
        self: "tgram.types.Message",
        voice: Union[Path, bytes, str],
        caption: str = None,
        message_thread_id: int = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        duration: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_voice(
            self.chat.id,
            voice=voice,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_video_note(
        self: "tgram.types.Message",
        video_note: Union[Path, bytes, str],
        message_thread_id: int = None,
        duration: int = None,
        length: int = None,
        thumbnail: Union[Path, bytes, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_video_note(
            self.chat.id,
            video_note=video_note,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            length=length,
            thumbnail=thumbnail,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_media_group(
        self: "tgram.types.Message",
        media: List["tgram.types.InputMedia"],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
    ) -> "tgram.types.Message":
        return await self._me.send_media_group(
            self.chat.id,
            media=media,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
        )

    async def reply_location(
        self: "tgram.types.Message",
        latitude: float,
        longitude: float,
        message_thread_id: int = None,
        horizontal_accuracy: float = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_location(
            self.chat.id,
            latitude=latitude,
            longitude=longitude,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_paid_media(
        self: "tgram.types.Message",
        star_count: int,
        media: List["tgram.types.InputPaidMedia"],
        caption: str = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_paid_media(
            self.chat.id,
            star_count=star_count,
            media=media,
            caption=caption,
            parse_mode=parse_mode or self.me_parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
            business_connection_id=self.business_connection_id,
        )

    async def reply_chat_action(
        self: "tgram.types.Message", action: str, message_thread_id: int = None
    ) -> bool:
        return await self._me.send_chat_action(
            self.chat.id,
            action=action,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
        )

    async def reply_contact(
        self: "tgram.types.Message",
        phone_number: str,
        first_name: str,
        last_name: str = None,
        vcard: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_contact(
            self.chat.id,
            phone_number=phone_number,
            first_name=first_name,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            last_name=last_name,
            vcard=vcard,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_dice(
        self: "tgram.types.Message",
        emoji: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_dice(
            self.chat.id,
            business_connection_id=self.usiness_connection_id,
            message_thread_id=message_thread_id,
            emoji=emoji,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_game(
        self: "tgram.types.Message",
        game_short_name: str,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> "tgram.types.Message":
        return await self._me.send_game(
            self.chat.id,
            game_short_name=game_short_name,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_invoice(
        self: "tgram.types.Message",
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List["tgram.types.LabeledPrice"],
        provider_token: str = None,
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        start_parameter: str = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> "tgram.types.Message":
        return await self._me.send_invoice(
            self.chat.id,
            title=title,
            description=description,
            payload=payload,
            currency=currency,
            prices=prices,
            message_thread_id=message_thread_id,
            provider_token=provider_token,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            start_parameter=start_parameter,
            provider_data=provider_data,
            photo_url=photo_url,
            photo_size=photo_size,
            photo_width=photo_width,
            photo_height=photo_height,
            need_name=need_name,
            need_phone_number=need_phone_number,
            need_email=need_email,
            need_shipping_address=need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider,
            is_flexible=is_flexible,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def reply_sticker(
        self: "tgram.types.Message",
        sticker: Union[Path, bytes, str],
        emoji: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_sticker(
            self.chat.id,
            sticker=sticker,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            emoji=emoji,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def forward(
        self: "tgram.types.Message",
        chat_id: Union[int, str],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> "tgram.types.Message":
        return await self._me.forward_message(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            message_id=self.id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
        )

    async def reply_media_from_file_id(
        self: "tgram.types.Message",
        file_id: str,
        caption: str = None,
        message_thread_id: int = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_media_from_file_id(
            self.chat.id,
            file_id=file_id,
            business_connection_id=self.business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=self.__reply_param,
            reply_markup=reply_markup,
        )

    async def copy(
        self: "tgram.types.Message",
        chat_id: Union[int, str],
        caption: str = None,
        message_thread_id: int = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: "tgram.types.ReplyParameters" = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.MessageId":
        return await self._me.copy_message(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            message_id=self.id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )

    async def edit_text(
        self: "tgram.types.Message",
        text: str,
        parse_mode: "tgram.types.ParseMode" = None,
        entities: List["tgram.types.MessageEntity"] = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_text(
            text=text,
            business_connection_id=self.business_connection_id,
            chat_id=self.chat.id,
            message_id=self.id,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options or self._me.link_preview_options,
            reply_markup=reply_markup,
        )

    edit = edit_text

    async def edit_caption(
        self: "tgram.types.Message",
        caption: str = None,
        parse_mode: "tgram.types.ParseMode" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: bool = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_caption(
            business_connection_id=self.business_connection_id,
            chat_id=self.chat.id,
            message_id=self.id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )

    async def edit_reply_markup(
        self: "tgram.types.Message",
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_reply_markup(
            business_connection_id=self.business_connection_id,
            chat_id=self.chat.id,
            message_id=self.id,
            reply_markup=reply_markup,
        )

    async def edit_media(
        self: "tgram.types.Message",
        media: "tgram.types.InputMedia",
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> Union["tgram.types.Message", "bool"]:
        return await self._me.edit_message_media(
            media=media,
            business_connection_id=self.business_connection_id,
            chat_id=self.chat.id,
            message_id=self.id,
            reply_markup=reply_markup,
        )

    async def edit_live_location(
        self: "tgram.types.Message",
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
            business_connection_id=self.business_connection_id,
            chat_id=self.chat.id,
            message_id=self.id,
            live_period=live_period,
            horizontal_accuracy=horizontal_accuracy,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            reply_markup=reply_markup,
        )

    async def react(
        self: "tgram.types.Message",
        reaction: Union[
            List["tgram.types.ReactionType"], "tgram.types.ReactionType", List[str], str
        ],
    ) -> bool:
        return await self._me.set_message_reaction(
            self.chat.id,
            self.id,
            reaction=[
                tgram.types.ReactionTypeEmoji(i) if isinstance(i, str) else i
                for i in reaction
            ]
            if isinstance(reaction, list)
            else [
                tgram.types.ReactionTypeEmoji(reaction)
                if isinstance(reaction, str)
                else reaction
            ],
        )

    async def download(
        self: "tgram.types.Message", file_path: str = None, in_memory: bool = None
    ) -> Union[Path, BytesIO]:
        if not self.media:
            raise ValueError("This message have no media to download.")

        media = getattr(self, self.media)
        file_id = (
            media[-1].file_id if isinstance(media, list) else media.file_id
        )  # Message.photo is list of PhotoSize
        return await self._me.download_file(
            file_id, file_path=file_path, in_memory=in_memory
        )

    async def delete(self: "tgram.types.Message") -> bool:
        return await self._me.delete_message(self.chat.id, self.id)

    @property
    def id(self: "tgram.types.Message") -> int:
        return self.message_id

    @property
    def media(
        self: "tgram.types.Message",
    ) -> Optional[
        Literal[
            "audio",
            "video",
            "photo",
            "animation",
            "voice",
            "video_note",
            "sticker",
            "document",
        ]
    ]:
        for media_type in MEDIA_TYPES:
            if getattr(self, media_type):
                return media_type

        return None

    @property
    def service(
        self: "tgram.types.Message",
    ) -> Optional[
        Literal[
            "video_chat_participants_invited",
            "video_chat_ended",
            "video_chat_started",
            "video_chat_scheduled",
            "giveaway_completed",
            "general_forum_topic_unhidden",
            "general_forum_topic_hidden",
            "forum_topic_reopened",
            "forum_topic_closed",
            "forum_topic_edited",
            "forum_topic_created",
            "chat_background_set",
            "boost_added",
            "proximity_alert_triggered",
            "write_access_allowed",
            "successful_payment",
            "refunded_payment",
            "users_shared",
            "chat_shared",
            "pinned_message",
            "message_auto_delete_timer_changed",
            "channel_chat_created",
            "supergroup_chat_created",
            "group_chat_created",
            "delete_chat_photo",
            "new_chat_photo",
            "new_chat_title",
            "left_chat_member",
            "new_chat_members",
        ]
    ]:
        for service_type in SERVICE_TYPES:
            if getattr(self, service_type):
                return service_type

        return None

    @property
    def link(self: "tgram.types.Message") -> Optional[str]:
        return (
            (
                "https://t.me/c/{chat_id}/{msg_id}"
                if not self.chat.username
                else "https://t.me/{chat_id}/{msg_id}"
            ).format(
                chat_id=self.chat.username or str(self.chat.id).replace("-100", ""),
                msg_id=self.id,
            )
            if self.chat.type != "private"
            else None
        )

    @property
    def file_id(self: "tgram.types.Message") -> str:
        media = self.media

        if media is None:
            raise ValueError("This message has no media.")

        m = getattr(self, media)

        if isinstance(m, list):
            return getattr(m[-1], "file_id")
        else:
            return getattr(m, "file_id")

    @property
    def user(self: "tgram.types.Message") -> Optional["tgram.types.User"]:
        return self.from_user

    sender_user = user

    @property
    def __reply_param(self) -> "tgram.types.ReplyParameters":
        return tgram.types.ReplyParameters(self.id, allow_sending_without_reply=True)
