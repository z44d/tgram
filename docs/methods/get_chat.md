# get_chat

**Use this method to get up to date information about the chat (current name of the user for one-on-one**

## Parameters

- **`chat_id`** (**`int` or `str`**): **Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)**

## Returns

#### [ChatFullInfo](../types/ChatFullInfo.md)

## Examples

- **Required Parameters**

```python
await bot.get_chat(
    chat_id=your_chat_id_here
)
```
