#🔧 send_paid_media

**Use this method to send paid media to channel chats. On success, the sent Message is returned.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`star_count`** (**`int`** ): **The number of Telegram Stars that must be paid to buy access to the media**
- **`media`** (**List of [InputPaidMediaPhoto](../types/InputPaidMediaPhoto.md) or [InputPaidMediaVideo](../types/InputPaidMediaVideo.md)** ): **A JSON-serialized array describing the media to be sent; up to 10 items**
- **`payload`** (**`str`** ) (`optional`): **Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes.**
- **`caption`** (**`str`** ) (`optional`): **Media caption, 0-1024 characters after entities parsing**
- **`parse_mode`** (**`Literal`** ) (`optional`): **Mode for parsing entities in the media caption**
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **List of special entities that appear in the caption, which can be specified instead of parse_mode**
- **`show_caption_above_media`** (**`bool`** ) (`optional`): **Pass True, if the caption must be shown above the message media**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Description of the message to reply to**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md) or [ReplyKeyboardMarkup](../types/ReplyKeyboardMarkup.md) or [ReplyKeyboardRemove](../types/ReplyKeyboardRemove.md) or [ForceReply](../types/ForceReply.md)** ) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user**
- **`business_connection_id`** (**`str`** ) (`optional`): **Unique identifier of the business connection on behalf of which the message will be sent**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**
- **`suggested_post_parameters`** (**[SuggestedPostParameters](../types/SuggestedPostParameters.md)** ) (`optional`): **A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_paid_media(
    chat_id=your_chat_id_here,
    star_count=your_star_count_here,
    media=your_media_here
)
```

-🔋 **All Parameters**

```python
await bot.send_paid_media(
    chat_id=your_chat_id_here,
    star_count=your_star_count_here,
    media=your_media_here,
    payload=your_payload_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    show_caption_above_media=your_show_caption_above_media_here,
    disable_notification=your_disable_notification_here,
    protect_content=your_protect_content_here,
    reply_parameters=your_reply_parameters_here,
    reply_markup=your_reply_markup_here,
    business_connection_id=your_business_connection_id_here,
    allow_paid_broadcast=your_allow_paid_broadcast_here,
    direct_messages_topic_id=your_direct_messages_topic_id_here,
    suggested_post_parameters=your_suggested_post_parameters_here
)
```
