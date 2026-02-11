#🔮 InlineQueryResultCachedGif

**Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.**

##⚙️ Properties

- **`gif_file_id`** (**`str`** ): **A valid file identifier for the GIF file**
- **`title`** (**`str`** ): **Optional. Title for the result**
- **`caption`** (**`str`** ): **Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the caption. See formatting options for more details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ): **Optional. Pass True, if a caption is not required for the media**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the GIF animation**
