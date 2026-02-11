#🔧 set_chat_administrator_custom_title

**Use this method to set a custom title for an administrator in a supergroup promoted by the bot.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target supergroup
(in the format @supergroupusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`custom_title`** (**`str`** ): **New custom title for the administrator;
0-16 characters, emoji are not allowed**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_chat_administrator_custom_title(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    custom_title=your_custom_title_here
)
```
