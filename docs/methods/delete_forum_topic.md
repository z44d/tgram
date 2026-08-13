#🔧 delete_forum_topic

**Use this method to delete a topic in a forum supergroup chat. The bot must be an administrator in the chat for this**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`message_thread_id`** (**`int`** ): **Identifier of the topic to delete**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.delete_forum_topic(
    chat_id=your_chat_id_here,
    message_thread_id=your_message_thread_id_here
)
```
