#🔧 set_chat_menu_button

**Use this method to change the bot's menu button in a private chat,**

##⚙️ Parameters

- **`chat_id`** (**`int`** ) (`optional`): **Unique identifier for the target private chat.
If not specified, default bot's menu button will be changed.**
- **`menu_button`** (**[MenuButton](../types/MenuButton.md)** ) (`optional`): **A JSON-serialized object for the new bot's menu button. Defaults to MenuButtonDefault**

##📲 Returns

#### `bool`

##📀 Examples


-🔋 **All Parameters**

```python
await bot.set_chat_menu_button(
    chat_id=your_chat_id_here,
    menu_button=your_menu_button_here
)
```
