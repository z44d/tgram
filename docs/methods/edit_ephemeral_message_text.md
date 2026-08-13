#🔧 edit_ephemeral_message_text

****

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** )
- **`message_id`** (**`int`** )
- **`text`** (**`str`** )
- **`parse_mode`** (**`Literal`** ) (`optional`)
- **`entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`)
- **`link_preview_options`** (**[LinkPreviewOptions](../types/LinkPreviewOptions.md)** ) (`optional`)
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_ephemeral_message_text(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    text=your_text_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_ephemeral_message_text(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    text=your_text_here,
    parse_mode=your_parse_mode_here,
    entities=your_entities_here,
    link_preview_options=your_link_preview_options_here,
    reply_markup=your_reply_markup_here
)
```
