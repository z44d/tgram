import tgram
from .type_ import Type_

from typing import Optional


class SwitchInlineQueryChosenChat(Type_):
    """
    Represents an inline button that switches the current user to inline mode in a chosen chat,
    with an optional default inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinekeyboardbutton

    :param query: Optional. The default inline query to be inserted in the input field.
                  If left empty, only the bot's username will be inserted
    :type query: :obj:`str`

    :param allow_user_chats: Optional. True, if private chats with users can be chosen
    :type allow_user_chats: :obj:`bool`

    :param allow_bot_chats: Optional. True, if private chats with bots can be chosen
    :type allow_bot_chats: :obj:`bool`

    :param allow_group_chats: Optional. True, if group and supergroup chats can be chosen
    :type allow_group_chats: :obj:`bool`

    :param allow_channel_chats: Optional. True, if channel chats can be chosen
    :type allow_channel_chats: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`SwitchInlineQueryChosenChat`
    """

    def __init__(
        self,
        query: "str" = None,
        allow_user_chats: "bool" = None,
        allow_bot_chats: "bool" = None,
        allow_group_chats: "bool" = None,
        allow_channel_chats: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SwitchInlineQueryChosenChat"]:
        return (
            SwitchInlineQueryChosenChat(
                me=me,
                json=d,
                query=d.get("query"),
                allow_user_chats=d.get("allow_user_chats"),
                allow_bot_chats=d.get("allow_bot_chats"),
                allow_group_chats=d.get("allow_group_chats"),
                allow_channel_chats=d.get("allow_channel_chats"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
