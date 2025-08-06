# unpin_all_forum_topic_messages

**Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the**

## Parameters

- **`chat_id`** (**`int, str`**): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`message_thread_id`** (**`int`**): **Identifier of the topic**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.unpin_all_forum_topic_messages(
    chat_id=your_chat_id_here,
    message_thread_id=your_message_thread_id_here
)
```
