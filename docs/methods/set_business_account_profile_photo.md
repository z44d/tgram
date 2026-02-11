#🔧 set_business_account_profile_photo

**Changes the profile photo of a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`photo`** (**[InputProfilePhotoStatic](../types/InputProfilePhotoStatic.md) or [InputProfilePhotoAnimated](../types/InputProfilePhotoAnimated.md)** ): **The new profile photo to set**
- **`is_public`** (**`bool`** ) (`optional`): **Pass True to set the public photo, which will be visible even if the main photo is hidden by the business account's privacy settings. An account can have only one public photo.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_business_account_profile_photo(
    business_connection_id=your_business_connection_id_here,
    photo=your_photo_here
)
```

-🔋 **All Parameters**

```python
await bot.set_business_account_profile_photo(
    business_connection_id=your_business_connection_id_here,
    photo=your_photo_here,
    is_public=your_is_public_here
)
```
