#🔮 VideoQuality

**This object represents a video file of a specific quality.**

##⚙️ Properties

- **`file_id`** (**`str`** ): **Identifier for this file, which can be used to download or reuse the file**
- **`file_unique_id`** (**`str`** ): **Unique identifier for this file, which is supposed to be the same over time and for
different bots. Can't be used to download or reuse the file.**
- **`width`** (**`int`** ): **Video width**
- **`height`** (**`int`** ): **Video height**
- **`codec`** (**`str`** ): **Codec used to encode the video, e.g. "h264", "h265", or "av01"**
- **`file_size`** (**`int`** ): **Optional. File size in bytes**
