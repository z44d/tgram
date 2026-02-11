#🔧 get_business_account_gifts

**Use this method to get the gifts received and owned by a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`exclude_unsaved`** (**`bool`** ) (`optional`): **Exclude gifts that aren't saved to the account's profile page**
- **`exclude_saved`** (**`bool`** ) (`optional`): **Exclude gifts that are saved to the account's profile page**
- **`exclude_unlimited`** (**`bool`** ) (`optional`): **Exclude gifts that can be purchased an unlimited number of times**
- **`exclude_limited_upgradable`** (**`bool`** ) (`optional`): **Exclude limited gifts that can be upgraded to unique**
- **`exclude_limited_non_upgradable`** (**`bool`** ) (`optional`): **Exclude limited gifts that cannot be upgraded to unique**
- **`exclude_unique`** (**`bool`** ) (`optional`): **Exclude unique gifts**
- **`exclude_from_blockchain`** (**`bool`** ) (`optional`): **Exclude gifts that were assigned from the TON blockchain**
- **`sort_by_price`** (**`bool`** ) (`optional`): **Sort results by gift price instead of send date**
- **`offset`** (**`str`** ) (`optional`): **Offset of the first entry to return; use empty string for first chunk**
- **`limit`** (**`int`** ) (`optional`): **Maximum number of gifts to return; 1-100, defaults to 100**

##📲 Returns

#### [OwnedGifts](../types/OwnedGifts.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.get_business_account_gifts(
    business_connection_id=your_business_connection_id_here
)
```

-🔋 **All Parameters**

```python
await bot.get_business_account_gifts(
    business_connection_id=your_business_connection_id_here,
    exclude_unsaved=your_exclude_unsaved_here,
    exclude_saved=your_exclude_saved_here,
    exclude_unlimited=your_exclude_unlimited_here,
    exclude_limited_upgradable=your_exclude_limited_upgradable_here,
    exclude_limited_non_upgradable=your_exclude_limited_non_upgradable_here,
    exclude_unique=your_exclude_unique_here,
    exclude_from_blockchain=your_exclude_from_blockchain_here,
    sort_by_price=your_sort_by_price_here,
    offset=your_offset_here,
    limit=your_limit_here
)
```
