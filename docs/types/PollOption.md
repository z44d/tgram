#🔮 PollOption

**This object contains information about one answer option in a poll.**

##⚙️ Properties

- **`text`** (**`String`** ): **Option text, 1-100 characters**
- **`voter_count`** (**`int`** ): **Number of users that voted for this option**
- **`text_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. Special entities that appear in the option text. Currently, only custom emoji entities are allowed in poll option texts**
- **`persistent_id`** (**`str`** ): **Optional. Persistent identifier of the poll option.**
- **`added_by_user`** (**[User](User.md)** ): **Optional. The user that added the poll option.**
- **`added_by_chat`** (**[Chat](Chat.md)** ): **Optional. The chat that added the poll option.**
- **`addition_date`** (**`int`** ): **Optional. Point in time (Unix timestamp) when the poll option was added.**
- **`media`** (**List of [PollMedia](PollMedia.md)** ): **Optional. Media in the poll option**
