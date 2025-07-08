import tgram
from .type_ import Type_
from typing import List, Optional
from tgram.utils import String


class Checklist(Type_):
    """
    Describes a checklist.

    :param title: Title of the checklist
    :type title: :class:`tgram.utils.String`

    :param title_entities: Optional. Special entities that appear in the checklist title
    :type title_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param tasks: List of tasks in the checklist
    :type tasks: :obj:`list` of :class:`tgram.types.ChecklistTask`

    :param others_can_add_tasks: Optional. True, if users other than the creator of the list can add tasks to the list
    :type others_can_add_tasks: :obj:`bool`

    :param others_can_mark_tasks_as_done: Optional. True, if users other than the creator of the list can mark tasks as done or not done
    :type others_can_mark_tasks_as_done: :obj:`bool`
    """

    def __init__(
        self,
        title: "String" = None,
        title_entities: List["tgram.types.MessageEntity"] = None,
        tasks: List["tgram.types.ChecklistTask"] = None,
        others_can_add_tasks: bool = None,
        others_can_mark_tasks_as_done: bool = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = String(title).put(title_entities) if title else None
        self.title_entities = title_entities
        self.tasks = tasks
        self.others_can_add_tasks = others_can_add_tasks
        self.others_can_mark_tasks_as_done = others_can_mark_tasks_as_done

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Checklist"]:
        return (
            Checklist(
                me=me,
                json=d,
                title=d.get("title"),
                title_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("title_entities")
                ]
                if d.get("title_entities")
                else None,
                tasks=[
                    tgram.types.ChecklistTask._parse(me=me, d=i) for i in d.get("tasks")
                ]
                if d.get("tasks")
                else None,
                others_can_add_tasks=d.get("others_can_add_tasks"),
                others_can_mark_tasks_as_done=d.get("others_can_mark_tasks_as_done"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
