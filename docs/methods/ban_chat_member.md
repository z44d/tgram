#🔧 ban_chat_member

**Use this method to ban a user in a group, a supergroup or a channel.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target group or username of the target supergroup
or channel (in the format @channelusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`until_date`** (**`int`** ) (`optional`): **Date when the user will be unbanned, unix time. If user is banned for more than 366 days or
less than 30 seconds from the current time they are considered to be banned forever**
- **`revoke_messages`** (**`bool`** ) (`optional`): **Bool: Pass True to delete all messages from the chat for the user that is being removed.
If False, the user will be able to see messages in the group that were sent before the user was removed.
Always True for supergroups and channels.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.ban_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```

-🔋 **All Parameters**

```python
await bot.ban_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    until_date=your_until_date_here,
    revoke_messages=your_revoke_messages_here
)
```
