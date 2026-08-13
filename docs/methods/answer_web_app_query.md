#🔧 answer_web_app_query

**Use this method to set the result of an interaction with a Web App and**

##⚙️ Parameters

- **`web_app_query_id`** (**`str`** ): **Unique identifier for the query to be answered**
- **`result`** (**[InlineQueryResultCachedAudio](../types/InlineQueryResultCachedAudio.md) or [InlineQueryResultCachedDocument](../types/InlineQueryResultCachedDocument.md) or [InlineQueryResultCachedGif](../types/InlineQueryResultCachedGif.md) or [InlineQueryResultCachedMpeg4Gif](../types/InlineQueryResultCachedMpeg4Gif.md) or [InlineQueryResultCachedPhoto](../types/InlineQueryResultCachedPhoto.md) or [InlineQueryResultCachedSticker](../types/InlineQueryResultCachedSticker.md) or [InlineQueryResultCachedVideo](../types/InlineQueryResultCachedVideo.md) or [InlineQueryResultCachedVoice](../types/InlineQueryResultCachedVoice.md) or [InlineQueryResultArticle](../types/InlineQueryResultArticle.md) or [InlineQueryResultAudio](../types/InlineQueryResultAudio.md) or [InlineQueryResultContact](../types/InlineQueryResultContact.md) or [InlineQueryResultGame](../types/InlineQueryResultGame.md) or [InlineQueryResultDocument](../types/InlineQueryResultDocument.md) or [InlineQueryResultGif](../types/InlineQueryResultGif.md) or [InlineQueryResultLocation](../types/InlineQueryResultLocation.md) or [InlineQueryResultMpeg4Gif](../types/InlineQueryResultMpeg4Gif.md) or [InlineQueryResultPhoto](../types/InlineQueryResultPhoto.md) or [InlineQueryResultVenue](../types/InlineQueryResultVenue.md) or [InlineQueryResultVideo](../types/InlineQueryResultVideo.md) or [InlineQueryResultVoice](../types/InlineQueryResultVoice.md)** ): **A JSON-serialized object describing the message to be sent**

##📲 Returns

#### [SentWebAppMessage](../types/SentWebAppMessage.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.answer_web_app_query(
    web_app_query_id=your_web_app_query_id_here,
    result=your_result_here
)
```
