from typing import Optional

import tgram

from .type_ import Type_


class RichBlockAnchor(Type_):
    """
    This object represents an anchor rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockanchor

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param name: Anchor name
    :type name: :obj:`str`

    :param fallback: Optional. Fallback text
    :type fallback: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockAnchor`
    """

    def __init__(
        self,
        type: "str" = "anchor",
        name: "str | None" = None,
        fallback: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.name = name
        self.fallback = fallback

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichBlockAnchor"]:
        return (
            RichBlockAnchor(
                me=me,
                json=d,
                type=d.get("type"),
                name=d.get("name"),
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
