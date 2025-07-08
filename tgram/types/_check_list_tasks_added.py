import tgram
from .type_ import Type_

from typing import List, Optional


class ChecklistTasksAdded(Type_):
    """
    Describes a service message about tasks added to a checklist.

    :param checklist_message: Optional. Message containing the checklist to which the tasks were added.
        Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.
    :type checklist_message: :class:`tgram.types.Message`

    :param tasks: List of tasks added to the checklist
    :type tasks: :obj:`list` of :class:`tgram.types.ChecklistTask`
    """

    def __init__(
        self,
        checklist_message: "tgram.types.Message" = None,
        tasks: List["tgram.types.ChecklistTask"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.checklist_message = checklist_message
        self.tasks = tasks

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChecklistTasksAdded"]:
        return (
            ChecklistTasksAdded(
                me=me,
                json=d,
                checklist_message=tgram.types.Message._parse(
                    me=me, d=d.get("checklist_message")
                ),
                tasks=[
                    tgram.types.ChecklistTask._parse(me=me, d=i) for i in d.get("tasks")
                ]
                if d.get("tasks")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
