#🔧 create_chat_invite_link

**Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Id: Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**
- **`name`** (**`str`** ) (`optional`): **Invite link name; 0-32 characters**
- **`expire_date`** (**`int`** ) (`optional`): **Point in time (Unix timestamp) when the link will expire**
- **`member_limit`** (**`int`** ) (`optional`): **Maximum number of users that can be members of the chat simultaneously**
- **`creates_join_request`** (**`bool`** ) (`optional`): **True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified**

##📲 Returns

#### [ChatInviteLink](../types/ChatInviteLink.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.create_chat_invite_link(
    chat_id=your_chat_id_here
)
```

-🔋 **All Parameters**

```python
await bot.create_chat_invite_link(
    chat_id=your_chat_id_here,
    name=your_name_here,
    expire_date=your_expire_date_here,
    member_limit=your_member_limit_here,
    creates_join_request=your_creates_join_request_here
)
```
