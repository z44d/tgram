#🔮 BusinessConnection

**This object describes the connection of the bot with a business account.**

##⚙️ Properties

- **`id`** (**`str`** ): **Unique identifier of the business connection**
- **`user`** (**[User](User.md)** ): **Business account user that created the business connection**
- **`user_chat_id`** (**`int`** ): **Identifier of a private chat with the user who created the business connection**
- **`date`** (**`int`** ): **Date the connection was established in Unix time**
- **`rights`** (**`BusinessBotRights`** ): **Optional. Rights of the business bot**
- **`is_enabled`** (**`bool`** ): **True, if the connection is active**
