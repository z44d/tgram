#🔧 send_game

**Used to send the game.**

##⚙️ Parameters

- **`chat_id`** (**`int`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`game_short_name`** (**`str`** ): **Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather.**
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of the business connection.**
- **`message_thread_id`** (**`int`** ) (`optional`): **Identifier of the thread to which the message will be sent.**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Pass True, if content of the message needs to be protected from being viewed by the bot.**
- **`message_effect_id`** (**`str`** ) (`optional`): **Identifier of the message effect.**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_game(
    chat_id=your_chat_id_here,
    game_short_name=your_game_short_name_here
)
```

-🔋 **All Parameters**

```python
await bot.send_game(
    chat_id=your_chat_id_here,
    game_short_name=your_game_short_name_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here
)
```
