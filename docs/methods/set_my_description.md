# set_my_description

**Use this method to change the bot's description, which is shown in**

## Parameters

- **`description`** (**`str`**) (`optional`): **New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.**
- **`language_code`** (**`str`**) (`optional`): **A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for
whose language there is no dedicated description.**

## Returns

#### `bool`

## Examples


- **All Parameters**

```python
await bot.set_my_description(
    description=your_description_here,
    language_code=your_language_code_here
)
```
