#🔧 edit_ephemeral_message_caption

****

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** )
- **`message_id`** (**`int`** )
- **`caption`** (**`str`** ) (`optional`)
- **`parse_mode`** (**`Literal`** ) (`optional`)
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`)
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_ephemeral_message_caption(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_ephemeral_message_caption(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    reply_markup=your_reply_markup_here
)
```
