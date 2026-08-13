#🔧 set_chat_title

**Use this method to change the title of a chat. Titles can't be changed for private chats.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**
- **`title`** (**`str`** ): **New chat title, 1-255 characters**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_chat_title(
    chat_id=your_chat_id_here,
    title=your_title_here
)
```
