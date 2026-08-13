#🔮 OwnedGiftRegular

**Describes a regular gift owned by a user or a chat.**

##⚙️ Properties

- **`gift`** (**[Gift](Gift.md)** ): **Information about the regular gift**
- **`owned_gift_id`** (**`str`** ): **Optional. Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only**
- **`sender_user`** (**[User](User.md)** ): **Optional. Sender of the gift if it is a known user**
- **`send_date`** (**`int`** ): **Date the gift was sent in Unix time**
- **`text`** (**`str`** ): **Optional. Text of the message that was added to the gift**
- **`entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. Special entities that appear in the text**
- **`is_private`** (**`bool`** ): **Optional. True, if the sender and gift text are shown only to the gift receiver**
- **`is_saved`** (**`bool`** ): **Optional. True, if the gift is displayed on the account's profile page**
- **`can_be_upgraded`** (**`bool`** ): **Optional. True, if the gift can be upgraded to a unique gift**
- **`was_refunded`** (**`bool`** ): **Optional. True, if the gift was refunded and isn't available anymore**
- **`convert_star_count`** (**`int`** ): **Optional. Number of Telegram Stars that can be claimed by the receiver instead of the gift**
- **`prepaid_upgrade_star_count`** (**`int`** ): **Optional. Number of Telegram Stars that were paid by the sender for the ability to upgrade the gift**
