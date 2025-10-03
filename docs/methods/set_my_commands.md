#🔧 set_my_commands

**Use this method to change the list of the bot's commands.**

##⚙️ Parameters

- **`commands`** (**List of [BotCommand](../types/BotCommand.md)** ): **List of BotCommand. At most 100 commands can be specified.**
- **`scope`** (**[BotCommandScope](../types/BotCommandScope.md)** ) (`optional`): **The scope of users for which the commands are relevant.
Defaults to BotCommandScopeDefault.**
- **`language_code`** (**`str`** ) (`optional`): **A two-letter ISO 639-1 language code. If empty,
commands will be applied to all users from the given scope,
for whose language there are no dedicated commands**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_my_commands(
    commands=your_commands_here
)
```

-🔋 **All Parameters**

```python
await bot.set_my_commands(
    commands=your_commands_here,
    scope=your_scope_here,
    language_code=your_language_code_here
)
```
