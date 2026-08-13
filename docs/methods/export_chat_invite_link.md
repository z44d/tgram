#🔧 export_chat_invite_link

**Use this method to export an invite link to a supergroup or a channel. The bot must be an administrator**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Id: Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**

##📲 Returns

#### `str`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.export_chat_invite_link(
    chat_id=your_chat_id_here
)
```
