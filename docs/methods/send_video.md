#🔧 send_video

**Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`video`** (**`Path` or `bytes` or `str`** ): **Video to send. You can either pass a file_id as String to resend a video that is already on the Telegram servers, or upload a new video file using multipart/form-data.**
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of a business connection, in which the message will be sent**
- **`message_thread_id`** (**`int`** ) (`optional`): **Identifier of a message thread, in which the video will be sent**
- **`duration`** (**`int`** ) (`optional`): **Duration of sent video in seconds**
- **`width`** (**`int`** ) (`optional`): **Video width**
- **`height`** (**`int`** ) (`optional`): **Video height**
- **`thumbnail`** (**`Path` or `bytes` or `str`** ) (`optional`): **Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.**
- **`cover`** (**`Path` or `bytes` or `str`** ) (`optional`): **Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name.**
- **`start_timestamp`** (**`int`** ) (`optional`)
- **`caption`** (**`str`** ) (`optional`): **Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing**
- **`parse_mode`** (**`Literal`** ) (`optional`): **Mode for parsing entities in the video caption**
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **List of special entities that appear in the caption, which can be specified instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ) (`optional`): **Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages.**
- **`has_spoiler`** (**`bool`** ) (`optional`): **Pass True, if the video should be sent as a spoiler**
- **`supports_streaming`** (**`bool`** ) (`optional`): **Pass True, if the uploaded video is suitable for streaming**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`** ) (`optional`): **Unique identifier of the message effect**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md) or [ReplyKeyboardMarkup](../types/ReplyKeyboardMarkup.md) or [ReplyKeyboardRemove](../types/ReplyKeyboardRemove.md) or [ForceReply](../types/ForceReply.md)** ) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
or to force a reply from the user.**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**
- **`suggested_post_parameters`** (**[SuggestedPostParameters](../types/SuggestedPostParameters.md)** ) (`optional`): **A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_video(
    chat_id=your_chat_id_here,
    video=your_video_here
)
```

-🔋 **All Parameters**

```python
await bot.send_video(
    chat_id=your_chat_id_here,
    video=your_video_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    duration=your_duration_here,
    width=your_width_here,
    height=your_height_here,
    thumbnail=your_thumbnail_here,
    cover=your_cover_here,
    start_timestamp=your_start_timestamp_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    show_caption_above_media=your_show_caption_above_media_here,
    has_spoiler=your_has_spoiler_here,
    supports_streaming=your_supports_streaming_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here,
    direct_messages_topic_id=your_direct_messages_topic_id_here,
    suggested_post_parameters=your_suggested_post_parameters_here
)
```
