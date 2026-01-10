#🔧 send_message_draft

**Use this method to send a draft message while it is being generated.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection on behalf
of which the message will be sent**
- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel**
- **`text`** (**`str`** ): **Text of the message draft to be sent**
- **`message_thread_id`** (**`int`** ) (`optional`): **Unique identifier for the target message thread (topic) of the forum;
for forum supergroups only**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_message_draft(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    text=your_text_here
)
```

-🔋 **All Parameters**

```python
await bot.send_message_draft(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    text=your_text_here,
    message_thread_id=your_message_thread_id_here
)
```
