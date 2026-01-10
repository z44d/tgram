#🔧 send_poll

**Use this method to send a native poll.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel**
- **`question`** (**`str`** ): **Poll question, 1-300 characters**
- **`options`** (**List of [InputPollOption](../types/InputPollOption.md)** ): **A JSON-serialized list of 2-10 answer options**
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of the business connection to send the message through**
- **`message_thread_id`** (**`int`** ) (`optional`): **The identifier of a message thread, in which the poll will be sent**
- **`question_parse_mode`** (**`Literal`** ) (`optional`): **Mode for parsing entities in the question. See formatting options for more details. Currently, only custom emoji entities are allowed**
- **`question_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of question_parse_mode**
- **`is_anonymous`** (**`bool`** ) (`optional`): **True, if the poll needs to be anonymous, defaults to True**
- **`type`** (**`str`** ) (`optional`): **Poll type, “quiz” or “regular”, defaults to “regular”**
- **`allows_multiple_answers`** (**`bool`** ) (`optional`): **True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False**
- **`correct_option_id`** (**`int`** ) (`optional`): **0-based identifier of the correct answer option. Available only for polls in quiz mode,
defaults to None**
- **`explanation`** (**`str`** ) (`optional`): **Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll,
0-200 characters with at most 2 line feeds after entities parsing**
- **`explanation_parse_mode`** (**`Literal`** ) (`optional`): **Mode for parsing entities in the explanation. See formatting options for more details.**
- **`explanation_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **A JSON-serialized list of special entities that appear in the explanation,
which can be specified instead of parse_mode**
- **`open_period`** (**`int`** ) (`optional`): **Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.**
- **`close_date`** (**`int`** ) (`optional`): **Point in time (Unix timestamp) when the poll will be automatically closed.**
- **`is_closed`** (**`bool`** ) (`optional`): **Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`** ) (`optional`): **Identifier of the message effect to apply to the sent message**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md) or [ReplyKeyboardMarkup](../types/ReplyKeyboardMarkup.md) or [ReplyKeyboardRemove](../types/ReplyKeyboardRemove.md) or [ForceReply](../types/ForceReply.md)** ) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard,
instructions to remove reply keyboard or to force a reply from the user.**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_poll(
    chat_id=your_chat_id_here,
    question=your_question_here,
    options=your_options_here
)
```

-🔋 **All Parameters**

```python
await bot.send_poll(
    chat_id=your_chat_id_here,
    question=your_question_here,
    options=your_options_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    question_parse_mode=your_question_parse_mode_here,
    question_entities=your_question_entities_here,
    is_anonymous=your_is_anonymous_here,
    type=your_type_here,
    allows_multiple_answers=your_allows_multiple_answers_here,
    correct_option_id=your_correct_option_id_here,
    explanation=your_explanation_here,
    explanation_parse_mode=your_explanation_parse_mode_here,
    explanation_entities=your_explanation_entities_here,
    open_period=your_open_period_here,
    close_date=your_close_date_here,
    is_closed=your_is_closed_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here
)
```
