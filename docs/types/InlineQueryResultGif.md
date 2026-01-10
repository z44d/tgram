#🔮 InlineQueryResultGif

**Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.**

##⚙️ Properties

- **`gif_url`** (**`str`** ): **A valid URL for the GIF file. File size must not exceed 1MB**
- **`thumbnail_url`** (**`str`** ): **URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result**
- **`gif_width`** (**`int`** ): **Optional. Width of the GIF**
- **`gif_height`** (**`int`** ): **Optional. Height of the GIF**
- **`gif_duration`** (**`int`** ): **Optional. Duration of the GIF in seconds**
- **`thumbnail_mime_type`** (**`str`** ): **Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or
“video/mp4”. Defaults to “image/jpeg”**
- **`title`** (**`str`** ): **Optional. Title for the result**
- **`caption`** (**`str`** ): **Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the caption. See formatting options for more details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ): **Optional. If true, a caption is shown over the photo or video**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the GIF animation**
