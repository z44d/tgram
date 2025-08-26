# refund_star_payment

**Refunds a successful payment in Telegram Stars. Returns True on success.**

## Parameters

- **`user_id`** (**`int`**): **Identifier of the user whose payment will be refunded**
- **`telegram_payment_charge_id`** (**`str`**): **Telegram payment identifier**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.refund_star_payment(
    user_id=your_user_id_here,
    telegram_payment_charge_id=your_telegram_payment_charge_id_here
)
```
