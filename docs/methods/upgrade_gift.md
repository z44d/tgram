#🔧 upgrade_gift

**Upgrades a given regular gift to a unique gift. Requires the can_transfer_and_upgrade_gifts business bot right.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection.**
- **`owned_gift_id`** (**`str`** ): **Unique identifier of the regular gift that should be upgraded to a unique one.**
- **`keep_original_details`** (**`bool`** ) (`optional`): **Pass True to keep the original gift text, sender and receiver in the upgraded gift.**
- **`star_count`** (**`int`** ) (`optional`): **The amount of Telegram Stars that will be paid for the upgrade from the business account balance.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.upgrade_gift(
    business_connection_id=your_business_connection_id_here,
    owned_gift_id=your_owned_gift_id_here
)
```

-🔋 **All Parameters**

```python
await bot.upgrade_gift(
    business_connection_id=your_business_connection_id_here,
    owned_gift_id=your_owned_gift_id_here,
    keep_original_details=your_keep_original_details_here,
    star_count=your_star_count_here
)
```
