#🔧 delete_messages

**Use this method to delete multiple messages simultaneously.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`message_ids`** (**List of `int`** ): **Identifiers of the messages to be deleted**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.delete_messages(
    chat_id=your_chat_id_here,
    message_ids=your_message_ids_here
)
```
