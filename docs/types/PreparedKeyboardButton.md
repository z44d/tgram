#🔮 PreparedKeyboardButton

**This object represents a keyboard button prepared by the bot to be sent by a user of a Mini App.**

##⚙️ Properties

- **`request_users`** (**[KeyboardButtonRequestUsers](KeyboardButtonRequestUsers.md)** ): **Optional. If specified, pressing the button will open a list of suitable users.
Identifiers of selected users will be sent to the bot in a “users_shared” service message.**
- **`request_chat`** (**[KeyboardButtonRequestChat](KeyboardButtonRequestChat.md)** ): **Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will
send its identifier to the bot in a “chat_shared” service message.**
- **`request_managed_bot`** (**[KeyboardButtonRequestManagedBot](KeyboardButtonRequestManagedBot.md)** ): **Optional. If specified, the user will be asked to create a managed bot and share its identifier.**
