#🔧 pin_chat_message

**Use this method to pin a message in a supergroup.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**
- **`message_id`** (**`int`** ): **Identifier of a message to pin**
- **`disable_notification`** (**`bool`** ) (`optional`): **Pass True, if it is not necessary to send a notification
to all group members about the new pinned message**
- **`business_connection_id`** (**`str`** ) (`optional`): **Unique identifier of the business connection on behalf of which the message will be pinned**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.pin_chat_message(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.pin_chat_message(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    disable_notification=your_disable_notification_here,
    business_connection_id=your_business_connection_id_here
)
```
