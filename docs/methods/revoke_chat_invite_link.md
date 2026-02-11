#🔧 revoke_chat_invite_link

**Use this method to revoke an invite link created by the bot.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Id: Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**
- **`invite_link`** (**`str`** ): **The invite link to revoke**

##📲 Returns

#### [ChatInviteLink](../types/ChatInviteLink.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.revoke_chat_invite_link(
    chat_id=your_chat_id_here,
    invite_link=your_invite_link_here
)
```
