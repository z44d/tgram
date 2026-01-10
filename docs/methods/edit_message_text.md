#🔧 edit_message_text

**Use this method to edit text and game messages.**

##⚙️ Parameters

- **`text`** (**`str`** )
- **`business_connection_id`** (**`str`** ) (`optional`)
- **`chat_id`** (**`int` or `str`** ) (`optional`)
- **`message_id`** (**`int`** ) (`optional`)
- **`inline_message_id`** (**`str`** ) (`optional`)
- **`parse_mode`** (**`Literal`** ) (`optional`)
- **`entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`)
- **`link_preview_options`** (**[LinkPreviewOptions](../types/LinkPreviewOptions.md)** ) (`optional`)
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md) or `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_message_text(
    text=your_text_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_message_text(
    text=your_text_here,
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    inline_message_id=your_inline_message_id_here,
    parse_mode=your_parse_mode_here,
    entities=your_entities_here,
    link_preview_options=your_link_preview_options_here,
    reply_markup=your_reply_markup_here
)
```
