#🔮 CallbackQuery

**This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.**

##⚙️ Properties

- **`id`** (**`str`** ): **Unique identifier for this query**
- **`from_user`** (**[User](User.md)** ): **Sender**
- **`chat_instance`** (**`str`** ): **Global identifier, uniquely corresponding to the chat to which the message with the callback
button was sent. Useful for high scores in games.**
- **`message`** (**[Message](Message.md)** ): **Optional. Message sent by the bot with the callback button that originated the query**
- **`inline_message_id`** (**`str`** ): **Optional. Identifier of the message sent via the bot in inline mode, that originated the
query.**
- **`data`** (**`str`** ): **Optional. Data associated with the callback button. Be aware that the message originated the query can
contain no callback buttons with this data.**
- **`game_short_name`** (**`str`** ): **Optional. Short name of a Game to be returned, serves as the unique identifier for the game**
