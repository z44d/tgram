#🔧 edit_message_caption

**Use this method to edit captions of messages.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ) (`optional`)
- **`chat_id`** (**`int` or `str`** ) (`optional`)
- **`message_id`** (**`int`** ) (`optional`)
- **`inline_message_id`** (**`str`** ) (`optional`)
- **`caption`** (**`str`** ) (`optional`)
- **`parse_mode`** (**`Literal`** ) (`optional`)
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`)
- **`show_caption_above_media`** (**`bool`** ) (`optional`)
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md) or `bool`

##📀 Examples


-🔋 **All Parameters**

```python
await bot.edit_message_caption(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    inline_message_id=your_inline_message_id_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    show_caption_above_media=your_show_caption_above_media_here,
    reply_markup=your_reply_markup_here
)
```
