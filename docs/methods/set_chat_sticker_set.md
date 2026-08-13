#🔧 set_chat_sticker_set

**Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)**
- **`sticker_set_name`** (**`str`** ): **Name of the sticker set to be set as the group sticker set**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_chat_sticker_set(
    chat_id=your_chat_id_here,
    sticker_set_name=your_sticker_set_name_here
)
```
