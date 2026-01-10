#🔧 copy_message

**Use this method to copy messages of any kind.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`from_chat_id`** (**`int` or `str`** ): **Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)**
- **`message_id`** (**`int`** ): **Message identifier in the chat specified in from_chat_id**
- **`message_thread_id`** (**`int`** ) (`optional`): **Identifier of a message thread, in which the message will be sent**
- **`video_start_timestamp`** (**`int`** ) (`optional`): **New start timestamp for the copied video in the message**
- **`caption`** (**`str`** ) (`optional`): **New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept**
- **`parse_mode`** (**`Literal`** ) (`optional`): **Mode for parsing entities in the new caption.**
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ) (`optional`): **Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages.**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md) or [ReplyKeyboardMarkup](../types/ReplyKeyboardMarkup.md) or [ReplyKeyboardRemove](../types/ReplyKeyboardRemove.md) or [ForceReply](../types/ForceReply.md)** ) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
or to force a reply from the user.**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**
- **`suggested_post_parameters`** (**[SuggestedPostParameters](../types/SuggestedPostParameters.md)** ) (`optional`): **A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.**
- **`message_effect_id`** (**`str`** ) (`optional`): **Unique identifier of the message effect to be added to the message**

##📲 Returns

#### [MessageId](../types/MessageId.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.copy_message(
    chat_id=your_chat_id_here,
    from_chat_id=your_from_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.copy_message(
    chat_id=your_chat_id_here,
    from_chat_id=your_from_chat_id_here,
    message_id=your_message_id_here,
    message_thread_id=your_message_thread_id_here,
    video_start_timestamp=your_video_start_timestamp_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    show_caption_above_media=your_show_caption_above_media_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here,
    direct_messages_topic_id=your_direct_messages_topic_id_here,
    suggested_post_parameters=your_suggested_post_parameters_here,
    message_effect_id=your_message_effect_id_here
)
```
