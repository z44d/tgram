#🔧 read_business_message

**Marks an incoming message as read on behalf of a business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection on behalf of which to read the message**
- **`chat_id`** (**`int`** ): **Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours.**
- **`message_id`** (**`int`** ): **Unique identifier of the message to mark as read**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.read_business_message(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```
