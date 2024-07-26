import tgram
from .type_ import Type_

from typing import Optional, Union


class BotCommandScope(Type_):
    """
    This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:

    * :class:`BotCommandScopeDefault`
    * :class:`BotCommandScopeAllPrivateChats`
    * :class:`BotCommandScopeAllGroupChats`
    * :class:`BotCommandScopeAllChatAdministrators`
    * :class:`BotCommandScopeChat`
    * :class:`BotCommandScopeChatAdministrators`
    * :class:`BotCommandScopeChatMember`

    Determining list of commands
    The following algorithm is used to determine the list of commands for a particular user viewing the bot menu. The first list of commands which is set is returned:

    Commands in the chat with the bot:

    * :class:`BotCommandScopeChat` + language_code
    * :class:`BotCommandScopeChat`
    * :class:`BotCommandScopeAllPrivateChats` + language_code
    * :class:`BotCommandScopeAllPrivateChats`
    * :class:`BotCommandScopeDefault` + language_code
    * :class:`BotCommandScopeDefault`

    Commands in group and supergroup chats:

    * :class:`BotCommandScopeChatMember` + language_code
    * :class:`BotCommandScopeChatMember`
    * :class:`BotCommandScopeChatAdministrators` + language_code (administrators only)
    * :class:`BotCommandScopeChatAdministrators` (administrators only)
    * :class:`BotCommandScopeChat` + language_code
    * :class:`BotCommandScopeChat`
    * :class:`BotCommandScopeAllChatAdministrators` + language_code (administrators only)
    * :class:`BotCommandScopeAllChatAdministrators` (administrators only)
    * :class:`BotCommandScopeAllGroupChats` + language_code
    * :class:`BotCommandScopeAllGroupChats`
    * :class:`BotCommandScopeDefault` + language_code
    * :class:`BotCommandScopeDefault`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScope`
    """

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional[
        Union[
            "tgram.types.BotCommandScopeDefault",
            "tgram.types.BotCommandScopeAllPrivateChats",
            "tgram.types.BotCommandScopeAllGroupChats",
            "tgram.types.BotCommandScopeAllChatAdministrators",
            "tgram.types.BotCommandScopeChat",
            "tgram.types.BotCommandScopeChatAdministrators",
            "tgram.types.BotCommandScopeChatMember",
        ]
    ]:
        return (
            None
            if not d
            else tgram.types.BotCommandScopeDefault._parse(me, d, force)
            if d["type"] == "default"
            else tgram.types.BotCommandScopeAllPrivateChats._parse(me, d, force)
            if d["type"] == "all_private_chats"
            else tgram.types.BotCommandScopeAllGroupChats._parse(me, d, force)
            if d["type"] == "all_group_chats"
            else tgram.types.BotCommandScopeAllChatAdministrators._parse(me, d, force)
            if d["type"] == "all_chat_administrators"
            else tgram.types.BotCommandScopeChat._parse(me, d, force)
            if d["type"] == "chat"
            else tgram.types.BotCommandScopeChatAdministrators._parse(me, d, force)
            if d["type"] == "chat_administrators"
            else tgram.types.BotCommandScopeChatMember._parse(me, d, force)
        )
