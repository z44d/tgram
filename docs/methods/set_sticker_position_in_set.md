# set_sticker_position_in_set

**Use this method to move a sticker in a set created by the bot to a specific position . Returns True on success.**

## Parameters

- **`sticker`** (**`str`**): **File identifier of the sticker**
- **`position`** (**`int`**): **New sticker position in the set, zero-based**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.set_sticker_position_in_set(
    sticker=your_sticker_here,
    position=your_position_here
)
```
