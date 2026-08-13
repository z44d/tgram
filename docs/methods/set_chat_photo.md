#🔧 set_chat_photo

**Use this method to set a new profile photo for the chat. Photos can't be changed for private chats.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Int or Str: Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**
- **`photo`** (**`Path` or `bytes` or `str`** ): **InputFile: New chat photo, uploaded using multipart/form-data**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_chat_photo(
    chat_id=your_chat_id_here,
    photo=your_photo_here
)
```
