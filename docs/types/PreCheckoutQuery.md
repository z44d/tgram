#🔮 PreCheckoutQuery

**This object contains information about an incoming pre-checkout query.**

##⚙️ Properties

- **`id`** (**`str`** ): **Unique query identifier**
- **`from_user`** (**[User](User.md)** )
- **`currency`** (**`str`** ): **Three-letter ISO 4217 currency code**
- **`total_amount`** (**`int`** ): **Total price in the smallest units of the currency (integer, not float/double). For example,
for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past
the decimal point for each currency (2 for the majority of currencies).**
- **`invoice_payload`** (**`str`** ): **Bot specified invoice payload**
- **`shipping_option_id`** (**`str`** ): **Optional. Identifier of the shipping option chosen by the user**
- **`order_info`** (**[OrderInfo](OrderInfo.md)** ): **Optional. Order information provided by the user**
