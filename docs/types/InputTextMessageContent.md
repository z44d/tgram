#🔮 InputTextMessageContent

**Represents the content of a text message to be sent as the result of an inline query.**

##⚙️ Properties

- **`message_text`** (**`str`** ): **Text of the message to be sent, 1-4096 characters**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the message text. See formatting options for more
details.**
- **`entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in message text, which can be specified instead of
parse_mode**
- **`link_preview_options`** (**[LinkPreviewOptions](LinkPreviewOptions.md)** ): **Optional. Link preview generation options for the message**
