import tgram
from .type_ import Type_

from typing import Optional


class ChatMemberRestricted(Type_):
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.

    Telegram Documentation: https://core.telegram.org/bots/api#chatmemberrestricted

    :param status: The member's status in the chat, always “restricted”
    :type status: :obj:`str`

    :param user: Information about the user
    :type user: :class:`tgram.types.User`

    :param is_member: True, if the user is a member of the chat at the moment of the request
    :type is_member: :obj:`bool`

    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :type can_change_info: :obj:`bool`

    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :type can_invite_users: :obj:`bool`

    :param can_pin_messages: True, if the user is allowed to pin messages
    :type can_pin_messages: :obj:`bool`

    :param can_manage_topics: True, if the user is allowed to create forum topics
    :type can_manage_topics: :obj:`bool`

    :param can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues
    :type can_send_messages: :obj:`bool`

    :param can_send_audios: True, if the user is allowed to send audios
    :type can_send_audios: :obj:`bool`

    :param can_send_documents: True, if the user is allowed to send documents
    :type can_send_documents: :obj:`bool`

    :param can_send_photos: True, if the user is allowed to send photos
    :type can_send_photos: :obj:`bool`

    :param can_send_videos: True, if the user is allowed to send videos
    :type can_send_videos: :obj:`bool`

    :param can_send_video_notes: True, if the user is allowed to send video notes
    :type can_send_video_notes: :obj:`bool`

    :param can_send_voice_notes: True, if the user is allowed to send voice notes
    :type can_send_voice_notes: :obj:`bool`

    :param can_send_polls: True, if the user is allowed to send polls
    :type can_send_polls: :obj:`bool`

    :param can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline
        bots
    :type can_send_other_messages: :obj:`bool`

    :param can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages
    :type can_add_web_page_previews: :obj:`bool`

    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted
        forever
    :type until_date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatMemberRestricted`
    """

    def __init__(
        self,
        status: "tgram.types.ChatMemberStatus" = None,
        user: "tgram.types.User" = None,
        is_member: "bool" = None,
        can_send_messages: "bool" = None,
        can_send_audios: "bool" = None,
        can_send_documents: "bool" = None,
        can_send_photos: "bool" = None,
        can_send_videos: "bool" = None,
        can_send_video_notes: "bool" = None,
        can_send_voice_notes: "bool" = None,
        can_send_polls: "bool" = None,
        can_send_other_messages: "bool" = None,
        can_add_web_page_previews: "bool" = None,
        can_change_info: "bool" = None,
        can_invite_users: "bool" = None,
        can_pin_messages: "bool" = None,
        can_manage_topics: "bool" = None,
        until_date: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.status = status
        self.user = user
        self.is_member = is_member
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.until_date = until_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatMemberRestricted"]:
        return (
            ChatMemberRestricted(
                me=me,
                json=d,
                status=d.get("status"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                is_member=d.get("is_member"),
                can_send_messages=d.get("can_send_messages"),
                can_send_audios=d.get("can_send_audios"),
                can_send_documents=d.get("can_send_documents"),
                can_send_photos=d.get("can_send_photos"),
                can_send_videos=d.get("can_send_videos"),
                can_send_video_notes=d.get("can_send_video_notes"),
                can_send_voice_notes=d.get("can_send_voice_notes"),
                can_send_polls=d.get("can_send_polls"),
                can_send_other_messages=d.get("can_send_other_messages"),
                can_add_web_page_previews=d.get("can_add_web_page_previews"),
                can_change_info=d.get("can_change_info"),
                can_invite_users=d.get("can_invite_users"),
                can_pin_messages=d.get("can_pin_messages"),
                can_manage_topics=d.get("can_manage_topics"),
                until_date=d.get("until_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
