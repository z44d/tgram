# send_message

**Use this method to send text messages.**

## Parameters

- **`chat_id`** (**`int, str`**): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`text`** (**`str`**): **Text of the message to be sent**
- **`business_connection_id`** (**`str`**) (`optional`): **Unique identifier for the target business connection**
- **`message_thread_id`** (**`int`**) (`optional`): **Unique identifier for the target message thread (topic) of the forum; for forum supergroups only**
- **`parse_mode`** (**`Literal`**) (`optional`): **Mode for parsing entities in the message text.**
- **`entities`** (**List of [MessageEntity](../types/MessageEntity.md)**) (`optional`): **List of special entities that appear in message text, which can be specified instead of parse_mode**
- **`link_preview_options`** (**[LinkPreviewOptions](../types/LinkPreviewOptions.md)**) (`optional`): **Options for previewing links.**
- **`disable_notification`** (**`bool`**) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`**) (`optional`): **If True, the message content will be hidden for all users except for the target user**
- **`message_effect_id`** (**`str`**) (`optional`): **Unique identifier for the message effect**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)**) (`optional`): **Reply parameters.**
- **`reply_markup`** (**`InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply`**) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.**
- **`allow_paid_broadcast`** (**`bool`**) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**

## Returns

#### [Message](../types/Message.md)

## Examples

- **Required Parameters**

```python
await bot.send_message(
    chat_id=your_chat_id_here,
    text=your_text_here
)
```

- **All Parameters**

```python
await bot.send_message(
    chat_id=your_chat_id_here,
    text=your_text_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    parse_mode=your_parse_mode_here,
    entities=your_entities_here,
    link_preview_options=your_link_preview_options_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here
)
```
