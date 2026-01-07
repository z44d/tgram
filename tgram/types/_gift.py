import tgram
from .type_ import Type_

from typing import Optional


class Gift(Type_):
    """
    This object represents a gift that can be sent by the bot.

    Telegram Documentation: https://core.telegram.org/bots/api#gift

    :param id: Unique identifier of the gift.
    :type id: :obj:`str`

    :param sticker: The sticker that represents the gift
    :type sticker: :class:`tgram.types.Sticker`

    :param star_count: The number of Telegram Stars that must be paid to send the sticker
    :type star_count: :obj:`int`

    :param upgrade_star_count: Optional. The number of Telegram Stars that must be paid to upgrade the gift to a unique one
    :type upgrade_star_count: :obj:`int`

    :param total_count: Optional. The total number of the gifts of this type that can be sent; for limited gifts only
    :type total_count: :obj:`int`

    :param remaining_count: Optional. The number of remaining gifts of this type that can be sent; for limited gifts only
    :type remaining_count: :obj:`int`

    :param publisher_chat: Optional. Information about the chat that published the gift
    :type publisher_chat: :class:`tgram.types.Chat`

    :param personal_total_count: Optional. The total number of gifts of this type that can be sent by the current user
    :type personal_total_count: :obj:`int`

    :param personal_remaining_count: Optional. The number of remaining gifts of this type that can be sent by the current user
    :type personal_remaining_count: :obj:`int`

    :param is_premium: Optional. True, if the gift is a premium gift
    :type is_premium: :obj:`bool`

    :param has_colors: Optional. True, if the gift has colors
    :type has_colors: :obj:`bool`

    :param background: Optional. Background of the gift
    :type background: :class:`tgram.types.GiftBackground`

    :param unique_gift_variant_count: Optional. The number of unique gift variants that can be created from this gift
    :type unique_gift_variant_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Gift`
    """

    def __init__(
        self,
        id: "str" = None,
        sticker: "tgram.types.Sticker" = None,
        star_count: "int" = None,
        upgrade_star_count: "int" = None,
        total_count: "int" = None,
        remaining_count: "int" = None,
        publisher_chat: "tgram.types.Chat" = None,
        personal_total_count: "int" = None,
        personal_remaining_count: "int" = None,
        is_premium: "bool" = None,
        has_colors: "bool" = None,
        background: "tgram.types.GiftBackground" = None,
        unique_gift_variant_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.sticker = sticker
        self.star_count = star_count
        self.upgrade_star_count = upgrade_star_count
        self.total_count = total_count
        self.remaining_count = remaining_count
        self.publisher_chat = publisher_chat
        self.personal_total_count = personal_total_count
        self.personal_remaining_count = personal_remaining_count
        self.is_premium = is_premium
        self.has_colors = has_colors
        self.background = background
        self.unique_gift_variant_count = unique_gift_variant_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Gift"]:
        return (
            Gift(
                id=d.get("id"),
                sticker=tgram.types.Sticker._parse(me, d.get("sticker")),
                star_count=d.get("star_count"),
                upgrade_star_count=d.get("upgrade_star_count"),
                total_count=d.get("total_count"),
                remaining_count=d.get("remaining_count"),
                publisher_chat=tgram.types.Chat._parse(me, d.get("publisher_chat"))
                if d.get("publisher_chat")
                else None,
                personal_total_count=d.get("personal_total_count"),
                personal_remaining_count=d.get("personal_remaining_count"),
                is_premium=d.get("is_premium"),
                has_colors=d.get("has_colors"),
                background=tgram.types.GiftBackground._parse(me, d.get("background"))
                if d.get("background")
                else None,
                unique_gift_variant_count=d.get("unique_gift_variant_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
