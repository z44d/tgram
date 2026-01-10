#🔮 Chat

**This object represents a chat.**

##⚙️ Properties

- **`id`** (**`int`** ): **Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.**
- **`type`** (**`str`** ): **Type of the chat, can be either “private”, “group”, “supergroup” or “channel”.**
- **`title`** (**`str`** ): **Optional. Title, for supergroups, channels and group chats.**
- **`username`** (**`str`** ): **Optional. Username, for private chats, supergroups and channels if available.**
- **`first_name`** (**`str`** ): **Optional. First name of the other party in a private chat.**
- **`last_name`** (**`str`** ): **Optional. Last name of the other party in a private chat.**
- **`is_forum`** (**`bool`** ): **Optional. True, if the supergroup chat is a forum (has topics enabled).**
- **`is_direct_messages`** (**`bool`** ): **Optional. True, if the chat is the direct messages chat of a channel.**
