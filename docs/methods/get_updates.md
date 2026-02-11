#🔧 get_updates

**Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.**

##⚙️ Parameters

- **`offset`** (**`int`** ) (`optional`): **Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates.
By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset
higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue.
All previous updates will forgotten.**
- **`limit`** (**`int`** ) (`optional`): **Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.**
- **`timeout`** (**`int`** ) (`optional`): **Request connection timeout**
- **`allowed_updates`** (**List of `str`** ) (`optional`): **Array of string. List the types of updates you want your bot to receive.**

##📲 Returns

#### List of [Update](../types/Update.md)

##📀 Examples


-🔋 **All Parameters**

```python
await bot.get_updates(
    offset=your_offset_here,
    limit=your_limit_here,
    timeout=your_timeout_here,
    allowed_updates=your_allowed_updates_here
)
```
