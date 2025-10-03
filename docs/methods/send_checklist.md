#🔧 send_checklist

**Use this method to send a checklist on behalf of a connected business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection on behalf of which the message will be sent**
- **`chat_id`** (**`int`** ): **Unique identifier for the target chat**
- **`checklist`** (**[InputChecklist](../types/InputChecklist.md)** ): **A JSON-serialized object for the checklist to send**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`** ) (`optional`): **Unique identifier of the message effect to be added to the message**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **A JSON-serialized object for description of the message to reply to**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`): **A JSON-serialized object for an inline keyboard**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_checklist(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    checklist=your_checklist_here
)
```

-🔋 **All Parameters**

```python
await bot.send_checklist(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    checklist=your_checklist_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here
)
```
