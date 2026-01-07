import tgram

from .type_ import Type_
from typing import List, Optional


class GiftInfo(Type_):
    """
    Describes a service message about a regular gift that was sent or received.

    :param gift: Information about the gift
    :type gift: :class:`tgram.types.Gift`
    :param owned_gift_id: Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts
    :type owned_gift_id: :obj:`str`
    :param convert_star_count: Optional. Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible
    :type convert_star_count: :obj:`int`
    :param prepaid_upgrade_star_count: Optional. Number of Telegram Stars that were prepaid by the sender for the ability to upgrade the gift
    :type prepaid_upgrade_star_count: :obj:`int`
    :param can_be_upgraded: Optional. True, if the gift can be upgraded to a unique gift
    :type can_be_upgraded: :obj:`bool`
    :param text: Optional. Text of the message that was added to the gift
    :type text: :obj:`str`
    :param entities: Optional. Special entities that appear in the text
    :type entities: List[:class:`tgram.types.MessageEntity`]
    :param is_private: Optional. True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them
    :type is_private: :obj:`bool`
    :param is_upgrade_separate: Optional. True, if the gift upgrade was separate
    :type is_upgrade_separate: :obj:`bool`
    :param unique_gift_number: Optional. Unique number of the gift variant
    :type unique_gift_number: :obj:`int`
    """

    def __init__(
        self,
        gift: "tgram.types.Gift" = None,
        owned_gift_id: "str" = None,
        convert_star_count: "int" = None,
        prepaid_upgrade_star_count: "int" = None,
        can_be_upgraded: "bool" = None,
        text: "str" = None,
        entities: List["tgram.types.MessageEntity"] = None,
        is_private: "bool" = None,
        is_upgrade_separate: "bool" = None,
        unique_gift_number: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.gift = gift
        self.owned_gift_id = owned_gift_id
        self.convert_star_count = convert_star_count
        self.prepaid_upgrade_star_count = prepaid_upgrade_star_count
        self.can_be_upgraded = can_be_upgraded
        self.text = text
        self.entities = entities
        self.is_private = is_private
        self.is_upgrade_separate = is_upgrade_separate
        self.unique_gift_number = unique_gift_number

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["GiftInfo"]:
        return (
            GiftInfo(
                gift=tgram.types.Gift._parse(me, d.get("gift")),
                owned_gift_id=d.get("owned_gift_id"),
                convert_star_count=d.get("convert_star_count"),
                prepaid_upgrade_star_count=d.get("prepaid_upgrade_star_count"),
                can_be_upgraded=d.get("can_be_upgraded"),
                text=d.get("text"),
                entities=[
                    tgram.types.MessageEntity._parse(me, ent)
                    for ent in d.get("entities", [])
                ]
                if d.get("entities")
                else None,
                is_private=d.get("is_private"),
                is_upgrade_separate=d.get("is_upgrade_separate"),
                unique_gift_number=d.get("unique_gift_number"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
