#🔮 InlineQueryResultCachedVoice

**Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.**

##⚙️ Properties

- **`voice_file_id`** (**`str`** ): **A valid file identifier for the voice message**
- **`title`** (**`str`** ): **Voice message title**
- **`caption`** (**`str`** ): **Optional. Caption, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the voice message caption. See formatting options for
more details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the voice message**
