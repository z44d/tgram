#🔧 demote_chat_member

**Use this method to demote a user in a supergroup or a channel. The bot must be an administrator**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (
in the format @channelusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.demote_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```
