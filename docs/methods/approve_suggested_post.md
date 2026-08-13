#🔧 approve_suggested_post

**Approves a suggested post in a direct messages chat.**

##⚙️ Parameters

- **`chat_id`** (**`int`** ): **Unique identifier for the target direct messages chat**
- **`message_id`** (**`int`** ): **Identifier of a suggested post message to approve**
- **`send_date`** (**`int`** ) (`optional`): **Point in time (Unix timestamp) when the post is expected to be published;
omit if the date has already been specified when the suggested post was created.
If specified, then the date must be not more than 2678400 seconds (30 days) in the future**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.approve_suggested_post(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.approve_suggested_post(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    send_date=your_send_date_here
)
```
