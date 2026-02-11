#🔮 TransactionPartnerUser

**Describes a transaction with a user.**

##⚙️ Properties

- **`user`** (**[User](User.md)** ): **Information about the user**
- **`transaction_type`** (**`str`** ): **Type of the transaction, currently one of “invoice_payment”, “paid_media_payment”, “gift_purchase”, “premium_purchase”, “business_account_transfer”**
- **`affiliate`** (**[AffiliateInfo](AffiliateInfo.md)** ): **Optional. Information about the affiliate that received a commission via this transaction. Can be available only for “invoice_payment” and “paid_media_payment” transactions.**
- **`invoice_payload`** (**`str`** ): **Optional. Bot-specified invoice payload. Can be available only for “invoice_payment” transactions.**
- **`subscription_period`** (**`int`** ): **Optional. The duration of the paid subscription. Can be available only for “invoice_payment” transactions.**
- **`paid_media`** (**List of `PaidMedia`** ): **Optional. Information about the paid media bought by the user; for “paid_media_payment” transactions only**
- **`paid_media_payload`** (**`str`** ): **Optional. Bot-specified paid media payload. Can be available only for “paid_media_payment” transactions.**
- **`gift`** (**[Gift](Gift.md)** ): **Optional. The gift sent to the user by the bot; for “gift_purchase” transactions only**
- **`premium_subscription_duration`** (**`int`** ): **Optional. Number of months the gifted Telegram Premium subscription will be active for; for “premium_purchase” transactions only**
