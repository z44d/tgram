#🔮 Video

**This object represents a video file.**

##⚙️ Properties

- **`file_id`** (**`str`** ): **Identifier for this file, which can be used to download or reuse the file**
- **`file_unique_id`** (**`str`** ): **Unique identifier for this file, which is supposed to be the same over time and for different
bots. Can't be used to download or reuse the file.**
- **`width`** (**`int`** ): **Video width as defined by sender**
- **`height`** (**`int`** ): **Video height as defined by sender**
- **`duration`** (**`int`** ): **Duration of the video in seconds as defined by sender**
- **`thumbnail`** (**[PhotoSize](PhotoSize.md)** ): **Optional. Video thumbnail**
- **`cover`** (**List of [PhotoSize](PhotoSize.md)** ): **Optional. Video thumbnail**
- **`start_timestamp`** (**`int`** ): **Optional. Timestamp in seconds from which the video will play in the message**
- **`file_name`** (**`str`** ): **Optional. Original filename as defined by sender**
- **`mime_type`** (**`str`** ): **Optional. MIME type of the file as defined by sender**
- **`file_size`** (**`int`** ): **Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have
difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
double-precision float type are safe for storing this value.**
