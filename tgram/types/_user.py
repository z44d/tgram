import tgram
from .type_ import Type_

from typing import Optional
from tgram import bound


class User(Type_, bound.UserB):
    """
    This object represents a Telegram user or bot.

    Telegram Documentation: https://core.telegram.org/bots/api#user

    :param id: Unique identifier for this user or bot. This number may have more than 32 significant bits and some
        programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant
        bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type id: :obj:`int`

    :param is_bot: True, if this user is a bot
    :type is_bot: :obj:`bool`

    :param first_name: User's or bot's first name
    :type first_name: :obj:`str`

    :param last_name: Optional. User's or bot's last name
    :type last_name: :obj:`str`

    :param username: Optional. User's or bot's username
    :type username: :obj:`str`

    :param language_code: Optional. IETF language tag of the user's language
    :type language_code: :obj:`str`

    :param is_premium: Optional. :obj:`bool`, if this user is a Telegram Premium user
    :type is_premium: :obj:`bool`

    :param added_to_attachment_menu: Optional. :obj:`bool`, if this user added the bot to the attachment menu
    :type added_to_attachment_menu: :obj:`bool`

    :param can_join_groups: Optional. True, if the bot can be invited to groups. Returned only in getMe.
    :type can_join_groups: :obj:`bool`

    :param can_read_all_group_messages: Optional. True, if privacy mode is disabled for the bot. Returned only in
        getMe.
    :type can_read_all_group_messages: :obj:`bool`

    :param supports_inline_queries: Optional. True, if the bot supports inline queries. Returned only in getMe.
    :type supports_inline_queries: :obj:`bool`

    :param can_connect_to_business: Optional. True, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in getMe.
    :type can_connect_to_business: :obj:`bool`

    :param has_main_web_app: Optional. True, if the bot has a main Web App. Returned only in getMe.
    :type has_main_web_app: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.User`
    """

    def __init__(
        self,
        id: "int" = None,
        is_bot: "bool" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        language_code: "str" = None,
        is_premium: "bool" = None,
        added_to_attachment_menu: "bool" = None,
        can_join_groups: "bool" = None,
        can_read_all_group_messages: "bool" = None,
        supports_inline_queries: "bool" = None,
        can_connect_to_business: "bool" = None,
        has_main_web_app: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
        self.can_connect_to_business = can_connect_to_business
        self.has_main_web_app = has_main_web_app

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.User"]:
        return (
            User(
                me=me,
                json=d,
                id=d.get("id"),
                is_bot=d.get("is_bot"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                language_code=d.get("language_code"),
                is_premium=d.get("is_premium"),
                added_to_attachment_menu=d.get("added_to_attachment_menu"),
                can_join_groups=d.get("can_join_groups"),
                can_read_all_group_messages=d.get("can_read_all_group_messages"),
                supports_inline_queries=d.get("supports_inline_queries"),
                can_connect_to_business=d.get("can_connect_to_business"),
                has_main_web_app=d.get("has_main_web_app"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
