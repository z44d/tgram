#🔧 get_chat_member

****

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** )
- **`user_id`** (**`int`** )

##📲 Returns

#### [ChatMemberOwner](../types/ChatMemberOwner.md) or [ChatMemberAdministrator](../types/ChatMemberAdministrator.md) or [ChatMemberMember](../types/ChatMemberMember.md) or [ChatMemberRestricted](../types/ChatMemberRestricted.md) or [ChatMemberBanned](../types/ChatMemberBanned.md) or [ChatMemberLeft](../types/ChatMemberLeft.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.get_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```
