#🔮 InputStoryContentVideo

**Describes a video to post as a story.**

##⚙️ Properties

- **`video`** (**`str`** ): **The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB.**
- **`duration`** (**`float`** ): **Optional. Precise duration of the video in seconds; 0-60**
- **`cover_frame_timestamp`** (**`float`** ): **Optional. Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0.**
- **`is_animation`** (**`bool`** ): **Optional. Pass True if the video has no sound**
