#🔮 InlineQueryResultDocument

**Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.**

##⚙️ Properties

- **`title`** (**`str`** ): **Title for the result**
- **`document_url`** (**`str`** ): **A valid URL for the file**
- **`mime_type`** (**`str`** ): **MIME type of the content of the file, either “application/pdf” or “application/zip”**
- **`caption`** (**`str`** ): **Optional. Caption of the document to be sent, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the document caption. See formatting options for more
details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`description`** (**`str`** ): **Optional. Short description of the result**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the file**
- **`thumbnail_url`** (**`str`** ): **Optional. URL of the thumbnail (JPEG only) for the file**
- **`thumbnail_width`** (**`int`** ): **Optional. Thumbnail width**
- **`thumbnail_height`** (**`int`** ): **Optional. Thumbnail height**
