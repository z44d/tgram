from typing import List, Union


class Type_:
    def __str__(self) -> str:
        return self.__parse()

    def __repr__(self) -> str:
        return self.__parse()

    def __parse(self, indent=1) -> str:
        lines = []
        indent_str = " " * indent if indent > 1 else ""

        for key, value in self.__dict__.items():
            if value is not None and not key.startswith("_"):
                if isinstance(value, Type_):
                    lines.append(f"{indent_str}{key}: {value.__parse(indent * 2)}")
                elif isinstance(value, list):
                    if not value:
                        lines.append(f"{indent_str}{key}: []")
                    else:
                        elements = []
                        for item in value:
                            if isinstance(item, Type_):
                                elements.append(item.__parse(indent * 2))
                            ## For InlineKeyboardMarkup, ReplyKeyboardMarkup
                            elif isinstance(item, list):
                                for item_2 in item:
                                    if isinstance(item_2, Type_):
                                        elements.append(
                                            f"\n{' ' * (indent * 2) if indent > 1 else ''}["
                                            + item_2.__parse(indent * 4)
                                            + f"\n{' ' * (indent * 2) if indent > 1 else ''}]"
                                        )
                            else:
                                elements.append(repr(item))
                        elements_str = (
                            "["
                            + ",\n".join([f"{' ' * (indent * 2)}{e}" for e in elements])
                            + f"\n{' ' * indent if indent > 1 else ''}]"
                        )
                        lines.append(f"{indent_str}{key}: {elements_str}")
                elif isinstance(value, dict):
                    if not value:
                        lines.append(f"{indent_str}{key}: {{}}")
                    else:
                        elements = [f"{repr(k)}: {repr(v)}" for k, v in value.items()]
                        elements_str = "{" + ", ".join(elements) + "}"
                        lines.append(f"{indent_str}{key}: {elements_str}")
                else:
                    lines.append(f"{indent_str}{key}: {repr(value)}")

        return (
            ("\n" if indent > 1 else "")
            + f"{indent_str}_: {repr(self.__class__.__name__)}\n"
            + "\n".join(lines)
        )

    @staticmethod
    def list_to_json(l) -> list:
        _ = []
        for i in l:
            if isinstance(i, list):
                _.append(Type_.list_to_json(i))
            elif isinstance(i, Type_):
                _.append(i.to_json())
            else:
                _.append(i)
        return _

    def to_json(self) -> dict:
        d = {}
        for key in filter(
            lambda x: not x.startswith("_") and getattr(self, x), self.__dict__
        ):
            value = getattr(self, key)
            if isinstance(value, list):
                value = Type_.list_to_json(value)
            elif isinstance(value, Type_):
                value = value.to_json()

            d.update({key: value})
        return d


class Update(Type_):
    def __init__(
        self,
        update_id: "int",
        message: "Message" = None,
        edited_message: "Message" = None,
        channel_post: "Message" = None,
        edited_channel_post: "Message" = None,
        business_connection: "BusinessConnection" = None,
        business_message: "Message" = None,
        edited_business_message: "Message" = None,
        deleted_business_messages: "BusinessMessagesDeleted" = None,
        message_reaction: "MessageReactionUpdated" = None,
        message_reaction_count: "MessageReactionCountUpdated" = None,
        inline_query: "InlineQuery" = None,
        chosen_inline_result: "ChosenInlineResult" = None,
        callback_query: "CallbackQuery" = None,
        shipping_query: "ShippingQuery" = None,
        pre_checkout_query: "PreCheckoutQuery" = None,
        poll: "Poll" = None,
        poll_answer: "PollAnswer" = None,
        my_chat_member: "ChatMemberUpdated" = None,
        chat_member: "ChatMemberUpdated" = None,
        chat_join_request: "ChatJoinRequest" = None,
        chat_boost: "ChatBoostUpdated" = None,
        removed_chat_boost: "ChatBoostRemoved" = None,
    ):
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.business_connection = business_connection
        self.business_message = business_message
        self.edited_business_message = edited_business_message
        self.deleted_business_messages = deleted_business_messages
        self.message_reaction = message_reaction
        self.message_reaction_count = message_reaction_count
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request
        self.chat_boost = chat_boost
        self.removed_chat_boost = removed_chat_boost


class WebhookInfo(Type_):
    def __init__(
        self,
        url: "str",
        has_custom_certificate: "bool",
        pending_update_count: "int",
        ip_address: "str" = None,
        last_error_date: "int" = None,
        last_error_message: "str" = None,
        last_synchronization_error_date: "int" = None,
        max_connections: "int" = None,
        allowed_updates: List["str"] = None,
    ):
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.last_synchronization_error_date = last_synchronization_error_date
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates


class User(Type_):
    def __init__(
        self,
        id: "int",
        is_bot: "bool",
        first_name: "str",
        last_name: "str" = None,
        username: "str" = None,
        language_code: "str" = None,
        is_premium: "bool" = None,
        added_to_attachment_menu: "bool" = None,
        can_join_groups: "bool" = None,
        can_read_all_group_messages: "bool" = None,
        supports_inline_queries: "bool" = None,
        can_connect_to_business: "bool" = None,
    ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
        self.can_connect_to_business = can_connect_to_business


class Chat(Type_):
    def __init__(
        self,
        id: "int",
        type: "str",
        title: "str" = None,
        username: "str" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        is_forum: "bool" = None,
    ):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum


class ChatFullInfo(Type_):
    def __init__(
        self,
        id: "int",
        type: "str",
        accent_color_id: "int",
        max_reaction_count: "int",
        title: "str" = None,
        username: "str" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        is_forum: "bool" = None,
        photo: "ChatPhoto" = None,
        active_usernames: List["str"] = None,
        birthdate: "Birthdate" = None,
        business_intro: "BusinessIntro" = None,
        business_location: "BusinessLocation" = None,
        business_opening_hours: "BusinessOpeningHours" = None,
        personal_chat: "Chat" = None,
        available_reactions: List["ReactionType"] = None,
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
        pinned_message: "Message" = None,
        permissions: "ChatPermissions" = None,
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
        location: "ChatLocation" = None,
    ):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.accent_color_id = accent_color_id
        self.max_reaction_count = max_reaction_count
        self.photo = photo
        self.active_usernames = active_usernames
        self.birthdate = birthdate
        self.business_intro = business_intro
        self.business_location = business_location
        self.business_opening_hours = business_opening_hours
        self.personal_chat = personal_chat
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


ReplyMarkup = Union[
    "InlineKeyboardMarkup",
    "ReplyKeyboardMarkup",
    "ReplyKeyboardRemove",
    "ForceReply",
]


class Message(Type_):
    def __init__(
        self,
        message_id: "int",
        date: "int",
        chat: "Chat",
        message_thread_id: "int" = None,
        from_user: "User" = None,
        sender_chat: "Chat" = None,
        sender_boost_count: "int" = None,
        sender_business_bot: "User" = None,
        business_connection_id: "str" = None,
        forward_origin: "MessageOrigin" = None,
        is_topic_message: "bool" = None,
        is_automatic_forward: "bool" = None,
        reply_to_message: "Message" = None,
        external_reply: "ExternalReplyInfo" = None,
        quote: "TextQuote" = None,
        reply_to_story: "Story" = None,
        via_bot: "User" = None,
        edit_date: "int" = None,
        has_protected_content: "bool" = None,
        is_from_offline: "bool" = None,
        media_group_id: "str" = None,
        author_signature: "str" = None,
        text: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
        effect_id: "str" = None,
        animation: "Animation" = None,
        audio: "Audio" = None,
        document: "Document" = None,
        photo: List["PhotoSize"] = None,
        sticker: "Sticker" = None,
        story: "Story" = None,
        video: "Video" = None,
        video_note: "VideoNote" = None,
        voice: "Voice" = None,
        caption: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        has_media_spoiler: "bool" = None,
        contact: "Contact" = None,
        dice: "Dice" = None,
        game: "Game" = None,
        poll: "Poll" = None,
        venue: "Venue" = None,
        location: "Location" = None,
        new_chat_members: List["User"] = None,
        left_chat_member: "User" = None,
        new_chat_title: "str" = None,
        new_chat_photo: List["PhotoSize"] = None,
        delete_chat_photo: "bool" = None,
        group_chat_created: "bool" = None,
        supergroup_chat_created: "bool" = None,
        channel_chat_created: "bool" = None,
        message_auto_delete_timer_changed: "MessageAutoDeleteTimerChanged" = None,
        migrate_to_chat_id: "int" = None,
        migrate_from_chat_id: "int" = None,
        pinned_message: "MaybeInaccessibleMessage" = None,
        invoice: "Invoice" = None,
        successful_payment: "SuccessfulPayment" = None,
        users_shared: "UsersShared" = None,
        chat_shared: "ChatShared" = None,
        connected_website: "str" = None,
        write_access_allowed: "WriteAccessAllowed" = None,
        passport_data: "PassportData" = None,
        proximity_alert_triggered: "ProximityAlertTriggered" = None,
        boost_added: "ChatBoostAdded" = None,
        chat_background_set: "ChatBackground" = None,
        forum_topic_created: "ForumTopicCreated" = None,
        forum_topic_edited: "ForumTopicEdited" = None,
        forum_topic_closed: "ForumTopicClosed" = None,
        forum_topic_reopened: "ForumTopicReopened" = None,
        general_forum_topic_hidden: "GeneralForumTopicHidden" = None,
        general_forum_topic_unhidden: "GeneralForumTopicUnhidden" = None,
        giveaway_created: "GiveawayCreated" = None,
        giveaway: "Giveaway" = None,
        giveaway_winners: "GiveawayWinners" = None,
        giveaway_completed: "GiveawayCompleted" = None,
        video_chat_scheduled: "VideoChatScheduled" = None,
        video_chat_started: "VideoChatStarted" = None,
        video_chat_ended: "VideoChatEnded" = None,
        video_chat_participants_invited: "VideoChatParticipantsInvited" = None,
        web_app_data: "WebAppData" = None,
        reply_markup: ReplyMarkup = None,
    ):
        self.message_id = message_id
        self.message_thread_id = message_thread_id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.sender_boost_count = sender_boost_count
        self.sender_business_bot = sender_business_bot
        self.date = date
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.forward_origin = forward_origin
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.external_reply = external_reply
        self.quote = quote
        self.reply_to_story = reply_to_story
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.is_from_offline = is_from_offline
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.effect_id = effect_id
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = message_auto_delete_timer_changed
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.users_shared = users_shared
        self.chat_shared = chat_shared
        self.connected_website = connected_website
        self.write_access_allowed = write_access_allowed
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.boost_added = boost_added
        self.chat_background_set = chat_background_set
        self.forum_topic_created = forum_topic_created
        self.forum_topic_edited = forum_topic_edited
        self.forum_topic_closed = forum_topic_closed
        self.forum_topic_reopened = forum_topic_reopened
        self.general_forum_topic_hidden = general_forum_topic_hidden
        self.general_forum_topic_unhidden = general_forum_topic_unhidden
        self.giveaway_created = giveaway_created
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.giveaway_completed = giveaway_completed
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup


class MessageId(Type_):
    def __init__(self, message_id: "int"):
        self.message_id = message_id


class InaccessibleMessage(Type_):
    def __init__(self, chat: "Chat", message_id: "int", date: "int"):
        self.chat = chat
        self.message_id = message_id
        self.date = date


class MaybeInaccessibleMessage(Type_):
    def __init__(
        self,
        type: "str",
        offset: "int",
        length: "int",
        url: "str" = None,
        user: "User" = None,
        language: "str" = None,
        custom_emoji_id: "str" = None,
    ):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id


class MessageEntity(Type_):
    def __init__(
        self,
        type: "str",
        offset: "int",
        length: "int",
        url: "str" = None,
        user: "User" = None,
        language: "str" = None,
        custom_emoji_id: "str" = None,
    ):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id


class TextQuote(Type_):
    def __init__(
        self,
        text: "str",
        position: "int",
        entities: List["MessageEntity"] = None,
        is_manual: "bool" = None,
    ):
        self.text = text
        self.entities = entities
        self.position = position
        self.is_manual = is_manual


class ExternalReplyInfo(Type_):
    def __init__(
        self,
        origin: "MessageOrigin",
        chat: "Chat" = None,
        message_id: "int" = None,
        link_preview_options: "LinkPreviewOptions" = None,
        animation: "Animation" = None,
        audio: "Audio" = None,
        document: "Document" = None,
        photo: List["PhotoSize"] = None,
        sticker: "Sticker" = None,
        story: "Story" = None,
        video: "Video" = None,
        video_note: "VideoNote" = None,
        voice: "Voice" = None,
        has_media_spoiler: "bool" = None,
        contact: "Contact" = None,
        dice: "Dice" = None,
        game: "Game" = None,
        giveaway: "Giveaway" = None,
        giveaway_winners: "GiveawayWinners" = None,
        invoice: "Invoice" = None,
        location: "Location" = None,
        poll: "Poll" = None,
        venue: "Venue" = None,
    ):
        self.origin = origin
        self.chat = chat
        self.message_id = message_id
        self.link_preview_options = link_preview_options
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.invoice = invoice
        self.location = location
        self.poll = poll
        self.venue = venue


class ReplyParameters(Type_):
    def __init__(
        self,
        message_id: "int",
        chat_id: Union["int", "str"] = None,
        allow_sending_without_reply: "bool" = None,
        quote: "str" = None,
        quote_parse_mode: "str" = None,
        quote_entities: List["MessageEntity"] = None,
        quote_position: "int" = None,
    ):
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities
        self.quote_position = quote_position


class MessageOrigin(Type_):
    def __init__(self, type: "str", date: "int", sender_user: "User"):
        self.type = type
        self.date = date
        self.sender_user = sender_user


class MessageOriginUser(Type_):
    def __init__(self, type: "str", date: "int", sender_user: "User"):
        self.type = type
        self.date = date
        self.sender_user = sender_user


class MessageOriginHiddenUser(Type_):
    def __init__(self, type: "str", date: "int", sender_user_name: "str"):
        self.type = type
        self.date = date
        self.sender_user_name = sender_user_name


class MessageOriginChat(Type_):
    def __init__(
        self,
        type: "str",
        date: "int",
        sender_chat: "Chat",
        author_signature: "str" = None,
    ):
        self.type = type
        self.date = date
        self.sender_chat = sender_chat
        self.author_signature = author_signature


class MessageOriginChannel(Type_):
    def __init__(
        self,
        type: "str",
        date: "int",
        chat: "Chat",
        message_id: "int",
        author_signature: "str" = None,
    ):
        self.type = type
        self.date = date
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature


class PhotoSize(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        width: "int",
        height: "int",
        file_size: "int" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size


class Animation(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        width: "int",
        height: "int",
        duration: "int",
        thumbnail: "PhotoSize" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Audio(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        duration: "int",
        performer: "str" = None,
        title: "str" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
        thumbnail: "PhotoSize" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail


class Document(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        thumbnail: "PhotoSize" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Story(Type_):
    def __init__(self, chat: "Chat", id: "int"):
        self.chat = chat
        self.id = id


class Video(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        width: "int",
        height: "int",
        duration: "int",
        thumbnail: "PhotoSize" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class VideoNote(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        length: "int",
        duration: "int",
        thumbnail: "PhotoSize" = None,
        file_size: "int" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size


class Voice(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        duration: "int",
        mime_type: "str" = None,
        file_size: "int" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size


class Contact(Type_):
    def __init__(
        self,
        phone_number: "str",
        first_name: "str",
        last_name: "str" = None,
        user_id: "int" = None,
        vcard: "str" = None,
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard


class Dice(Type_):
    def __init__(self, emoji: "str", value: "int"):
        self.emoji = emoji
        self.value = value


class PollOption(Type_):
    def __init__(
        self,
        text: "str",
        voter_count: "int",
        text_entities: List["MessageEntity"] = None,
    ):
        self.text = text
        self.text_entities = text_entities
        self.voter_count = voter_count


class InputPollOption(Type_):
    def __init__(
        self,
        text: "str",
        text_parse_mode: "str" = None,
        text_entities: List["MessageEntity"] = None,
    ):
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities


class PollAnswer(Type_):
    def __init__(
        self,
        poll_id: "str",
        option_ids: List["int"],
        voter_chat: "Chat" = None,
        user: "User" = None,
    ):
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids


class Poll(Type_):
    def __init__(
        self,
        id: "str",
        question: "str",
        options: List["PollOption"],
        total_voter_count: "int",
        is_closed: "bool",
        is_anonymous: "bool",
        type: "str",
        allows_multiple_answers: "bool",
        question_entities: List["MessageEntity"] = None,
        correct_option_id: "int" = None,
        explanation: "str" = None,
        explanation_entities: List["MessageEntity"] = None,
        open_period: "int" = None,
        close_date: "int" = None,
    ):
        self.id = id
        self.question = question
        self.question_entities = question_entities
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date


class Location(Type_):
    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


class Venue(Type_):
    def __init__(
        self,
        location: "Location",
        title: "str",
        address: "str",
        foursquare_id: "str" = None,
        foursquare_type: "str" = None,
        google_place_id: "str" = None,
        google_place_type: "str" = None,
    ):
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type


class WebAppData(Type_):
    def __init__(self, data: "str", button_text: "str"):
        self.data = data
        self.button_text = button_text


class ProximityAlertTriggered(Type_):
    def __init__(self, traveler: "User", watcher: "User", distance: "int"):
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance


class MessageAutoDeleteTimerChanged(Type_):
    def __init__(self, message_auto_delete_time: "int"):
        self.message_auto_delete_time = message_auto_delete_time


class ChatBoostAdded(Type_):
    def __init__(self, boost_count: "int"):
        self.boost_count = boost_count


class BackgroundFill(Type_):
    def __init__(self, type: "str", color: "int"):
        self.type = type
        self.color = color


class BackgroundFillSolid(Type_):
    def __init__(self, type: "str", color: "int"):
        self.type = type
        self.color = color


class BackgroundFillGradient(Type_):
    def __init__(
        self, type: "str", top_color: "int", bottom_color: "int", rotation_angle: "int"
    ):
        self.type = type
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.rotation_angle = rotation_angle


class BackgroundFillFreeformGradient(Type_):
    def __init__(self, type: "str", colors: List["int"]):
        self.type = type
        self.colors = colors


class BackgroundType(Type_):
    def __init__(self, type: "str", fill: "BackgroundFill", dark_theme_dimming: "int"):
        self.type = type
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming


class BackgroundTypeFill(Type_):
    def __init__(self, type: "str", fill: "BackgroundFill", dark_theme_dimming: "int"):
        self.type = type
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming


class BackgroundTypeWallpaper(Type_):
    def __init__(
        self,
        type: "str",
        document: "Document",
        dark_theme_dimming: "int",
        is_blurred: "bool" = None,
        is_moving: "bool" = None,
    ):
        self.type = type
        self.document = document
        self.dark_theme_dimming = dark_theme_dimming
        self.is_blurred = is_blurred
        self.is_moving = is_moving


class BackgroundTypePattern(Type_):
    def __init__(
        self,
        type: "str",
        document: "Document",
        fill: "BackgroundFill",
        intensity: "int",
        is_inverted: "bool" = None,
        is_moving: "bool" = None,
    ):
        self.type = type
        self.document = document
        self.fill = fill
        self.intensity = intensity
        self.is_inverted = is_inverted
        self.is_moving = is_moving


class BackgroundTypeChatTheme(Type_):
    def __init__(self, type: "str", theme_name: "str"):
        self.type = type
        self.theme_name = theme_name


class ChatBackground(Type_):
    def __init__(self, type: "BackgroundType"):
        self.type = type


class ForumTopicCreated(Type_):
    def __init__(
        self, name: "str", icon_color: "int", icon_custom_emoji_id: "str" = None
    ):
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id


class ForumTopicClosed(Type_):
    def __init__(self, name: "str" = None, icon_custom_emoji_id: "str" = None):
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id


class ForumTopicEdited(Type_):
    def __init__(self, name: "str" = None, icon_custom_emoji_id: "str" = None):
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id


class ForumTopicReopened(Type_):
    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo


class GeneralForumTopicHidden(Type_):
    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo


class GeneralForumTopicUnhidden(Type_):
    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo


class SharedUser(Type_):
    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo


class UsersShared(Type_):
    def __init__(self, request_id: "int", users: List["SharedUser"]):
        self.request_id = request_id
        self.users = users


class ChatShared(Type_):
    def __init__(
        self,
        request_id: "int",
        chat_id: "int",
        title: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
    ):
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo


class WriteAccessAllowed(Type_):
    def __init__(
        self,
        from_request: "bool" = None,
        web_app_name: "str" = None,
        from_attachment_menu: "bool" = None,
    ):
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu


class VideoChatScheduled(Type_):
    def __init__(self, start_date: "int"):
        self.start_date = start_date


class VideoChatStarted(Type_):
    def __init__(self, duration: "int"):
        self.duration = duration


class VideoChatEnded(Type_):
    def __init__(self, duration: "int"):
        self.duration = duration


class VideoChatParticipantsInvited(Type_):
    def __init__(self, users: List["User"]):
        self.users = users


class GiveawayCreated(Type_):
    def __init__(
        self,
        chats: List["Chat"],
        winners_selection_date: "int",
        winner_count: "int",
        only_new_members: "bool" = None,
        has_public_winners: "bool" = None,
        prize_description: "str" = None,
        country_codes: List["str"] = None,
        premium_subscription_month_count: "int" = None,
    ):
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.premium_subscription_month_count = premium_subscription_month_count


class Giveaway(Type_):
    def __init__(
        self,
        chats: List["Chat"],
        winners_selection_date: "int",
        winner_count: "int",
        only_new_members: "bool" = None,
        has_public_winners: "bool" = None,
        prize_description: "str" = None,
        country_codes: List["str"] = None,
        premium_subscription_month_count: "int" = None,
    ):
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.premium_subscription_month_count = premium_subscription_month_count


class GiveawayWinners(Type_):
    def __init__(
        self,
        chat: "Chat",
        giveaway_message_id: "int",
        winners_selection_date: "int",
        winner_count: "int",
        winners: List["User"],
        additional_chat_count: "int" = None,
        premium_subscription_month_count: "int" = None,
        unclaimed_prize_count: "int" = None,
        only_new_members: "bool" = None,
        was_refunded: "bool" = None,
        prize_description: "str" = None,
    ):
        self.chat = chat
        self.giveaway_message_id = giveaway_message_id
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.winners = winners
        self.additional_chat_count = additional_chat_count
        self.premium_subscription_month_count = premium_subscription_month_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.only_new_members = only_new_members
        self.was_refunded = was_refunded
        self.prize_description = prize_description


class GiveawayCompleted(Type_):
    def __init__(
        self,
        winner_count: "int",
        unclaimed_prize_count: "int" = None,
        giveaway_message: "Message" = None,
    ):
        self.winner_count = winner_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.giveaway_message = giveaway_message


class LinkPreviewOptions(Type_):
    def __init__(
        self,
        is_disabled: "bool" = None,
        url: "str" = None,
        prefer_small_media: "bool" = None,
        prefer_large_media: "bool" = None,
        show_above_text: "bool" = None,
    ):
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text


class UserProfilePhotos(Type_):
    def __init__(self, total_count: "int", photos: List[List["PhotoSize"]]):
        self.total_count = total_count
        self.photos = photos


class File(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        file_size: "int" = None,
        file_path: "str" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path


class WebAppInfo(Type_):
    def __init__(self, url: "str"):
        self.url = url


class ReplyKeyboardMarkup(Type_):
    def __init__(
        self,
        keyboard: List[List["KeyboardButton"]],
        is_persistent: "bool" = None,
        resize_keyboard: "bool" = None,
        one_time_keyboard: "bool" = None,
        input_field_placeholder: "str" = None,
        selective: "bool" = None,
    ):
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective


class KeyboardButton(Type_):
    def __init__(
        self,
        text: "str",
        request_users: "KeyboardButtonRequestUsers" = None,
        request_chat: "KeyboardButtonRequestChat" = None,
        request_contact: "bool" = None,
        request_location: "bool" = None,
        request_poll: "KeyboardButtonPollType" = None,
        web_app: "WebAppInfo" = None,
    ):
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app


class KeyboardButtonRequestUsers(Type_):
    def __init__(
        self,
        request_id: "int",
        user_is_bot: "bool" = None,
        user_is_premium: "bool" = None,
        max_quantity: "int" = None,
        request_name: "bool" = None,
        request_username: "bool" = None,
        request_photo: "bool" = None,
    ):
        self.request_id = request_id
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity
        self.request_name = request_name
        self.request_username = request_username
        self.request_photo = request_photo


class KeyboardButtonRequestChat(Type_):
    def __init__(
        self,
        request_id: "int",
        chat_is_channel: "bool",
        chat_is_forum: "bool" = None,
        chat_has_username: "bool" = None,
        chat_is_created: "bool" = None,
        user_administrator_rights: "ChatAdministratorRights" = None,
        bot_administrator_rights: "ChatAdministratorRights" = None,
        bot_is_member: "bool" = None,
        request_title: "bool" = None,
        request_username: "bool" = None,
        request_photo: "bool" = None,
    ):
        self.request_id = request_id
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


class KeyboardButtonPollType(Type_):
    def __init__(self, type: "str" = None):
        self.type = type


class ReplyKeyboardRemove(Type_):
    def __init__(self, remove_keyboard: "bool", selective: "bool" = None):
        self.remove_keyboard = remove_keyboard
        self.selective = selective


class InlineKeyboardMarkup(Type_):
    def __init__(self, inline_keyboard: List[List["InlineKeyboardButton"]]):
        self.inline_keyboard = inline_keyboard


class InlineKeyboardButton(Type_):
    def __init__(
        self,
        text: "str",
        url: "str" = None,
        callback_data: "str" = None,
        web_app: "WebAppInfo" = None,
        login_url: "LoginUrl" = None,
        switch_inline_query: "str" = None,
        switch_inline_query_current_chat: "str" = None,
        switch_inline_query_chosen_chat: "SwitchInlineQueryChosenChat" = None,
        callback_game: "CallbackGame" = None,
        pay: "bool" = None,
    ):
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.callback_game = callback_game
        self.pay = pay


class LoginUrl(Type_):
    def __init__(
        self,
        url: "str",
        forward_text: "str" = None,
        bot_username: "str" = None,
        request_write_access: "bool" = None,
    ):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access


class SwitchInlineQueryChosenChat(Type_):
    def __init__(
        self,
        query: "str" = None,
        allow_user_chats: "bool" = None,
        allow_bot_chats: "bool" = None,
        allow_group_chats: "bool" = None,
        allow_channel_chats: "bool" = None,
    ):
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats


class CallbackQuery(Type_):
    def __init__(
        self,
        id: "str",
        from_user: "User",
        chat_instance: "str",
        message: "MaybeInaccessibleMessage" = None,
        inline_message_id: "str" = None,
        data: "str" = None,
        game_short_name: "str" = None,
    ):
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name


class ForceReply(Type_):
    def __init__(
        self,
        input_field_placeholder: "str" = None,
        selective: "bool" = None,
    ):
        self.force_reply = True
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective


class ChatPhoto(Type_):
    def __init__(
        self,
        small_file_id: "str",
        small_file_unique_id: "str",
        big_file_id: "str",
        big_file_unique_id: "str",
    ):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id


class ChatInviteLink(Type_):
    def __init__(
        self,
        invite_link: "str",
        creator: "User",
        creates_join_request: "bool",
        is_primary: "bool",
        is_revoked: "bool",
        name: "str" = None,
        expire_date: "int" = None,
        member_limit: "int" = None,
        pending_join_request_count: "int" = None,
    ):
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count


class ChatAdministratorRights(Type_):
    def __init__(
        self,
        is_anonymous: "bool",
        can_manage_chat: "bool",
        can_delete_messages: "bool",
        can_manage_video_chats: "bool",
        can_restrict_members: "bool",
        can_promote_members: "bool",
        can_change_info: "bool",
        can_invite_users: "bool",
        can_post_stories: "bool",
        can_edit_stories: "bool",
        can_delete_stories: "bool",
        can_post_messages: "bool" = None,
        can_edit_messages: "bool" = None,
        can_pin_messages: "bool" = None,
        can_manage_topics: "bool" = None,
    ):
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


class ChatMemberUpdated(Type_):
    def __init__(
        self,
        chat: "Chat",
        from_user: "User",
        date: "int",
        old_chat_member: "ChatMember",
        new_chat_member: "ChatMember",
        invite_link: "ChatInviteLink" = None,
        via_join_request: "bool" = None,
        via_chat_folder_invite_link: "bool" = None,
    ):
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_join_request = via_join_request
        self.via_chat_folder_invite_link = via_chat_folder_invite_link


class ChatMember(Type_):
    def __init__(
        self,
        status: "str",
        user: "User",
        is_anonymous: "bool",
        custom_title: "str" = None,
    ):
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title


class ChatMemberOwner(Type_):
    def __init__(
        self,
        status: "str",
        user: "User",
        is_anonymous: "bool",
        custom_title: "str" = None,
    ):
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title


class ChatMemberAdministrator(Type_):
    def __init__(
        self,
        status: "str",
        user: "User",
        can_be_edited: "bool",
        is_anonymous: "bool",
        can_manage_chat: "bool",
        can_delete_messages: "bool",
        can_manage_video_chats: "bool",
        can_restrict_members: "bool",
        can_promote_members: "bool",
        can_change_info: "bool",
        can_invite_users: "bool",
        can_post_stories: "bool",
        can_edit_stories: "bool",
        can_delete_stories: "bool",
        can_post_messages: "bool" = None,
        can_edit_messages: "bool" = None,
        can_pin_messages: "bool" = None,
        can_manage_topics: "bool" = None,
        custom_title: "str" = None,
    ):
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


class ChatMemberMember(Type_):
    def __init__(self, status: "str", user: "User"):
        self.status = status
        self.user = user


class ChatMemberRestricted(Type_):
    def __init__(
        self,
        status: "str",
        user: "User",
        is_member: "bool",
        can_send_messages: "bool",
        can_send_audios: "bool",
        can_send_documents: "bool",
        can_send_photos: "bool",
        can_send_videos: "bool",
        can_send_video_notes: "bool",
        can_send_voice_notes: "bool",
        can_send_polls: "bool",
        can_send_other_messages: "bool",
        can_add_web_page_previews: "bool",
        can_change_info: "bool",
        can_invite_users: "bool",
        can_pin_messages: "bool",
        can_manage_topics: "bool",
        until_date: "int",
    ):
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


class ChatMemberLeft(Type_):
    def __init__(self, status: "str", user: "User"):
        self.status = status
        self.user = user


class ChatMemberBanned(Type_):
    def __init__(self, status: "str", user: "User", until_date: "int"):
        self.status = status
        self.user = user
        self.until_date = until_date


class ChatJoinRequest(Type_):
    def __init__(
        self,
        chat: "Chat",
        from_user: "User",
        user_chat_id: "int",
        date: "int",
        bio: "str" = None,
        invite_link: "ChatInviteLink" = None,
    ):
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link


class ChatPermissions(Type_):
    def __init__(
        self,
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
    ):
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


class Birthdate(Type_):
    def __init__(self, day: "int", month: "int", year: "int" = None):
        self.day = day
        self.month = month
        self.year = year


class BusinessIntro(Type_):
    def __init__(
        self, title: "str" = None, message: "str" = None, sticker: "Sticker" = None
    ):
        self.title = title
        self.message = message
        self.sticker = sticker


class BusinessLocation(Type_):
    def __init__(self, address: "str", location: "Location" = None):
        self.address = address
        self.location = location


class BusinessOpeningHoursInterval(Type_):
    def __init__(self, opening_minute: "int", closing_minute: "int"):
        self.opening_minute = opening_minute
        self.closing_minute = closing_minute


class BusinessOpeningHours(Type_):
    def __init__(
        self, time_zone_name: "str", opening_hours: List["BusinessOpeningHoursInterval"]
    ):
        self.time_zone_name = time_zone_name
        self.opening_hours = opening_hours


class ChatLocation(Type_):
    def __init__(self, location: "Location", address: "str"):
        self.location = location
        self.address = address


class ReactionType(Type_):
    def __init__(self, type: "str", emoji: "str"):
        self.type = type
        self.emoji = emoji


class ReactionTypeEmoji(Type_):
    def __init__(self, type: "str", emoji: "str"):
        self.type = type
        self.emoji = emoji


class ReactionTypeCustomEmoji(Type_):
    def __init__(self, type: "str", custom_emoji_id: "str"):
        self.type = type
        self.custom_emoji_id = custom_emoji_id


class ReactionCount(Type_):
    def __init__(self, type: "ReactionType", total_count: "int"):
        self.type = type
        self.total_count = total_count


class MessageReactionUpdated(Type_):
    def __init__(
        self,
        chat: "Chat",
        message_id: "int",
        date: "int",
        old_reaction: List["ReactionType"],
        new_reaction: List["ReactionType"],
        user: "User" = None,
        actor_chat: "Chat" = None,
    ):
        self.chat = chat
        self.message_id = message_id
        self.user = user
        self.actor_chat = actor_chat
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction


class MessageReactionCountUpdated(Type_):
    def __init__(
        self,
        chat: "Chat",
        message_id: "int",
        date: "int",
        reactions: List["ReactionCount"],
    ):
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions


class ForumTopic(Type_):
    def __init__(
        self,
        message_thread_id: "int",
        name: "str",
        icon_color: "int",
        icon_custom_emoji_id: "str" = None,
    ):
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id


class BotCommand(Type_):
    def __init__(self, command: "str", description: "str"):
        self.command = command
        self.description = description


class BotCommandScope(Type_):
    def __init__(self, type: "str"):
        self.type = type


class BotCommandScopeDefault(Type_):
    def __init__(self, type: "str"):
        self.type = type


class BotCommandScopeAllPrivateChats(Type_):
    def __init__(self, type: "str"):
        self.type = type


class BotCommandScopeAllGroupChats(Type_):
    def __init__(self, type: "str"):
        self.type = type


class BotCommandScopeAllChatAdministrators(Type_):
    def __init__(self, type: "str"):
        self.type = type


class BotCommandScopeChat(Type_):
    def __init__(self, type: "str", chat_id: Union["int", "str"]):
        self.type = type
        self.chat_id = chat_id


class BotCommandScopeChatAdministrators(Type_):
    def __init__(self, type: "str", chat_id: Union["int", "str"]):
        self.type = type
        self.chat_id = chat_id


class BotCommandScopeChatMember(Type_):
    def __init__(self, type: "str", chat_id: Union["int", "str"], user_id: "int"):
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id


class BotName(Type_):
    def __init__(self, name: "str"):
        self.name = name


class BotDescription(Type_):
    def __init__(self, description: "str"):
        self.description = description


class BotShortDescription(Type_):
    def __init__(self, short_description: "str"):
        self.short_description = short_description


class MenuButton(Type_):
    def __init__(self, type: "str"):
        self.type = type


class MenuButtonCommands(Type_):
    def __init__(self, type: "str"):
        self.type = type


class MenuButtonWebApp(Type_):
    def __init__(self, type: "str", text: "str", web_app: "WebAppInfo"):
        self.type = type
        self.text = text
        self.web_app = web_app


class MenuButtonDefault(Type_):
    def __init__(self, type: "str"):
        self.type = type


class ChatBoostSource(Type_):
    def __init__(self, source: "str", user: "User"):
        self.source = source
        self.user = user


class ChatBoostSourcePremium(Type_):
    def __init__(self, source: "str", user: "User"):
        self.source = source
        self.user = user


class ChatBoostSourceGiftCode(Type_):
    def __init__(self, source: "str", user: "User"):
        self.source = source
        self.user = user


class ChatBoostSourceGiveaway(Type_):
    def __init__(
        self,
        source: "str",
        giveaway_message_id: "int",
        user: "User" = None,
        is_unclaimed: "bool" = None,
    ):
        self.source = source
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.is_unclaimed = is_unclaimed


class ChatBoost(Type_):
    def __init__(
        self,
        boost_id: "str",
        add_date: "int",
        expiration_date: "int",
        source: "ChatBoostSource",
    ):
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source


class ChatBoostUpdated(Type_):
    def __init__(self, chat: "Chat", boost: "ChatBoost"):
        self.chat = chat
        self.boost = boost


class ChatBoostRemoved(Type_):
    def __init__(
        self,
        chat: "Chat",
        boost_id: "str",
        remove_date: "int",
        source: "ChatBoostSource",
    ):
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source


class UserChatBoosts(Type_):
    def __init__(self, boosts: List["ChatBoost"]):
        self.boosts = boosts


class BusinessConnection(Type_):
    def __init__(
        self,
        id: "str",
        user: "User",
        user_chat_id: "int",
        date: "int",
        can_reply: "bool",
        is_enabled: "bool",
    ):
        self.id = id
        self.user = user
        self.user_chat_id = user_chat_id
        self.date = date
        self.can_reply = can_reply
        self.is_enabled = is_enabled


class BusinessMessagesDeleted(Type_):
    def __init__(
        self, business_connection_id: "str", chat: "Chat", message_ids: List["int"]
    ):
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.message_ids = message_ids


class ResponseParameters(Type_):
    def __init__(self, migrate_to_chat_id: "int" = None, retry_after: "int" = None):
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after


class InputMedia(Type_):
    def __init__(
        self,
        type: "str",
        media: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        has_spoiler: "bool" = None,
    ):
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler


class InputMediaPhoto(Type_):
    def __init__(
        self,
        media: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        has_spoiler: "bool" = None,
    ):
        self.type = "photo"
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler


class InputMediaVideo(Type_):
    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        supports_streaming: "bool" = None,
        has_spoiler: "bool" = None,
    ):
        self.type = "video"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler


class InputMediaAnimation(Type_):
    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        width: "int" = None,
        height: "int" = None,
        duration: "int" = None,
        has_spoiler: "bool" = None,
    ):
        self.type = "animation"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.has_spoiler = has_spoiler


class InputMediaAudio(Type_):
    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        duration: "int" = None,
        performer: "str" = None,
        title: "str" = None,
    ):
        self.type = "audio"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title


class InputMediaDocument(Type_):
    def __init__(
        self,
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        disable_content_type_detection: "bool" = None,
    ):
        self.type = "document"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection


class InputFile(Type_):
    def __init__(
        self,
        chat_id: Union["int", "str"],
        text: "str",
        business_connection_id: "str" = None,
        message_thread_id: "int" = None,
        parse_mode: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
        disable_notification: "bool" = None,
        protect_content: "bool" = None,
        message_effect_id: "str" = None,
        reply_parameters: "ReplyParameters" = None,
        reply_markup: ReplyMarkup = None,
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.message_effect_id = message_effect_id
        self.reply_parameters = reply_parameters
        self.reply_markup = reply_markup


class Sticker(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        type: "str",
        width: "int",
        height: "int",
        is_animated: "bool",
        is_video: "bool",
        thumbnail: "PhotoSize" = None,
        emoji: "str" = None,
        set_name: "str" = None,
        premium_animation: "File" = None,
        mask_position: "MaskPosition" = None,
        custom_emoji_id: "str" = None,
        needs_repainting: "bool" = None,
        file_size: "int" = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.custom_emoji_id = custom_emoji_id
        self.needs_repainting = needs_repainting
        self.file_size = file_size


class StickerSet(Type_):
    def __init__(
        self,
        name: "str",
        title: "str",
        sticker_type: "str",
        stickers: List["Sticker"],
        thumbnail: "PhotoSize" = None,
    ):
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.stickers = stickers
        self.thumbnail = thumbnail


class MaskPosition(Type_):
    def __init__(
        self, point: "str", x_shift: "float", y_shift: "float", scale: "float"
    ):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale


class InputSticker(Type_):
    def __init__(
        self,
        sticker: Union["InputFile", "str"],
        format: "str",
        emoji_list: List["str"],
        mask_position: "MaskPosition" = None,
        keywords: List["str"] = None,
    ):
        self.sticker = sticker
        self.format = format
        self.emoji_list = emoji_list
        self.mask_position = mask_position
        self.keywords = keywords


class InlineQuery(Type_):
    def __init__(
        self,
        id: "str",
        from_user: "User",
        query: "str",
        offset: "str",
        chat_type: "str" = None,
        location: "Location" = None,
    ):
        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location


class InlineQueryResultsButton(Type_):
    def __init__(
        self, text: "str", web_app: "WebAppInfo" = None, start_parameter: "str" = None
    ):
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter


class InlineQueryResult(Type_):
    def __init__(
        self,
        id: "str",
        title: "str",
        input_message_content: "InputMessageContent",
        reply_markup: "InlineKeyboardMarkup" = None,
        url: "str" = None,
        hide_url: "bool" = None,
        description: "str" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
    ):
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultArticle(Type_):
    def __init__(
        self,
        id: "str",
        title: "str",
        input_message_content: "InputMessageContent",
        reply_markup: "InlineKeyboardMarkup" = None,
        url: "str" = None,
        hide_url: "bool" = None,
        description: "str" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
    ):
        self.type = "article"
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultPhoto(Type_):
    def __init__(
        self,
        id: "str",
        photo_url: "str",
        thumbnail_url: "str",
        photo_width: "int" = None,
        photo_height: "int" = None,
        title: "str" = None,
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "photo"
        self.id = id
        self.photo_url = photo_url
        self.thumbnail_url = thumbnail_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultGif(Type_):
    def __init__(
        self,
        id: "str",
        gif_url: "str",
        thumbnail_url: "str",
        gif_width: "int" = None,
        gif_height: "int" = None,
        gif_duration: "int" = None,
        thumbnail_mime_type: "str" = None,
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "gif"
        self.id = id
        self.gif_url = gif_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultMpeg4Gif(Type_):
    def __init__(
        self,
        id: "str",
        mpeg4_url: "str",
        thumbnail_url: "str",
        mpeg4_width: "int" = None,
        mpeg4_height: "int" = None,
        mpeg4_duration: "int" = None,
        thumbnail_mime_type: "str" = None,
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "gif"
        self.id = id
        self.mpeg4_url = mpeg4_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVideo(Type_):
    def __init__(
        self,
        id: "str",
        video_url: "str",
        mime_type: "str",
        thumbnail_url: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        video_width: "int" = None,
        video_height: "int" = None,
        video_duration: "int" = None,
        description: "str" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "video"
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultAudio(Type_):
    def __init__(
        self,
        id: "str",
        audio_url: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        performer: "str" = None,
        audio_duration: "int" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "audio"
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVoice(Type_):
    def __init__(
        self,
        id: "str",
        voice_url: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        voice_duration: "int" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "voice"
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultDocument(Type_):
    def __init__(
        self,
        id: "str",
        title: "str",
        document_url: "str",
        mime_type: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        description: "str" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
    ):
        self.type = "document"
        self.id = id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.document_url = document_url
        self.mime_type = mime_type
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultLocation(Type_):
    def __init__(
        self,
        id: "str",
        latitude: "float",
        longitude: "float",
        title: "str",
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
    ):
        self.type = "location"
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultVenue(Type_):
    def __init__(
        self,
        id: "str",
        latitude: "float",
        longitude: "float",
        title: "str",
        address: "str",
        foursquare_id: "str" = None,
        foursquare_type: "str" = None,
        google_place_id: "str" = None,
        google_place_type: "str" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
    ):
        self.type = "venue"
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultContact(Type_):
    def __init__(
        self,
        id: "str",
        phone_number: "str",
        first_name: "str",
        last_name: "str" = None,
        vcard: "str" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
    ):
        self.type = "contact"
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultGame(Type_):
    def __init__(
        self,
        id: "str",
        game_short_name: "str",
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self.type = "game"
        self.id = id
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup


class InlineQueryResultCachedPhoto(Type_):
    def __init__(
        self,
        id: "str",
        photo_file_id: "str",
        title: "str" = None,
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "photo"
        self.id = id
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedGif(Type_):
    def __init__(
        self,
        id: "str",
        gif_file_id: "str",
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "gif"
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedMpeg4Gif(Type_):
    def __init__(
        self,
        id: "str",
        mpeg4_file_id: "str",
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "gif"
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedSticker(Type_):
    def __init__(
        self,
        id: "str",
        sticker_file_id: "str",
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "sticker"
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedDocument(Type_):
    def __init__(
        self,
        id: "str",
        title: "str",
        document_file_id: "str",
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "document"
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVideo(Type_):
    def __init__(
        self,
        id: "str",
        video_file_id: "str",
        title: "str",
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "video"
        self.id = id
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVoice(Type_):
    def __init__(
        self,
        id: "str",
        voice_file_id: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "voice"
        self.id = id
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedAudio(Type_):
    def __init__(
        self,
        id: "str",
        audio_file_id: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
    ):
        self.type = "audio"
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InputMessageContent(Type_):
    def __init__(
        self,
        message_text: "str",
        parse_mode: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
    ):
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options


class InputTextMessageContent(Type_):
    def __init__(
        self,
        message_text: "str",
        parse_mode: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
    ):
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options


class InputLocationMessageContent(Type_):
    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


class InputVenueMessageContent(Type_):
    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        title: "str",
        address: "str",
        foursquare_id: "str" = None,
        foursquare_type: "str" = None,
        google_place_id: "str" = None,
        google_place_type: "str" = None,
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type


class InputContactMessageContent(Type_):
    def __init__(
        self,
        phone_number: "str",
        first_name: "str",
        last_name: "str" = None,
        vcard: "str" = None,
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard


class InputInvoiceMessageContent(Type_):
    def __init__(
        self,
        title: "str",
        description: "str",
        payload: "str",
        currency: "str",
        prices: List["LabeledPrice"],
        provider_token: "str" = None,
        max_tip_amount: "int" = None,
        suggested_tip_amounts: List["int"] = None,
        provider_data: "str" = None,
        photo_url: "str" = None,
        photo_size: "int" = None,
        photo_width: "int" = None,
        photo_height: "int" = None,
        need_name: "bool" = None,
        need_phone_number: "bool" = None,
        need_email: "bool" = None,
        need_shipping_address: "bool" = None,
        send_phone_number_to_provider: "bool" = None,
        send_email_to_provider: "bool" = None,
        is_flexible: "bool" = None,
    ):
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible


class ChosenInlineResult(Type_):
    def __init__(
        self,
        result_id: "str",
        from_user: "User",
        query: "str",
        location: "Location" = None,
        inline_message_id: "str" = None,
    ):
        self.result_id = result_id
        self.from_user = from_user
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query


class SentWebAppMessage(Type_):
    def __init__(self, inline_message_id: "str" = None):
        self.inline_message_id = inline_message_id


class LabeledPrice(Type_):
    def __init__(self, label: "str", amount: "int"):
        self.label = label
        self.amount = amount


class Invoice(Type_):
    def __init__(
        self,
        title: "str",
        description: "str",
        start_parameter: "str",
        currency: "str",
        total_amount: "int",
    ):
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount


class ShippingAddress(Type_):
    def __init__(
        self,
        country_code: "str",
        state: "str",
        city: "str",
        street_line1: "str",
        street_line2: "str",
        post_code: "str",
    ):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code


class OrderInfo(Type_):
    def __init__(
        self,
        name: "str" = None,
        phone_number: "str" = None,
        email: "str" = None,
        shipping_address: "ShippingAddress" = None,
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address


class ShippingOption(Type_):
    def __init__(self, id: "str", title: "str", prices: List["LabeledPrice"]):
        self.id = id
        self.title = title
        self.prices = prices


class SuccessfulPayment(Type_):
    def __init__(
        self,
        currency: "str",
        total_amount: "int",
        invoice_payload: "str",
        telegram_payment_charge_id: "str",
        provider_payment_charge_id: "str",
        shipping_option_id: "str" = None,
        order_info: "OrderInfo" = None,
    ):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id


class ShippingQuery(Type_):
    def __init__(
        self,
        id: "str",
        from_user: "User",
        invoice_payload: "str",
        shipping_address: "ShippingAddress",
    ):
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address


class PreCheckoutQuery(Type_):
    def __init__(
        self,
        id: "str",
        from_user: "User",
        currency: "str",
        total_amount: "int",
        invoice_payload: "str",
        shipping_option_id: "str" = None,
        order_info: "OrderInfo" = None,
    ):
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info


class PassportData(Type_):
    def __init__(
        self,
        data: List["EncryptedPassportElement"],
        credentials: "EncryptedCredentials",
    ):
        self.data = data
        self.credentials = credentials


class PassportFile(Type_):
    def __init__(
        self, file_id: "str", file_unique_id: "str", file_size: "int", file_date: "int"
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date


class EncryptedPassportElement(Type_):
    def __init__(
        self,
        type: "str",
        hash: "str",
        data: "str" = None,
        phone_number: "str" = None,
        email: "str" = None,
        files: List["PassportFile"] = None,
        front_side: "PassportFile" = None,
        reverse_side: "PassportFile" = None,
        selfie: "PassportFile" = None,
        translation: List["PassportFile"] = None,
    ):
        self.type = type
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.hash = hash


class EncryptedCredentials(Type_):
    def __init__(self, data: "str", hash: "str", secret: "str"):
        self.data = data
        self.hash = hash
        self.secret = secret


class PassportElementError(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        field_name: "str",
        data_hash: "str",
        message: "str",
    ):
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message


class PassportElementErrorDataField(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        field_name: "str",
        data_hash: "str",
        message: "str",
    ):
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message


class PassportElementErrorFrontSide(Type_):
    def __init__(self, source: "str", type: "str", file_hash: "str", message: "str"):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorReverseSide(Type_):
    def __init__(self, source: "str", type: "str", file_hash: "str", message: "str"):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorSelfie(Type_):
    def __init__(self, source: "str", type: "str", file_hash: "str", message: "str"):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorFile(Type_):
    def __init__(self, source: "str", type: "str", file_hash: "str", message: "str"):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorFiles(Type_):
    def __init__(
        self, source: "str", type: "str", file_hashes: List["str"], message: "str"
    ):
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message


class PassportElementErrorTranslationFile(Type_):
    def __init__(self, source: "str", type: "str", file_hash: "str", message: "str"):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorTranslationFiles(Type_):
    def __init__(
        self, source: "str", type: "str", file_hashes: List["str"], message: "str"
    ):
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message


class PassportElementErrorUnspecified(Type_):
    def __init__(self, source: "str", type: "str", element_hash: "str", message: "str"):
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message


class Game(Type_):
    def __init__(
        self,
        title: "str",
        description: "str",
        photo: List["PhotoSize"],
        text: "str" = None,
        text_entities: List["MessageEntity"] = None,
        animation: "Animation" = None,
    ):
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation


class CallbackGame(Type_):
    def __init__(
        self,
        user_id: "int",
        score: "int",
        force: "bool" = None,
        disable_edit_message: "bool" = None,
        chat_id: "int" = None,
        message_id: "int" = None,
        inline_message_id: "str" = None,
    ):
        self.user_id = user_id
        self.score = score
        self.force = force
        self.disable_edit_message = disable_edit_message
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id


class GameHighScore(Type_):
    def __init__(self, position: "int", user: "User", score: "int"):
        self.position = position
        self.user = user
        self.score = score
