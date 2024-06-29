import inspect
import sys

from typing import Union, List
from tgram import sync
from tgram.types import (
    InputFile,
    InputMedia,
    Message,
    MessageEntity,
    LinkPreviewOptions,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    ReplyParameters,
    MessageId,
)


class MessageB:
    async def reply_text(
        self: Message,
        text: str,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            InlineKeyboardMarkup,
            ReplyKeyboardMarkup,
            ReplyKeyboardRemove,
            ForceReply,
        ] = None,
    ) -> Message:
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
        self: Message,
        photo: Union[InputFile, str],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        return await self._me.send_photo(
            self.chat.id,
            photo=photo,
            business_connection_id=self.business_connection_id,
            message_thread_id=self.message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
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
        self: Message,
        audio: Union[InputFile, str],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        performer: str = None,
        title: str = None,
        thumbnail: Union[InputFile, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        return await self._me.send_audio(
            self.chat.id,
            audio=audio,
            business_connection_id=self.business_connection_id,
            message_thread_id=self.message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
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
        self: Message,
        document: Union[InputFile, str],
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        disable_content_type_detection: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        return await self._me.send_document(
            self.chat.id,
            document=document,
            business_connection_id=self.business_connection_id,
            message_thread_id=self.message_thread_id,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
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
        self: Message,
        video: Union[InputFile, str],
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        supports_streaming: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
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
            parse_mode=parse_mode or self.parse_mode,
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
        self: Message,
        animation: Union[InputFile, str],
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
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
            parse_mode=parse_mode or self.parse_mode,
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
        self: Message,
        voice: Union[InputFile, str],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        return await self._me.send_voice(
            self.chat.id,
            voice=voice,
            business_connection_id=self.business_connection_id,
            message_thread_id=self.message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
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
        self: Message,
        video_note: Union[InputFile, str],
        duration: int = None,
        length: int = None,
        thumbnail: Union[InputFile, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
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
        self: Message,
        media: List[InputMedia],
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
    ) -> Message:
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
        self: Message,
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
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
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
        self: Message,
        chat_id: Union[int, str],
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> Message:
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

    async def copy(
        self: Message,
        chat_id: Union[int, str],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> MessageId:
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

    @property
    def id(self: Message) -> int:
        return self.message_id

    @property
    def __reply_param(self) -> ReplyParameters:
        return ReplyParameters(self.id)


for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        sync.wrap(obj)
