#🔧 delete_message

**Use this method to delete a message, including service messages, with the following limitations:**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`message_id`** (**`int`** ): **Identifier of the message to delete**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.delete_message(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```
