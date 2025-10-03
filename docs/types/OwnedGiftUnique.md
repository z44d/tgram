#🔮 OwnedGiftUnique

**Describes a unique gift received and owned by a user or a chat.**

##⚙️ Properties

- **`gift`** (**[UniqueGift](UniqueGift.md)** ): **Information about the unique gift**
- **`owned_gift_id`** (**`str`** ): **Optional. Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only**
- **`sender_user`** (**[User](User.md)** ): **Optional. Sender of the gift if it is a known user**
- **`send_date`** (**`int`** ): **Date the gift was sent in Unix time**
- **`is_saved`** (**`bool`** ): **Optional. True, if the gift is displayed on the account's profile page**
- **`can_be_transferred`** (**`bool`** ): **Optional. True, if the gift can be transferred to another owner**
- **`transfer_star_count`** (**`int`** ): **Optional. Number of Telegram Stars that must be paid to transfer the gift**
- **`next_transfer_date`** (**`int`** )
