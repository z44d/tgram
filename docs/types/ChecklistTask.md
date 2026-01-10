#🔮 ChecklistTask

**Describes a task in a checklist.**

##⚙️ Properties

- **`id`** (**`int`** ): **Unique identifier of the task**
- **`text`** (**`str`** ): **Text of the task**
- **`text_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. Special entities that appear in the task text**
- **`completed_by_user`** (**[User](User.md)** ): **Optional. User that completed the task; omitted if the task wasn't completed**
- **`completion_date`** (**`int`** ): **Optional. Point in time (Unix timestamp) when the task was completed; 0 if the task wasn't completed**
- **`completed_by_chat`** (**[Chat](Chat.md)** ): **Optional. Chat that completed the task; omitted if the task wasn't completed**
