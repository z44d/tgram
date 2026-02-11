#🔧 send_chat_action

**Use this method when you need to tell the user that something is happening on the bot's side.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel**
- **`action`** (**`str`** ): **Type of action to broadcast. Choose one, depending on what the user is about
to receive: typing for text messages, upload_photo for photos, record_video or upload_video
for videos, record_voice or upload_voice for voice notes, upload_document for general files,
choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes.**
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of a business connection, in which the message will be sent**
- **`message_thread_id`** (**`int`** ) (`optional`): **The thread to which the message will be sent(supergroups only)**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_chat_action(
    chat_id=your_chat_id_here,
    action=your_action_here
)
```

-🔋 **All Parameters**

```python
await bot.send_chat_action(
    chat_id=your_chat_id_here,
    action=your_action_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here
)
```
