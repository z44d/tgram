#🔧 edit_user_star_subscription

**Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns True on success.**

##⚙️ Parameters

- **`user_id`** (**`int`** )
- **`telegram_payment_charge_id`** (**`str`** )
- **`is_canceled`** (**`bool`** )

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_user_star_subscription(
    user_id=your_user_id_here,
    telegram_payment_charge_id=your_telegram_payment_charge_id_here,
    is_canceled=your_is_canceled_here
)
```
