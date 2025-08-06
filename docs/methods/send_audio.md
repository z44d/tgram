# send_audio

**Use this method to send audio files, if you want Telegram clients to display them in the music player.**

## Parameters

- **`chat_id`** (**`int, str`**): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`audio`** (**`Path, bytes, str`**): **Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended),
pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data.
Audio must be in the .MP3 or .M4A format.**
- **`business_connection_id`** (**`str`**) (`optional`): **Unique identifier for the target business connection**
- **`message_thread_id`** (**`int`**) (`optional`): **Identifier of a message thread, in which the message will be sent**
- **`caption`** (**`str`**) (`optional`): **Audio caption, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`Literal`**) (`optional`): **Mode for parsing entities in the audio caption. See formatting options for more details.**
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)**) (`optional`): **A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode**
- **`duration`** (**`int`**) (`optional`): **Duration of the audio in seconds**
- **`performer`** (**`str`**) (`optional`): **Performer**
- **`title`** (**`str`**) (`optional`): **Track name**
- **`thumbnail`** (**`Path, bytes, str`**) (`optional`): **Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,
so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>**
- **`disable_notification`** (**`bool`**) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`**) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`**) (`optional`): **Unique identifier for the message effect**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)**) (`optional`): **Reply parameters.**
- **`reply_markup`** (**`InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply`**) (`optional`)
- **`allow_paid_broadcast`** (**`bool`**) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**

## Returns

#### [Message](../types/Message.md)

## Examples

- **Required Parameters**

```python
await bot.send_audio(
    chat_id=your_chat_id_here,
    audio=your_audio_here
)
```

- **All Parameters**

```python
await bot.send_audio(
    chat_id=your_chat_id_here,
    audio=your_audio_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    duration=your_duration_here,
    performer=your_performer_here,
    title=your_title_here,
    thumbnail=your_thumbnail_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here
)
```
