from typing import Optional

import tgram

from .type_ import Type_


class InputMediaLink(Type_):
    """
    Represents a link to be added to a poll option.

    Telegram Documentation: https://core.telegram.org/bots/api#inputmedialink

    :param type: Type of the media
    :type type: :obj:`str`

    :param url: URL
    :type url: :obj:`str`

    :param text: Text
    :type text: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputMediaLink`
    """

    def __init__(
        self,
        type: "str" = "link",
        url: "str | None" = None,
        text: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.url = url
        self.text = text

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputMediaLink"]:
        return (
            InputMediaLink(
                me=me,
                json=d,
                type=d.get("type"),
                url=d.get("url"),
                text=d.get("text"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
