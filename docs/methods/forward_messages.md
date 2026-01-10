#🔧 forward_messages

**Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded,**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`from_chat_id`** (**`int` or `str`** ): **Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)**
- **`message_ids`** (**List of `int`** ): **Message identifiers in the chat specified in from_chat_id**
- **`message_thread_id`** (**`int`** ) (`optional`): **Identifier of a message thread, in which the messages will be sent**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the forwarded message from forwarding and saving**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**

##📲 Returns

#### List of [MessageId](../types/MessageId.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.forward_messages(
    chat_id=your_chat_id_here,
    from_chat_id=your_from_chat_id_here,
    message_ids=your_message_ids_here
)
```

-🔋 **All Parameters**

```python
await bot.forward_messages(
    chat_id=your_chat_id_here,
    from_chat_id=your_from_chat_id_here,
    message_ids=your_message_ids_here,
    message_thread_id=your_message_thread_id_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    direct_messages_topic_id=your_direct_messages_topic_id_here
)
```
