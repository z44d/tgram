#🔧 create_new_sticker_set

**Use this method to create new sticker set owned by a user.**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **User identifier of created sticker set owner**
- **`name`** (**`str`** ): **Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only English letters,
digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>".
<bot_username> is case insensitive. 1-64 characters.**
- **`title`** (**`str`** ): **Sticker set title, 1-64 characters**
- **`stickers`** (**List of [InputSticker](../types/InputSticker.md)** ): **List of stickers to be added to the set**
- **`sticker_type`** (**`str`** ) (`optional`): **Type of stickers in the set, pass “regular”, “mask”, or “custom_emoji”. By default, a regular sticker set is created.**
- **`needs_repainting`** (**`bool`** ) (`optional`): **Pass True if stickers in the sticker set must be repainted to the color of text when used in messages,
the accent color if used as emoji status, white on chat photos, or another appropriate color based on context;
for custom emoji sticker sets only**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.create_new_sticker_set(
    user_id=your_user_id_here,
    name=your_name_here,
    title=your_title_here,
    stickers=your_stickers_here
)
```

-🔋 **All Parameters**

```python
await bot.create_new_sticker_set(
    user_id=your_user_id_here,
    name=your_name_here,
    title=your_title_here,
    stickers=your_stickers_here,
    sticker_type=your_sticker_type_here,
    needs_repainting=your_needs_repainting_here
)
```
