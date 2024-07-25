import tgram
from .type_ import Type_

from typing import List, Optional


class InputPollOption(Type_):
    """
    This object contains information about one answer option in a poll to send.

    Telegram Documentation: https://core.telegram.org/bots/api#inputpolloption

    :param text: Option text, 1-100 characters
    :type text: :obj:`str`

    :param text_parse_mode: Optional. Mode for parsing entities in the text. See formatting options for more details. Currently, only custom emoji entities are allowed
    :type text_parse_mode: :obj:`str`

    :param text_entities: Optional. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of text_parse_mode
    :type text_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollOption`
    """

    def __init__(
        self,
        text: "str" = None,
        text_parse_mode: "str" = None,
        text_entities: List["tgram.types.MessageEntity"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputPollOption"]:
        return (
            InputPollOption(
                me=me,
                json=d,
                text=d.get("text"),
                text_parse_mode=d.get("text_parse_mode"),
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
