import tgram
from .type_ import Type_

from typing import Optional


class ChatMemberAdministrator(Type_):
    """
    Represents a chat member that has some additional privileges.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberadministrator

    :param status: The member's status in the chat, always “administrator”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param can_be_edited: True, if the bot is allowed to edit administrator privileges of that user
    :type can_be_edited: :obj:`bool`

    :param is_anonymous: True, if the user's presence in the chat is hidden
    :type is_anonymous: :obj:`bool`

    :param can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message
        statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode.
        Implied by any other administrator privilege
    :type can_manage_chat: :obj:`bool`

    :param can_delete_messages: True, if the administrator can delete messages of other users
    :type can_delete_messages: :obj:`bool`

    :param can_manage_video_chats: True, if the administrator can manage video chats
    :type can_manage_video_chats: :obj:`bool`

    :param can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    :type can_restrict_members: :obj:`bool`

    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own
        privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that
        were appointed by the user)
    :type can_promote_members: :obj:`bool`

    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :type can_change_info: :obj:`bool`

    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :type can_invite_users: :obj:`bool`

    :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only
    :type can_post_messages: :obj:`bool`

    :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin
        messages; channels only
    :type can_edit_messages: :obj:`bool`

    :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only
    :type can_pin_messages: :obj:`bool`

    :param can_manage_topics: Optional. True, if the user is allowed to create, rename, close, and reopen forum topics;
        supergroups only
    :type can_manage_topics: :obj:`bool`

    :param custom_title: Optional. Custom title for this user
    :type custom_title: :obj:`str`

    :param can_post_stories: Optional. True, if the administrator can post channel stories
    :type can_post_stories: :obj:`bool`

    :param can_edit_stories: Optional. True, if the administrator can edit stories
    :type can_edit_stories: :obj:`bool`

    :param can_delete_stories: Optional. True, if the administrator can delete stories of other users
    :type can_delete_stories: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberAdministrator`
    """

    def __init__(
        self,
        status: "tgram.types.ChatMemberStatus" = None,
        user: "tgram.types.User" = None,
        can_be_edited: "bool" = None,
        is_anonymous: "bool" = None,
        can_manage_chat: "bool" = None,
        can_delete_messages: "bool" = None,
        can_manage_video_chats: "bool" = None,
        can_restrict_members: "bool" = None,
        can_promote_members: "bool" = None,
        can_change_info: "bool" = None,
        can_invite_users: "bool" = None,
        can_post_stories: "bool" = None,
        can_edit_stories: "bool" = None,
        can_delete_stories: "bool" = None,
        can_post_messages: "bool" = None,
        can_edit_messages: "bool" = None,
        can_pin_messages: "bool" = None,
        can_manage_topics: "bool" = None,
        custom_title: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user
        self.can_be_edited = can_be_edited
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.custom_title = custom_title

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatMemberAdministrator"]:
        return (
            ChatMemberAdministrator(
                me=me,
                json=d,
                status=d.get("status"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                can_be_edited=d.get("can_be_edited"),
                is_anonymous=d.get("is_anonymous"),
                can_manage_chat=d.get("can_manage_chat"),
                can_delete_messages=d.get("can_delete_messages"),
                can_manage_video_chats=d.get("can_manage_video_chats"),
                can_restrict_members=d.get("can_restrict_members"),
                can_promote_members=d.get("can_promote_members"),
                can_change_info=d.get("can_change_info"),
                can_invite_users=d.get("can_invite_users"),
                can_post_stories=d.get("can_post_stories"),
                can_edit_stories=d.get("can_edit_stories"),
                can_delete_stories=d.get("can_delete_stories"),
                can_post_messages=d.get("can_post_messages"),
                can_edit_messages=d.get("can_edit_messages"),
                can_pin_messages=d.get("can_pin_messages"),
                can_manage_topics=d.get("can_manage_topics"),
                custom_title=d.get("custom_title"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
