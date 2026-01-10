#🔮 InlineQueryResultPhoto

**Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.**

##⚙️ Properties

- **`photo_url`** (**`str`** ): **A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB**
- **`thumbnail_url`** (**`str`** ): **URL of the thumbnail for the photo**
- **`photo_width`** (**`int`** ): **Optional. Width of the photo**
- **`photo_height`** (**`int`** ): **Optional. Height of the photo**
- **`title`** (**`str`** ): **Optional. Title for the result**
- **`description`** (**`str`** ): **Optional. Short description of the result**
- **`caption`** (**`str`** ): **Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the photo caption. See formatting options for more
details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ): **Optional. If true, a caption is shown over the photo or video**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the photo**
