#🔧 add_sticker_to_set

**Use this method to add a new sticker to a set created by the bot.**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **User identifier of created sticker set owner**
- **`name`** (**`str`** ): **Sticker set name**
- **`sticker`** (**[InputSticker](../types/InputSticker.md)** ): **A JSON-serialized object for sticker to be added to the sticker set**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.add_sticker_to_set(
    user_id=your_user_id_here,
    name=your_name_here,
    sticker=your_sticker_here
)
```
