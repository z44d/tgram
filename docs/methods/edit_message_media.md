#🔧 edit_message_media

**Use this method to edit animation, audio, document, photo, or video messages, or to add media to text messages.**

##⚙️ Parameters

- **`media`** (**[InputMediaAudio](../types/InputMediaAudio.md) or [InputMediaDocument](../types/InputMediaDocument.md) or [InputMediaPhoto](../types/InputMediaPhoto.md) or [InputMediaVideo](../types/InputMediaVideo.md)** )
- **`business_connection_id`** (**`str`** ) (`optional`)
- **`chat_id`** (**`int` or `str`** ) (`optional`)
- **`message_id`** (**`int`** ) (`optional`)
- **`inline_message_id`** (**`str`** ) (`optional`)
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md) or `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_message_media(
    media=your_media_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_message_media(
    media=your_media_here,
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    inline_message_id=your_inline_message_id_here,
    reply_markup=your_reply_markup_here
)
```
