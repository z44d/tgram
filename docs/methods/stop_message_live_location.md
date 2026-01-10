#🔧 stop_message_live_location

****

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ) (`optional`)
- **`chat_id`** (**`int` or `str`** ) (`optional`)
- **`message_id`** (**`int`** ) (`optional`)
- **`inline_message_id`** (**`str`** ) (`optional`)
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md) or `bool`

##📀 Examples


-🔋 **All Parameters**

```python
await bot.stop_message_live_location(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    inline_message_id=your_inline_message_id_here,
    reply_markup=your_reply_markup_here
)
```
