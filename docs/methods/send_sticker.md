#🔧 send_sticker

**Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`sticker`** (**`Path` or `bytes` or `str`** ): **Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL
as a String for Telegram to get a .webp file from the Internet, or upload a new one using multipart/form-data.**
- **`business_connection_id`** (**`str`** ) (`optional`): **Unique identifier for the target business connection**
- **`message_thread_id`** (**`int`** ) (`optional`): **Identifier of a message thread, in which the message will be sent**
- **`emoji`** (**`str`** ) (`optional`): **Emoji associated with the sticker; only for just uploaded stickers**
- **`disable_notification`** (**`bool`** ) (`optional`): **to disable the notification**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`** ) (`optional`): **Unique identifier for the message effect**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md) or [ReplyKeyboardMarkup](../types/ReplyKeyboardMarkup.md) or [ReplyKeyboardRemove](../types/ReplyKeyboardRemove.md) or [ForceReply](../types/ForceReply.md)** ) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
or to force a reply from the user.**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**
- **`suggested_post_parameters`** (**[SuggestedPostParameters](../types/SuggestedPostParameters.md)** ) (`optional`): **A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_sticker(
    chat_id=your_chat_id_here,
    sticker=your_sticker_here
)
```

-🔋 **All Parameters**

```python
await bot.send_sticker(
    chat_id=your_chat_id_here,
    sticker=your_sticker_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    emoji=your_emoji_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    message_effect_id=your_message_effect_id_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here,
    direct_messages_topic_id=your_direct_messages_topic_id_here,
    suggested_post_parameters=your_suggested_post_parameters_here
)
```
