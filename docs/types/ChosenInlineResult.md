#🔮 ChosenInlineResult

**Represents a result of an inline query that was chosen by the user and sent to their chat partner.**

##⚙️ Properties

- **`result_id`** (**`str`** ): **The unique identifier for the result that was chosen**
- **`from_user`** (**[User](User.md)** )
- **`query`** (**`str`** ): **The query that was used to obtain the result**
- **`location`** (**[Location](Location.md)** ): **Optional. Sender location, only for bots that require user location**
- **`inline_message_id`** (**`str`** ): **Optional. Identifier of the sent inline message. Available only if there is an inline
keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.**
