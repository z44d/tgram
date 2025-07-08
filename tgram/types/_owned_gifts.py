import tgram
from .type_ import Type_
from typing import List, Optional, Union


class OwnedGiftRegular(Type_):
    """
    Describes a regular gift owned by a user or a chat.

    :param type: Type of the gift, always "regular"
    :type type: :obj:`str`
    :param gift: Information about the regular gift
    :type gift: :class:`tgram.types.Gift`
    :param owned_gift_id: Optional. Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only
    :type owned_gift_id: :obj:`str`
    :param sender_user: Optional. Sender of the gift if it is a known user
    :type sender_user: :class:`tgram.types.User`
    :param send_date: Date the gift was sent in Unix time
    :type send_date: :obj:`int`
    :param text: Optional. Text of the message that was added to the gift
    :type text: :obj:`str`
    :param entities: Optional. Special entities that appear in the text
    :type entities: List[:class:`tgram.types.MessageEntity`]
    :param is_private: Optional. True, if the sender and gift text are shown only to the gift receiver
    :type is_private: :obj:`bool`
    :param is_saved: Optional. True, if the gift is displayed on the account's profile page
    :type is_saved: :obj:`bool`
    :param can_be_upgraded: Optional. True, if the gift can be upgraded to a unique gift
    :type can_be_upgraded: :obj:`bool`
    :param was_refunded: Optional. True, if the gift was refunded and isn't available anymore
    :type was_refunded: :obj:`bool`
    :param convert_star_count: Optional. Number of Telegram Stars that can be claimed by the receiver instead of the gift
    :type convert_star_count: :obj:`int`
    :param prepaid_upgrade_star_count: Optional. Number of Telegram Stars that were paid by the sender for the ability to upgrade the gift
    :type prepaid_upgrade_star_count: :obj:`int`
    """

    def __init__(
        self,
        gift: "tgram.types.Gift" = None,
        owned_gift_id: str = None,
        sender_user: "tgram.types.User" = None,
        send_date: int = None,
        text: str = None,
        entities: List["tgram.types.MessageEntity"] = None,
        is_private: bool = None,
        is_saved: bool = None,
        can_be_upgraded: bool = None,
        was_refunded: bool = None,
        convert_star_count: int = None,
        prepaid_upgrade_star_count: int = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "regular"
        self.gift = gift
        self.owned_gift_id = owned_gift_id
        self.sender_user = sender_user
        self.send_date = send_date
        self.text = text
        self.entities = entities
        self.is_private = is_private
        self.is_saved = is_saved
        self.can_be_upgraded = can_be_upgraded
        self.was_refunded = was_refunded
        self.convert_star_count = convert_star_count
        self.prepaid_upgrade_star_count = prepaid_upgrade_star_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["OwnedGiftRegular"]:
        return (
            OwnedGiftRegular(
                gift=tgram.types.Gift._parse(me, d.get("gift")),
                owned_gift_id=d.get("owned_gift_id"),
                sender_user=tgram.types.User._parse(me, d.get("sender_user")),
                send_date=d.get("send_date"),
                text=d.get("text"),
                entities=[
                    tgram.types.MessageEntity._parse(me, ent)
                    for ent in d.get("entities")
                ]
                if d.get("entities")
                else None,
                is_private=d.get("is_private"),
                is_saved=d.get("is_saved"),
                can_be_upgraded=d.get("can_be_upgraded"),
                was_refunded=d.get("was_refunded"),
                convert_star_count=d.get("convert_star_count"),
                prepaid_upgrade_star_count=d.get("prepaid_upgrade_star_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class OwnedGiftUnique(Type_):
    """
    Describes a unique gift received and owned by a user or a chat.

    :param type: Type of the gift, always "unique"
    :type type: :obj:`str`
    :param gift: Information about the unique gift
    :type gift: :class:`tgram.types.UniqueGift`
    :param owned_gift_id: Optional. Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only
    :type owned_gift_id: :obj:`str`
    :param sender_user: Optional. Sender of the gift if it is a known user
    :type sender_user: :class:`tgram.types.User`
    :param send_date: Date the gift was sent in Unix time
    :type send_date: :obj:`int`
    :param is_saved: Optional. True, if the gift is displayed on the account's profile page
    :type is_saved: :obj:`bool`
    :param can_be_transferred: Optional. True, if the gift can be transferred to another owner
    :type can_be_transferred: :obj:`bool`
    :param transfer_star_count: Optional. Number of Telegram Stars that must be paid to transfer the gift
    :type transfer_star_count: :obj:`int`
    """

    def __init__(
        self,
        gift: "tgram.types.UniqueGift" = None,
        owned_gift_id: str = None,
        sender_user: "tgram.types.User" = None,
        send_date: int = None,
        is_saved: bool = None,
        can_be_transferred: bool = None,
        transfer_star_count: int = None,
        next_transfer_date: int = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "unique"
        self.gift = gift
        self.owned_gift_id = owned_gift_id
        self.sender_user = sender_user
        self.send_date = send_date
        self.is_saved = is_saved
        self.can_be_transferred = can_be_transferred
        self.transfer_star_count = transfer_star_count
        self.next_transfer_date = next_transfer_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["OwnedGiftUnique"]:
        return (
            OwnedGiftUnique(
                gift=tgram.types.UniqueGift._parse(me, d.get("gift")),
                owned_gift_id=d.get("owned_gift_id"),
                sender_user=tgram.types.User._parse(me, d.get("sender_user")),
                send_date=d.get("send_date"),
                is_saved=d.get("is_saved"),
                can_be_transferred=d.get("can_be_transferred"),
                transfer_star_count=d.get("transfer_star_count"),
                next_transfer_date=d.get("next_transfer_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class OwnedGifts(Type_):
    """
    Contains the list of gifts received and owned by a user or a chat.

    :param total_count: The total number of gifts owned by the user or the chat
    :type total_count: :obj:`int`
    :param gifts: The list of gifts
    :type gifts: List[Union[:class:`OwnedGiftRegular`, :class:`OwnedGiftUnique`]]
    :param next_offset: Optional. Offset for the next request. If empty, then there are no more results
    :type next_offset: :obj:`str`
    """

    def __init__(
        self,
        total_count: int = None,
        gifts: List[Union["OwnedGiftRegular", "OwnedGiftUnique"]] = None,
        next_offset: str = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.total_count = total_count
        self.gifts = gifts
        self.next_offset = next_offset

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["OwnedGifts"]:
        return (
            OwnedGifts(
                total_count=d.get("total_count"),
                gifts=[
                    (
                        OwnedGiftRegular._parse(me, g)
                        if g.get("type") == "regular"
                        else OwnedGiftUnique._parse(me, g)
                    )
                    for g in d.get("gifts")
                ],
                next_offset=d.get("next_offset"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
