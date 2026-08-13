#🔮 GiveawayCompleted

**This object represents a service message about the completion of a giveaway without public winners.**

##⚙️ Properties

- **`winner_count`** (**`int`** ): **Number of winners in the giveaway**
- **`unclaimed_prize_count`** (**`int`** ): **Optional. Number of undistributed prizes**
- **`giveaway_message`** (**[Message](Message.md)** ): **Optional. Message with the giveaway that was completed, if it wasn't deleted**
- **`is_star_giveaway`** (**`bool`** ): **Optional. True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.**
