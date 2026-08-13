#🔧 send_venue

**Use this method to send information about a venue. On success, the sent Message is returned.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel**
- **`latitude`** (**`float`** ): **Latitude of the venue**
- **`longitude`** (**`float`** ): **Longitude of the venue**
- **`title`** (**`str`** ): **Name of the venue**
- **`address`** (**`str`** ): **Address of the venue**
- **`business_connection_id`** (**`str`** ) (`optional`): **Identifier of a business connection, in which the message will be sent**
- **`message_thread_id`** (**`int`** ) (`optional`): **The thread to which the message will be sent**
- **`foursquare_id`** (**`str`** ) (`optional`): **Foursquare identifier of the venue**
- **`foursquare_type`** (**`str`** ) (`optional`): **Foursquare type of the venue, if known. (For example, “arts_entertainment/default”,
“arts_entertainment/aquarium” or “food/icecream”.)**
- **`google_place_id`** (**`str`** ) (`optional`): **Google Places identifier of the venue**
- **`google_place_type`** (**`str`** ) (`optional`): **Google Places type of the venue.**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`** ) (`optional`): **Unique identifier of the message effect**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md) or [ReplyKeyboardMarkup](../types/ReplyKeyboardMarkup.md) or [ReplyKeyboardRemove](../types/ReplyKeyboardRemove.md) or [ForceReply](../types/ForceReply.md)** ) (`optional`): **Additional interface options. A JSON-serialized object for an inline keyboard,
custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**
- **`suggested_post_parameters`** (**[SuggestedPostParameters](../types/SuggestedPostParameters.md)** ) (`optional`): **A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_venue(
    chat_id=your_chat_id_here,
    latitude=your_latitude_here,
    longitude=your_longitude_here,
    title=your_title_here,
    address=your_address_here
)
```

-🔋 **All Parameters**

```python
await bot.send_venue(
    chat_id=your_chat_id_here,
    latitude=your_latitude_here,
    longitude=your_longitude_here,
    title=your_title_here,
    address=your_address_here,
    business_connection_id=your_business_connection_id_here,
    message_thread_id=your_message_thread_id_here,
    foursquare_id=your_foursquare_id_here,
    foursquare_type=your_foursquare_type_here,
    google_place_id=your_google_place_id_here,
    google_place_type=your_google_place_type_here,
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
