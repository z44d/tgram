# get_my_description

**Use this method to get the current bot description for the given user language.**

## Parameters

- **`language_code`** (**`str`**) (`optional`): **A two-letter ISO 639-1 language code or an empty string**

## Returns

#### [BotDescription](../types/BotDescription.md)

## Examples


- **All Parameters**

```python
await bot.get_my_description(
    language_code=your_language_code_here
)
```
