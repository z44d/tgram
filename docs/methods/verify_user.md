# verify_user

**Verifies a user on behalf of the organization which is represented by the bot. Returns True on success.**

## Parameters

- **`user_id`** (**`int`**): **Unique identifier of the target user**
- **`custom_description`** (**`str`**) (`optional`): **UCustom description for the verification; 0-70 characters.
Must be empty if the organization isn't allowed to provide a custom verification description.**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.verify_user(
    user_id=your_user_id_here
)
```

- **All Parameters**

```python
await bot.verify_user(
    user_id=your_user_id_here,
    custom_description=your_custom_description_here
)
```
