#🔮 ExternalReplyInfo

**This object contains information about a message that is being replied to,**

##⚙️ Properties

- **`origin`** (**`MessageOrigin`** ): **Origin of the message replied to by the given message**
- **`chat`** (**[Chat](Chat.md)** ): **Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel.**
- **`message_id`** (**`int`** ): **Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.**
- **`link_preview_options`** (**[LinkPreviewOptions](LinkPreviewOptions.md)** ): **Optional. Options used for link preview generation for the original message, if it is a text message**
- **`animation`** (**[Animation](Animation.md)** ): **Optional. Message is an animation, information about the animation**
- **`audio`** (**[Audio](Audio.md)** ): **Optional. Message is an audio file, information about the file**
- **`document`** (**[Document](Document.md)** ): **Optional. Message is a general file, information about the file**
- **`paid_media`** (**[PaidMediaInfo](PaidMediaInfo.md)** )
- **`photo`** (**List of [PhotoSize](PhotoSize.md)** ): **Optional. Message is a photo, available sizes of the photo**
- **`sticker`** (**[Sticker](Sticker.md)** ): **Optional. Message is a sticker, information about the sticker**
- **`story`** (**[Story](Story.md)** ): **Optional. Message is a forwarded story**
- **`video`** (**[Video](Video.md)** ): **Optional. Message is a video, information about the video**
- **`video_note`** (**[VideoNote](VideoNote.md)** ): **Optional. Message is a video note, information about the video message**
- **`voice`** (**[Voice](Voice.md)** ): **Optional. Message is a voice message, information about the file**
- **`has_media_spoiler`** (**`bool`** ): **Optional. True, if the message media is covered by a spoiler animation**
- **`checklist`** (**[Checklist](Checklist.md)** ): **Optional. Message is a checklist**
- **`contact`** (**[Contact](Contact.md)** ): **Optional. Message is a shared contact, information about the contact**
- **`dice`** (**[Dice](Dice.md)** ): **Optional. Message is a dice with random value**
- **`game`** (**[Game](Game.md)** ): **Optional. Message is a game, information about the game. More about games »**
- **`giveaway`** (**[Giveaway](Giveaway.md)** ): **Optional. Message is a scheduled giveaway, information about the giveaway**
- **`giveaway_winners`** (**[GiveawayWinners](GiveawayWinners.md)** ): **Optional. A giveaway with public winners was completed**
- **`invoice`** (**[Invoice](Invoice.md)** ): **Optional. Message is an invoice for a payment, information about the invoice. More about payments »**
- **`location`** (**[Location](Location.md)** ): **Optional. Message is a shared location, information about the location**
- **`poll`** (**[Poll](Poll.md)** ): **Optional. Message is a native poll, information about the poll**
- **`venue`** (**[Venue](Venue.md)** ): **Optional. Message is a venue, information about the venue**
