#🔧 decline_chat_join_request

**Use this method to decline a chat join request.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target supergroup
(in the format @supergroupusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.decline_chat_join_request(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```
