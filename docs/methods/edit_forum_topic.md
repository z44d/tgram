#🔧 edit_forum_topic

**Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`message_thread_id`** (**`int`** ): **Identifier of the topic to edit**
- **`name`** (**`str`** ) (`optional`): **Optional, New name of the topic, 1-128 characters. If not specififed or empty,
the current name of the topic will be kept**
- **`icon_custom_emoji_id`** (**`str`** ) (`optional`): **Optional, New unique identifier of the custom emoji shown as the topic icon.
Use getForumTopicIconStickers to get all allowed custom emoji identifiers. Pass an empty string to remove the
icon. If not specified, the current icon will be kept**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_forum_topic(
    chat_id=your_chat_id_here,
    message_thread_id=your_message_thread_id_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_forum_topic(
    chat_id=your_chat_id_here,
    message_thread_id=your_message_thread_id_here,
    name=your_name_here,
    icon_custom_emoji_id=your_icon_custom_emoji_id_here
)
```
