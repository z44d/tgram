#🔮 AffiliateInfo

**This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).**

##⚙️ Properties

- **`affiliate_user`** (**[User](User.md)** ): **Optional. The bot or the user that received an affiliate commission if it was received by a bot or a user**
- **`affiliate_chat`** (**[Chat](Chat.md)** ): **Optional. The chat that received an affiliate commission if it was received by a chat**
- **`commission_per_mille`** (**`int`** ): **The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users**
- **`amount`** (**`int`** ): **Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds**
- **`nanostar_amount`** (**`int`** ): **Optional. The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds**
