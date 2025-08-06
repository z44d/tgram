# delete_webhook

**Use this method to remove webhook integration if you decide to switch back to getUpdates.**

## Parameters

- **`drop_pending_updates`** (**`bool`**) (`optional`): **Pass True to drop all pending updates, defaults to None**

## Returns

#### `bool`

## Examples


- **All Parameters**

```python
await bot.delete_webhook(
    drop_pending_updates=your_drop_pending_updates_here
)
```
