# get_star_transactions

**Returns the bot's Telegram Star transactions in chronological order.**

## Parameters

- **`offset`** (**`int`**) (`optional`): **Number of transactions to skip in the response**
- **`limit`** (**`int`**) (`optional`): **The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.**

## Returns

#### [StarTransactions](../types/StarTransactions.md)

## Examples


- **All Parameters**

```python
await bot.get_star_transactions(
    offset=your_offset_here,
    limit=your_limit_here
)
```
