#🔮 InlineQueryResultVideo

**Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.**

##⚙️ Properties

- **`video_url`** (**`str`** ): **A valid URL for the embedded video player or video file**
- **`mime_type`** (**`str`** ): **MIME type of the content of the video URL, “text/html” or “video/mp4”**
- **`thumbnail_url`** (**`str`** ): **URL of the thumbnail (JPEG only) for the video**
- **`title`** (**`str`** ): **Title for the result**
- **`caption`** (**`str`** ): **Optional. Caption of the video to be sent, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the video caption. See formatting options for more
details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ): **Optional. If true, a caption is shown over the video**
- **`video_width`** (**`int`** ): **Optional. Video width**
- **`video_height`** (**`int`** ): **Optional. Video height**
- **`video_duration`** (**`int`** ): **Optional. Video duration in seconds**
- **`description`** (**`str`** ): **Optional. Short description of the result**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the video. This field is
required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).**
