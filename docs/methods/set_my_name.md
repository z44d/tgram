# set_my_name

**Use this method to change the bot's name. Returns True on success.**

## Parameters

- **`name`** (**`str`**) (`optional`): **Optional. New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language.**
- **`language_code`** (**`str`**) (`optional`): **Optional. A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose
language there is no dedicated name.**

## Returns

#### `bool`

## Examples


- **All Parameters**

```python
await bot.set_my_name(
    name=your_name_here,
    language_code=your_language_code_here
)
```
