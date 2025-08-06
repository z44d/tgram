# unpin_all_chat_messages

**Use this method to unpin a all pinned messages in a supergroup chat.**

## Parameters

- **`chat_id`** (**`int, str`**): **Int or Str: Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.unpin_all_chat_messages(
    chat_id=your_chat_id_here
)
```
