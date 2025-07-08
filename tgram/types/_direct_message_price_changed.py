import tgram
from .type_ import Type_
from typing import Optional


class DirectMessagePriceChanged(Type_):
    """
    Describes a service message about a change in the price of direct messages sent to a channel chat.

    :param are_direct_messages_enabled: True, if direct messages are enabled for the channel chat; false otherwise
    :type are_direct_messages_enabled: :obj:`bool`

    :param direct_message_star_count: Optional. The new number of Telegram Stars that must be paid by users for each direct message sent to the channel. Does not apply to users who have been exempted by administrators. Defaults to 0.
    :type direct_message_star_count: :obj:`int`
    """

    def __init__(
        self,
        are_direct_messages_enabled: bool,
        direct_message_star_count: Optional[int] = 0,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.are_direct_messages_enabled = are_direct_messages_enabled
        self.direct_message_star_count = direct_message_star_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.DirectMessagePriceChanged"]:
        return (
            DirectMessagePriceChanged(
                me=me,
                json=d,
                are_direct_messages_enabled=d.get("are_direct_messages_enabled"),
                direct_message_star_count=d.get("direct_message_star_count", 0),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
