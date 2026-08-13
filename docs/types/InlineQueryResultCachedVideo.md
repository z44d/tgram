#🔮 InlineQueryResultCachedVideo

**Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.**

##⚙️ Properties

- **`video_file_id`** (**`str`** ): **A valid file identifier for the video file**
- **`title`** (**`str`** ): **Title for the result**
- **`description`** (**`str`** ): **Optional. Short description of the result**
- **`caption`** (**`str`** ): **Optional. Caption of the video to be sent, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the video caption. See formatting options for more
details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ): **Optional. Pass True, if a caption is not required for the media**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the video**
