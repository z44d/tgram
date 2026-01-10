#🔧 send_invoice

**Sends invoice.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target private chat**
- **`title`** (**`str`** ): **Product name, 1-32 characters**
- **`description`** (**`str`** ): **Product description, 1-255 characters**
- **`payload`** (**`str`** )
- **`currency`** (**`str`** ): **Three-letter ISO 4217 currency code,
see https://core.telegram.org/bots/payments#supported-currencies**
- **`prices`** (**List of [LabeledPrice](../types/LabeledPrice.md)** ): **Price breakdown, a list of components
(e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)**
- **`message_thread_id`** (**`int`** ) (`optional`): **The identifier of a message thread, in which the invoice message will be sent**
- **`provider_token`** (**`str`** ) (`optional`): **Payments provider token, obtained via @Botfather; Pass None to omit the parameter
to use "XTR" currency**
- **`max_tip_amount`** (**`int`** ) (`optional`): **The maximum accepted amount for tips in the smallest units of the currency**
- **`suggested_tip_amounts`** (**List of `int`** ) (`optional`): **A JSON-serialized array of suggested amounts of tips in the smallest
units of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip
amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.**
- **`start_parameter`** (**`str`** ) (`optional`): **Unique deep-linking parameter that can be used to generate this invoice
when used as a start parameter**
- **`provider_data`** (**`str`** ) (`optional`): **A JSON-serialized data about the invoice, which will be shared with the payment provider.
A detailed description of required fields should be provided by the payment provider.**
- **`photo_url`** (**`str`** ) (`optional`): **URL of the product photo for the invoice. Can be a photo of the goods
or a marketing image for a service. People like it better when they see what they are paying for.**
- **`photo_size`** (**`int`** ) (`optional`): **Photo size in bytes**
- **`photo_width`** (**`int`** ) (`optional`): **Photo width**
- **`photo_height`** (**`int`** ) (`optional`): **Photo height**
- **`need_name`** (**`bool`** ) (`optional`): **Pass True, if you require the user's full name to complete the order**
- **`need_phone_number`** (**`bool`** ) (`optional`): **Pass True, if you require the user's phone number to complete the order**
- **`need_email`** (**`bool`** ) (`optional`): **Pass True, if you require the user's email to complete the order**
- **`need_shipping_address`** (**`bool`** ) (`optional`): **Pass True, if you require the user's shipping address to complete the order**
- **`send_phone_number_to_provider`** (**`bool`** ) (`optional`): **Pass True, if user's phone number should be sent to provider**
- **`send_email_to_provider`** (**`bool`** ) (`optional`): **Pass True, if user's email address should be sent to provider**
- **`is_flexible`** (**`bool`** ) (`optional`): **Pass True, if the final price depends on the shipping method**
- **`disable_notification`** (**`bool`** ) (`optional`): **Sends the message silently. Users will receive a notification with no sound.**
- **`protect_content`** (**`bool`** ) (`optional`): **Protects the contents of the sent message from forwarding and saving**
- **`message_effect_id`** (**`str`** ) (`optional`): **The identifier of a message effect to be applied to the message**
- **`reply_parameters`** (**[ReplyParameters](../types/ReplyParameters.md)** ) (`optional`): **Reply parameters.**
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`): **A JSON-serialized object for an inline keyboard. If empty,
one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button**
- **`allow_paid_broadcast`** (**`bool`** ) (`optional`): **Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
The relevant Stars will be withdrawn from the bot's balance**
- **`direct_messages_topic_id`** (**`int`** ) (`optional`): **Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat**
- **`suggested_post_parameters`** (**[SuggestedPostParameters](../types/SuggestedPostParameters.md)** ) (`optional`): **A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.**

##📲 Returns

#### [Message](../types/Message.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_invoice(
    chat_id=your_chat_id_here,
    title=your_title_here,
    description=your_description_here,
    payload=your_payload_here,
    currency=your_currency_here,
    prices=your_prices_here
)
```

-🔋 **All Parameters**

```python
await bot.send_invoice(
    chat_id=your_chat_id_here,
    title=your_title_here,
    description=your_description_here,
    payload=your_payload_here,
    currency=your_currency_here,
    prices=your_prices_here,
    message_thread_id=your_message_thread_id_here,
    provider_token=your_provider_token_here,
    max_tip_amount=your_max_tip_amount_here,
    suggested_tip_amounts=your_suggested_tip_amounts_here,
    start_parameter=your_start_parameter_here,
    provider_data=your_provider_data_here,
    photo_url=your_photo_url_here,
    photo_size=your_photo_size_here,
    photo_width=your_photo_width_here,
    photo_height=your_photo_height_here,
    need_name=your_need_name_here,
    need_phone_number=your_need_phone_number_here,
    need_email=your_need_email_here,
    need_shipping_address=your_need_shipping_address_here,
    send_phone_number_to_provider=your_send_phone_number_to_provider_here,
    send_email_to_provider=your_send_email_to_provider_here,
    is_flexible=your_is_flexible_here,
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
