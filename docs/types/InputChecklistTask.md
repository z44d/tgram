#🔮 InputChecklistTask

**Describes a task to add to a checklist.**

##⚙️ Properties

- **`text`** (**`str`** ): **Text of the task; 1-100 characters after entities parsing**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the text. See formatting options for more details.**
- **`text_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the text, which can be specified instead of parse_mode.
Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed.**
