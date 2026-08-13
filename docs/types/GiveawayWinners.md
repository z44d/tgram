#🔮 GiveawayWinners

**This object represents a message about the completion of a giveaway with public winners.**

##⚙️ Properties

- **`chat`** (**[Chat](Chat.md)** ): **The chat that created the giveaway**
- **`giveaway_message_id`** (**`int`** ): **Identifier of the messsage with the giveaway in the chat**
- **`winners_selection_date`** (**`int`** ): **Point in time (Unix timestamp) when winners of the giveaway were selected**
- **`winner_count`** (**`int`** ): **Total number of winners in the giveaway**
- **`winners`** (**List of [User](User.md)** ): **List of up to 100 winners of the giveaway**
- **`additional_chat_count`** (**`int`** ): **Optional. The number of other chats the user had to join in order to be eligible for the giveaway**
- **`prize_star_count`** (**`int`** ): **Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only**
- **`premium_subscription_month_count`** (**`int`** ): **Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for**
- **`unclaimed_prize_count`** (**`int`** ): **Optional. Number of undistributed prizes**
- **`only_new_members`** (**`bool`** ): **Optional. True, if only users who had joined the chats after the giveaway started were eligible to win**
- **`was_refunded`** (**`bool`** ): **Optional. True, if the giveaway was canceled because the payment for it was refunded**
- **`prize_description`** (**`str`** ): **Optional. Description of additional giveaway prize**
