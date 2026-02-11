#🔮 UniqueGift

**This object describes a unique gift that was upgraded from a regular gift.**

##⚙️ Properties

- **`base_name`** (**`str`** ): **Human-readable name of the regular gift from which this unique gift was upgraded**
- **`name`** (**`str`** ): **Unique name of the gift. This name can be used in https://t.me/nft/... links and story areas**
- **`number`** (**`int`** ): **Unique number of the upgraded gift among gifts upgraded from the same regular gift**
- **`model`** (**[UniqueGiftModel](UniqueGiftModel.md)** ): **Model of the gift**
- **`symbol`** (**[UniqueGiftSymbol](UniqueGiftSymbol.md)** ): **Symbol of the gift**
- **`backdrop`** (**[UniqueGiftBackdrop](UniqueGiftBackdrop.md)** ): **Backdrop of the gift**
- **`publisher_chat`** (**[Chat](Chat.md)** ): **Optional. Information about the chat that published the gift**
- **`gift_id`** (**`str`** ): **Optional. Unique identifier of the gift**
- **`is_from_blockchain`** (**`bool`** ): **Optional. True, if the gift was assigned from the TON blockchain**
- **`is_premium`** (**`bool`** ): **Optional. True, if the gift is a premium gift**
- **`is_burned`** (**`bool`** ): **Optional. True, if the gift was used to craft another gift and isn't available anymore**
- **`colors`** (**[UniqueGiftColors](UniqueGiftColors.md)** ): **Optional. The colors of the unique gift**
