#🔧 set_managed_bot_access_settings

**Use this method to change the access settings of a managed bot.**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **User identifier of the managed bot whose access settings will be changed**
- **`is_access_restricted`** (**`bool`** ): **Pass True, if only selected users can access the bot. The bot's owner can always access it.**
- **`added_user_ids`** (**List of `int`** ) (`optional`): **A list of up to 10 identifiers of users who will have access to the bot in addition to its owner.
Ignored if is_access_restricted is false.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_managed_bot_access_settings(
    user_id=your_user_id_here,
    is_access_restricted=your_is_access_restricted_here
)
```

-🔋 **All Parameters**

```python
await bot.set_managed_bot_access_settings(
    user_id=your_user_id_here,
    is_access_restricted=your_is_access_restricted_here,
    added_user_ids=your_added_user_ids_here
)
```
