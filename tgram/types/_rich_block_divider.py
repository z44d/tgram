from typing import Optional

import tgram

from .type_ import Type_


class RichBlockDivider(Type_):
    """
    This object represents a divider rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockdivider

    :param type: Type of the rich block
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockDivider`
    """

    def __init__(
        self,
        type: "str" = "divider",
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichBlockDivider"]:
        return (
            RichBlockDivider(
                me=me,
                json=d,
                type=d.get("type"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
