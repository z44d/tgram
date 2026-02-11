#🔧 send_media_from_file_id

****

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** )
- **`file_id`** (**`str`** )
- **`business_connection_id`** (**`str`** ) (`optional`)
- **`message_thread_id`** (**`int`** ) (`optional`)
- **`caption`** (**`str`** ) (`optional`)
- **`parse_mode`** (**`Literal`** ) (`optional`)
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`)
- **`show_caption_above_media`** (**`bool`** ) (`optional`)
- **`disable_notification`** (**`bool`** ) (`optional`)
- **`protect_content`** (**`bool`** ) (`optional`)
- **`message_effect_id`** (**`str`** ) (`optional`)
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`)
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md) or [ReplyKeyboardMarkup](../types/ReplyKeyboardMarkup.md) or [ReplyKeyboardRemove](../types/ReplyKeyboardRemove.md) or [ForceReply](../types/ForceReply.md)** ) (`optional`)
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_media_from_file_id(
    chat_id=your_chat_id_here,
    file_id=your_file_id_here
)
```

-🔋 **All Parameters**

```python
await bot.send_media_from_file_id(
    chat_id=your_chat_id_here,
    file_id=your_file_id_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    show_caption_above_media=your_show_caption_above_media_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here
)
```
