#🔧 edit_ephemeral_message_reply_markup

****

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** )
- **`message_id`** (**`int`** )
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_ephemeral_message_reply_markup(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_ephemeral_message_reply_markup(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    reply_markup=your_reply_markup_here
)
```
