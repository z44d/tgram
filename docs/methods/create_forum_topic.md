#🔧 create_forum_topic

**Use this method to create a topic in a forum supergroup chat. The bot must be an administrator**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`name`** (**`str`** ): **Name of the topic, 1-128 characters**
- **`icon_color`** (**`int`** ) (`optional`): **Color of the topic icon in RGB format. Currently, must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F**
- **`icon_custom_emoji_id`** (**`str`** ) (`optional`): **Custom emoji for the topic icon. Must be an emoji of type “tgs” and must be exactly 1 character long**

##📲 Returns

#### [ForumTopic](../types/ForumTopic.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.create_forum_topic(
    chat_id=your_chat_id_here,
    name=your_name_here
)
```

-🔋 **All Parameters**

```python
await bot.create_forum_topic(
    chat_id=your_chat_id_here,
    name=your_name_here,
    icon_color=your_icon_color_here,
    icon_custom_emoji_id=your_icon_custom_emoji_id_here
)
```
