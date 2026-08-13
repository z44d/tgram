#🔮 GiftInfo

**Describes a service message about a regular gift that was sent or received.**

##⚙️ Properties

- **`gift`** (**[Gift](Gift.md)** ): **Information about the gift**
- **`owned_gift_id`** (**`str`** ): **Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts**
- **`convert_star_count`** (**`int`** ): **Optional. Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible**
- **`prepaid_upgrade_star_count`** (**`int`** ): **Optional. Number of Telegram Stars that were prepaid by the sender for the ability to upgrade the gift**
- **`can_be_upgraded`** (**`bool`** ): **Optional. True, if the gift can be upgraded to a unique gift**
- **`text`** (**`str`** ): **Optional. Text of the message that was added to the gift**
- **`entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. Special entities that appear in the text**
- **`is_private`** (**`bool`** ): **Optional. True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them**
- **`is_upgrade_separate`** (**`bool`** ): **Optional. True, if the gift upgrade was separate**
- **`unique_gift_number`** (**`int`** ): **Optional. Unique number of the gift variant**
