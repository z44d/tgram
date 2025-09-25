import tgram
from .type_ import Type_

from typing import List, Optional
from tgram import bound, utils


class ChatFullInfo(Type_, bound.ChatB):
    """
    This object contains full information about a chat.

    Telegram Documentation: https://core.telegram.org/bots/api#chatfullinfo

    :param id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming
        languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed
        64-bit integer or double-precision float type are safe for storing this identifier.
    :type id: :obj:`int`

    :param type: Type of the chat, can be either “private”, “group”, “supergroup” or “channel”
    :type type: :obj:`str`

    :param title: Optional. Title, for supergroups, channels and group chats
    :type title: :obj:`str`

    :param username: Optional. Username, for private chats, supergroups and channels if available
    :type username: :obj:`str`

    :param first_name: Optional. First name of the other party in a private chat
    :type first_name: :obj:`str`

    :param last_name: Optional. Last name of the other party in a private chat
    :type last_name: :obj:`str`

    :param is_forum: Optional. True, if the supergroup chat is a forum (has topics enabled)
    :type is_forum: :obj:`bool`

    :param is_direct_messages: Optional. True, if the chat is the direct messages chat of a channel
    :type is_direct_messages: :obj:`bool`

    :param accent_color_id: Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview.
    :type accent_color_id: :obj:`int`

    :param max_reaction_count: The maximum number of reactions that can be set on a message in the chat
    :type max_reaction_count: :obj:`int`

    :param photo: Optional. Chat photo
    :type photo: :class:`tgram.types.ChatPhoto`

    :param active_usernames: Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels
    :type active_usernames: :obj:`list` of :obj:`str`

    :param birthdate: Optional. For private chats, the date of birth of the user
    :type birthdate: :class:`tgram.types.Birthdate`

    :param business_intro: Optional. For private chats with business accounts, the intro of the business
    :type business_intro: :class:`tgram.types.BusinessIntro`

    :param business_location: Optional. For private chats with business accounts, the location of the business
    :type business_location: :class:`tgram.types.BusinessLocation`

    :param business_opening_hours: Optional. For private chats with business accounts, the opening hours of the business
    :type business_opening_hours: :class:`tgram.types.BusinessOpeningHours`

    :param personal_chat: Optional. For private chats, the personal channel of the user
    :type personal_chat: :class:`tgram.types.Chat`

    :param parent_chat: Optional. Information about the corresponding channel chat; for direct messages chats only
    :type parent_chat: :class:`tgram.types.Chat`

    :param available_reactions: Optional. List of available reactions allowed in the chat. If omitted, then all emoji reactions are allowed.
    :type available_reactions: :obj:`list` of :class:`tgram.types.ReactionType`

    :param background_custom_emoji_id: Optional. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background
    :type background_custom_emoji_id: :obj:`str`

    :param profile_accent_color_id: Optional. Identifier of the accent color for the chat's profile background. See profile accent colors for more details.
    :type profile_accent_color_id: :obj:`int`

    :param profile_background_custom_emoji_id: Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background
    :type profile_background_custom_emoji_id: :obj:`str`

    :param emoji_status_custom_emoji_id: Optional. Custom emoji identifier of the emoji status of the chat or the other party in a private chat
    :type emoji_status_custom_emoji_id: :obj:`str`

    :param emoji_status_expiration_date: Optional. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any
    :type emoji_status_expiration_date: :obj:`int`

    :param bio: Optional. Bio of the other party in a private chat
    :type bio: :obj:`str`

    :param has_private_forwards: Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user
    :type has_private_forwards: :obj:`bool`

    :param has_restricted_voice_and_video_messages: Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat
    :type has_restricted_voice_and_video_messages: :obj:`bool`

    :param join_to_send_messages: Optional. True, if users need to join the supergroup before they can send messages
    :type join_to_send_messages: :obj:`bool`

    :param join_by_request: Optional. True, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators
    :type join_by_request: :obj:`bool`

    :param description: Optional. Description, for groups, supergroups and channel chats
    :type description: :obj:`str`

    :param invite_link: Optional. Primary invite link, for groups, supergroups and channel chats
    :type invite_link: :obj:`str`

    :param pinned_message: Optional. The most recent pinned message (by sending date)
    :type pinned_message: :class:`tgram.types.Message`

    :param permissions: Optional. Default chat member permissions, for groups and supergroups
    :type permissions: :class:`tgram.types.ChatPermissions`

    :param accepted_gift_types: Information about types of gifts that are accepted by the chat or by the corresponding user for private chats
    :type accepted_gift_types: :class:`tgram.types.AcceptedGiftTypes`

    :param can_send_paid_media: Optional. True, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.
    :type can_send_paid_media: :obj:`bool`

    :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds
    :type slow_mode_delay: :obj:`int`

    :param unrestrict_boost_count: Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions
    :type unrestrict_boost_count: :obj:`int`

    :param message_auto_delete_time: Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds
    :type message_auto_delete_time: :obj:`int`

    :param has_aggressive_anti_spam_enabled: Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.
    :type has_aggressive_anti_spam_enabled: :obj:`bool`

    :param has_hidden_members: Optional. True, if non-administrators can only get the list of bots and administrators in the chat
    :type has_hidden_members: :obj:`bool`

    :param has_protected_content: Optional. True, if messages from the chat can't be forwarded to other chats
    :type has_protected_content: :obj:`bool`

    :param has_visible_history: Optional. True, if new chat members will have access to old messages; available only to chat administrators
    :type has_visible_history: :obj:`bool`

    :param sticker_set_name: Optional. For supergroups, name of the group sticker set
    :type sticker_set_name: :obj:`str`

    :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set
    :type can_set_sticker_set: :obj:`bool`

    :param custom_emoji_sticker_set_name: Optional. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.
    :type custom_emoji_sticker_set_name: :obj:`str`

    :param linked_chat_id: Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats.
    :type linked_chat_id: :obj:`int`

    :param location: Optional. For supergroups, the location to which the supergroup is connected
    :type location: :class:`tgram.types.ChatLocation`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatFullInfo`
    """

    def __init__(
        self,
        id: "int" = None,
        type: "tgram.types.ChatType" = None,
        title: "str" = None,
        username: "str" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        is_forum: "bool" = None,
        is_direct_messages: "bool" = None,
        accent_color_id: "int" = None,
        max_reaction_count: "int" = None,
        photo: "tgram.types.ChatPhoto" = None,
        active_usernames: List["str"] = None,
        birthdate: "tgram.types.Birthdate" = None,
        business_intro: "tgram.types.BusinessIntro" = None,
        business_location: "tgram.types.BusinessLocation" = None,
        business_opening_hours: "tgram.types.BusinessOpeningHours" = None,
        personal_chat: "tgram.types.Chat" = None,
        parent_chat: "tgram.types.Chat" = None,
        available_reactions: List["tgram.types.ReactionType"] = None,
        background_custom_emoji_id: "str" = None,
        profile_accent_color_id: "int" = None,
        profile_background_custom_emoji_id: "str" = None,
        emoji_status_custom_emoji_id: "str" = None,
        emoji_status_expiration_date: "int" = None,
        bio: "str" = None,
        has_private_forwards: "bool" = None,
        has_restricted_voice_and_video_messages: "bool" = None,
        join_to_send_messages: "bool" = None,
        join_by_request: "bool" = None,
        description: "str" = None,
        invite_link: "str" = None,
        pinned_message: "tgram.types.Message" = None,
        permissions: "tgram.types.ChatPermissions" = None,
        accepted_gift_types: "tgram.types.AcceptedGiftTypes" = None,
        can_send_paid_media: "bool" = None,
        slow_mode_delay: "int" = None,
        unrestrict_boost_count: "int" = None,
        message_auto_delete_time: "int" = None,
        has_aggressive_anti_spam_enabled: "bool" = None,
        has_hidden_members: "bool" = None,
        has_protected_content: "bool" = None,
        has_visible_history: "bool" = None,
        sticker_set_name: "str" = None,
        can_set_sticker_set: "bool" = None,
        custom_emoji_sticker_set_name: "str" = None,
        linked_chat_id: "int" = None,
        location: "tgram.types.ChatLocation" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.is_direct_messages = is_direct_messages
        self.accent_color_id = accent_color_id
        self.max_reaction_count = max_reaction_count
        self.photo = photo
        self.active_usernames = active_usernames
        self.birthdate = birthdate
        self.business_intro = business_intro
        self.business_location = business_location
        self.business_opening_hours = business_opening_hours
        self.personal_chat = personal_chat
        self.parent_chat = parent_chat
        self.available_reactions = available_reactions
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = (
            has_restricted_voice_and_video_messages
        )
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.accepted_gift_types = accepted_gift_types
        self.can_send_paid_media = can_send_paid_media
        self.slow_mode_delay = slow_mode_delay
        self.unrestrict_boost_count = unrestrict_boost_count
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.linked_chat_id = linked_chat_id
        self.location = location

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatFullInfo"]:
        return (
            ChatFullInfo(
                me=me,
                json=d,
                id=d.get("id"),
                type=d.get("type"),
                title=d.get("title"),
                username=d.get("username"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                is_forum=d.get("is_forum"),
                is_direct_messages=d.get("is_direct_messages"),
                accent_color_id=d.get("accent_color_id"),
                max_reaction_count=d.get("max_reaction_count"),
                photo=tgram.types.ChatPhoto._parse(me=me, d=d.get("photo")),
                active_usernames=d.get("active_usernames"),
                birthdate=tgram.types.Birthdate._parse(me=me, d=d.get("birthdate")),
                business_intro=tgram.types.BusinessIntro._parse(
                    me=me, d=d.get("business_intro")
                ),
                business_location=tgram.types.BusinessLocation._parse(
                    me=me, d=d.get("business_location")
                ),
                business_opening_hours=tgram.types.BusinessOpeningHours._parse(
                    me=me, d=d.get("business_opening_hours")
                ),
                personal_chat=tgram.types.Chat._parse(me=me, d=d.get("personal_chat")),
                parent_chat=tgram.types.Chat._parse(me=me, d=d.get("parent_chat")),
                available_reactions=utils.reaction_type_parse(
                    me, d.get("available_reactions")
                ),
                background_custom_emoji_id=d.get("background_custom_emoji_id"),
                profile_accent_color_id=d.get("profile_accent_color_id"),
                profile_background_custom_emoji_id=d.get(
                    "profile_background_custom_emoji_id"
                ),
                emoji_status_custom_emoji_id=d.get("emoji_status_custom_emoji_id"),
                emoji_status_expiration_date=d.get("emoji_status_expiration_date"),
                bio=d.get("bio"),
                has_private_forwards=d.get("has_private_forwards"),
                has_restricted_voice_and_video_messages=d.get(
                    "has_restricted_voice_and_video_messages"
                ),
                join_to_send_messages=d.get("join_to_send_messages"),
                join_by_request=d.get("join_by_request"),
                description=d.get("description"),
                invite_link=d.get("invite_link"),
                pinned_message=tgram.types.Message._parse(
                    me=me, d=d.get("pinned_message")
                ),
                permissions=tgram.types.ChatPermissions._parse(
                    me=me, d=d.get("permissions")
                ),
                accepted_gift_types=tgram.types.AcceptedGiftTypes._parse(
                    me=me, d=d.get("accepted_gift_types")
                ),
                can_send_paid_media=d.get("can_send_paid_media"),
                slow_mode_delay=d.get("slow_mode_delay"),
                unrestrict_boost_count=d.get("unrestrict_boost_count"),
                message_auto_delete_time=d.get("message_auto_delete_time"),
                has_aggressive_anti_spam_enabled=d.get(
                    "has_aggressive_anti_spam_enabled"
                ),
                has_hidden_members=d.get("has_hidden_members"),
                has_protected_content=d.get("has_protected_content"),
                has_visible_history=d.get("has_visible_history"),
                sticker_set_name=d.get("sticker_set_name"),
                can_set_sticker_set=d.get("can_set_sticker_set"),
                custom_emoji_sticker_set_name=d.get("custom_emoji_sticker_set_name"),
                linked_chat_id=d.get("linked_chat_id"),
                location=tgram.types.ChatLocation._parse(me=me, d=d.get("location")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
