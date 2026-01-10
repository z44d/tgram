#🔮 MessageReactionUpdated

**This object represents a service message about a change in the list of the current user's reactions to a message.**

##⚙️ Properties

- **`chat`** (**[Chat](Chat.md)** ): **The chat containing the message the user reacted to**
- **`message_id`** (**`int`** ): **Unique identifier of the message inside the chat**
- **`date`** (**`int`** ): **Date of the change in Unix time**
- **`old_reaction`** (**List of `ReactionType`** ): **Previous list of reaction types that were set by the user**
- **`new_reaction`** (**List of `ReactionType`** ): **New list of reaction types that have been set by the user**
- **`user`** (**[User](User.md)** ): **Optional. The user that changed the reaction, if the user isn't anonymous**
- **`actor_chat`** (**[Chat](Chat.md)** ): **Optional. The chat on behalf of which the reaction was changed, if the user is anonymous**
