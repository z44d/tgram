#🔧 create_invoice_link

**Use this method to create a link for an invoice.**

##⚙️ Parameters

- **`title`** (**`str`** ): **Product name, 1-32 characters**
- **`description`** (**`str`** ): **Product description, 1-255 characters**
- **`payload`** (**`str`** ): **Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
use for your internal processes.**
- **`currency`** (**`str`** ): **Three-letter ISO 4217 currency code,
see https://core.telegram.org/bots/payments#supported-currencies**
- **`prices`** (**List of [LabeledPrice](../types/LabeledPrice.md)** ): **Price breakdown, a list of components
(e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)**
- **`business_connection_id`** (**`str`** ) (`optional`): **Unique identifier of the business connection on behalf of which the link will be created.**
- **`subscription_period`** (**`int`** ) (`optional`): **The number of seconds the subscription will be active for before the next payment.
The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified.**
- **`provider_token`** (**`str`** ) (`optional`): **Payments provider token, obtained via @Botfather; Pass None to omit the parameter
to use "XTR" currency**
- **`max_tip_amount`** (**`int`** ) (`optional`): **The maximum accepted amount for tips in the smallest units of the currency**
- **`suggested_tip_amounts`** (**List of `int`** ) (`optional`): **A JSON-serialized array of suggested amounts of tips in the smallest
units of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip
amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.**
- **`provider_data`** (**`str`** ) (`optional`): **A JSON-serialized data about the invoice, which will be shared with the payment provider.
A detailed description of required fields should be provided by the payment provider.**
- **`photo_url`** (**`str`** ) (`optional`): **URL of the product photo for the invoice. Can be a photo of the goods
or a photo of the invoice. People like it better when they see a photo of what they are paying for.**
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

##📲 Returns

#### `str`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.create_invoice_link(
    title=your_title_here,
    description=your_description_here,
    payload=your_payload_here,
    currency=your_currency_here,
    prices=your_prices_here
)
```

-🔋 **All Parameters**

```python
await bot.create_invoice_link(
    title=your_title_here,
    description=your_description_here,
    payload=your_payload_here,
    currency=your_currency_here,
    prices=your_prices_here,
    business_connection_id=your_business_connection_id_here,
    subscription_period=your_subscription_period_here,
    provider_token=your_provider_token_here,
    max_tip_amount=your_max_tip_amount_here,
    suggested_tip_amounts=your_suggested_tip_amounts_here,
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
    is_flexible=your_is_flexible_here
)
```
