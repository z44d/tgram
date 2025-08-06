# get_business_account_star_balance

**Returns the amount of Telegram Stars owned by a managed business account.**

## Parameters

- **`business_connection_id`** (**`str`**): **Unique identifier of the business connection**

## Returns

#### [StarAmount](../types/StarAmount.md)

## Examples

- **Required Parameters**

```python
await bot.get_business_account_star_balance(
    business_connection_id=your_business_connection_id_here
)
```
