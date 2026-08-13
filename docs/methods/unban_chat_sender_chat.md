#🔧 unban_chat_sender_chat

**Use this method to unban a previously banned channel chat in a supergroup or channel.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`sender_chat_id`** (**`int`** ): **Unique identifier of the target sender chat.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.unban_chat_sender_chat(
    chat_id=your_chat_id_here,
    sender_chat_id=your_sender_chat_id_here
)
```
