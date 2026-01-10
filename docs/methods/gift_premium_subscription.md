#🔧 gift_premium_subscription

**Gifts a Telegram Premium subscription to the given user.**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **Unique identifier of the target user who will receive a Telegram Premium subscription**
- **`month_count`** (**`int`** ): **Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12**
- **`star_count`** (**`int`** ): **Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months**
- **`text`** (**`str`** ) (`optional`): **Text that will be shown along with the service message about the subscription; 0-128 characters**
- **`text_parse_mode`** (**`str`** ) (`optional`): **Mode for parsing entities in the text**
- **`text_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **A JSON-serialized list of special entities that appear in the gift text**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.gift_premium_subscription(
    user_id=your_user_id_here,
    month_count=your_month_count_here,
    star_count=your_star_count_here
)
```

-🔋 **All Parameters**

```python
await bot.gift_premium_subscription(
    user_id=your_user_id_here,
    month_count=your_month_count_here,
    star_count=your_star_count_here,
    text=your_text_here,
    text_parse_mode=your_text_parse_mode_here,
    text_entities=your_text_entities_here
)
```
