#🔮 InputMediaPhoto

**Represents a photo to be sent.**

##⚙️ Properties

- **`media`** (**`Path` or `str`** ): **File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using
multipart/form-data under <file_attach_name> name. More information on Sending Files »**
- **`caption`** (**`str`** ): **Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the photo caption. See formatting options for more
details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ): **Optional. True, if the caption should be shown above the photo**
- **`has_spoiler`** (**`bool`** ): **Optional. True, if the uploaded photo is a spoiler**
