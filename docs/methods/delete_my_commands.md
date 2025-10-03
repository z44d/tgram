#🔧 delete_my_commands

**Use this method to delete the list of the bot's commands for the given scope and user language.**

##⚙️ Parameters

- **`scope`** (**[BotCommandScope](../types/BotCommandScope.md)** ) (`optional`): **The scope of users for which the commands are relevant.
Defaults to BotCommandScopeDefault.**
- **`language_code`** (**`str`** ) (`optional`): **A two-letter ISO 639-1 language code. If empty,
commands will be applied to all users from the given scope,
for whose language there are no dedicated commands**

##📲 Returns

#### `bool`

##📀 Examples


-🔋 **All Parameters**

```python
await bot.delete_my_commands(
    scope=your_scope_here,
    language_code=your_language_code_here
)
```
