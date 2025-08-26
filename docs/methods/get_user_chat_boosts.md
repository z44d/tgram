# get_user_chat_boosts

**Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object.**

## Parameters

- **`chat_id`** (**`int` or `str`**): **Unique identifier for the target chat or username of the target channel**
- **`user_id`** (**`int`**): **Unique identifier of the target user**

## Returns

#### [UserChatBoosts](../types/UserChatBoosts.md)

## Examples

- **Required Parameters**

```python
await bot.get_user_chat_boosts(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```
