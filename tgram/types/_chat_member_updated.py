import tgram
from .type_ import Type_

from typing import Union, Optional

from tgram import bound


class ChatMemberUpdated(Type_, bound.ChatMemberUpdatedB):
    """
    This object represents changes in the status of a chat member.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberupdated

    :param chat: Chat the user belongs to
    :type chat: :class:`tgram.types.Chat`

    :param from_user: Performer of the action, which resulted in the change
    :type from_user: :class:`tgram.types.User`

    :param date: Date the change was done in Unix time
    :type date: :obj:`int`

    :param old_chat_member: Previous information about the chat member
    :type old_chat_member: :class:`tgram.types.ChatMember`

    :param new_chat_member: New information about the chat member
    :type new_chat_member: :class:`tgram.types.ChatMember`

    :param invite_link: Optional. Chat invite link, which was used by the user to join the chat; for joining by invite
        link events only.
    :type invite_link: :class:`tgram.types.ChatInviteLink`

    :param via_join_request: Optional. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator
    :type via_join_request: :obj:`bool`

    :param via_chat_folder_invite_link: Optional. True, if the user joined the chat via a chat folder invite link
    :type via_chat_folder_invite_link: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberUpdated`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        from_user: "tgram.types.User" = None,
        date: "int" = None,
        old_chat_member: Union[
            "tgram.types.ChatMemberOwner",
            "tgram.types.ChatMemberAdministrator",
            "tgram.types.ChatMemberMember",
            "tgram.types.ChatMemberRestricted",
            "tgram.types.ChatMemberBanned",
            "tgram.types.ChatMemberLeft",
        ] = None,
        new_chat_member: Union[
            "tgram.types.ChatMemberOwner",
            "tgram.types.ChatMemberAdministrator",
            "tgram.types.ChatMemberMember",
            "tgram.types.ChatMemberRestricted",
            "tgram.types.ChatMemberBanned",
            "tgram.types.ChatMemberLeft",
        ] = None,
        invite_link: "tgram.types.ChatInviteLink" = None,
        via_join_request: "bool" = None,
        via_chat_folder_invite_link: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_join_request = via_join_request
        self.via_chat_folder_invite_link = via_chat_folder_invite_link

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatMemberUpdated"]:
        return (
            ChatMemberUpdated(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                date=d.get("date"),
                old_chat_member=tgram.types.ChatMember._parse(
                    me=me, d=d.get("old_chat_member")
                ),
                new_chat_member=tgram.types.ChatMember._parse(
                    me=me, d=d.get("new_chat_member")
                ),
                invite_link=tgram.types.ChatInviteLink._parse(
                    me=me, d=d.get("invite_link")
                ),
                via_join_request=d.get("via_join_request"),
                via_chat_folder_invite_link=d.get("via_chat_folder_invite_link"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
