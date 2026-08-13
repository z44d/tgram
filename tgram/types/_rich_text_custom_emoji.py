from typing import Optional

import tgram

from .type_ import Type_


class RichTextCustomEmoji(Type_):
    """
    This object represents a custom emoji rich text.

    Telegram Documentation: https://core.telegram.org/bots/api#richtextcustomemoji

    :param type: Type of the rich text
    :type type: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :param custom_emoji_id: Custom emoji ID
    :type custom_emoji_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichTextCustomEmoji`
    """

    def __init__(
        self,
        type: "str" = "custom_emoji",
        text: "str | None" = None,
        custom_emoji_id: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichTextCustomEmoji"]:
        return (
            RichTextCustomEmoji(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                custom_emoji_id=d.get("custom_emoji_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
