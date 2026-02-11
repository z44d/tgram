#🔮 InlineQueryResultAudio

**Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.**

##⚙️ Properties

- **`audio_url`** (**`str`** ): **A valid URL for the audio file**
- **`title`** (**`str`** ): **Title**
- **`caption`** (**`str`** ): **Optional. Caption, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the audio caption. See formatting options for more
details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`performer`** (**`str`** ): **Optional. Performer**
- **`audio_duration`** (**`int`** ): **Optional. Audio duration in seconds**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the audio**
