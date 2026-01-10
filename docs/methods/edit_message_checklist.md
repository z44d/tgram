#🔧 edit_message_checklist

**Use this method to edit a checklist on behalf of a connected business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection on behalf of which the message will be sent**
- **`chat_id`** (**`int`** ): **Unique identifier for the target chat**
- **`message_id`** (**`int`** ): **Unique identifier for the target message**
- **`checklist`** (**[InputChecklist](../types/InputChecklist.md)** ): **A JSON-serialized object for the new checklist**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`): **A JSON-serialized object for the new inline keyboard for the message**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_message_checklist(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    checklist=your_checklist_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_message_checklist(
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    checklist=your_checklist_here,
    reply_markup=your_reply_markup_here
)
```
