import tgram
from .type_ import Type_

from typing import Union, Optional


class ChatMember(Type_):
    """
    This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are supported:

    * :class:`tgram.types.ChatMemberOwner`
    * :class:`tgram.types.ChatMemberAdministrator`
    * :class:`tgram.types.ChatMemberMember`
    * :class:`tgram.types.ChatMemberRestricted`
    * :class:`tgram.types.ChatMemberLeft`
    * :class:`tgram.types.ChatMemberBanned`

    Telegram Documentation: https://core.telegram.org/bots/api#chatmember
    """

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional[
        Union[
            "tgram.types.ChatMemberOwner",
            "tgram.types.ChatMemberAdministrator",
            "tgram.types.ChatMemberMember",
            "tgram.types.ChatMemberRestricted",
            "tgram.types.ChatMemberBanned",
            "tgram.types.ChatMemberLeft",
        ]
    ]:
        return (
            (
                tgram.types.ChatMemberOwner._parse(me=me, d=d)
                if d.get("status") == "creator"
                else tgram.types.ChatMemberAdministrator._parse(me=me, d=d)
                if d.get("status") == "administrator"
                else tgram.types.ChatMemberMember._parse(me=me, d=d)
                if d.get("status") == "member"
                else tgram.types.ChatMemberRestricted._parse(me=me, d=d)
                if d.get("status") == "restricted"
                else tgram.types.ChatMemberLeft._parse(me=me, d=d)
                if d.get("status") == "left"
                else tgram.types.ChatMemberBanned._parse(me=me, d=d)
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
