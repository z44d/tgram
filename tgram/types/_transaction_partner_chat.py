import tgram
from .type_ import Type_

from typing import Optional


class TransactionPartnerChat(Type_):
    """
    Describes a transaction with a chat.

    Telegram documentation: https://core.telegram.org/bots/api#transactionpartnerchat

    :param type: Type of the transaction partner, always “chat”
    :type type: :obj:`str`

    :param chat: Information about the chat
    :type user: :class:`Chat`

    :param gift: Optional. The gift sent to the chat by the bot
    :type gift: :class:`Gift`

    :return: Instance of the class
    :rtype: :class:`TransactionPartnerChat`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        gift: "tgram.types.Gift" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "chat"
        self.chat = chat
        self.gift = gift

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.TransactionPartnerChat"]:
        return (
            TransactionPartnerChat(
                me=me,
                json=d,
                type=d.get("type"),
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                gift=tgram.types.Gift._parse(me=me, d=d.get("gift"))
                if d.get("gift")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
