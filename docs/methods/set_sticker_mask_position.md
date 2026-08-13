#🔧 set_sticker_mask_position

**Use this method to change the mask position of a mask sticker.**

##⚙️ Parameters

- **`sticker`** (**`str`** ): **File identifier of the sticker.**
- **`mask_position`** (**[MaskPosition](../types/MaskPosition.md)** ) (`optional`): **A JSON-serialized object for position where the mask should be placed on faces.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_sticker_mask_position(
    sticker=your_sticker_here
)
```

-🔋 **All Parameters**

```python
await bot.set_sticker_mask_position(
    sticker=your_sticker_here,
    mask_position=your_mask_position_here
)
```
