#🔧 remove_chat_verification

**Removes verification from a chat that is currently verified on behalf of the organization represented by the bot. Returns True on success.**

##⚙️ Parameters

- **`chat_id`** (**`str` or `int`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.remove_chat_verification(
    chat_id=your_chat_id_here
)
```
