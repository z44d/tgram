#🔧 set_my_short_description

**Use this method to change the bot's short description, which is shown on the bot's profile page and**

##⚙️ Parameters

- **`short_description`** (**`str`** ) (`optional`): **New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language.**
- **`language_code`** (**`str`** ) (`optional`): **A two-letter ISO 639-1 language code.
If empty, the short description will be applied to all users for whose language there is no dedicated short description.**

##📲 Returns

#### `bool`

##📀 Examples


-🔋 **All Parameters**

```python
await bot.set_my_short_description(
    short_description=your_short_description_here,
    language_code=your_language_code_here
)
```
