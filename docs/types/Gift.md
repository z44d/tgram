#🔮 Gift

**This object represents a gift that can be sent by the bot.**

##⚙️ Properties

- **`id`** (**`str`** ): **Unique identifier of the gift.**
- **`sticker`** (**[Sticker](Sticker.md)** ): **The sticker that represents the gift**
- **`star_count`** (**`int`** ): **The number of Telegram Stars that must be paid to send the sticker**
- **`upgrade_star_count`** (**`int`** ): **Optional. The number of Telegram Stars that must be paid to upgrade the gift to a unique one**
- **`total_count`** (**`int`** ): **Optional. The total number of the gifts of this type that can be sent; for limited gifts only**
- **`remaining_count`** (**`int`** ): **Optional. The number of remaining gifts of this type that can be sent; for limited gifts only**
- **`publisher_chat`** (**[Chat](Chat.md)** ): **Optional. Information about the chat that published the gift**
- **`personal_total_count`** (**`int`** ): **Optional. The total number of gifts of this type that can be sent by the current user**
- **`personal_remaining_count`** (**`int`** ): **Optional. The number of remaining gifts of this type that can be sent by the current user**
- **`is_premium`** (**`bool`** ): **Optional. True, if the gift is a premium gift**
- **`has_colors`** (**`bool`** ): **Optional. True, if the gift has colors**
- **`background`** (**[GiftBackground](GiftBackground.md)** ): **Optional. Background of the gift**
- **`unique_gift_variant_count`** (**`int`** ): **Optional. The number of unique gift variants that can be created from this gift**
