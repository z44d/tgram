#🔧 unban_chat_member

**Use this method to unban a previously kicked user in a supergroup or channel.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target group or username of the target supergroup or channel
(in the format @username)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`only_if_banned`** (**`bool`** ) (`optional`): **Do nothing if the user is not banned**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.unban_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```

-🔋 **All Parameters**

```python
await bot.unban_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    only_if_banned=your_only_if_banned_here
)
```
