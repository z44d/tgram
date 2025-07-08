import tgram
from .type_ import Type_

from typing import List, Optional


class InputChecklist(Type_):
    """
    Describes a checklist to create.

    Telegram Documentation: https://core.telegram.org/bots/api#inputchecklist

    :param title: Title of the checklist; 1-255 characters after entities parsing
    :type title: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the title. See formatting options for more details.
    :type parse_mode: :obj:`str`

    :param title_entities: Optional. List of special entities that appear in the title, which can be specified instead of parse_mode.
        Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed.
    :type title_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param tasks: List of 1-30 tasks in the checklist
    :type tasks: :obj:`list` of :class:`tgram.types.InputChecklistTask`

    :param others_can_add_tasks: Optional. Pass True if other users can add tasks to the checklist
    :type others_can_add_tasks: :obj:`bool`

    :param others_can_mark_tasks_as_done: Optional. Pass True if other users can mark tasks as done or not done in the checklist
    :type others_can_mark_tasks_as_done: :obj:`bool`
    """

    def __init__(
        self,
        title: str,
        tasks: List["tgram.types.InputChecklistTask"],
        parse_mode: "str" = None,
        title_entities: List["tgram.types.MessageEntity"] = None,
        others_can_add_tasks: "bool" = None,
        others_can_mark_tasks_as_done: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.parse_mode = parse_mode
        self.title_entities = title_entities
        self.tasks = tasks
        self.others_can_add_tasks = others_can_add_tasks
        self.others_can_mark_tasks_as_done = others_can_mark_tasks_as_done

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputChecklist"]:
        return (
            InputChecklist(
                me=me,
                json=d,
                title=d.get("title"),
                parse_mode=d.get("parse_mode"),
                title_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("title_entities")
                ]
                if d.get("title_entities")
                else None,
                tasks=[
                    tgram.types.InputChecklistTask._parse(me=me, d=i)
                    for i in d.get("tasks")
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
