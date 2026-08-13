#🔧 transfer_gift

**Transfers an owned unique gift to another user. Requires the can_transfer_and_upgrade_gifts business bot right.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection.**
- **`owned_gift_id`** (**`str`** ): **Unique identifier of the regular gift that should be transferred.**
- **`new_owner_chat_id`** (**`int`** ): **Unique identifier of the chat which will own the gift. The chat must be active in the last 24 hours.**
- **`star_count`** (**`int`** ) (`optional`): **The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the can_transfer_stars business bot right is required.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.transfer_gift(
    business_connection_id=your_business_connection_id_here,
    owned_gift_id=your_owned_gift_id_here,
    new_owner_chat_id=your_new_owner_chat_id_here
)
```

-🔋 **All Parameters**

```python
await bot.transfer_gift(
    business_connection_id=your_business_connection_id_here,
    owned_gift_id=your_owned_gift_id_here,
    new_owner_chat_id=your_new_owner_chat_id_here,
    star_count=your_star_count_here
)
```
