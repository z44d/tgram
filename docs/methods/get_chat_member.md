# get_chat_member

****

## Parameters

- **`chat_id`** (**`int, str`**)
- **`user_id`** (**`int`**)

## Returns

#### `ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberBanned, ChatMemberLeft`

## Examples

- **Required Parameters**

```python
await bot.get_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```
