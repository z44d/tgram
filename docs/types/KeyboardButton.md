#🔮 KeyboardButton

**This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive.**

##⚙️ Properties

- **`text`** (**`str`** ): **Text of the button. If none of the optional fields are used, it will be sent as a message when the button is
pressed**
- **`request_users`** (**[KeyboardButtonRequestUsers](KeyboardButtonRequestUsers.md)** ): **Optional. If specified, pressing the button will open a list of suitable users.
Identifiers of selected users will be sent to the bot in a “users_shared” service message. Available in private chats only.**
- **`request_chat`** (**[KeyboardButtonRequestChat](KeyboardButtonRequestChat.md)** ): **Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will
send its identifier to the bot in a “chat_shared” service message. Available in private chats only.**
- **`request_contact`** (**`bool`** ): **Optional. If True, the user's phone number will be sent as a contact when the button is
pressed. Available in private chats only.**
- **`request_location`** (**`bool`** ): **Optional. If True, the user's current location will be sent when the button is pressed.
Available in private chats only.**
- **`request_poll`** (**[KeyboardButtonPollType](KeyboardButtonPollType.md)** ): **Optional. If specified, the user will be asked to create a poll and send it to the bot when the
button is pressed. Available in private chats only.**
- **`web_app`** (**[WebAppInfo](WebAppInfo.md)** ): **Optional. If specified, the described Web App will be launched when the button is pressed. The Web App
will be able to send a “web_app_data” service message. Available in private chats only.**
- **`icon_custom_emoji_id`** (**`str`** ): **Optional. Unique identifier of the custom emoji shown before the text of the button**
- **`style`** (**`str`** ): **Optional. Style of the button. Must be one of “danger”, “success”, or “primary”**
