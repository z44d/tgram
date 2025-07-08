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
    "checklist_tasks_added",
    "checklist_tasks_done",
    "direct_message_price_changed",
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
        """
        Sends a text message in reply to the current message.

        Args:
            text (str): The text of the message to be sent.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the message text.
            entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in message text, which can be specified instead of parse_mode.
            link_preview_options (tgram.types.LinkPreviewOptions, optional): Options for link previews.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_text(
                text="<code>Hello, world!</code>",
                parse_mode="HTML",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a photo in reply to the current message.

        Args:
            photo (Union[Path, bytes, str]): The photo to be sent. Can be a file path, bytes, or a URL.
            caption (str, optional): Caption for the photo.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the photo caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            show_caption_above_media (bool, optional): Whether to show the caption above the media.
            has_spoiler (bool, optional): Whether the photo contains a spoiler.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_photo(
                photo="path/to/photo.jpg",
                caption="Check out this *photo!*",
                parse_mode="Markdown",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends an audio file in reply to the current message.

        Args:
            audio (Union[Path, bytes, str]): The audio file to be sent. Can be a file path, bytes, or a URL.
            caption (str, optional): Caption for the audio file.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the audio caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            duration (int, optional): Duration of the audio in seconds.
            performer (str, optional): Performer of the audio.
            title (str, optional): Title of the audio.
            thumbnail (Union[Path, bytes, str], optional): Thumbnail of the audio file.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_audio(
                audio="path/to/audio.mp3",
                caption="Here is the audio file.",
                parse_mode="Markdown",
                duration=120,
                performer="Artist Name",
                title="Audio Title",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a document in reply to the current message.

        Args:
            document (Union[Path, bytes, str]): The document to send. Can be a file path, bytes, or a URL.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            thumbnail (Union[Path, bytes, str], optional): Thumbnail of the file sent; can be ignored if server-side thumbnail generation is supported.
            caption (str, optional): Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the document caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            disable_content_type_detection (bool, optional): Disables automatic server-side content type detection for files uploaded using multipart/form-data.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Unique identifier for the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_document(
                document="path/to/document.pdf",
                caption="Here is the document you requested.",
                parse_mode="Markdown",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a video in reply to the current message.

        Args:
            video (Union[Path, bytes, str]): The video to be sent. Can be a file path, bytes, or a URL.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            duration (int, optional): Duration of the video in seconds.
            width (int, optional): Video width.
            height (int, optional): Video height.
            thumbnail (Union[Path, bytes, str], optional): Thumbnail of the video.
            caption (str, optional): Caption for the video.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the video caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            show_caption_above_media (bool, optional): Whether to show the caption above the media.
            has_spoiler (bool, optional): Whether the video contains a spoiler.
            supports_streaming (bool, optional): Whether the video supports streaming.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_video(
                video="path/to/video.mp4",
                caption="Check out this video!",
                parse_mode="Markdown",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends an animation (GIF) in reply to the current message.

        Args:
            animation (Union[Path, bytes, str]): The animation to be sent. Can be a file path, bytes, or a URL.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            duration (int, optional): Duration of the animation in seconds.
            width (int, optional): Width of the animation.
            height (int, optional): Height of the animation.
            thumbnail (Union[Path, bytes, str], optional): Thumbnail of the animation.
            caption (str, optional): Caption for the animation.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the animation caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            show_caption_above_media (bool, optional): Whether to show the caption above the media.
            has_spoiler (bool, optional): Whether the animation contains a spoiler.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_animation(
                animation="path/to/animation.gif",
                caption="Check out this cool animation!",
                parse_mode="Markdown",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a voice message in reply to the current message.

        Args:
            voice (Union[Path, bytes, str]): The voice message to be sent. Can be a file path, bytes, or a URL.
            caption (str, optional): Caption for the voice message.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the voice message caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            duration (int, optional): Duration of the voice message in seconds.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_voice(
                voice="path/to/voice.ogg",
                caption="Here is the voice message.",
                parse_mode="Markdown",
                duration=60,
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a video note in reply to the current message.

        Args:
            video_note (Union[Path, bytes, str]): The video note to be sent. Can be a file path, bytes, or a URL.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            duration (int, optional): Duration of the video note in seconds.
            length (int, optional): Video width and height (diameter of the video message) in pixels.
            thumbnail (Union[Path, bytes, str], optional): Thumbnail of the video note.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_video_note(
                video_note="path/to/video_note.mp4",
                duration=60,
                length=240,
                disable_notification=True
            )
            ```
        """
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
    ) -> List["tgram.types.Message"]:
        """
        Sends a group of photos or videos as an album in reply to the current message.

        Args:
            media (List[tgram.types.InputMedia]): A list of media to be sent. Each media item can be a photo or video.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.

        Returns:
            List[tgram.types.Message]: The sent messages.

        Example:
            ```python
            media = [
                tgram.types.InputMediaPhoto(media="path/to/photo1.jpg"),
                tgram.types.InputMediaPhoto(media="path/to/photo2.jpg"),
                tgram.types.InputMediaVideo(media="path/to/video.mp4")
            ]
            await message.reply_media_group(
                media=media,
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a location in reply to the current message.

        Args:
            latitude (float): Latitude of the location.
            longitude (float): Longitude of the location.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            horizontal_accuracy (float, optional): The radius of uncertainty for the location, measured in meters; 0-1500.
            live_period (int, optional): Period in seconds for which the location will be updated (should be between 60 and 86400).
            heading (int, optional): For live locations, a direction in which the user is moving, in degrees; 1-360.
            proximity_alert_radius (int, optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters; 1-100000.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_location(
                latitude=37.7749,
                longitude=-122.4194,
                live_period=3600,
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a paid media message in reply to the current message.

        Args:
            star_count (int): Number of stars required to view the media.
            media (List[tgram.types.InputPaidMedia]): A list of paid media to be sent.
            caption (str, optional): Caption for the media.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the media caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            show_caption_above_media (bool, optional): Whether to show the caption above the media.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            media = [
                tgram.types.InputPaidMedia(media="path/to/photo1.jpg"),
                tgram.types.InputPaidMedia(media="path/to/photo2.jpg")
            ]
            await message.reply_paid_media(
                star_count=5,
                media=media,
                caption="Check out this paid media!",
                parse_mode="Markdown",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a chat action in reply to the current message.

        Args:
            action (str): Type of action to broadcast. Choose one, depending on what the user is about to receive: 'typing' for text messages, 'upload_photo' for photos, 'record_video' or 'upload_video' for videos, 'record_voice' or 'upload_voice' for voice notes, 'upload_document' for general files, 'find_location' for location data, 'record_video_note' or 'upload_video_note' for video notes.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

        Returns:
            bool: True on success.

        Example:
            ```python
            await message.reply_chat_action(
                action="typing"
            )
            ```
        """
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
        """
        Sends a contact in reply to the current message.

        Args:
            phone_number (str): Contact's phone number.
            first_name (str): Contact's first name.
            last_name (str, optional): Contact's last name.
            vcard (str, optional): Additional data about the contact in the form of a vCard, 0-2048 bytes.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_contact(
                phone_number="+123456789",
                first_name="John",
                last_name="Doe",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a dice message in reply to the current message.

        Args:
            emoji (str, optional): Emoji on which the dice throw animation is based. Currently, must be one of '🎲', '🎯', '🏀', '⚽', '🎳', or '🎰'.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_dice(
                emoji="🎲",
                disable_notification=True
            )
            ```
        """
        return await self._me.send_dice(
            self.chat.id,
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

    async def reply_game(
        self: "tgram.types.Message",
        game_short_name: str,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
    ) -> "tgram.types.Message":
        """
        Sends a game in reply to the current message.

        Args:
            game_short_name (str): Short name of the game.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): Additional interface options. A JSON-serialized object for an inline keyboard.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_game(
                game_short_name="game_name",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends an invoice in reply to the current message.

        Args:
            title (str): Product name, 1-32 characters.
            description (str): Product description, 1-255 characters.
            payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
            currency (str): Three-letter ISO 4217 currency code.
            prices (List[tgram.types.LabeledPrice]): Price breakdown, a list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.).
            provider_token (str, optional): Payment provider token, obtained via BotFather.
            max_tip_amount (int, optional): The maximum accepted amount for tips in the smallest units of the currency.
            suggested_tip_amounts (List[int], optional): A list of suggested amounts of tips in the smallest units of the currency.
            start_parameter (str, optional): Unique deep-linking parameter that can be used to generate this invoice when used as a start parameter.
            provider_data (str, optional): JSON-encoded data about the invoice, which will be shared with the payment provider.
            photo_url (str, optional): URL of the product photo for the invoice.
            photo_size (int, optional): Photo size.
            photo_width (int, optional): Photo width.
            photo_height (int, optional): Photo height.
            need_name (bool, optional): Pass True if you require the user's full name to complete the order.
            need_phone_number (bool, optional): Pass True if you require the user's phone number to complete the order.
            need_email (bool, optional): Pass True if you require the user's email address to complete the order.
            need_shipping_address (bool, optional): Pass True if you require the user's shipping address to complete the order.
            send_phone_number_to_provider (bool, optional): Pass True if the user's phone number should be sent to the provider.
            send_email_to_provider (bool, optional): Pass True if the user's email address should be sent to the provider.
            is_flexible (bool, optional): Pass True if the final price depends on the shipping method.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): Additional interface options. A JSON-serialized object for an inline keyboard.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            prices = [tgram.types.LabeledPrice(label="Product", amount=1000)]
            await message.reply_invoice(
                title="Product Title",
                description="Product Description",
                payload="payload",
                currency="USD",
                prices=prices,
                provider_token="provider_token",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a sticker in reply to the current message.

        Args:
            sticker (Union[Path, bytes, str]): The sticker to be sent. Can be a file path, bytes, or a URL.
            emoji (str, optional): Emoji associated with the sticker.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_sticker(
                sticker="path/to/sticker.webp",
                emoji="😊",
                disable_notification=True
            )
            ```
        """
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
        """
        Forwards the current message to another chat.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the forwarded message from forwarding and saving.

        Returns:
            tgram.types.Message: The forwarded message.

        Example:
            ```python
            await message.forward(
                chat_id="@target_channel",
                disable_notification=True
            )
            ```
        """
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
        """
        Sends a media message using a file_id in reply to the current message.

        Args:
            file_id (str): The file_id of the media to be sent.
            caption (str, optional): Caption for the media.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the media caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            show_caption_above_media (bool, optional): Whether to show the caption above the media.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            message_effect_id (str, optional): Identifier of the message effect.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.Message: The sent message.

        Example:
            ```python
            await message.reply_media_from_file_id(
                file_id="ABC123",
                caption="Check out this media!",
                parse_mode="Markdown",
                disable_notification=True
            )
            ```
        """
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
        """
        Copies the current message to another chat.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
            caption (str, optional): New caption for the message, if any.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the message caption.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode.
            show_caption_above_media (bool, optional): Whether to show the caption above the media.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the copied message from forwarding and saving.
            reply_parameters (tgram.types.ReplyParameters, optional): Additional parameters for the reply.
            reply_markup (Union[tgram.types.InlineKeyboardMarkup, tgram.types.ReplyKeyboardMarkup, tgram.types.ReplyKeyboardRemove, tgram.types.ForceReply], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            tgram.types.MessageId: The ID of the copied message.

        Example:
            ```python
            await message.copy(
                chat_id="@target_channel",
                caption="Check out this copied message!",
                disable_notification=True
            )
            ```
        """
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
        """
        Edit the text of a message.

        Parameters:
        self (tgram.types.Message): The message object itself.
        text (str): New text of the message.
        parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the message text. Defaults to None.
        entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in message text. Defaults to None.
        link_preview_options (tgram.types.LinkPreviewOptions, optional): Options for link previews in the message. Defaults to None.
        reply_markup (tgram.types.InlineKeyboardMarkup, optional): Inline keyboard attached to the message. Defaults to None.

        Returns:
        Union[tgram.types.Message, bool]: On success, the edited message is returned, otherwise True is returned.

        Example:
        ```python
        message = await bot.send_message(chat_id, "Original text")
        edited_message = await message.edit_text(
            text="Edited text",
            parse_mode=tgram.types.ParseMode.MARKDOWN,
            entities=[tgram.types.MessageEntity(type="bold", offset=0, length=5)],
            link_preview_options=tgram.types.LinkPreviewOptions(disable_web_page_preview=True),
            reply_markup=tgram.types.InlineKeyboardMarkup(inline_keyboard=[[tgram.types.InlineKeyboardButton(text="Button", callback_data="data")]])
        ```
        """
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
        """
        Edit the caption of a message.

        Args:
            caption (str, optional): New caption of the message. Defaults to None.
            parse_mode (tgram.types.ParseMode, optional): Mode for parsing entities in the message caption. Defaults to None.
            caption_entities (List[tgram.types.MessageEntity], optional): List of special entities that appear in the caption, which can be specified instead of parse_mode. Defaults to None.
            show_caption_above_media (bool, optional): Whether to show the caption above the media. Defaults to None.
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): Inline keyboard attached to the message. Defaults to None.

        Returns:
            Union[tgram.types.Message, bool]: On success, the edited message is returned, otherwise True is returned.

        Example:
            ```python
            message = await bot.send_photo(chat_id, photo="path/to/photo.jpg", caption="Original caption")
            edited_message = await message.edit_caption(
                caption="Edited caption",
                parse_mode=tgram.types.ParseMode.MARKDOWN,
                caption_entities=[tgram.types.MessageEntity(type="bold", offset=0, length=6)],
                show_caption_above_media=True,
                reply_markup=tgram.types.InlineKeyboardMarkup(inline_keyboard=[[tgram.types.InlineKeyboardButton(text="Button", callback_data="data")]])
            )
            ```
        """
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
        """
        Edit the reply markup of a message.

        Args:
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): Inline keyboard attached to the message. Defaults to None.

        Returns:
            Union[tgram.types.Message, bool]: On success, the edited message is returned, otherwise True is returned.

        Example:
            ```python
            message = await bot.send_message(chat_id, "Original text")
            edited_message = await message.edit_reply_markup(
                reply_markup=tgram.types.InlineKeyboardMarkup(
                    inline_keyboard=[
                        [tgram.types.InlineKeyboardButton(text="Button", callback_data="data")]
                    ]
                )
            )
            ```
        """
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
        """
        Edit the media content of a message.

        Args:
            media (tgram.types.InputMedia): The new media content to replace the current media.
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): Inline keyboard attached to the message. Defaults to None.

        Returns:
            Union[tgram.types.Message, bool]: On success, the edited message is returned, otherwise True is returned.

        Example:
            ```python
            new_media = tgram.types.InputMediaPhoto(media="path/to/new_photo.jpg")
            edited_message = await message.edit_media(
                media=new_media,
                reply_markup=tgram.types.InlineKeyboardMarkup(
                    inline_keyboard=[
                        [tgram.types.InlineKeyboardButton(text="Button", callback_data="data")]
                    ]
                )
            )
            ```
        """
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
        """
        Edits the live location of a message.

        Args:
            latitude (float): Latitude of the new location.
            longitude (float): Longitude of the new location.
            live_period (int, optional): Period in seconds for which the location will be updated (should be between 60 and 86400).
            horizontal_accuracy (float, optional): The radius of uncertainty for the location, measured in meters; 0-1500.
            heading (int, optional): For live locations, a direction in which the user is moving, in degrees; 1-360.
            proximity_alert_radius (int, optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters; 1-100000.
            reply_markup (tgram.types.InlineKeyboardMarkup, optional): Inline keyboard attached to the message.

        Returns:
            Union[tgram.types.Message, bool]: On success, the edited message is returned, otherwise True is returned.

        Example:
            ```python
            await message.edit_live_location(
                latitude=37.7749,
                longitude=-122.4194,
                live_period=3600,
                horizontal_accuracy=50,
                heading=90,
                proximity_alert_radius=100,
                reply_markup=tgram.types.InlineKeyboardMarkup(
                    inline_keyboard=[
                        [tgram.types.InlineKeyboardButton(text="Stop", callback_data="stop")]
                    ]
                )
            )
            ```
        """
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
        """
        Adds a reaction to the current message.

        Args:
            reaction (Union[List[tgram.types.ReactionType], tgram.types.ReactionType, List[str], str]):
                The reaction(s) to be added. Can be a list of ReactionType objects, a single ReactionType object,
                a list of emoji strings, or a single emoji string.

        Returns:
            bool: True on success.

        Example:
            ```python
            # Adding a single reaction using an emoji string
            await message.react(reaction="👍")

            # Adding multiple reactions using emoji strings
            await message.react(reaction=["👍", "❤️"])

            # Adding a single reaction using a ReactionType object
            reaction_type = tgram.types.ReactionTypeEmoji("👍")
            await message.react(reaction=reaction_type)

            # Adding multiple reactions using ReactionType objects
            reaction_types = [tgram.types.ReactionTypeEmoji("👍"), tgram.types.ReactionTypeEmoji("❤️")]
            await message.react(reaction=reaction_types)
            ```
        """
        reactions = (
            [
                tgram.types.ReactionTypeEmoji(i) if isinstance(i, str) else i
                for i in reaction
            ]
            if isinstance(reaction, list)
            else [
                tgram.types.ReactionTypeEmoji(reaction)
                if isinstance(reaction, str)
                else reaction
            ]
        )
        return await self._me.set_message_reaction(
            self.chat.id,
            self.id,
            reaction=reactions,
        )

    async def download(
        self: "tgram.types.Message", file_path: str = None, in_memory: bool = None
    ) -> Union[Path, BytesIO]:
        """
        Downloads the media content of the message.

        Args:
            file_path (str, optional): The path where the file should be saved. If not provided, the file will be saved in the current directory with its original name.
            in_memory (bool, optional): If True, the file will be downloaded into memory and returned as a BytesIO object. If False or not provided, the file will be saved to disk.

        Returns:
            Union[Path, BytesIO]: The path to the saved file or a BytesIO object containing the file data.

        Raises:
            ValueError: If the message does not contain any media.

        Example:
            ```python
            # Downloading a photo to a specific path
            await message.download(file_path="downloads/photo.jpg")

            # Downloading a video into memory
            video_data = await message.download(in_memory=True)
            with open("downloads/video.mp4", "wb") as f:
                f.write(video_data.getbuffer())
            ```
        """
        if not self.media:
            raise ValueError("This message has no media to download.")

        media = getattr(self, self.media)
        file_id = media[-1].file_id if isinstance(media, list) else media.file_id
        return await self._me.download_file(
            file_id, file_path=file_path, in_memory=in_memory
        )

    async def delete(self: "tgram.types.Message") -> bool:
        """
        Deletes the current message.

        Args:
            self (tgram.types.Message): The message object itself.

        Returns:
            bool: True on success.

        Example:
            ```python
            # Assuming 'message' is an instance of tgram.types.Message
            success = await message.delete()
            if success:
                print("Message deleted successfully.")
            else:
                print("Failed to delete the message.")
            ```
        """
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
        """
        Returns the type of media contained in the message, if any.

        This property checks the message for various types of media (e.g., audio, video, photo, etc.) and returns the type of media if found.

        Returns:
            Optional[Literal["audio", "video", "photo", "animation", "voice", "video_note", "sticker", "document"]]: The type of media contained in the message, or None if no media is found.

        Example:
            ```python
            media_type = message.media
            if media_type:
                print(f"The message contains {media_type}.")
            else:
                print("The message does not contain any media.")
            ```
        """
        for media_type in MEDIA_TYPES:
            if getattr(self, media_type):
                return media_type

        return None

    @property
    def service(
        self: "tgram.types.Message",
    ) -> Optional[str]:
        """
        Returns the type of service message contained in the message, if any.

        This property checks the message for various types of service messages (e.g., video chat started, pinned message, etc.) and returns the type of service message if found.

        Returns:
            Optional[str]: The type of service message contained in the message, or None if no service message is found.

        Example:
            ```python
            service_type = message.service
            if service_type:
                print(f"The message contains a service message of type {service_type}.")
            else:
                print("The message does not contain any service message.")
            ```
        """
        for service_type in SERVICE_TYPES:
            if getattr(self, service_type):
                return service_type

        return None

    @property
    def link(self: "tgram.types.Message") -> Optional[str]:
        """
        Generates a link to the message.

        This property generates a link to the message based on the chat type and chat username or ID.

        Returns:
            Optional[str]: The link to the message, or None if the chat type is private.

        Example:
            ```python
            message_link = message.link
            if message_link:
                print(f"Message link: {message_link}")
            else:
                print("This message is in a private chat and does not have a link.")
            ```
        """
        if self.chat.type == "private":
            return None

        chat_id = self.chat.username or str(self.chat.id).replace("-100", "")
        return f"https://t.me/{chat_id}/{self.id}"

    @property
    def file_id(self: "tgram.types.Message") -> str:
        """
        Returns the file_id of the media contained in the message.

        This property checks the message for various types of media (e.g., audio, video, photo, etc.) and returns the file_id of the media if found.

        Raises:
            ValueError: If the message does not contain any media.

        Returns:
            str: The file_id of the media contained in the message.

        Example:
            ```python
            file_id = message.file_id
            print(f"The file_id of the media is: {file_id}")
            ```
        """
        media_type = self.media

        if media_type is None:
            raise ValueError("This message has no media.")

        media = getattr(self, media_type)

        if isinstance(media, list):
            return media[-1].file_id
        else:
            return media.file_id

    @property
    def user(self: "tgram.types.Message") -> Optional["tgram.types.User"]:
        """
        Returns the user who sent the message.

        This property retrieves the user who sent the message, if available.

        Returns:
            Optional[tgram.types.User]: The user who sent the message, or None if the user is not available.

        Example:
            ```python
            user = message.user
            if user:
                print(f"Message sent by: {user.first_name}")
            else:
                print("User information is not available.")
            ```
        """
        return self.from_user

    sender_user = user

    @property
    def __reply_param(self) -> "tgram.types.ReplyParameters":
        return tgram.types.ReplyParameters(self.id, allow_sending_without_reply=True)
