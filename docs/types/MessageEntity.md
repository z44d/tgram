#🔮 MessageEntity

**This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.**

##⚙️ Properties

- **`type`** (**`MessageEntityType`** ): **Type of the entity. Currently, can be “mention” (@username), “hashtag” (#hashtag), “cashtag” ($USD),
“bot_command” (/start@jobs_bot),“url” (https://telegram.org), “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123),
“bold” (bold text), “italic” (italic text), “underline” (underlined text), “strikethrough” (strikethrough text),
“spoiler” (spoiler message), “blockquote” (block quotation), “expandable_blockquote” (collapsed-by-default block quotation),
“code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs),
“text_mention” (for users without usernames), “custom_emoji” (for inline custom emoji stickers)**
- **`offset`** (**`int`** ): **Offset in UTF-16 code units to the start of the entity**
- **`length`** (**`int`** ): **Length of the entity in UTF-16 code units**
- **`url`** (**`str`** ): **Optional. For “text_link” only, URL that will be opened after user taps on the text**
- **`user`** (**[User](User.md)** ): **Optional. For “text_mention” only, the mentioned user**
- **`language`** (**`str`** ): **Optional. For “pre” only, the programming language of the entity text**
- **`custom_emoji_id`** (**`str`** ): **Optional. For “custom_emoji” only, unique identifier of the custom emoji.
Use get_custom_emoji_stickers to get full information about the sticker.**
