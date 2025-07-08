import tgram
from .type_ import Type_

from typing import List, Optional
from tgram.utils import String


class ChecklistTask(Type_):
    """
    Describes a task in a checklist.

    :param id: Unique identifier of the task
    :type id: :obj:`int`

    :param text: Text of the task
    :type text: :class:`tgram.utils.String`

    :param text_entities: Optional. Special entities that appear in the task text
    :type text_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param completed_by_user: Optional. User that completed the task; omitted if the task wasn't completed
    :type completed_by_user: :class:`tgram.types.User`

    :param completion_date: Optional. Point in time (Unix timestamp) when the task was completed; 0 if the task wasn't completed
    :type completion_date: :obj:`int`
    """

    def __init__(
        self,
        id: int = None,
        text: "str" = None,
        text_entities: List["tgram.types.MessageEntity"] = None,
        completed_by_user: "tgram.types.User" = None,
        completion_date: int = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.text = String(text).put(text_entities) if text else None
        self.text_entities = text_entities
        self.completed_by_user = completed_by_user
        self.completion_date = completion_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChecklistTask"]:
        return (
            ChecklistTask(
                me=me,
                json=d,
                id=d.get("id"),
                text=d.get("text"),
                text_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("text_entities")
                ]
                if d.get("text_entities")
                else None,
                completed_by_user=tgram.types.User._parse(
                    me=me, d=d.get("completed_by_user")
                ),
                completion_date=d.get("completion_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
