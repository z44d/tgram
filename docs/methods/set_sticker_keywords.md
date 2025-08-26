# set_sticker_keywords

**Use this method to change search keywords assigned to a regular or custom emoji sticker.**

## Parameters

- **`sticker`** (**`str`**): **File identifier of the sticker.**
- **`keywords`** (**List of `str`**) (`optional`): **A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.set_sticker_keywords(
    sticker=your_sticker_here
)
```

- **All Parameters**

```python
await bot.set_sticker_keywords(
    sticker=your_sticker_here,
    keywords=your_keywords_here
)
```
