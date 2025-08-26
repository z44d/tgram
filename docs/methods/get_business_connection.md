# get_business_connection

**Use this method to get information about the connection of the bot with a business account.**

## Parameters

- **`business_connection_id`** (**`str`**): **Unique identifier of the business connection**

## Returns

#### [BusinessConnection](../types/BusinessConnection.md)

## Examples

- **Required Parameters**

```python
await bot.get_business_connection(
    business_connection_id=your_business_connection_id_here
)
```
