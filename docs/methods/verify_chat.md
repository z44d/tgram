#🔧 verify_chat

**Verifies a chat on behalf of the organization which is represented by the bot. Returns True on success.**

##⚙️ Parameters

- **`chat_id`** (**`str` or `int`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`custom_description`** (**`str`** ) (`optional`): **UCustom description for the verification; 0-70 characters.
Must be empty if the organization isn't allowed to provide a custom verification description.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.verify_chat(
    chat_id=your_chat_id_here
)
```

-🔋 **All Parameters**

```python
await bot.verify_chat(
    chat_id=your_chat_id_here,
    custom_description=your_custom_description_here
)
```
