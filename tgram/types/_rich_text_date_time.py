from typing import Optional

import tgram

from .type_ import Type_


class RichTextDateTime(Type_):
    """
    This object represents a date-time rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtextdatetime

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :param timestamp: Timestamp
    :type timestamp: :obj:`int`

    :param fallback: Fallback text
    :type fallback: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextDateTime`
    """

    def __init__(
        self,
        type: "str" = "date_time",
        text: "str | None" = None,
        timestamp: "int | None" = None,
        fallback: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.timestamp = timestamp
        self.fallback = fallback

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichTextDateTime"]:
        return (
            RichTextDateTime(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                timestamp=d.get("timestamp"),
                fallback=d.get("fallback"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
