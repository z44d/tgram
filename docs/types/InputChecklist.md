#🔮 InputChecklist

**Describes a checklist to create.**

##⚙️ Properties

- **`title`** (**`str`** ): **Title of the checklist; 1-255 characters after entities parsing**
- **`tasks`** (**List of [InputChecklistTask](InputChecklistTask.md)** ): **List of 1-30 tasks in the checklist**
- **`parse_mode`** (**`str`** ): **Optional. Mode for parsing entities in the title. See formatting options for more details.**
- **`title_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. List of special entities that appear in the title, which can be specified instead of parse_mode.
Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed.**
- **`others_can_add_tasks`** (**`bool`** ): **Optional. Pass True if other users can add tasks to the checklist**
- **`others_can_mark_tasks_as_done`** (**`bool`** ): **Optional. Pass True if other users can mark tasks as done or not done in the checklist**
