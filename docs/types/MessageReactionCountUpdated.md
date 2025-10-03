#🔮 MessageReactionCountUpdated

**This object represents a service message about a change in the list of the current user's reactions to a message.**

##⚙️ Properties

- **`chat`** (**[Chat](Chat.md)** ): **The chat containing the message**
- **`message_id`** (**`int`** ): **Unique message identifier inside the chat**
- **`date`** (**`int`** ): **Date of the change in Unix time**
- **`reactions`** (**List of [ReactionCount](ReactionCount.md)** ): **List of reactions that are present on the message**
