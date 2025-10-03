#🔧 get_custom_emoji_stickers

**Use this method to get information about custom emoji stickers by their identifiers.**

##⚙️ Parameters

- **`custom_emoji_ids`** (**List of `str`** ): **List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.**

##📲 Returns

#### List of [Sticker](../types/Sticker.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.get_custom_emoji_stickers(
    custom_emoji_ids=your_custom_emoji_ids_here
)
```
