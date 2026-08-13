#🔧 edit_ephemeral_message_media

****

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** )
- **`message_id`** (**`int`** )
- **`media`** (**[InputMediaAnimation](../types/InputMediaAnimation.md) or [InputMediaAudio](../types/InputMediaAudio.md) or [InputMediaDocument](../types/InputMediaDocument.md) or [InputMediaLivePhoto](../types/InputMediaLivePhoto.md) or [InputMediaPhoto](../types/InputMediaPhoto.md) or [InputMediaVideo](../types/InputMediaVideo.md) or [InputMediaVoiceNote](../types/InputMediaVoiceNote.md)** )
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_ephemeral_message_media(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    media=your_media_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_ephemeral_message_media(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    media=your_media_here,
    reply_markup=your_reply_markup_here
)
```
