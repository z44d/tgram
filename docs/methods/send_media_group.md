#🔧 send_media_group

**Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`media`** (**List of [InputMediaAudio](../types/InputMediaAudio.md) or [InputMediaDocument](../types/InputMediaDocument.md) or [InputMediaPhoto](../types/InputMediaPhoto.md) or [InputMediaVideo](../types/InputMediaVideo.md)** ): **A JSON-serialized array describing messages to be sent, must include 2-10 items**
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of a business connection, in which the message will be sent**
- **`message_thread_id`** (**`int`** ) (`optional`): **Identifier of a message thread, in which the messages will be sent**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the messages silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`** ) (`optional`): **Unique identifier of the message effect**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**

##📲 Returns

#### List of [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_media_group(
    chat_id=your_chat_id_here,
    media=your_media_here
)
```

-🔋 **All Parameters**

```python
await bot.send_media_group(
    chat_id=your_chat_id_here,
    media=your_media_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here,
    direct_messages_topic_id=your_direct_messages_topic_id_here
)
```
