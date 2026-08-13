#🔮 ReplyKeyboardMarkup

**This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).**

##⚙️ Properties

- **`keyboard`** (**List of List of [KeyboardButton](KeyboardButton.md) or `str`** ): **:obj:`list` of button rows, each represented by an :obj:`list` of
:class:`tgram.types.KeyboardButton` or :obj:`str` objects**
- **`is_persistent`** (**`bool`** ): **Optional. Use this parameter if you want to show the keyboard to specific users only.
Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a
reply (has reply_to_message_id), sender of the original message.

Example: A user requests to change the bot's language, bot replies to the request with a keyboard to
select the new language. Other users in the group don't see the keyboard.**
- **`resize_keyboard`** (**`bool`** ): **Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make
the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is
always of the same height as the app's standard keyboard.**
- **`one_time_keyboard`** (**`bool`** ): **Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard
will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can
press a special button in the input field to see the custom keyboard again. Defaults to false.**
- **`input_field_placeholder`** (**`str`** ): **Optional. The placeholder to be shown in the input field when the keyboard is
active; 1-64 characters**
- **`selective`** (**`bool`** ): **Optional. Use this parameter if you want to show the keyboard to specific users only. Targets:
1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message
in the same chat and forum topic, sender of the original message. Example: A user requests to change the bot's
language, bot replies to the request with a keyboard to select the new language. Other users in the group don't
see the keyboard.**
