#🔧 remove_user_verification

**Removes verification from a user who is currently verified on behalf of the organization represented by the bot. Returns True on success.**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **Unique identifier of the target user**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.remove_user_verification(
    user_id=your_user_id_here
)
```
