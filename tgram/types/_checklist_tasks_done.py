import tgram

from typing import List, Optional
from .type_ import Type_


class ChecklistTasksDone(Type_):
    """
    Describes a service message about checklist tasks marked as done or not done.

    :param checklist_message: Optional. Message containing the checklist whose tasks were marked as done or not done. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.
    :type checklist_message: :class:`tgram.types.Message`

    :param marked_as_done_task_ids: Optional. Identifiers of the tasks that were marked as done
    :type marked_as_done_task_ids: :obj:`list` of :obj:`int`

    :param marked_as_not_done_task_ids: Optional. Identifiers of the tasks that were marked as not done
    :type marked_as_not_done_task_ids: :obj:`list` of :obj:`int`
    """

    def __init__(
        self,
        checklist_message: "tgram.types.Message" = None,
        marked_as_done_task_ids: List[int] = None,
        marked_as_not_done_task_ids: List[int] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.checklist_message = checklist_message
        self.marked_as_done_task_ids = marked_as_done_task_ids
        self.marked_as_not_done_task_ids = marked_as_not_done_task_ids

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["ChecklistTasksDone"]:
        return (
            ChecklistTasksDone(
                me=me,
                json=d,
                checklist_message=tgram.types.Message._parse(
                    me=me, d=d.get("checklist_message")
                ),
                marked_as_done_task_ids=d.get("marked_as_done_task_ids"),
                marked_as_not_done_task_ids=d.get("marked_as_not_done_task_ids"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
