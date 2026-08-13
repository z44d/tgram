#🔧 send_live_photo

**Use this method to send a live photo.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel**
- **`live_photo`** (**`str`** ): **Live photo to send. Pass a file_id to send a file that exists on the Telegram servers**
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of the business connection to send the message through**
- **`message_thread_id`** (**`int`** ) (`optional`): **Unique identifier for the target message thread (topic) of the forum**
- **`caption`** (**`str`** ) (`optional`): **Live photo caption, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`Literal`** ) (`optional`): **Mode for parsing entities in the live photo caption**
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **List of special entities that appear in the caption**
- **`show_caption_above_media`** (**`bool`** ) (`optional`): **True, if the caption must be shown above the message media**
- **`has_spoiler`** (**`bool`** ) (`optional`): **True, if the live photo needs to be covered with a spoiler animation**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`** ) (`optional`): **Unique identifier of the message effect**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md) or [ReplyKeyboardMarkup](../types/ReplyKeyboardMarkup.md) or [ReplyKeyboardRemove](../types/ReplyKeyboardRemove.md) or [ForceReply](../types/ForceReply.md)** ) (`optional`): **Additional interface options.**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_live_photo(
    chat_id=your_chat_id_here,
    live_photo=your_live_photo_here
)
```

-🔋 **All Parameters**

```python
await bot.send_live_photo(
    chat_id=your_chat_id_here,
    live_photo=your_live_photo_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    show_caption_above_media=your_show_caption_above_media_here,
    has_spoiler=your_has_spoiler_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here
)
```
