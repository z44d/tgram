#🔮 ChecklistTasksAdded

**Describes a service message about tasks added to a checklist.**

##⚙️ Properties

- **`checklist_message`** (**[Message](Message.md)** ): **Optional. Message containing the checklist to which the tasks were added.
Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.**
- **`tasks`** (**List of [ChecklistTask](ChecklistTask.md)** ): **List of tasks added to the checklist**
