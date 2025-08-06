# answer_inline_query

**Use this method to send answers to an inline query. On success, True is returned.**

## Parameters

- **`inline_query_id`** (**`str`**): **Unique identifier for the answered query**
- **`results`** (**List of [InlineQueryResultCachedAudio](../types/InlineQueryResultCachedAudio.md)**): **Array of results for the inline query**
- **`cache_time`** (**`int`**) (`optional`): **The maximum amount of time in seconds that the result of the inline query
may be cached on the server.**
- **`is_personal`** (**`bool`**) (`optional`): **Pass True, if results may be cached on the server side only for
the user that sent the query.**
- **`next_offset`** (**`str`**) (`optional`): **Pass the offset that a client should send in the next query with the same text
to receive more results.**
- **`button`** (**[InlineQueryResultsButton](../types/InlineQueryResultsButton.md)**) (`optional`): **A JSON-serialized object describing a button to be shown above inline query results**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.answer_inline_query(
    inline_query_id=your_inline_query_id_here,
    results=your_results_here
)
```

- **All Parameters**

```python
await bot.answer_inline_query(
    inline_query_id=your_inline_query_id_here,
    results=your_results_here,
    cache_time=your_cache_time_here,
    is_personal=your_is_personal_here,
    next_offset=your_next_offset_here,
    button=your_button_here
)
```
