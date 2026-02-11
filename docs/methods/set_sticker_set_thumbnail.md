#🔧 set_sticker_set_thumbnail

**Use this method to set the thumbnail of a sticker set.**

##⚙️ Parameters

- **`name`** (**`str`** ): **Sticker set name**
- **`user_id`** (**`int`** ): **User identifier**
- **`format`** (**`str`** )
- **`thumbnail`** (**`Path` or `bytes` or `str`** ) (`optional`): **A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a .TGS animation
with a thumbnail up to 32 kilobytes in size (see https://core.telegram.org/stickers#animated-sticker-requirements for animated sticker technical requirements),
or a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-sticker-requirements for video sticker technical
requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from
the Internet, or upload a new one using multipart/form-data. More information on Sending Files ». Animated and video sticker set thumbnails can't be uploaded via
HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_sticker_set_thumbnail(
    name=your_name_here,
    user_id=your_user_id_here,
    format=your_format_here
)
```

-🔋 **All Parameters**

```python
await bot.set_sticker_set_thumbnail(
    name=your_name_here,
    user_id=your_user_id_here,
    format=your_format_here,
    thumbnail=your_thumbnail_here
)
```
