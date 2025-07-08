import tgram
import random

from typing import List, Optional


class InputChecklistTask:
    """
    Describes a task to add to a checklist.

    :param id: Unique identifier of the task; must be positive and unique among all task identifiers currently present in the checklist
    :type id: int

    :param text: Text of the task; 1-100 characters after entities parsing
    :type text: str

    :param parse_mode: Optional. Mode for parsing entities in the text. See formatting options for more details.
    :type parse_mode: str

    :param text_entities: Optional. List of special entities that appear in the text, which can be specified instead of parse_mode.
        Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed.
    :type text_entities: List[tgram.types.MessageEntity]
    """

    def __init__(
        self,
        text: str,
        parse_mode: Optional[str] = None,
        text_entities: Optional[List["tgram.types.MessageEntity"]] = None,
    ):
        self.id = random.randint(10000, 99999)
        self.text = text
        self.parse_mode = parse_mode
        self.text_entities = text_entities

    @staticmethod
    def _parse(d: dict = None) -> Optional["InputChecklistTask"]:
        return (
            InputChecklistTask(
                id=d.get("id"),
                text=d.get("text"),
                parse_mode=d.get("parse_mode"),
                text_entities=[
                    tgram.types.MessageEntity._parse(d=i)
                    for i in d.get("text_entities")
                ]
                if d.get("text_entities")
                else None,
            )
            if d
            else None
        )
