# set_user_emoji_status

**Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method requestEmojiStatusAccess. Returns True on success.**

## Parameters

- **`user_id`** (**`int`**): **OUnique identifier of the target user.**
- **`emoji_status_custom_emoji_id`** (**`str`**) (`optional`): **Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status.**
- **`emoji_status_expiration_date`** (**`int`**) (`optional`): **Expiration date of the emoji status, if any.**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.set_user_emoji_status(
    user_id=your_user_id_here
)
```

- **All Parameters**

```python
await bot.set_user_emoji_status(
    user_id=your_user_id_here,
    emoji_status_custom_emoji_id=your_emoji_status_custom_emoji_id_here,
    emoji_status_expiration_date=your_emoji_status_expiration_date_here
)
```
