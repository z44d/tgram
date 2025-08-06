# delete_chat_sticker_set

**Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat**

## Parameters

- **`chat_id`** (**`int, str`**): **Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.delete_chat_sticker_set(
    chat_id=your_chat_id_here
)
```
