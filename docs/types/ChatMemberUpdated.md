#🔮 ChatMemberUpdated

**This object represents changes in the status of a chat member.**

##⚙️ Properties

- **`chat`** (**[Chat](Chat.md)** ): **Chat the user belongs to**
- **`from_user`** (**[User](User.md)** ): **Performer of the action, which resulted in the change**
- **`date`** (**`int`** ): **Date the change was done in Unix time**
- **`old_chat_member`** (**[ChatMemberLeft](ChatMemberLeft.md)** ): **Previous information about the chat member**
- **`new_chat_member`** (**[ChatMemberLeft](ChatMemberLeft.md)** ): **New information about the chat member**
- **`invite_link`** (**[ChatInviteLink](ChatInviteLink.md)** ): **Optional. Chat invite link, which was used by the user to join the chat; for joining by invite
link events only.**
- **`via_join_request`** (**`bool`** ): **Optional. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator**
- **`via_chat_folder_invite_link`** (**`bool`** ): **Optional. True, if the user joined the chat via a chat folder invite link**
