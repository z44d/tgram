#🔧 decline_suggested_post

**Declines a suggested post in a direct messages chat.**

##⚙️ Parameters

- **`chat_id`** (**`int`** ): **Unique identifier for the target direct messages chat**
- **`message_id`** (**`int`** ): **Identifier of a suggested post message to decline**
- **`comment`** (**`str`** ) (`optional`): **Comment for the creator of the suggested post; 0-128 characters**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.decline_suggested_post(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.decline_suggested_post(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    comment=your_comment_here
)
```
