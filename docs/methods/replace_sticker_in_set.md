#🔧 replace_sticker_in_set

**Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling deleteStickerFromSet, then addStickerToSet,**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **User identifier of the sticker set owner**
- **`name`** (**`str`** ): **Sticker set name**
- **`old_sticker`** (**`str`** ): **File identifier of the replaced sticker**
- **`sticker`** (**[InputSticker](../types/InputSticker.md)** ): **A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.replace_sticker_in_set(
    user_id=your_user_id_here,
    name=your_name_here,
    old_sticker=your_old_sticker_here,
    sticker=your_sticker_here
)
```
