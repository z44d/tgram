#🔮 BusinessMessagesDeleted

**This object is received when messages are deleted from a connected business account.**

##⚙️ Properties

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`chat`** (**[Chat](Chat.md)** ): **Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.**
- **`message_ids`** (**List of `int`** ): **A JSON-serialized list of identifiers of deleted messages in the chat of the business account**
