#🔧 edit_general_forum_topic

**Use this method to edit the name of the 'General' topic in a forum supergroup chat.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`name`** (**`str`** ): **New topic name, 1-128 characters**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_general_forum_topic(
    chat_id=your_chat_id_here,
    name=your_name_here
)
```
