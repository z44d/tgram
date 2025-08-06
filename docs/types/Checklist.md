# Checklist

**Describes a checklist.**

## Properties

- **`title`** (**`String`**): **Title of the checklist**
- **`title_entities`** (**List of `tgram.types.MessageEntity`**): **Optional. Special entities that appear in the checklist title**
- **`tasks`** (**List of `tgram.types.ChecklistTask`**): **List of tasks in the checklist**
- **`others_can_add_tasks`** (**`bool`**): **Optional. True, if users other than the creator of the list can add tasks to the list**
- **`others_can_mark_tasks_as_done`** (**`bool`**): **Optional. True, if users other than the creator of the list can mark tasks as done or not done**
