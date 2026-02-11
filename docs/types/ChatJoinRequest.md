#🔮 ChatJoinRequest

**Represents a join request sent to a chat.**

##⚙️ Properties

- **`chat`** (**[Chat](Chat.md)** ): **Chat to which the request was sent**
- **`from_user`** (**[User](User.md)** ): **User that sent the join request**
- **`user_chat_id`** (**`int`** ): **Optional. Identifier of a private chat with the user who sent the join request.
This number may have more than 32 significant bits and some programming languages may have difficulty/silent
defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision
float type are safe for storing this identifier. The bot can use this identifier for 24 hours to send messages
until the join request is processed, assuming no other administrator contacted the user.**
- **`date`** (**`int`** ): **Date the request was sent in Unix time**
- **`bio`** (**`str`** ): **Optional. Bio of the user.**
- **`invite_link`** (**[ChatInviteLink](ChatInviteLink.md)** ): **Optional. Chat invite link that was used by the user to send the join request**
