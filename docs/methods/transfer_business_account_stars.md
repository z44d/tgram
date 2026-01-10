#🔧 transfer_business_account_stars

**Transfers Telegram Stars from the business account balance to the bot's balance.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`star_count`** (**`int`** ): **Number of Telegram Stars to transfer; 1-10000**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.transfer_business_account_stars(
    business_connection_id=your_business_connection_id_here,
    star_count=your_star_count_here
)
```
