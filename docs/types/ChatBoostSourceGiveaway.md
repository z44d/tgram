#🔮 ChatBoostSourceGiveaway

**The boost was obtained by the creation of a Telegram Premium giveaway.**

##⚙️ Properties

- **`source`** (**`str`** ): **Source of the boost, always “giveaway”**
- **`giveaway_message_id`** (**`int`** ): **Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet.**
- **`user`** (**[User](User.md)** ): **User that won the prize in the giveaway if any**
- **`prize_star_count`** (**`int`** ): **Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only**
- **`is_unclaimed`** (**`bool`** ): **True, if the giveaway was completed, but there was no user to win the prize**
