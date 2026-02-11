#🔧 convert_gift_to_stars

**Converts a given regular gift to Telegram Stars. Requires the can_convert_gifts_to_stars business bot right. Returns True on success.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection.**
- **`owned_gift_id`** (**`str`** ): **Unique identifier of the regular gift that should be converted to Telegram Stars.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.convert_gift_to_stars(
    business_connection_id=your_business_connection_id_here,
    owned_gift_id=your_owned_gift_id_here
)
```
