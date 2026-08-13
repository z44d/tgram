#🔧 replace_managed_bot_token

**Use this method to replace the current bot token for a managed bot.**

##⚙️ Parameters

- **`managed_bot_user_id`** (**`int`** )
- **`reason`** (**`str`** ) (`optional`)

##📲 Returns

#### `str`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.replace_managed_bot_token(
    managed_bot_user_id=your_managed_bot_user_id_here
)
```

-🔋 **All Parameters**

```python
await bot.replace_managed_bot_token(
    managed_bot_user_id=your_managed_bot_user_id_here,
    reason=your_reason_here
)
```
