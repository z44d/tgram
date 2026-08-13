#🔮 SuggestedPostPaid

**Describes a service message about a successful payment for a suggested post.**

##⚙️ Properties

- **`suggested_post_message`** (**[Message](Message.md)** ): **Optional. Message containing the suggested post.**
- **`currency`** (**`str`** ): **Currency in which the payment was made. "XTR" for Telegram Stars or "TON" for toncoins.**
- **`amount`** (**`int`** ): **Optional. The amount of the currency that was received by the channel in nanotoncoins; for payments in toncoins only.**
- **`star_amount`** (**[StarAmount](StarAmount.md)** ): **Optional. The amount of Telegram Stars that was received by the channel; for payments in Telegram Stars only.**
