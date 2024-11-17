import tgram
from .type_ import Type_

from typing import List, Optional


class Gifts(Type_):
    """
    This object represent a list of gifts.

    Telegram Documentation: https://core.telegram.org/bots/api#gifts

    :param gifts: Photo that will be displayed in the game message in chats.
    :type gifts: :obj:`list` of :class:`tgram.types.Gift`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Gifts`
    """

    def __init__(
        self,
        gifts: List["tgram.types.Gift"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.gifts = gifts

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Gifts"]:
        return (
            Gifts(gifts=[tgram.types.Gift._parse(me, i) for i in d.get("gifts")])
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
