#🔮 KeyboardButtonRequestChat

**This object defines the criteria used to request a suitable chat. The identifier of the selected chat will**

##⚙️ Properties

- **`chat_is_channel`** (**`bool`** ): **Pass True to request a channel chat, pass False to request a group or a supergroup chat.**
- **`chat_is_forum`** (**`bool`** ): **Optional. Pass True to request a forum supergroup, pass False to request a non-forum chat.
If not specified, no additional restrictions are applied.**
- **`chat_has_username`** (**`bool`** ): **Optional. Pass True to request a supergroup or a channel with a username, pass False to request a
chat without a username. If not specified, no additional restrictions are applied.**
- **`chat_is_created`** (**`bool`** ): **Optional. Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied.**
- **`user_administrator_rights`** (**[ChatAdministratorRights](ChatAdministratorRights.md)** ): **Optional. A JSON-serialized object listing the required administrator rights of the user in the chat.
The rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied.**
- **`bot_administrator_rights`** (**[ChatAdministratorRights](ChatAdministratorRights.md)** ): **Optional. A JSON-serialized object listing the required administrator rights of the bot in the chat.
The rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied.**
- **`bot_is_member`** (**`bool`** ): **Optional. Pass True to request a chat where the bot is a member. Otherwise, no additional restrictions are applied.**
- **`request_title`** (**`bool`** ): **Optional. Request title**
- **`request_username`** (**`bool`** ): **Optional. Request username**
- **`request_photo`** (**`bool`** ): **Optional. Request photo**
