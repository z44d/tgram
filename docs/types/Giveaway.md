#🔮 Giveaway

**This object represents a message about a scheduled giveaway.**

##⚙️ Properties

- **`chats`** (**List of [Chat](Chat.md)** ): **The list of chats which the user must join to participate in the giveaway**
- **`winners_selection_date`** (**`int`** ): **Point in time (Unix timestamp) when winners of the giveaway will be selected**
- **`winner_count`** (**`int`** ): **The number of users which are supposed to be selected as winners of the giveaway**
- **`only_new_members`** (**`bool`** ): **Optional. True, if only users who join the chats after the giveaway started should be eligible to win**
- **`has_public_winners`** (**`bool`** ): **Optional. True, if the list of giveaway winners will be visible to everyone**
- **`prize_description`** (**`str`** ): **Optional. Description of additional giveaway prize**
- **`country_codes`** (**List of `str`** ): **Optional. A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway.**
- **`prize_star_count`** (**`int`** ): **Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only**
- **`premium_subscription_month_count`** (**`int`** ): **Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for**
