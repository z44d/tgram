#🔮 InputMediaAnimation

**Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.**

##⚙️ Properties

- **`media`** (**`Path` or `str`** ): **File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an
HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using
multipart/form-data under <file_attach_name> name. More information on Sending Files »**
- **`thumbnail`** (**`InputFile` or `str`** ): **Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported
server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should
not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be
only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using
multipart/form-data under <file_attach_name>. More information on Sending Files »**
- **`caption`** (**`str`** ): **Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the animation caption. See formatting options for more
details.**
- **`caption_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the caption, which can be specified
instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ): **Optional. True, if the caption should be shown above the animation**
- **`width`** (**`int`** ): **Optional. Animation width**
- **`height`** (**`int`** ): **Optional. Animation height**
- **`duration`** (**`int`** ): **Optional. Animation duration in seconds**
- **`has_spoiler`** (**`bool`** ): **Optional. True, if the uploaded animation is a spoiler**
