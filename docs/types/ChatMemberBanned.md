#🔮 ChatMemberBanned

**Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.**

##⚙️ Properties

- **`status`** (**`ChatMemberStatus`** ): **The member's status in the chat, always “kicked”**
- **`user`** (**[User](User.md)** ): **Information about the user**
- **`until_date`** (**`int`** ): **Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned
forever**
