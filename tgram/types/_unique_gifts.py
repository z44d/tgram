import tgram
from .type_ import Type_
from typing import Optional


class UniqueGiftModel(Type_):
    """
    This object describes the model of a unique gift.

    Telegram Documentation: https://core.telegram.org/bots/api#uniquegiftmodel

    :param name: Name of the model
    :type name: :obj:`str`
    :param sticker: The sticker that represents the unique gift
    :type sticker: :class:`tgram.types.Sticker`
    :param rarity_per_mille: The number of unique gifts that receive this model for every 1000 gifts upgraded
    :type rarity_per_mille: :obj:`int`
    """

    def __init__(
        self,
        name: "str" = None,
        sticker: "tgram.types.Sticker" = None,
        rarity_per_mille: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.sticker = sticker
        self.rarity_per_mille = rarity_per_mille

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["UniqueGiftModel"]:
        return (
            UniqueGiftModel(
                name=d.get("name"),
                sticker=tgram.types.Sticker._parse(me, d.get("sticker")),
                rarity_per_mille=d.get("rarity_per_mille"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class UniqueGiftSymbol(Type_):
    """
    This object describes the symbol shown on the pattern of a unique gift.

    :param name: Name of the symbol
    :type name: :obj:`str`
    :param sticker: The sticker that represents the unique gift
    :type sticker: :class:`tgram.types.Sticker`
    :param rarity_per_mille: The number of unique gifts that receive this model for every 1000 gifts upgraded
    :type rarity_per_mille: :obj:`int`
    """

    def __init__(
        self,
        name: "str" = None,
        sticker: "tgram.types.Sticker" = None,
        rarity_per_mille: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.sticker = sticker
        self.rarity_per_mille = rarity_per_mille

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["UniqueGiftSymbol"]:
        return (
            UniqueGiftSymbol(
                name=d.get("name"),
                sticker=tgram.types.Sticker._parse(me, d.get("sticker")),
                rarity_per_mille=d.get("rarity_per_mille"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class UniqueGiftBackdropColors(Type_):
    """
    This object describes the colors of the backdrop of a unique gift.

    :param center_color: The color in the center of the backdrop in RGB format
    :type center_color: :obj:`int`
    :param edge_color: The color on the edges of the backdrop in RGB format
    :type edge_color: :obj:`int`
    :param symbol_color: The color to be applied to the symbol in RGB format
    :type symbol_color: :obj:`int`
    :param text_color: The color for the text on the backdrop in RGB format
    :type text_color: :obj:`int`
    """

    def __init__(
        self,
        center_color: "int" = None,
        edge_color: "int" = None,
        symbol_color: "int" = None,
        text_color: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.center_color = center_color
        self.edge_color = edge_color
        self.symbol_color = symbol_color
        self.text_color = text_color

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["UniqueGiftBackdropColors"]:
        return (
            UniqueGiftBackdropColors(
                center_color=d.get("center_color"),
                edge_color=d.get("edge_color"),
                symbol_color=d.get("symbol_color"),
                text_color=d.get("text_color"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class UniqueGiftBackdrop(Type_):
    """
    This object describes the backdrop of a unique gift.

    :param name: Name of the backdrop
    :type name: :obj:`str`
    :param colors: Colors of the backdrop
    :type colors: :class:`tgram.types.UniqueGiftBackdropColors`
    :param rarity_per_mille: The number of unique gifts that receive this backdrop for every 1000 gifts upgraded
    :type rarity_per_mille: :obj:`int`
    """

    def __init__(
        self,
        name: "str" = None,
        colors: "UniqueGiftBackdropColors" = None,
        rarity_per_mille: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.colors = colors
        self.rarity_per_mille = rarity_per_mille

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["UniqueGiftBackdrop"]:
        return (
            UniqueGiftBackdrop(
                name=d.get("name"),
                colors=UniqueGiftBackdropColors._parse(me, d.get("colors")),
                rarity_per_mille=d.get("rarity_per_mille"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class UniqueGift(Type_):
    """
    This object describes a unique gift that was upgraded from a regular gift.

    :param base_name: Human-readable name of the regular gift from which this unique gift was upgraded
    :type base_name: :obj:`str`
    :param name: Unique name of the gift. This name can be used in https://t.me/nft/... links and story areas
    :type name: :obj:`str`
    :param number: Unique number of the upgraded gift among gifts upgraded from the same regular gift
    :type number: :obj:`int`
    :param model: Model of the gift
    :type model: :class:`tgram.types.UniqueGiftModel`
    :param symbol: Symbol of the gift
    :type symbol: :class:`tgram.types.UniqueGiftSymbol`
    :param backdrop: Backdrop of the gift
    :type backdrop: :class:`tgram.types.UniqueGiftBackdrop`
    """

    def __init__(
        self,
        base_name: "str" = None,
        name: "str" = None,
        number: "int" = None,
        model: "UniqueGiftModel" = None,
        symbol: "UniqueGiftSymbol" = None,
        backdrop: "UniqueGiftBackdrop" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.base_name = base_name
        self.name = name
        self.number = number
        self.model = model
        self.symbol = symbol
        self.backdrop = backdrop

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["UniqueGift"]:
        return (
            UniqueGift(
                base_name=d.get("base_name"),
                name=d.get("name"),
                number=d.get("number"),
                model=UniqueGiftModel._parse(me, d.get("model")),
                symbol=UniqueGiftSymbol._parse(me, d.get("symbol")),
                backdrop=UniqueGiftBackdrop._parse(me, d.get("backdrop")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class UniqueGiftInfo(Type_):
    """
    Describes a service message about a unique gift that was sent or received.

    :param gift: Information about the gift
    :type gift: :class:`tgram.types.UniqueGift`
    :param origin: Origin of the gift. Currently, either “upgrade” for gifts upgraded from regular gifts, “transfer” for gifts transferred from other users or channels, or “resale” for gifts bought from other users
    :type origin: :obj:`str`
    :param owned_gift_id: Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts
    :type owned_gift_id: :obj:`str`
    :param transfer_star_count: Optional. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift
    :type transfer_star_count: :obj:`int`
    """

    def __init__(
        self,
        gift: "UniqueGift" = None,
        origin: "str" = None,
        owned_gift_id: "str" = None,
        transfer_star_count: "int" = None,
        next_transfer_date: int = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.gift = gift
        self.origin = origin
        self.owned_gift_id = owned_gift_id
        self.transfer_star_count = transfer_star_count
        self.next_transfer_date = next_transfer_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["UniqueGiftInfo"]:
        return (
            UniqueGiftInfo(
                gift=UniqueGift._parse(me, d.get("gift")),
                origin=d.get("origin"),
                owned_gift_id=d.get("owned_gift_id"),
                transfer_star_count=d.get("transfer_star_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
