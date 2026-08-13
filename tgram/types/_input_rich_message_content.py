from typing import Optional

import tgram

from .type_ import Type_


class InputRichMessageContent(Type_):
    """
    This object represents a rich message content for inline queries.

    Telegram Documentation: https://core.telegram.org/bots/api#inputrichmessagecontent

    :param text: Optional. Text
    :type text: :obj:`str`

    :param parse_mode: Optional. Parse mode
    :type parse_mode: :obj:`str`

    :param entities: Optional. Entities
    :type entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputRichMessageContent`
    """

    def __init__(
        self,
        text: "str | None" = None,
        parse_mode: "str | None" = None,
        entities: list["tgram.types.MessageEntity"] | None = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputRichMessageContent"]:
        return (
            InputRichMessageContent(
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
