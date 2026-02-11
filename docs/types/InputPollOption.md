#🔮 InputPollOption

**This object contains information about one answer option in a poll to send.**

##⚙️ Properties

- **`text`** (**`str`** ): **Option text, 1-100 characters**
- **`text_parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the text. See formatting options for more details. Currently, only custom emoji entities are allowed**
- **`text_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of text_parse_mode**
