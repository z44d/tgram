import inspect
import sys
import tgram

from typing import Union, List, Optional, Literal
from tgram import sync

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


class MessageB:
    async def reply_text(
        self: "tgram.types.Message",
        text: str,
        parse_mode: str = None,
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
            message_thread_id=self.message_thread_id,
            parse_mode=parse_mode or self._me.parse_mode,
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

    async def reply_photo(
        self: "tgram.types.Message",
        photo: Union["tgram.types.InputFile", str],
        caption: str = None,
        parse_mode: str = None,
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
            message_thread_id=self.message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self._me.parse_mode,
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
        audio: Union["tgram.types.InputFile", str],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        duration: int = None,
        performer: str = None,
        title: str = None,
        thumbnail: Union["tgram.types.InputFile", str] = None,
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
            message_thread_id=self.message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self._me.parse_mode,
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
        document: Union["tgram.types.InputFile", str],
        thumbnail: Union["tgram.types.InputFile", str] = None,
        caption: str = None,
        parse_mode: str = None,
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
            message_thread_id=self.message_thread_id,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode or self._me.parse_mode,
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
        video: Union["tgram.types.InputFile", str],
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union["tgram.types.InputFile", str] = None,
        caption: str = None,
        parse_mode: str = None,
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
            message_thread_id=self.message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode or self._me.parse_mode,
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
        animation: Union["tgram.types.InputFile", str],
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union["tgram.types.InputFile", str] = None,
        caption: str = None,
        parse_mode: str = None,
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
            message_thread_id=self.message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode or self._me.parse_mode,
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
        voice: Union["tgram.types.InputFile", str],
        caption: str = None,
        parse_mode: str = None,
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
            message_thread_id=self.message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self._me.parse_mode,
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
        video_note: Union["tgram.types.InputFile", str],
        duration: int = None,
        length: int = None,
        thumbnail: Union["tgram.types.InputFile", str] = None,
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
            message_thread_id=self.message_thread_id,
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
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
    ) -> "tgram.types.Message":
        return await self._me.send_media_group(
            self.chat.id,
            media=media,
            business_connection_id=self.business_connection_id,
            message_thread_id=self.message_thread_id,
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
            message_thread_id=self.message_thread_id,
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

    # TODO More soon

    async def forward(
        self: "tgram.types.Message",
        chat_id: Union[int, str],
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> "tgram.types.Message":
        return await self._me.forward_message(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            message_id=self.id,
            message_thread_id=self.message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
        )

    async def reply_media_from_file_id(
        self: "tgram.types.Message",
        file_id: str,
        caption: str = None,
        parse_mode: str = None,
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
            message_thread_id=self.message_thread_id,
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
        parse_mode: str = None,
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
            message_thread_id=self.message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self._me.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
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
    def __reply_param(self) -> "tgram.types.ReplyParameters":
        return tgram.types.ReplyParameters(self.id)


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


class UserB:
    @property
    def mention(
        self: "tgram.types.User",
        name: str = None,
        parse_mode: Literal["HTML", "Markdown", "MarkdownV2"] = "HTML",
    ) -> str:
        return (
            "[{name}](tg://user?id={id})"
            if parse_mode.lower() != "html"
            else '<a href="tg://user?id={id}">{name}</a>'
        ).format(name=name or self.first_name, id=self.id)

    @property
    def full_name(self: "tgram.types.User") -> str:
        return (
            self.first_name
            if not self.last_name
            else f"{self.first_name} {self.last_name}"
        )

    @property
    def profile_link(self: "tgram.types.User") -> str:
        return (
            f"tg://user?id={self.id}"
            if not self.username
            else f"https://t.me/{self.username}"
        )


for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        sync.wrap(obj)
