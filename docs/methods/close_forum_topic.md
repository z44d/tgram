# close_forum_topic

**Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator**

## Parameters

- **`chat_id`** (**`int` or `str`**): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`message_thread_id`** (**`int`**): **Identifier of the topic to close**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.close_forum_topic(
    chat_id=your_chat_id_here,
    message_thread_id=your_message_thread_id_here
)
```
