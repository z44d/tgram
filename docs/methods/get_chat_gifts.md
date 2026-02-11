#🔧 get_chat_gifts

**Use this method to get the list of gifts received by a chat.**

##⚙️ Parameters

- **`chat_id`** (**`int`** ): **Unique identifier of the target chat**
- **`offset`** (**`str`** ) (`optional`): **Offset of the first entry to return; use empty string for first chunk**
- **`limit`** (**`int`** ) (`optional`): **Maximum number of gifts to return; 1-100, defaults to 100**

##📲 Returns

#### [OwnedGifts](../types/OwnedGifts.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.get_chat_gifts(
    chat_id=your_chat_id_here
)
```

-🔋 **All Parameters**

```python
await bot.get_chat_gifts(
    chat_id=your_chat_id_here,
    offset=your_offset_here,
    limit=your_limit_here
)
```
