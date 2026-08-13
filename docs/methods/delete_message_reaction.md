#🔧 delete_message_reaction

**Use this method to delete a reaction from a message.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel**
- **`message_id`** (**`int`** ): **Identifier of the message**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.delete_message_reaction(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```
