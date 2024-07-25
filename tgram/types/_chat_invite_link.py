import tgram
from .type_ import Type_

from typing import Optional


class ChatInviteLink(Type_):
    """
    Represents an invite link for a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chatinvitelink

    :param invite_link: The invite link. If the link was created by another chat administrator, then the second part of
        the link will be replaced with “…”.
    :type invite_link: :obj:`str`

    :param creator: Creator of the link
    :type creator: :class:`tgram.types.User`

    :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators
    :type creates_join_request: :obj:`bool`

    :param is_primary: True, if the link is primary
    :type is_primary: :obj:`bool`

    :param is_revoked: True, if the link is revoked
    :type is_revoked: :obj:`bool`

    :param name: Optional. Invite link name
    :type name: :obj:`str`

    :param expire_date: Optional. Point in time (Unix timestamp) when the link will expire or has been expired
    :type expire_date: :obj:`int`

    :param member_limit: Optional. The maximum number of users that can be members of the chat simultaneously after
        joining the chat via this invite link; 1-99999
    :type member_limit: :obj:`int`

    :param pending_join_request_count: Optional. Number of pending join requests created using this link
    :type pending_join_request_count: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatInviteLink`
    """

    def __init__(
        self,
        invite_link: "str" = None,
        creator: "tgram.types.User" = None,
        creates_join_request: "bool" = None,
        is_primary: "bool" = None,
        is_revoked: "bool" = None,
        name: "str" = None,
        expire_date: "int" = None,
        member_limit: "int" = None,
        pending_join_request_count: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatInviteLink"]:
        return (
            ChatInviteLink(
                me=me,
                json=d,
                invite_link=d.get("invite_link"),
                creator=tgram.types.User._parse(me=me, d=d.get("creator")),
                creates_join_request=d.get("creates_join_request"),
                is_primary=d.get("is_primary"),
                is_revoked=d.get("is_revoked"),
                name=d.get("name"),
                expire_date=d.get("expire_date"),
                member_limit=d.get("member_limit"),
                pending_join_request_count=d.get("pending_join_request_count"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
