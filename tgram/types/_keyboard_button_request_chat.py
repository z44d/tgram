import tgram
import random
from .type_ import Type_

from typing import Optional


class KeyboardButtonRequestChat(Type_):
    """
    This object defines the criteria used to request a suitable chat. The identifier of the selected chat will
    be shared with the bot when the corresponding button is pressed.

    Telegram documentation: https://core.telegram.org/bots/api#keyboardbuttonrequestchat

    :param request_id: Signed 32-bit identifier of the request, which will be received back in the ChatShared object.
        Must be unique within the message
    :type request_id: :obj:`int`

    :param chat_is_channel: Pass True to request a channel chat, pass False to request a group or a supergroup chat.
    :type chat_is_channel: :obj:`bool`

    :param chat_is_forum: Optional. Pass True to request a forum supergroup, pass False to request a non-forum chat.
        If not specified, no additional restrictions are applied.
    :type chat_is_forum: :obj:`bool`

    :param chat_has_username: Optional. Pass True to request a supergroup or a channel with a username, pass False to request a
        chat without a username. If not specified, no additional restrictions are applied.
    :type chat_has_username: :obj:`bool`

    :param chat_is_created: Optional. Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied.
    :type chat_is_created: :obj:`bool`

    :param user_administrator_rights: Optional. A JSON-serialized object listing the required administrator rights of the user in the chat.
        The rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied.
    :type user_administrator_rights: :class:`tgram.types.ChatAdministratorRights`

    :param bot_administrator_rights: Optional. A JSON-serialized object listing the required administrator rights of the bot in the chat.
        The rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied.
    :type bot_administrator_rights: :class:`tgram.types.ChatAdministratorRights`

    :param bot_is_member: Optional. Pass True to request a chat where the bot is a member. Otherwise, no additional restrictions are applied.
    :type bot_is_member: :obj:`bool`

    :param request_title: Optional. Request title
    :type request_title: :obj:`bool`

    :param request_photo: Optional. Request photo
    :type request_photo: :obj:`bool`

    :param request_username: Optional. Request username
    :type request_username: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.KeyboardButtonRequestChat`
    """

    def __init__(
        self,
        chat_is_channel: "bool" = None,
        chat_is_forum: "bool" = None,
        chat_has_username: "bool" = None,
        chat_is_created: "bool" = None,
        user_administrator_rights: "tgram.types.ChatAdministratorRights" = None,
        bot_administrator_rights: "tgram.types.ChatAdministratorRights" = None,
        bot_is_member: "bool" = None,
        request_title: "bool" = None,
        request_username: "bool" = None,
        request_photo: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_id = random.randint(10000, 99999)
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.chat_is_created = chat_is_created
        self.user_administrator_rights = user_administrator_rights
        self.bot_administrator_rights = bot_administrator_rights
        self.bot_is_member = bot_is_member
        self.request_title = request_title
        self.request_username = request_username
        self.request_photo = request_photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.KeyboardButtonRequestChat"]:
        return (
            KeyboardButtonRequestChat(
                me=me,
                json=d,
                chat_is_channel=d.get("chat_is_channel"),
                chat_is_forum=d.get("chat_is_forum"),
                chat_has_username=d.get("chat_has_username"),
                chat_is_created=d.get("chat_is_created"),
                user_administrator_rights=tgram.types.ChatAdministratorRights._parse(
                    me=me, d=d.get("user_administrator_rights")
                ),
                bot_administrator_rights=tgram.types.ChatAdministratorRights._parse(
                    me=me, d=d.get("bot_administrator_rights")
                ),
                bot_is_member=d.get("bot_is_member"),
                request_title=d.get("request_title"),
                request_username=d.get("request_username"),
                request_photo=d.get("request_photo"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
