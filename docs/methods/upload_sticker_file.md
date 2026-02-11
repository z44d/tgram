#🔧 upload_sticker_file

**Use this method to upload a .png file with a sticker for later use in createNewStickerSet and addStickerToSet**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **User identifier of sticker set owner**
- **`sticker`** (**`Path` or `bytes` or `str`** ): **A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format.
See https://core.telegram.org/stickers for technical requirements. More information on Sending Files »**
- **`sticker_format`** (**`str`** ): **One of "static", "animated", "video".**

##📲 Returns

#### [File](../types/File.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.upload_sticker_file(
    user_id=your_user_id_here,
    sticker=your_sticker_here,
    sticker_format=your_sticker_format_here
)
```
