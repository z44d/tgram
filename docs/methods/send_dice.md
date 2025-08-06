# send_dice

**Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.**

## Parameters

- **`chat_id`** (**`int, str`**): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`business_connection_id`** (**`str`**) (`optional`): **Unique identifier for the target business connection**
- **`message_thread_id`** (**`int`**) (`optional`): **The identifier of a message thread, unique within the chat to which the message with the thread identifier belongs**
- **`emoji`** (**`str`**) (`optional`): **Emoji on which the dice throw animation is based. Currently, must be one of “🎲”, “🎯”, “🏀”, “⚽”, “🎳”, or “🎰”.
Dice can have values 1-6 for “🎲”, “🎯” and “🎳”, values 1-5 for “🏀” and “⚽”, and values 1-64 for “🎰”. Defaults to “🎲”**
- **`disable_notification`** (**`bool`**) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`**) (`optional`): **Protects the contents of the sent message from forwarding**
- **`message_effect_id`** (**`str`**) (`optional`): **Unique identifier for the message effect**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)**) (`optional`): **Reply parameters.**
- **`reply_markup`** (**`InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply`**) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions
to remove reply keyboard or to force a reply from the user.**
- **`allow_paid_broadcast`** (**`bool`**) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**

## Returns

#### [Message](../types/Message.md)

## Examples

- **Required Parameters**

```python
await bot.send_dice(
    chat_id=your_chat_id_here
)
```

- **All Parameters**

```python
await bot.send_dice(
    chat_id=your_chat_id_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    emoji=your_emoji_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here
)
```
