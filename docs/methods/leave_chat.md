# leave_chat

**Use this method for your bot to leave a group, supergroup or channel. Returns True on success.**

## Parameters

- **`chat_id`** (**`int, str`**): **Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.leave_chat(
    chat_id=your_chat_id_here
)
```
