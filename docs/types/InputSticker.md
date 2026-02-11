#🔮 InputSticker

**This object describes a sticker to be added to a sticker set.**

##⚙️ Properties

- **`sticker`** (**`InputFile` or `str`** ): **The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers,
pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
Animated and video stickers can't be uploaded via HTTP URL.**
- **`format`** (**`str`** ): **Format of the added sticker, must be one of “static” for a .WEBP or .PNG image, “animated” for a .TGS animation, “video” for a WEBM video**
- **`emoji_list`** (**List of `str`** ): **One or more(up to 20) emoji(s) corresponding to the sticker**
- **`mask_position`** (**[MaskPosition](MaskPosition.md)** ): **Optional. Position where the mask should be placed on faces. For “mask” stickers only.**
- **`keywords`** (**List of `str`** ): **Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters.
For “regular” and “custom_emoji” stickers only.**
