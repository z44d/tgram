#🔧 set_chat_member_tag

**Use this method to set a custom profile tag for a chat member.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`tag`** (**`str`** ): **New profile tag for the user. May be an empty string to remove the tag.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_chat_member_tag(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    tag=your_tag_here
)
```
