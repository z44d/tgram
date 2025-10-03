#🔧 save_prepared_inline_message

**Stores a message that can be sent by a user of a Mini App. Returns a PreparedInlineMessage object.**

##⚙️ Parameters

- **`user_id`** (**`int`** )
- **`result`** (**[InlineQueryResultCachedAudio](../types/InlineQueryResultCachedAudio.md) or [InlineQueryResultCachedDocument](../types/InlineQueryResultCachedDocument.md) or [InlineQueryResultCachedGif](../types/InlineQueryResultCachedGif.md) or [InlineQueryResultCachedMpeg4Gif](../types/InlineQueryResultCachedMpeg4Gif.md) or [InlineQueryResultCachedPhoto](../types/InlineQueryResultCachedPhoto.md) or [InlineQueryResultCachedSticker](../types/InlineQueryResultCachedSticker.md) or [InlineQueryResultCachedVideo](../types/InlineQueryResultCachedVideo.md) or [InlineQueryResultCachedVoice](../types/InlineQueryResultCachedVoice.md) or [InlineQueryResultArticle](../types/InlineQueryResultArticle.md) or [InlineQueryResultAudio](../types/InlineQueryResultAudio.md) or [InlineQueryResultContact](../types/InlineQueryResultContact.md) or [InlineQueryResultGame](../types/InlineQueryResultGame.md) or [InlineQueryResultDocument](../types/InlineQueryResultDocument.md) or [InlineQueryResultGif](../types/InlineQueryResultGif.md) or [InlineQueryResultLocation](../types/InlineQueryResultLocation.md) or [InlineQueryResultMpeg4Gif](../types/InlineQueryResultMpeg4Gif.md) or [InlineQueryResultPhoto](../types/InlineQueryResultPhoto.md) or [InlineQueryResultVenue](../types/InlineQueryResultVenue.md) or [InlineQueryResultVideo](../types/InlineQueryResultVideo.md) or [InlineQueryResultVoice](../types/InlineQueryResultVoice.md)** )
- **`allow_user_chats`** (**`bool`** ) (`optional`)
- **`allow_bot_chats`** (**`bool`** ) (`optional`)
- **`allow_group_chats`** (**`bool`** ) (`optional`)
- **`allow_channel_chats`** (**`bool`** ) (`optional`)

##📲 Returns

#### [PreparedInlineMessage](../types/PreparedInlineMessage.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.save_prepared_inline_message(
    user_id=your_user_id_here,
    result=your_result_here
)
```

-🔋 **All Parameters**

```python
await bot.save_prepared_inline_message(
    user_id=your_user_id_here,
    result=your_result_here,
    allow_user_chats=your_allow_user_chats_here,
    allow_bot_chats=your_allow_bot_chats_here,
    allow_group_chats=your_allow_group_chats_here,
    allow_channel_chats=your_allow_channel_chats_here
)
```
