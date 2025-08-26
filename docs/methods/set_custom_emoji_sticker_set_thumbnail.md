# set_custom_emoji_sticker_set_thumbnail

**Use this method to set the thumbnail of a custom emoji sticker set.**

## Parameters

- **`name`** (**`str`**): **Sticker set name**
- **`custom_emoji_id`** (**`str`**) (`optional`): **Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.set_custom_emoji_sticker_set_thumbnail(
    name=your_name_here
)
```

- **All Parameters**

```python
await bot.set_custom_emoji_sticker_set_thumbnail(
    name=your_name_here,
    custom_emoji_id=your_custom_emoji_id_here
)
```
