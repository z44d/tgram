#🔧 get_chat_administrators

****

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** )
- **`return_bots`** (**`bool`** ) (`optional`)

##📲 Returns

#### List of [ChatMemberAdministrator](../types/ChatMemberAdministrator.md) or [ChatMemberOwner](../types/ChatMemberOwner.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.get_chat_administrators(
    chat_id=your_chat_id_here
)
```

-🔋 **All Parameters**

```python
await bot.get_chat_administrators(
    chat_id=your_chat_id_here,
    return_bots=your_return_bots_here
)
```
