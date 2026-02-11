#🔧 set_my_default_administrator_rights

**Use this method to change the default administrator rights requested by the bot**

##⚙️ Parameters

- **`rights`** (**[ChatAdministratorRights](../types/ChatAdministratorRights.md)** ) (`optional`): **A JSON-serialized object describing new default administrator rights. If not specified,
the default administrator rights will be cleared.**
- **`for_channels`** (**`bool`** ) (`optional`): **Pass True to change the default administrator rights of the bot in channels.
Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.**

##📲 Returns

#### `bool`

##📀 Examples


-🔋 **All Parameters**

```python
await bot.set_my_default_administrator_rights(
    rights=your_rights_here,
    for_channels=your_for_channels_here
)
```
