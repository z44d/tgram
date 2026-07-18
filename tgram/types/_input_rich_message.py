import tgram
from .type_ import Type_

from typing import List, Optional


class InputRichMessage(Type_):
    """
    This object represents a rich message to be sent.

    Telegram Documentation: https://core.telegram.org/bots/api#inputrichmessage

    :param text: Optional. Text
    :type text: :obj:`str`

    :param parse_mode: Optional. Parse mode
    :type parse_mode: :obj:`str`

    :param entities: Optional. Entities
    :type entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputRichMessage`
    """

    def __init__(
        self,
        text: "str" = None,
        parse_mode: "str" = None,
        entities: List["tgram.types.MessageEntity"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputRichMessage"]:
        return (
            InputRichMessage(
                me=me,
                json=d,
                text=d.get("text"),
                parse_mode=d.get("parse_mode"),
                entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("entities")
                ]
                if d.get("entities")
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
