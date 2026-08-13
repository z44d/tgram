#🔮 Game

**This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.**

##⚙️ Properties

- **`title`** (**`str`** ): **Title of the game**
- **`description`** (**`str`** ): **Description of the game**
- **`photo`** (**List of [PhotoSize](PhotoSize.md)** ): **Photo that will be displayed in the game message in chats.**
- **`text`** (**`str`** ): **Optional. Brief description of the game or high scores included in the game message. Can be
automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited
using editMessageText. 0-4096 characters.**
- **`text_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.**
- **`animation`** (**[Animation](Animation.md)** ): **Optional. Animation that will be displayed in the game message in chats. Upload via BotFather**
