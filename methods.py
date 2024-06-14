from typing import Optional, List, Any
from types_ import *


class TelegramBotMethods:
    def get_updates(
        self,
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: List[str] = None,
    ) -> List[Update]:
        """https://core.telegram.org/bots/api/#getupdates"""
        ...

    def set_webhook(
        self,
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

    def delete_webhook(self, drop_pending_updates: bool = None) -> bool:
        """https://core.telegram.org/bots/api/#deletewebhook"""
        ...

    def get_webhook_info(self) -> WebhookInfo:
        """https://core.telegram.org/bots/api/#getwebhookinfo"""
        ...

    def get_me(self) -> User:
        """https://core.telegram.org/bots/api/#getme"""
        ...

    def log_out(self) -> bool:
        """https://core.telegram.org/bots/api/#logout"""
        ...

    def close(self) -> bool:
        """https://core.telegram.org/bots/api/#close"""
        ...

    def send_message(
        self,
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

    def forward_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#forwardmessage"""
        ...

    def forward_messages(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> List[MessageId]:
        """https://core.telegram.org/bots/api/#forwardmessages"""
        ...

    def copy_message(
        self,
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

    def copy_messages(
        self,
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

    def send_photo(
        self,
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

    def send_audio(
        self,
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

    def send_document(
        self,
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

    def send_video(
        self,
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

    def send_animation(
        self,
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

    def send_voice(
        self,
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

    def send_video_note(
        self,
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

    def send_media_group(
        self,
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

    def send_location(
        self,
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

    def send_venue(
        self,
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

    def send_contact(
        self,
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

    def send_poll(
        self,
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

    def send_dice(
        self,
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

    def send_chat_action(
        self,
        chat_id: Union[int, str],
        action: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#sendchataction"""
        ...

    def set_message_reaction(
        self,
        chat_id: Union[int, str],
        message_id: int,
        reaction: List[ReactionType] = None,
        is_big: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmessagereaction"""
        ...

    def get_user_profile_photos(
        self, user_id: int, offset: int = None, limit: int = None
    ) -> UserProfilePhotos:
        """https://core.telegram.org/bots/api/#getuserprofilephotos"""
        ...

    def get_file(self, file_id: str) -> File:
        """https://core.telegram.org/bots/api/#getfile"""
        ...

    def ban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#banchatmember"""
        ...

    def unban_chat_member(
        self, chat_id: Union[int, str], user_id: int, only_if_banned: bool = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#unbanchatmember"""
        ...

    def restrict_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
        until_date: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#restrictchatmember"""
        ...

    def promote_chat_member(
        self,
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

    def set_chat_administrator_custom_title(
        self, chat_id: Union[int, str], user_id: int, custom_title: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatadministratorcustomtitle"""
        ...

    def ban_chat_sender_chat(
        self, chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#banchatsenderchat"""
        ...

    def unban_chat_sender_chat(
        self, chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#unbanchatsenderchat"""
        ...

    def set_chat_permissions(
        self,
        chat_id: Union[int, str],
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatpermissions"""
        ...

    def export_chat_invite_link(self, chat_id: Union[int, str]) -> str:
        """https://core.telegram.org/bots/api/#exportchatinvitelink"""
        ...

    def create_chat_invite_link(
        self,
        chat_id: Union[int, str],
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#createchatinvitelink"""
        ...

    def edit_chat_invite_link(
        self,
        chat_id: Union[int, str],
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#editchatinvitelink"""
        ...

    def revoke_chat_invite_link(
        self, chat_id: Union[int, str], invite_link: str
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#revokechatinvitelink"""
        ...

    def approve_chat_join_request(self, chat_id: Union[int, str], user_id: int) -> bool:
        """https://core.telegram.org/bots/api/#approvechatjoinrequest"""
        ...

    def decline_chat_join_request(self, chat_id: Union[int, str], user_id: int) -> bool:
        """https://core.telegram.org/bots/api/#declinechatjoinrequest"""
        ...

    def set_chat_photo(self, chat_id: Union[int, str], photo: InputFile) -> bool:
        """https://core.telegram.org/bots/api/#setchatphoto"""
        ...

    def delete_chat_photo(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#deletechatphoto"""
        ...

    def set_chat_title(self, chat_id: Union[int, str], title: str) -> bool:
        """https://core.telegram.org/bots/api/#setchattitle"""
        ...

    def set_chat_description(
        self, chat_id: Union[int, str], description: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatdescription"""
        ...

    def pin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#pinchatmessage"""
        ...

    def unpin_chat_message(
        self, chat_id: Union[int, str], message_id: int = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinchatmessage"""
        ...

    def unpin_all_chat_messages(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#unpinallchatmessages"""
        ...

    def leave_chat(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#leavechat"""
        ...

    def get_chat(self, chat_id: Union[int, str]) -> ChatFullInfo:
        """https://core.telegram.org/bots/api/#getchat"""
        ...

    def get_chat_administrators(self, chat_id: Union[int, str]) -> List[ChatMember]:
        """https://core.telegram.org/bots/api/#getchatadministrators"""
        ...

    def get_chat_member_count(self, chat_id: Union[int, str]) -> int:
        """https://core.telegram.org/bots/api/#getchatmembercount"""
        ...

    def get_chat_member(self, chat_id: Union[int, str], user_id: int) -> ChatMember:
        """https://core.telegram.org/bots/api/#getchatmember"""
        ...

    def set_chat_sticker_set(
        self, chat_id: Union[int, str], sticker_set_name: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatstickerset"""
        ...

    def delete_chat_sticker_set(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#deletechatstickerset"""
        ...

    def get_forum_topic_icon_stickers(self) -> List[Sticker]:
        """https://core.telegram.org/bots/api/#getforumtopiciconstickers"""
        ...

    def create_forum_topic(
        self,
        chat_id: Union[int, str],
        name: str,
        icon_color: int = None,
        icon_custom_emoji_id: str = None,
    ) -> ForumTopic:
        """https://core.telegram.org/bots/api/#createforumtopic"""
        ...

    def edit_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        name: str = None,
        icon_custom_emoji_id: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#editforumtopic"""
        ...

    def close_forum_topic(
        self, chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#closeforumtopic"""
        ...

    def reopen_forum_topic(
        self, chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#reopenforumtopic"""
        ...

    def delete_forum_topic(
        self, chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#deleteforumtopic"""
        ...

    def unpin_all_forum_topic_messages(
        self, chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinallforumtopicmessages"""
        ...

    def edit_general_forum_topic(self, chat_id: Union[int, str], name: str) -> bool:
        """https://core.telegram.org/bots/api/#editgeneralforumtopic"""
        ...

    def close_general_forum_topic(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#closegeneralforumtopic"""
        ...

    def reopen_general_forum_topic(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#reopengeneralforumtopic"""
        ...

    def hide_general_forum_topic(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#hidegeneralforumtopic"""
        ...

    def unhide_general_forum_topic(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#unhidegeneralforumtopic"""
        ...

    def unpin_all_general_forum_topic_messages(self, chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#unpinallgeneralforumtopicmessages"""
        ...

    def answer_callback_query(
        self,
        callback_query_id: str,
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answercallbackquery"""
        ...

    def get_user_chat_boosts(
        self, chat_id: Union[int, str], user_id: int
    ) -> UserChatBoosts:
        """https://core.telegram.org/bots/api/#getuserchatboosts"""
        ...

    def get_business_connection(
        self, business_connection_id: str
    ) -> BusinessConnection:
        """https://core.telegram.org/bots/api/#getbusinessconnection"""
        ...

    def set_my_commands(
        self,
        commands: List[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmycommands"""
        ...

    def delete_my_commands(
        self, scope: BotCommandScope = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletemycommands"""
        ...

    def get_my_commands(
        self, scope: BotCommandScope = None, language_code: str = None
    ) -> List[BotCommand]:
        """https://core.telegram.org/bots/api/#getmycommands"""
        ...

    def set_my_name(self, name: str = None, language_code: str = None) -> bool:
        """https://core.telegram.org/bots/api/#setmyname"""
        ...

    def get_my_name(self, language_code: str = None) -> BotName:
        """https://core.telegram.org/bots/api/#getmyname"""
        ...

    def set_my_description(
        self, description: str = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmydescription"""
        ...

    def get_my_description(self, language_code: str = None) -> BotDescription:
        """https://core.telegram.org/bots/api/#getmydescription"""
        ...

    def set_my_short_description(
        self, short_description: str = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmyshortdescription"""
        ...

    def get_my_short_description(
        self, language_code: str = None
    ) -> BotShortDescription:
        """https://core.telegram.org/bots/api/#getmyshortdescription"""
        ...

    def set_chat_menu_button(
        self, chat_id: int = None, menu_button: MenuButton = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatmenubutton"""
        ...

    def get_chat_menu_button(self, chat_id: int = None) -> MenuButton:
        """https://core.telegram.org/bots/api/#getchatmenubutton"""
        ...

    def set_my_default_administrator_rights(
        self, rights: ChatAdministratorRights = None, for_channels: bool = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmydefaultadministratorrights"""
        ...

    def get_my_default_administrator_rights(
        self, for_channels: bool = None
    ) -> ChatAdministratorRights:
        """https://core.telegram.org/bots/api/#getmydefaultadministratorrights"""
        ...

    def edit_message_text(
        self,
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

    def edit_message_caption(
        self,
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

    def edit_message_media(
        self,
        media: InputMedia,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagemedia"""
        ...

    def edit_message_live_location(
        self,
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

    def stop_message_live_location(
        self,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#stopmessagelivelocation"""
        ...

    def edit_message_reply_markup(
        self,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagereplymarkup"""
        ...

    def stop_poll(
        self,
        chat_id: Union[int, str],
        message_id: int,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Poll:
        """https://core.telegram.org/bots/api/#stoppoll"""
        ...

    def delete_message(self, chat_id: Union[int, str], message_id: int) -> bool:
        """https://core.telegram.org/bots/api/#deletemessage"""
        ...

    def delete_messages(self, chat_id: Union[int, str], message_ids: List[int]) -> bool:
        """https://core.telegram.org/bots/api/#deletemessages"""
        ...

    def send_sticker(
        self,
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

    def get_sticker_set(self, name: str) -> StickerSet:
        """https://core.telegram.org/bots/api/#getstickerset"""
        ...

    def get_custom_emoji_stickers(self, custom_emoji_ids: List[str]) -> List[Sticker]:
        """https://core.telegram.org/bots/api/#getcustomemojistickers"""
        ...

    def upload_sticker_file(
        self, user_id: int, sticker: InputFile, sticker_format: str
    ) -> File:
        """https://core.telegram.org/bots/api/#uploadstickerfile"""
        ...

    def create_new_sticker_set(
        self,
        user_id: int,
        name: str,
        title: str,
        stickers: List[InputSticker],
        sticker_type: str = None,
        needs_repainting: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#createnewstickerset"""
        ...

    def add_sticker_to_set(
        self, user_id: int, name: str, sticker: InputSticker
    ) -> bool:
        """https://core.telegram.org/bots/api/#addstickertoset"""
        ...

    def set_sticker_position_in_set(self, sticker: str, position: int) -> bool:
        """https://core.telegram.org/bots/api/#setstickerpositioninset"""
        ...

    def delete_sticker_from_set(self, sticker: str) -> bool:
        """https://core.telegram.org/bots/api/#deletestickerfromset"""
        ...

    def replace_sticker_in_set(
        self, user_id: int, name: str, old_sticker: str, sticker: InputSticker
    ) -> bool:
        """https://core.telegram.org/bots/api/#replacestickerinset"""
        ...

    def set_sticker_emoji_list(self, sticker: str, emoji_list: List[str]) -> bool:
        """https://core.telegram.org/bots/api/#setstickeremojilist"""
        ...

    def set_sticker_keywords(self, sticker: str, keywords: List[str] = None) -> bool:
        """https://core.telegram.org/bots/api/#setstickerkeywords"""
        ...

    def set_sticker_mask_position(
        self, sticker: str, mask_position: MaskPosition = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickermaskposition"""
        ...

    def set_sticker_set_title(self, name: str, title: str) -> bool:
        """https://core.telegram.org/bots/api/#setstickersettitle"""
        ...

    def set_sticker_set_thumbnail(
        self,
        name: str,
        user_id: int,
        format: str,
        thumbnail: Union[InputFile, str] = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickersetthumbnail"""
        ...

    def set_custom_emoji_sticker_set_thumbnail(
        self, name: str, custom_emoji_id: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setcustomemojistickersetthumbnail"""
        ...

    def delete_sticker_set(self, name: str) -> bool:
        """https://core.telegram.org/bots/api/#deletestickerset"""
        ...

    def answer_inline_query(
        self,
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        button: InlineQueryResultsButton = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answerinlinequery"""
        ...

    def answer_web_app_query(
        self, web_app_query_id: str, result: InlineQueryResult
    ) -> SentWebAppMessage:
        """https://core.telegram.org/bots/api/#answerwebappquery"""
        ...

    def send_invoice(
        self,
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

    def create_invoice_link(
        self,
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

    def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: List[ShippingOption] = None,
        error_message: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answershippingquery"""
        ...

    def answer_pre_checkout_query(
        self, pre_checkout_query_id: str, ok: bool, error_message: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#answerprecheckoutquery"""
        ...

    def refund_star_payment(
        self, user_id: int, telegram_payment_charge_id: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#refundstarpayment"""
        ...

    def set_passport_data_errors(
        self, user_id: int, errors: List[PassportElementError]
    ) -> bool:
        """https://core.telegram.org/bots/api/#setpassportdataerrors"""
        ...

    def send_game(
        self,
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

    def set_game_score(
        self,
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

    def get_game_high_scores(
        self,
        user_id: int,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> List[GameHighScore]:
        """https://core.telegram.org/bots/api/#getgamehighscores"""
        ...
