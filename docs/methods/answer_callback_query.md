#🔧 answer_callback_query

**Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to**

##⚙️ Parameters

- **`callback_query_id`** (**`str`** ): **Unique identifier for the query to be answered**
- **`text`** (**`str`** ) (`optional`): **Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters**
- **`show_alert`** (**`bool`** ) (`optional`): **If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.**
- **`url`** (**`str`** ) (`optional`): **URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your
game - note that this will only work if the query comes from a callback_game button.**
- **`cache_time`** (**`int`** ) (`optional`): **The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching
starting in version 3.14. Defaults to 0.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.answer_callback_query(
    callback_query_id=your_callback_query_id_here
)
```

-🔋 **All Parameters**

```python
await bot.answer_callback_query(
    callback_query_id=your_callback_query_id_here,
    text=your_text_here,
    show_alert=your_show_alert_here,
    url=your_url_here,
    cache_time=your_cache_time_here
)
```
