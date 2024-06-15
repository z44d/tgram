# This is auto generated file, if you found any issue, please report me here: https://github.com/2ei/tgram/issues/new


from typing import List, Union
from .types import *

import tgram


class Methods:
    async def get_updates(
        self: "tgram.TgBot",
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: List[str] = None,
    ) -> List[Update]:
        """https://core.telegram.org/bots/api/#getupdates"""
        ...

    async def set_webhook(
        self: "tgram.TgBot",
        url: str,
        certificate: InputFile = None,
        ip_address: str = None,
        max_connections: int = None,
        allowed_updates: List[str] = None,
        drop_pending_updates: bool = None,
        secret_token: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setwebhook"""
        ...

    async def delete_webhook(
        self: "tgram.TgBot", drop_pending_updates: bool = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletewebhook"""
        ...

    async def get_webhook_info(self: "tgram.TgBot") -> WebhookInfo:
        """https://core.telegram.org/bots/api/#getwebhookinfo"""
        ...

    async def get_me(self: "tgram.TgBot") -> User:
        """https://core.telegram.org/bots/api/#getme"""
        ...

    async def log_out(self: "tgram.TgBot") -> bool:
        """https://core.telegram.org/bots/api/#logout"""
        ...

    async def close(self: "tgram.TgBot") -> bool:
        """https://core.telegram.org/bots/api/#close"""
        ...

    async def send_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        text: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendmessage"""
        ...

    async def forward_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#forwardmessage"""
        ...

    async def forward_messages(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> List[MessageId]:
        """https://core.telegram.org/bots/api/#forwardmessages"""
        ...

    async def copy_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> MessageId:
        """https://core.telegram.org/bots/api/#copymessage"""
        ...

    async def copy_messages(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        remove_caption: bool = None,
    ) -> List[MessageId]:
        """https://core.telegram.org/bots/api/#copymessages"""
        ...

    async def send_photo(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendphoto"""
        ...

    async def send_audio(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        audio: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        performer: str = None,
        title: str = None,
        thumbnail: Union[InputFile, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendaudio"""
        ...

    async def send_document(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        document: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        disable_content_type_detection: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#senddocument"""
        ...

    async def send_video(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        video: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        supports_streaming: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendvideo"""
        ...

    async def send_animation(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        animation: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendanimation"""
        ...

    async def send_voice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        voice: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendvoice"""
        ...

    async def send_video_note(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        video_note: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        length: int = None,
        thumbnail: Union[InputFile, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendvideonote"""
        ...

    async def send_media_group(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        media: List[bool],
        business_connection_id: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
    ) -> List[Message]:
        """https://core.telegram.org/bots/api/#sendmediagroup"""
        ...

    async def send_location(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        business_connection_id: str = None,
        message_thread_id: int = None,
        horizontal_accuracy: float = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendlocation"""
        ...

    async def send_venue(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        foursquare_id: str = None,
        foursquare_type: str = None,
        google_place_id: str = None,
        google_place_type: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendvenue"""
        ...

    async def send_contact(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        last_name: str = None,
        vcard: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendcontact"""
        ...

    async def send_poll(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        question: str,
        options: List[InputPollOption],
        business_connection_id: str = None,
        message_thread_id: int = None,
        question_parse_mode: str = None,
        question_entities: List[MessageEntity] = None,
        is_anonymous: bool = None,
        type: str = None,
        allows_multiple_answers: bool = None,
        correct_option_id: int = None,
        explanation: str = None,
        explanation_parse_mode: str = None,
        explanation_entities: List[MessageEntity] = None,
        open_period: int = None,
        close_date: int = None,
        is_closed: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendpoll"""
        ...

    async def send_dice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#senddice"""
        ...

    async def send_chat_action(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        action: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#sendchataction"""
        ...

    async def set_message_reaction(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        reaction: List[ReactionType] = None,
        is_big: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmessagereaction"""
        ...

    async def get_user_profile_photos(
        self: "tgram.TgBot", user_id: int, offset: int = None, limit: int = None
    ) -> UserProfilePhotos:
        """https://core.telegram.org/bots/api/#getuserprofilephotos"""
        ...

    async def get_file(self: "tgram.TgBot", file_id: str) -> File:
        """https://core.telegram.org/bots/api/#getfile"""
        ...

    async def ban_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#banchatmember"""
        ...

    async def unban_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#unbanchatmember"""
        ...

    async def restrict_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
        until_date: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#restrictchatmember"""
        ...

    async def promote_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: bool = None,
        can_manage_chat: bool = None,
        can_delete_messages: bool = None,
        can_manage_video_chats: bool = None,
        can_restrict_members: bool = None,
        can_promote_members: bool = None,
        can_change_info: bool = None,
        can_invite_users: bool = None,
        can_post_stories: bool = None,
        can_edit_stories: bool = None,
        can_delete_stories: bool = None,
        can_post_messages: bool = None,
        can_edit_messages: bool = None,
        can_pin_messages: bool = None,
        can_manage_topics: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#promotechatmember"""
        ...

    async def set_chat_administrator_custom_title(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int, custom_title: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatadministratorcustomtitle"""
        ...

    async def ban_chat_sender_chat(
        self: "tgram.TgBot", chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#banchatsenderchat"""
        ...

    async def unban_chat_sender_chat(
        self: "tgram.TgBot", chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#unbanchatsenderchat"""
        ...

    async def set_chat_permissions(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatpermissions"""
        ...

    async def export_chat_invite_link(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> str:
        """https://core.telegram.org/bots/api/#exportchatinvitelink"""
        ...

    async def create_chat_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#createchatinvitelink"""
        ...

    async def edit_chat_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#editchatinvitelink"""
        ...

    async def revoke_chat_invite_link(
        self: "tgram.TgBot", chat_id: Union[int, str], invite_link: str
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#revokechatinvitelink"""
        ...

    async def approve_chat_join_request(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#approvechatjoinrequest"""
        ...

    async def decline_chat_join_request(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#declinechatjoinrequest"""
        ...

    async def set_chat_photo(
        self: "tgram.TgBot", chat_id: Union[int, str], photo: InputFile
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatphoto"""
        ...

    async def delete_chat_photo(self: "tgram.TgBot", chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#deletechatphoto"""
        ...

    async def set_chat_title(
        self: "tgram.TgBot", chat_id: Union[int, str], title: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchattitle"""
        ...

    async def set_chat_description(
        self: "tgram.TgBot", chat_id: Union[int, str], description: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatdescription"""
        ...

    async def pin_chat_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#pinchatmessage"""
        ...

    async def unpin_chat_message(
        self: "tgram.TgBot", chat_id: Union[int, str], message_id: int = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinchatmessage"""
        ...

    async def unpin_all_chat_messages(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinallchatmessages"""
        ...

    async def leave_chat(self: "tgram.TgBot", chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#leavechat"""
        ...

    async def get_chat(self: "tgram.TgBot", chat_id: Union[int, str]) -> ChatFullInfo:
        """https://core.telegram.org/bots/api/#getchat"""
        ...

    async def get_chat_administrators(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> List[ChatMember]:
        """https://core.telegram.org/bots/api/#getchatadministrators"""
        ...

    async def get_chat_member_count(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> int:
        """https://core.telegram.org/bots/api/#getchatmembercount"""
        ...

    async def get_chat_member(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> ChatMember:
        """https://core.telegram.org/bots/api/#getchatmember"""
        ...

    async def set_chat_sticker_set(
        self: "tgram.TgBot", chat_id: Union[int, str], sticker_set_name: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatstickerset"""
        ...

    async def delete_chat_sticker_set(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletechatstickerset"""
        ...

    async def get_forum_topic_icon_stickers(self: "tgram.TgBot") -> List[Sticker]:
        """https://core.telegram.org/bots/api/#getforumtopiciconstickers"""
        ...

    async def create_forum_topic(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        name: str,
        icon_color: int = None,
        icon_custom_emoji_id: str = None,
    ) -> ForumTopic:
        """https://core.telegram.org/bots/api/#createforumtopic"""
        ...

    async def edit_forum_topic(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_thread_id: int,
        name: str = None,
        icon_custom_emoji_id: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#editforumtopic"""
        ...

    async def close_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#closeforumtopic"""
        ...

    async def reopen_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#reopenforumtopic"""
        ...

    async def delete_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#deleteforumtopic"""
        ...

    async def unpin_all_forum_topic_messages(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinallforumtopicmessages"""
        ...

    async def edit_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], name: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#editgeneralforumtopic"""
        ...

    async def close_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#closegeneralforumtopic"""
        ...

    async def reopen_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#reopengeneralforumtopic"""
        ...

    async def hide_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#hidegeneralforumtopic"""
        ...

    async def unhide_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#unhidegeneralforumtopic"""
        ...

    async def unpin_all_general_forum_topic_messages(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinallgeneralforumtopicmessages"""
        ...

    async def answer_callback_query(
        self: "tgram.TgBot",
        callback_query_id: str,
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answercallbackquery"""
        ...

    async def get_user_chat_boosts(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> UserChatBoosts:
        """https://core.telegram.org/bots/api/#getuserchatboosts"""
        ...

    async def get_business_connection(
        self: "tgram.TgBot", business_connection_id: str
    ) -> BusinessConnection:
        """https://core.telegram.org/bots/api/#getbusinessconnection"""
        ...

    async def set_my_commands(
        self: "tgram.TgBot",
        commands: List[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmycommands"""
        ...

    async def delete_my_commands(
        self: "tgram.TgBot", scope: BotCommandScope = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletemycommands"""
        ...

    async def get_my_commands(
        self: "tgram.TgBot", scope: BotCommandScope = None, language_code: str = None
    ) -> List[BotCommand]:
        """https://core.telegram.org/bots/api/#getmycommands"""
        ...

    async def set_my_name(
        self: "tgram.TgBot", name: str = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmyname"""
        ...

    async def get_my_name(self: "tgram.TgBot", language_code: str = None) -> BotName:
        """https://core.telegram.org/bots/api/#getmyname"""
        ...

    async def set_my_description(
        self: "tgram.TgBot", description: str = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmydescription"""
        ...

    async def get_my_description(
        self: "tgram.TgBot", language_code: str = None
    ) -> BotDescription:
        """https://core.telegram.org/bots/api/#getmydescription"""
        ...

    async def set_my_short_description(
        self: "tgram.TgBot", short_description: str = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmyshortdescription"""
        ...

    async def get_my_short_description(
        self: "tgram.TgBot", language_code: str = None
    ) -> BotShortDescription:
        """https://core.telegram.org/bots/api/#getmyshortdescription"""
        ...

    async def set_chat_menu_button(
        self: "tgram.TgBot", chat_id: int = None, menu_button: MenuButton = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatmenubutton"""
        ...

    async def get_chat_menu_button(
        self: "tgram.TgBot", chat_id: int = None
    ) -> MenuButton:
        """https://core.telegram.org/bots/api/#getchatmenubutton"""
        ...

    async def set_my_default_administrator_rights(
        self: "tgram.TgBot",
        rights: ChatAdministratorRights = None,
        for_channels: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmydefaultadministratorrights"""
        ...

    async def get_my_default_administrator_rights(
        self: "tgram.TgBot", for_channels: bool = None
    ) -> ChatAdministratorRights:
        """https://core.telegram.org/bots/api/#getmydefaultadministratorrights"""
        ...

    async def edit_message_text(
        self: "tgram.TgBot",
        text: str,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagetext"""
        ...

    async def edit_message_caption(
        self: "tgram.TgBot",
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagecaption"""
        ...

    async def edit_message_media(
        self: "tgram.TgBot",
        media: InputMedia,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagemedia"""
        ...

    async def edit_message_live_location(
        self: "tgram.TgBot",
        latitude: float,
        longitude: float,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        live_period: int = None,
        horizontal_accuracy: float = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagelivelocation"""
        ...

    async def stop_message_live_location(
        self: "tgram.TgBot",
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#stopmessagelivelocation"""
        ...

    async def edit_message_reply_markup(
        self: "tgram.TgBot",
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagereplymarkup"""
        ...

    async def stop_poll(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Poll:
        """https://core.telegram.org/bots/api/#stoppoll"""
        ...

    async def delete_message(
        self: "tgram.TgBot", chat_id: Union[int, str], message_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletemessage"""
        ...

    async def delete_messages(
        self: "tgram.TgBot", chat_id: Union[int, str], message_ids: List[int]
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletemessages"""
        ...

    async def send_sticker(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        sticker: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendsticker"""
        ...

    async def get_sticker_set(self: "tgram.TgBot", name: str) -> StickerSet:
        """https://core.telegram.org/bots/api/#getstickerset"""
        ...

    async def get_custom_emoji_stickers(
        self: "tgram.TgBot", custom_emoji_ids: List[str]
    ) -> List[Sticker]:
        """https://core.telegram.org/bots/api/#getcustomemojistickers"""
        ...

    async def upload_sticker_file(
        self: "tgram.TgBot", user_id: int, sticker: InputFile, sticker_format: str
    ) -> File:
        """https://core.telegram.org/bots/api/#uploadstickerfile"""
        ...

    async def create_new_sticker_set(
        self: "tgram.TgBot",
        user_id: int,
        name: str,
        title: str,
        stickers: List[InputSticker],
        sticker_type: str = None,
        needs_repainting: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#createnewstickerset"""
        ...

    async def add_sticker_to_set(
        self: "tgram.TgBot", user_id: int, name: str, sticker: InputSticker
    ) -> bool:
        """https://core.telegram.org/bots/api/#addstickertoset"""
        ...

    async def set_sticker_position_in_set(
        self: "tgram.TgBot", sticker: str, position: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickerpositioninset"""
        ...

    async def delete_sticker_from_set(self: "tgram.TgBot", sticker: str) -> bool:
        """https://core.telegram.org/bots/api/#deletestickerfromset"""
        ...

    async def replace_sticker_in_set(
        self: "tgram.TgBot",
        user_id: int,
        name: str,
        old_sticker: str,
        sticker: InputSticker,
    ) -> bool:
        """https://core.telegram.org/bots/api/#replacestickerinset"""
        ...

    async def set_sticker_emoji_list(
        self: "tgram.TgBot", sticker: str, emoji_list: List[str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickeremojilist"""
        ...

    async def set_sticker_keywords(
        self: "tgram.TgBot", sticker: str, keywords: List[str] = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickerkeywords"""
        ...

    async def set_sticker_mask_position(
        self: "tgram.TgBot", sticker: str, mask_position: MaskPosition = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickermaskposition"""
        ...

    async def set_sticker_set_title(self: "tgram.TgBot", name: str, title: str) -> bool:
        """https://core.telegram.org/bots/api/#setstickersettitle"""
        ...

    async def set_sticker_set_thumbnail(
        self: "tgram.TgBot",
        name: str,
        user_id: int,
        format: str,
        thumbnail: Union[InputFile, str] = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickersetthumbnail"""
        ...

    async def set_custom_emoji_sticker_set_thumbnail(
        self: "tgram.TgBot", name: str, custom_emoji_id: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setcustomemojistickersetthumbnail"""
        ...

    async def delete_sticker_set(self: "tgram.TgBot", name: str) -> bool:
        """https://core.telegram.org/bots/api/#deletestickerset"""
        ...

    async def answer_inline_query(
        self: "tgram.TgBot",
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        button: InlineQueryResultsButton = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answerinlinequery"""
        ...

    async def answer_web_app_query(
        self: "tgram.TgBot", web_app_query_id: str, result: InlineQueryResult
    ) -> SentWebAppMessage:
        """https://core.telegram.org/bots/api/#answerwebappquery"""
        ...

    async def send_invoice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        message_thread_id: int = None,
        provider_token: str = None,
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        start_parameter: str = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendinvoice"""
        ...

    async def create_invoice_link(
        self: "tgram.TgBot",
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        provider_token: str = None,
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
    ) -> str:
        """https://core.telegram.org/bots/api/#createinvoicelink"""
        ...

    async def answer_shipping_query(
        self: "tgram.TgBot",
        shipping_query_id: str,
        ok: bool,
        shipping_options: List[ShippingOption] = None,
        error_message: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answershippingquery"""
        ...

    async def answer_pre_checkout_query(
        self: "tgram.TgBot",
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answerprecheckoutquery"""
        ...

    async def refund_star_payment(
        self: "tgram.TgBot", user_id: int, telegram_payment_charge_id: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#refundstarpayment"""
        ...

    async def set_passport_data_errors(
        self: "tgram.TgBot", user_id: int, errors: List[PassportElementError]
    ) -> bool:
        """https://core.telegram.org/bots/api/#setpassportdataerrors"""
        ...

    async def send_game(
        self: "tgram.TgBot",
        chat_id: int,
        game_short_name: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendgame"""
        ...

    async def set_game_score(
        self: "tgram.TgBot",
        user_id: int,
        score: int,
        force: bool = None,
        disable_edit_message: bool = None,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#setgamescore"""
        ...

    async def get_game_high_scores(
        self: "tgram.TgBot",
        user_id: int,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> List[GameHighScore]:
        """https://core.telegram.org/bots/api/#getgamehighscores"""
        ...
