# save_prepared_inline_message

**Stores a message that can be sent by a user of a Mini App. Returns a PreparedInlineMessage object.**

## Parameters

- **`user_id`** (**`int`**)
- **`result`** (**`InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultContact, InlineQueryResultGame, InlineQueryResultDocument, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice`**)
- **`allow_user_chats`** (**`bool`**) (`optional`)
- **`allow_bot_chats`** (**`bool`**) (`optional`)
- **`allow_group_chats`** (**`bool`**) (`optional`)
- **`allow_channel_chats`** (**`bool`**) (`optional`)

## Returns

#### [PreparedInlineMessage](../types/PreparedInlineMessage.md)

## Examples

- **Required Parameters**

```python
await bot.save_prepared_inline_message(
    user_id=your_user_id_here,
    result=your_result_here
)
```

- **All Parameters**

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
