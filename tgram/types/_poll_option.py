import tgram
from .type_ import Type_

from typing import List, Optional


class PollOption(Type_):
    """
    This object contains information about one answer option in a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#polloption

    :param text: Option text, 1-100 characters
    :type text: :obj:`str`

    :param voter_count: Number of users that voted for this option
    :type voter_count: :obj:`int`

    :param text_entities: Optional. Special entities that appear in the option text. Currently, only custom emoji entities are allowed in poll option texts
    :type text_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollOption`
    """

    def __init__(
        self,
        text: "str" = None,
        voter_count: "int" = None,
        text_entities: List["tgram.types.MessageEntity"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.text_entities = text_entities
        self.voter_count = voter_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PollOption"]:
        return (
            PollOption(
                me=me,
                json=d,
                text=d.get("text"),
                voter_count=d.get("voter_count"),
                text_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("text_entities")
                ]
                if d.get("text_entities")
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
