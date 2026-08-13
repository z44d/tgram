#🔧 get_my_default_administrator_rights

**Use this method to get the current default administrator rights of the bot.**

##⚙️ Parameters

- **`for_channels`** (**`bool`** ) (`optional`): **Pass True to get the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be returned.**

##📲 Returns

#### [ChatAdministratorRights](../types/ChatAdministratorRights.md)

##📀 Examples


-🔋 **All Parameters**

```python
await bot.get_my_default_administrator_rights(
    for_channels=your_for_channels_here
)
```
