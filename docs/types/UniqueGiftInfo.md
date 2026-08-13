#🔮 UniqueGiftInfo

**Describes a service message about a unique gift that was sent or received.**

##⚙️ Properties

- **`gift`** (**[UniqueGift](UniqueGift.md)** ): **Information about the gift**
- **`origin`** (**`str`** ): **Origin of the gift. Currently, either “upgrade” for gifts upgraded from regular gifts, “transfer” for gifts transferred from other users or channels, or “resale” for gifts bought from other users**
- **`last_resale_currency`** (**`str`** )
- **`last_resale_amount`** (**`int`** )
- **`owned_gift_id`** (**`str`** ): **Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts**
- **`transfer_star_count`** (**`int`** ): **Optional. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift**
- **`next_transfer_date`** (**`int`** )
