#🔮 Sticker

**This object represents a sticker.**

##⚙️ Properties

- **`file_id`** (**`str`** ): **Identifier for this file, which can be used to download or reuse the file**
- **`file_unique_id`** (**`str`** ): **Unique identifier for this file, which is supposed to be the same over time and for different
bots. Can't be used to download or reuse the file.**
- **`type`** (**`str`** ): **Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is
independent from its format, which is determined by the fields is_animated and is_video.**
- **`width`** (**`int`** ): **Sticker width**
- **`height`** (**`int`** ): **Sticker height**
- **`is_animated`** (**`bool`** ): **True, if the sticker is animated**
- **`is_video`** (**`bool`** ): **True, if the sticker is a video sticker**
- **`thumbnail`** (**[PhotoSize](PhotoSize.md)** ): **Optional. Sticker thumbnail in the .WEBP or .JPG format**
- **`emoji`** (**`str`** ): **Optional. Emoji associated with the sticker**
- **`set_name`** (**`str`** ): **Optional. Name of the sticker set to which the sticker belongs**
- **`premium_animation`** (**[File](File.md)** ): **Optional. Premium animation for the sticker, if the sticker is premium**
- **`mask_position`** (**[MaskPosition](MaskPosition.md)** ): **Optional. For mask stickers, the position where the mask should be placed**
- **`custom_emoji_id`** (**`str`** ): **Optional. For custom emoji stickers, unique identifier of the custom emoji**
- **`needs_repainting`** (**`bool`** ): **Optional. True, if the sticker must be repainted to a text color in messages,
the color of the Telegram Premium badge in emoji status, white color on chat photos, or another
appropriate color in other places**
- **`file_size`** (**`int`** ): **Optional. File size in bytes**
