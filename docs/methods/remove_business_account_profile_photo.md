#🔧 remove_business_account_profile_photo

**Removes the current profile photo of a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`is_public`** (**`bool`** ) (`optional`): **Pass True to remove the public photo, which is visible even if the main photo is hidden by the business account's privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.remove_business_account_profile_photo(
    business_connection_id=your_business_connection_id_here
)
```

-🔋 **All Parameters**

```python
await bot.remove_business_account_profile_photo(
    business_connection_id=your_business_connection_id_here,
    is_public=your_is_public_here
)
```
