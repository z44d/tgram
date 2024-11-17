import tgram
from .type_ import Type_

from typing import Optional


class Gift(Type_):
    """
    This object represents a gift that can be sent by the bot.

    Telegram Documentation: https://core.telegram.org/bots/api#gift

    :param id: Unique identifier of the gift.
    :type id: :obj:`int`

    :param sticker: The sticker that represents the gift
    :type sticker: :class:`tgram.types.Sticker`

    :param star_count: The number of Telegram Stars that must be paid to send the sticker
    :type star_count: :obj:`int`

    :param total_count: Optional. The total number of the gifts of this type that can be sent; for limited gifts only
    :type total_count: :obj:`int`

    :param remaining_count: Optional. The number of remaining gifts of this type that can be sent; for limited gifts only
    :type remaining_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Gift`
    """

    def __init__(
        self,
        id: "str" = None,
        sticker: "tgram.types.Sticker" = None,
        star_count: "int" = None,
        total_count: "int" = None,
        remaining_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.sticker = sticker
        self.star_count = star_count
        self.total_count = total_count
        self.remaining_count = remaining_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Gift"]:
        return (
            Gift(
                id=d.get("id"),
                sticker=tgram.types.Sticker._parse(me, d.get("sticker")),
                star_count=d.get("star_count"),
                total_count=d.get("total_count"),
                remaining_count=d.get("remaining_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
