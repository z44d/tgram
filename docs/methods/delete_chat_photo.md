# delete_chat_photo

**Use this method to delete a chat photo. Photos can't be changed for private chats.**

## Parameters

- **`chat_id`** (**`int, str`**): **Int or Str: Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.delete_chat_photo(
    chat_id=your_chat_id_here
)
```
