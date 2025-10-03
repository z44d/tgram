#🔧 stop_poll

**Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel**
- **`message_id`** (**`int`** ): **Identifier of the original message with the poll**
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of the business connection to send the message through**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`): **A JSON-serialized object for a new message markup.**

##📲 Returns

#### [Poll](../types/Poll.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.stop_poll(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.stop_poll(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    business_connection_id=your_business_connection_id_here,
    reply_markup=your_reply_markup_here
)
```
