#🔧 forward_message

**Use this method to forward messages of any kind.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`from_chat_id`** (**`int` or `str`** ): **Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)**
- **`message_id`** (**`int`** ): **Message identifier in the chat specified in from_chat_id**
- **`message_thread_id`** (**`int`** ) (`optional`): **Unique identifier for the target message thread (topic) of the forum; for forum supergroups only**
- **`video_start_timestamp`** (**`int`** ) (`optional`): **New start timestamp for the forwarded video in the message**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the forwarded message from forwarding and saving**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**
- **`suggested_post_parameters`** (**[SuggestedPostParameters](../types/SuggestedPostParameters.md)** ) (`optional`): **A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.**
- **`message_effect_id`** (**`str`** ) (`optional`): **Unique identifier of the message effect to be added to the message**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.forward_message(
    chat_id=your_chat_id_here,
    from_chat_id=your_from_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.forward_message(
    chat_id=your_chat_id_here,
    from_chat_id=your_from_chat_id_here,
    message_id=your_message_id_here,
    message_thread_id=your_message_thread_id_here,
    video_start_timestamp=your_video_start_timestamp_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    direct_messages_topic_id=your_direct_messages_topic_id_here,
    suggested_post_parameters=your_suggested_post_parameters_here,
    message_effect_id=your_message_effect_id_here
)
```
