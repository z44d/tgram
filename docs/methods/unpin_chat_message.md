#🔧 unpin_chat_message

**Use this method to unpin specific pinned message in a supergroup chat.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**
- **`message_id`** (**`int`** ) (`optional`): **Int: Identifier of a message to unpin**
- **`business_connection_id`** (**`str`** ) (`optional`): **Unique identifier of the business connection on behalf of which the message will be pinned**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.unpin_chat_message(
    chat_id=your_chat_id_here
)
```

-🔋 **All Parameters**

```python
await bot.unpin_chat_message(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    business_connection_id=your_business_connection_id_here
)
```
