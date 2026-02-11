#🔧 send_video_note

**As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`video_note`** (**`Path` or `bytes` or `str`** )
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of a business connection, in which the message will be sent**
- **`message_thread_id`** (**`int`** ) (`optional`): **Identifier of a message thread, in which the video note will be sent**
- **`duration`** (**`int`** ) (`optional`): **Duration of sent video in seconds**
- **`length`** (**`int`** ) (`optional`): **Video width and height, i.e. diameter of the video message**
- **`thumbnail`** (**`Path` or `bytes` or `str`** ) (`optional`): **Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,
so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.**
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
await bot.send_video_note(
    chat_id=your_chat_id_here,
    video_note=your_video_note_here
)
```

-🔋 **All Parameters**

```python
await bot.send_video_note(
    chat_id=your_chat_id_here,
    video_note=your_video_note_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    duration=your_duration_here,
    length=your_length_here,
    thumbnail=your_thumbnail_here,
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
