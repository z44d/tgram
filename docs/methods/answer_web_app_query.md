# answer_web_app_query

**Use this method to set the result of an interaction with a Web App and**

## Parameters

- **`web_app_query_id`** (**`str`**): **Unique identifier for the query to be answered**
- **`result`** (**`InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultContact, InlineQueryResultGame, InlineQueryResultDocument, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice`**): **A JSON-serialized object describing the message to be sent**

## Returns

#### [SentWebAppMessage](../types/SentWebAppMessage.md)

## Examples

- **Required Parameters**

```python
await bot.answer_web_app_query(
    web_app_query_id=your_web_app_query_id_here,
    result=your_result_here
)
```
