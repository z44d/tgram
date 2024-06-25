import tgram
from typing import List, Optional, Union


class Type_:
    def __init__(self, client: "tgram.TgBot") -> None:
        self._client = client

    def __str__(self) -> str:
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Update" | None:
        return (
            Update(
                client=client,
                update_id=d.get("update_id"),
                message=Message._parse(d.get("message")),
                edited_message=Message._parse(d.get("edited_message")),
                channel_post=Message._parse(d.get("channel_post")),
                edited_channel_post=Message._parse(d.get("edited_channel_post")),
                business_connection=BusinessConnection._parse(
                    d.get("business_connection")
                ),
                business_message=Message._parse(d.get("business_message")),
                edited_business_message=Message._parse(
                    d.get("edited_business_message")
                ),
                deleted_business_messages=BusinessMessagesDeleted._parse(
                    d.get("deleted_business_messages")
                ),
                message_reaction=MessageReactionUpdated._parse(
                    d.get("message_reaction")
                ),
                message_reaction_count=MessageReactionCountUpdated._parse(
                    d.get("message_reaction_count")
                ),
                inline_query=InlineQuery._parse(d.get("inline_query")),
                chosen_inline_result=ChosenInlineResult._parse(
                    d.get("chosen_inline_result")
                ),
                callback_query=CallbackQuery._parse(d.get("callback_query")),
                shipping_query=ShippingQuery._parse(d.get("shipping_query")),
                pre_checkout_query=PreCheckoutQuery._parse(d.get("pre_checkout_query")),
                poll=Poll._parse(d.get("poll")),
                poll_answer=PollAnswer._parse(d.get("poll_answer")),
                my_chat_member=ChatMemberUpdated._parse(d.get("my_chat_member")),
                chat_member=ChatMemberUpdated._parse(d.get("chat_member")),
                chat_join_request=ChatJoinRequest._parse(d.get("chat_join_request")),
                chat_boost=ChatBoostUpdated._parse(d.get("chat_boost")),
                removed_chat_boost=ChatBoostRemoved._parse(d.get("removed_chat_boost")),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.last_synchronization_error_date = last_synchronization_error_date
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "WebhookInfo" | None:
        return (
            WebhookInfo(
                client=client,
                url=d.get("url"),
                has_custom_certificate=d.get("has_custom_certificate"),
                pending_update_count=d.get("pending_update_count"),
                ip_address=d.get("ip_address"),
                last_error_date=d.get("last_error_date"),
                last_error_message=d.get("last_error_message"),
                last_synchronization_error_date=d.get(
                    "last_synchronization_error_date"
                ),
                max_connections=d.get("max_connections"),
                allowed_updates=[str._parse(i) for i in d.get("allowed_updates")]
                if d.get("allowed_updates", None)
                else None,
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "User" | None:
        return (
            User(
                client=client,
                id=d.get("id"),
                is_bot=d.get("is_bot"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                language_code=d.get("language_code"),
                is_premium=d.get("is_premium"),
                added_to_attachment_menu=d.get("added_to_attachment_menu"),
                can_join_groups=d.get("can_join_groups"),
                can_read_all_group_messages=d.get("can_read_all_group_messages"),
                supports_inline_queries=d.get("supports_inline_queries"),
                can_connect_to_business=d.get("can_connect_to_business"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Chat" | None:
        return (
            Chat(
                client=client,
                id=d.get("id"),
                type=d.get("type"),
                title=d.get("title"),
                username=d.get("username"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                is_forum=d.get("is_forum"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatFullInfo" | None:
        return (
            ChatFullInfo(
                client=client,
                id=d.get("id"),
                type=d.get("type"),
                accent_color_id=d.get("accent_color_id"),
                max_reaction_count=d.get("max_reaction_count"),
                title=d.get("title"),
                username=d.get("username"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                is_forum=d.get("is_forum"),
                photo=ChatPhoto._parse(d.get("photo")),
                active_usernames=[str._parse(i) for i in d.get("active_usernames")]
                if d.get("active_usernames", None)
                else None,
                birthdate=Birthdate._parse(d.get("birthdate")),
                business_intro=BusinessIntro._parse(d.get("business_intro")),
                business_location=BusinessLocation._parse(d.get("business_location")),
                business_opening_hours=BusinessOpeningHours._parse(
                    d.get("business_opening_hours")
                ),
                personal_chat=Chat._parse(d.get("personal_chat")),
                available_reactions=[
                    ReactionType._parse(i) for i in d.get("available_reactions")
                ]
                if d.get("available_reactions", None)
                else None,
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
                pinned_message=Message._parse(d.get("pinned_message")),
                permissions=ChatPermissions._parse(d.get("permissions")),
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
                location=ChatLocation._parse(d.get("location")),
            )
            if d
            else None
        )


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
        reply_markup: "InlineKeyboardMarkup" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Message" | None:
        return (
            Message(
                client=client,
                message_id=d.get("message_id"),
                date=d.get("date"),
                chat=Chat._parse(d.get("chat")),
                message_thread_id=d.get("message_thread_id"),
                from_user=User._parse(d.get("from")),
                sender_chat=Chat._parse(d.get("sender_chat")),
                sender_boost_count=d.get("sender_boost_count"),
                sender_business_bot=User._parse(d.get("sender_business_bot")),
                business_connection_id=d.get("business_connection_id"),
                forward_origin=MessageOrigin._parse(d.get("forward_origin")),
                is_topic_message=d.get("is_topic_message"),
                is_automatic_forward=d.get("is_automatic_forward"),
                reply_to_message=Message._parse(d.get("reply_to_message")),
                external_reply=ExternalReplyInfo._parse(d.get("external_reply")),
                quote=TextQuote._parse(d.get("quote")),
                reply_to_story=Story._parse(d.get("reply_to_story")),
                via_bot=User._parse(d.get("via_bot")),
                edit_date=d.get("edit_date"),
                has_protected_content=d.get("has_protected_content"),
                is_from_offline=d.get("is_from_offline"),
                media_group_id=d.get("media_group_id"),
                author_signature=d.get("author_signature"),
                text=d.get("text"),
                entities=[MessageEntity._parse(i) for i in d.get("entities")]
                if d.get("entities", None)
                else None,
                link_preview_options=LinkPreviewOptions._parse(
                    d.get("link_preview_options")
                ),
                effect_id=d.get("effect_id"),
                animation=Animation._parse(d.get("animation")),
                audio=Audio._parse(d.get("audio")),
                document=Document._parse(d.get("document")),
                photo=[PhotoSize._parse(i) for i in d.get("photo")]
                if d.get("photo", None)
                else None,
                sticker=Sticker._parse(d.get("sticker")),
                story=Story._parse(d.get("story")),
                video=Video._parse(d.get("video")),
                video_note=VideoNote._parse(d.get("video_note")),
                voice=Voice._parse(d.get("voice")),
                caption=d.get("caption"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                has_media_spoiler=d.get("has_media_spoiler"),
                contact=Contact._parse(d.get("contact")),
                dice=Dice._parse(d.get("dice")),
                game=Game._parse(d.get("game")),
                poll=Poll._parse(d.get("poll")),
                venue=Venue._parse(d.get("venue")),
                location=Location._parse(d.get("location")),
                new_chat_members=[User._parse(i) for i in d.get("new_chat_members")]
                if d.get("new_chat_members", None)
                else None,
                left_chat_member=User._parse(d.get("left_chat_member")),
                new_chat_title=d.get("new_chat_title"),
                new_chat_photo=[PhotoSize._parse(i) for i in d.get("new_chat_photo")]
                if d.get("new_chat_photo", None)
                else None,
                delete_chat_photo=d.get("delete_chat_photo"),
                group_chat_created=d.get("group_chat_created"),
                supergroup_chat_created=d.get("supergroup_chat_created"),
                channel_chat_created=d.get("channel_chat_created"),
                message_auto_delete_timer_changed=MessageAutoDeleteTimerChanged._parse(
                    d.get("message_auto_delete_timer_changed")
                ),
                migrate_to_chat_id=d.get("migrate_to_chat_id"),
                migrate_from_chat_id=d.get("migrate_from_chat_id"),
                pinned_message=MaybeInaccessibleMessage._parse(d.get("pinned_message")),
                invoice=Invoice._parse(d.get("invoice")),
                successful_payment=SuccessfulPayment._parse(
                    d.get("successful_payment")
                ),
                users_shared=UsersShared._parse(d.get("users_shared")),
                chat_shared=ChatShared._parse(d.get("chat_shared")),
                connected_website=d.get("connected_website"),
                write_access_allowed=WriteAccessAllowed._parse(
                    d.get("write_access_allowed")
                ),
                passport_data=PassportData._parse(d.get("passport_data")),
                proximity_alert_triggered=ProximityAlertTriggered._parse(
                    d.get("proximity_alert_triggered")
                ),
                boost_added=ChatBoostAdded._parse(d.get("boost_added")),
                chat_background_set=ChatBackground._parse(d.get("chat_background_set")),
                forum_topic_created=ForumTopicCreated._parse(
                    d.get("forum_topic_created")
                ),
                forum_topic_edited=ForumTopicEdited._parse(d.get("forum_topic_edited")),
                forum_topic_closed=ForumTopicClosed._parse(d.get("forum_topic_closed")),
                forum_topic_reopened=ForumTopicReopened._parse(
                    d.get("forum_topic_reopened")
                ),
                general_forum_topic_hidden=GeneralForumTopicHidden._parse(
                    d.get("general_forum_topic_hidden")
                ),
                general_forum_topic_unhidden=GeneralForumTopicUnhidden._parse(
                    d.get("general_forum_topic_unhidden")
                ),
                giveaway_created=GiveawayCreated._parse(d.get("giveaway_created")),
                giveaway=Giveaway._parse(d.get("giveaway")),
                giveaway_winners=GiveawayWinners._parse(d.get("giveaway_winners")),
                giveaway_completed=GiveawayCompleted._parse(
                    d.get("giveaway_completed")
                ),
                video_chat_scheduled=VideoChatScheduled._parse(
                    d.get("video_chat_scheduled")
                ),
                video_chat_started=VideoChatStarted._parse(d.get("video_chat_started")),
                video_chat_ended=VideoChatEnded._parse(d.get("video_chat_ended")),
                video_chat_participants_invited=VideoChatParticipantsInvited._parse(
                    d.get("video_chat_participants_invited")
                ),
                web_app_data=WebAppData._parse(d.get("web_app_data")),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
            )
            if d
            else None
        )


class MessageId(Type_):
    def __init__(self, message_id: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.message_id = message_id

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "MessageId" | None:
        return (
            MessageId(
                client=client,
                message_id=d.get("message_id"),
            )
            if d
            else None
        )


class InaccessibleMessage(Type_):
    def __init__(
        self, chat: "Chat", message_id: "int", date: "int", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.chat = chat
        self.message_id = message_id
        self.date = date

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InaccessibleMessage" | None:
        return (
            InaccessibleMessage(
                client=client,
                chat=Chat._parse(d.get("chat")),
                message_id=d.get("message_id"),
                date=d.get("date"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MaybeInaccessibleMessage" | None:
        return (
            MaybeInaccessibleMessage(
                client=client,
                type=d.get("type"),
                offset=d.get("offset"),
                length=d.get("length"),
                url=d.get("url"),
                user=User._parse(d.get("user")),
                language=d.get("language"),
                custom_emoji_id=d.get("custom_emoji_id"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "MessageEntity" | None:
        return (
            MessageEntity(
                client=client,
                type=d.get("type"),
                offset=d.get("offset"),
                length=d.get("length"),
                url=d.get("url"),
                user=User._parse(d.get("user")),
                language=d.get("language"),
                custom_emoji_id=d.get("custom_emoji_id"),
            )
            if d
            else None
        )


class TextQuote(Type_):
    def __init__(
        self,
        text: "str",
        position: "int",
        entities: List["MessageEntity"] = None,
        is_manual: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.text = text
        self.entities = entities
        self.position = position
        self.is_manual = is_manual

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "TextQuote" | None:
        return (
            TextQuote(
                client=client,
                text=d.get("text"),
                position=d.get("position"),
                entities=[MessageEntity._parse(i) for i in d.get("entities")]
                if d.get("entities", None)
                else None,
                is_manual=d.get("is_manual"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ExternalReplyInfo" | None:
        return (
            ExternalReplyInfo(
                client=client,
                origin=MessageOrigin._parse(d.get("origin")),
                chat=Chat._parse(d.get("chat")),
                message_id=d.get("message_id"),
                link_preview_options=LinkPreviewOptions._parse(
                    d.get("link_preview_options")
                ),
                animation=Animation._parse(d.get("animation")),
                audio=Audio._parse(d.get("audio")),
                document=Document._parse(d.get("document")),
                photo=[PhotoSize._parse(i) for i in d.get("photo")]
                if d.get("photo", None)
                else None,
                sticker=Sticker._parse(d.get("sticker")),
                story=Story._parse(d.get("story")),
                video=Video._parse(d.get("video")),
                video_note=VideoNote._parse(d.get("video_note")),
                voice=Voice._parse(d.get("voice")),
                has_media_spoiler=d.get("has_media_spoiler"),
                contact=Contact._parse(d.get("contact")),
                dice=Dice._parse(d.get("dice")),
                game=Game._parse(d.get("game")),
                giveaway=Giveaway._parse(d.get("giveaway")),
                giveaway_winners=GiveawayWinners._parse(d.get("giveaway_winners")),
                invoice=Invoice._parse(d.get("invoice")),
                location=Location._parse(d.get("location")),
                poll=Poll._parse(d.get("poll")),
                venue=Venue._parse(d.get("venue")),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities
        self.quote_position = quote_position

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ReplyParameters" | None:
        return (
            ReplyParameters(
                client=client,
                message_id=d.get("message_id"),
                chat_id=d.get("chat_id"),
                allow_sending_without_reply=d.get("allow_sending_without_reply"),
                quote=d.get("quote"),
                quote_parse_mode=d.get("quote_parse_mode"),
                quote_entities=[
                    MessageEntity._parse(i) for i in d.get("quote_entities")
                ]
                if d.get("quote_entities", None)
                else None,
                quote_position=d.get("quote_position"),
            )
            if d
            else None
        )


class MessageOrigin(Type_):
    def __init__(
        self,
        type: "str",
        date: "int",
        sender_user: "User",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.date = date
        self.sender_user = sender_user

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "MessageOrigin" | None:
        return (
            MessageOrigin(
                client=client,
                type=d.get("type"),
                date=d.get("date"),
                sender_user=User._parse(d.get("sender_user")),
            )
            if d
            else None
        )


class MessageOriginUser(Type_):
    def __init__(
        self,
        type: "str",
        date: "int",
        sender_user: "User",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.date = date
        self.sender_user = sender_user

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MessageOriginUser" | None:
        return (
            MessageOriginUser(
                client=client,
                type=d.get("type"),
                date=d.get("date"),
                sender_user=User._parse(d.get("sender_user")),
            )
            if d
            else None
        )


class MessageOriginHiddenUser(Type_):
    def __init__(
        self,
        type: "str",
        date: "int",
        sender_user_name: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.date = date
        self.sender_user_name = sender_user_name

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MessageOriginHiddenUser" | None:
        return (
            MessageOriginHiddenUser(
                client=client,
                type=d.get("type"),
                date=d.get("date"),
                sender_user_name=d.get("sender_user_name"),
            )
            if d
            else None
        )


class MessageOriginChat(Type_):
    def __init__(
        self,
        type: "str",
        date: "int",
        sender_chat: "Chat",
        author_signature: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.date = date
        self.sender_chat = sender_chat
        self.author_signature = author_signature

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MessageOriginChat" | None:
        return (
            MessageOriginChat(
                client=client,
                type=d.get("type"),
                date=d.get("date"),
                sender_chat=Chat._parse(d.get("sender_chat")),
                author_signature=d.get("author_signature"),
            )
            if d
            else None
        )


class MessageOriginChannel(Type_):
    def __init__(
        self,
        type: "str",
        date: "int",
        chat: "Chat",
        message_id: "int",
        author_signature: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.date = date
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MessageOriginChannel" | None:
        return (
            MessageOriginChannel(
                client=client,
                type=d.get("type"),
                date=d.get("date"),
                chat=Chat._parse(d.get("chat")),
                message_id=d.get("message_id"),
                author_signature=d.get("author_signature"),
            )
            if d
            else None
        )


class PhotoSize(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        width: "int",
        height: "int",
        file_size: "int" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "PhotoSize" | None:
        return (
            PhotoSize(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                file_size=d.get("file_size"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Animation" | None:
        return (
            Animation(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                thumbnail=PhotoSize._parse(d.get("thumbnail")),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Audio" | None:
        return (
            Audio(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                duration=d.get("duration"),
                performer=d.get("performer"),
                title=d.get("title"),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
                thumbnail=PhotoSize._parse(d.get("thumbnail")),
            )
            if d
            else None
        )


class Document(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        thumbnail: "PhotoSize" = None,
        file_name: "str" = None,
        mime_type: "str" = None,
        file_size: "int" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Document" | None:
        return (
            Document(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                thumbnail=PhotoSize._parse(d.get("thumbnail")),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d
            else None
        )


class Story(Type_):
    def __init__(self, chat: "Chat", id: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.chat = chat
        self.id = id

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Story" | None:
        return (
            Story(
                client=client,
                chat=Chat._parse(d.get("chat")),
                id=d.get("id"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Video" | None:
        return (
            Video(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                thumbnail=PhotoSize._parse(d.get("thumbnail")),
                file_name=d.get("file_name"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d
            else None
        )


class VideoNote(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        length: "int",
        duration: "int",
        thumbnail: "PhotoSize" = None,
        file_size: "int" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "VideoNote" | None:
        return (
            VideoNote(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                length=d.get("length"),
                duration=d.get("duration"),
                thumbnail=PhotoSize._parse(d.get("thumbnail")),
                file_size=d.get("file_size"),
            )
            if d
            else None
        )


class Voice(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        duration: "int",
        mime_type: "str" = None,
        file_size: "int" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Voice" | None:
        return (
            Voice(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                duration=d.get("duration"),
                mime_type=d.get("mime_type"),
                file_size=d.get("file_size"),
            )
            if d
            else None
        )


class Contact(Type_):
    def __init__(
        self,
        phone_number: "str",
        first_name: "str",
        last_name: "str" = None,
        user_id: "int" = None,
        vcard: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Contact" | None:
        return (
            Contact(
                client=client,
                phone_number=d.get("phone_number"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                user_id=d.get("user_id"),
                vcard=d.get("vcard"),
            )
            if d
            else None
        )


class Dice(Type_):
    def __init__(self, emoji: "str", value: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.emoji = emoji
        self.value = value

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Dice" | None:
        return (
            Dice(
                client=client,
                emoji=d.get("emoji"),
                value=d.get("value"),
            )
            if d
            else None
        )


class PollOption(Type_):
    def __init__(
        self,
        text: "str",
        voter_count: "int",
        text_entities: List["MessageEntity"] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.text = text
        self.text_entities = text_entities
        self.voter_count = voter_count

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "PollOption" | None:
        return (
            PollOption(
                client=client,
                text=d.get("text"),
                voter_count=d.get("voter_count"),
                text_entities=[MessageEntity._parse(i) for i in d.get("text_entities")]
                if d.get("text_entities", None)
                else None,
            )
            if d
            else None
        )


class InputPollOption(Type_):
    def __init__(
        self,
        text: "str",
        text_parse_mode: "str" = None,
        text_entities: List["MessageEntity"] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputPollOption" | None:
        return (
            InputPollOption(
                client=client,
                text=d.get("text"),
                text_parse_mode=d.get("text_parse_mode"),
                text_entities=[MessageEntity._parse(i) for i in d.get("text_entities")]
                if d.get("text_entities", None)
                else None,
            )
            if d
            else None
        )


class PollAnswer(Type_):
    def __init__(
        self,
        poll_id: "str",
        option_ids: List["int"],
        voter_chat: "Chat" = None,
        user: "User" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "PollAnswer" | None:
        return (
            PollAnswer(
                client=client,
                poll_id=d.get("poll_id"),
                option_ids=[int._parse(i) for i in d.get("option_ids")]
                if d.get("option_ids", None)
                else None,
                voter_chat=Chat._parse(d.get("voter_chat")),
                user=User._parse(d.get("user")),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Poll" | None:
        return (
            Poll(
                client=client,
                id=d.get("id"),
                question=d.get("question"),
                options=[PollOption._parse(i) for i in d.get("options")]
                if d.get("options", None)
                else None,
                total_voter_count=d.get("total_voter_count"),
                is_closed=d.get("is_closed"),
                is_anonymous=d.get("is_anonymous"),
                type=d.get("type"),
                allows_multiple_answers=d.get("allows_multiple_answers"),
                question_entities=[
                    MessageEntity._parse(i) for i in d.get("question_entities")
                ]
                if d.get("question_entities", None)
                else None,
                correct_option_id=d.get("correct_option_id"),
                explanation=d.get("explanation"),
                explanation_entities=[
                    MessageEntity._parse(i) for i in d.get("explanation_entities")
                ]
                if d.get("explanation_entities", None)
                else None,
                open_period=d.get("open_period"),
                close_date=d.get("close_date"),
            )
            if d
            else None
        )


class Location(Type_):
    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Location" | None:
        return (
            Location(
                client=client,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                horizontal_accuracy=d.get("horizontal_accuracy"),
                live_period=d.get("live_period"),
                heading=d.get("heading"),
                proximity_alert_radius=d.get("proximity_alert_radius"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Venue" | None:
        return (
            Venue(
                client=client,
                location=Location._parse(d.get("location")),
                title=d.get("title"),
                address=d.get("address"),
                foursquare_id=d.get("foursquare_id"),
                foursquare_type=d.get("foursquare_type"),
                google_place_id=d.get("google_place_id"),
                google_place_type=d.get("google_place_type"),
            )
            if d
            else None
        )


class WebAppData(Type_):
    def __init__(self, data: "str", button_text: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.data = data
        self.button_text = button_text

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "WebAppData" | None:
        return (
            WebAppData(
                client=client,
                data=d.get("data"),
                button_text=d.get("button_text"),
            )
            if d
            else None
        )


class ProximityAlertTriggered(Type_):
    def __init__(
        self,
        traveler: "User",
        watcher: "User",
        distance: "int",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ProximityAlertTriggered" | None:
        return (
            ProximityAlertTriggered(
                client=client,
                traveler=User._parse(d.get("traveler")),
                watcher=User._parse(d.get("watcher")),
                distance=d.get("distance"),
            )
            if d
            else None
        )


class MessageAutoDeleteTimerChanged(Type_):
    def __init__(self, message_auto_delete_time: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.message_auto_delete_time = message_auto_delete_time

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MessageAutoDeleteTimerChanged" | None:
        return (
            MessageAutoDeleteTimerChanged(
                client=client,
                message_auto_delete_time=d.get("message_auto_delete_time"),
            )
            if d
            else None
        )


class ChatBoostAdded(Type_):
    def __init__(self, boost_count: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.boost_count = boost_count

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatBoostAdded" | None:
        return (
            ChatBoostAdded(
                client=client,
                boost_count=d.get("boost_count"),
            )
            if d
            else None
        )


class BackgroundFill(Type_):
    def __init__(self, type: "str", color: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type
        self.color = color

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "BackgroundFill" | None:
        return (
            BackgroundFill(
                client=client,
                type=d.get("type"),
                color=d.get("color"),
            )
            if d
            else None
        )


class BackgroundFillSolid(Type_):
    def __init__(self, type: "str", color: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type
        self.color = color

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BackgroundFillSolid" | None:
        return (
            BackgroundFillSolid(
                client=client,
                type=d.get("type"),
                color=d.get("color"),
            )
            if d
            else None
        )


class BackgroundFillGradient(Type_):
    def __init__(
        self,
        type: "str",
        top_color: "int",
        bottom_color: "int",
        rotation_angle: "int",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.rotation_angle = rotation_angle

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BackgroundFillGradient" | None:
        return (
            BackgroundFillGradient(
                client=client,
                type=d.get("type"),
                top_color=d.get("top_color"),
                bottom_color=d.get("bottom_color"),
                rotation_angle=d.get("rotation_angle"),
            )
            if d
            else None
        )


class BackgroundFillFreeformGradient(Type_):
    def __init__(self, type: "str", colors: List["int"], client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type
        self.colors = colors

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BackgroundFillFreeformGradient" | None:
        return (
            BackgroundFillFreeformGradient(
                client=client,
                type=d.get("type"),
                colors=[int._parse(i) for i in d.get("colors")]
                if d.get("colors", None)
                else None,
            )
            if d
            else None
        )


class BackgroundType(Type_):
    def __init__(
        self,
        type: "str",
        fill: "BackgroundFill",
        dark_theme_dimming: "int",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "BackgroundType" | None:
        return (
            BackgroundType(
                client=client,
                type=d.get("type"),
                fill=BackgroundFill._parse(d.get("fill")),
                dark_theme_dimming=d.get("dark_theme_dimming"),
            )
            if d
            else None
        )


class BackgroundTypeFill(Type_):
    def __init__(
        self,
        type: "str",
        fill: "BackgroundFill",
        dark_theme_dimming: "int",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BackgroundTypeFill" | None:
        return (
            BackgroundTypeFill(
                client=client,
                type=d.get("type"),
                fill=BackgroundFill._parse(d.get("fill")),
                dark_theme_dimming=d.get("dark_theme_dimming"),
            )
            if d
            else None
        )


class BackgroundTypeWallpaper(Type_):
    def __init__(
        self,
        type: "str",
        document: "Document",
        dark_theme_dimming: "int",
        is_blurred: "bool" = None,
        is_moving: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.document = document
        self.dark_theme_dimming = dark_theme_dimming
        self.is_blurred = is_blurred
        self.is_moving = is_moving

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BackgroundTypeWallpaper" | None:
        return (
            BackgroundTypeWallpaper(
                client=client,
                type=d.get("type"),
                document=Document._parse(d.get("document")),
                dark_theme_dimming=d.get("dark_theme_dimming"),
                is_blurred=d.get("is_blurred"),
                is_moving=d.get("is_moving"),
            )
            if d
            else None
        )


class BackgroundTypePattern(Type_):
    def __init__(
        self,
        type: "str",
        document: "Document",
        fill: "BackgroundFill",
        intensity: "int",
        is_inverted: "bool" = None,
        is_moving: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.document = document
        self.fill = fill
        self.intensity = intensity
        self.is_inverted = is_inverted
        self.is_moving = is_moving

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BackgroundTypePattern" | None:
        return (
            BackgroundTypePattern(
                client=client,
                type=d.get("type"),
                document=Document._parse(d.get("document")),
                fill=BackgroundFill._parse(d.get("fill")),
                intensity=d.get("intensity"),
                is_inverted=d.get("is_inverted"),
                is_moving=d.get("is_moving"),
            )
            if d
            else None
        )


class BackgroundTypeChatTheme(Type_):
    def __init__(self, type: "str", theme_name: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type
        self.theme_name = theme_name

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BackgroundTypeChatTheme" | None:
        return (
            BackgroundTypeChatTheme(
                client=client,
                type=d.get("type"),
                theme_name=d.get("theme_name"),
            )
            if d
            else None
        )


class ChatBackground(Type_):
    def __init__(self, type: "BackgroundType", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatBackground" | None:
        return (
            ChatBackground(
                client=client,
                type=BackgroundType._parse(d.get("type")),
            )
            if d
            else None
        )


class ForumTopicCreated(Type_):
    def __init__(
        self,
        name: "str",
        icon_color: "int",
        icon_custom_emoji_id: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ForumTopicCreated" | None:
        return (
            ForumTopicCreated(
                client=client,
                name=d.get("name"),
                icon_color=d.get("icon_color"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d
            else None
        )


class ForumTopicClosed(Type_):
    def __init__(
        self,
        name: "str" = None,
        icon_custom_emoji_id: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ForumTopicClosed" | None:
        return (
            ForumTopicClosed(
                client=client,
                name=d.get("name"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d
            else None
        )


class ForumTopicEdited(Type_):
    def __init__(
        self,
        name: "str" = None,
        icon_custom_emoji_id: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ForumTopicEdited" | None:
        return (
            ForumTopicEdited(
                client=client,
                name=d.get("name"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d
            else None
        )


class ForumTopicReopened(Type_):
    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ForumTopicReopened" | None:
        return (
            ForumTopicReopened(
                client=client,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[PhotoSize._parse(i) for i in d.get("photo")]
                if d.get("photo", None)
                else None,
            )
            if d
            else None
        )


class GeneralForumTopicHidden(Type_):
    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "GeneralForumTopicHidden" | None:
        return (
            GeneralForumTopicHidden(
                client=client,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[PhotoSize._parse(i) for i in d.get("photo")]
                if d.get("photo", None)
                else None,
            )
            if d
            else None
        )


class GeneralForumTopicUnhidden(Type_):
    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "GeneralForumTopicUnhidden" | None:
        return (
            GeneralForumTopicUnhidden(
                client=client,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[PhotoSize._parse(i) for i in d.get("photo")]
                if d.get("photo", None)
                else None,
            )
            if d
            else None
        )


class SharedUser(Type_):
    def __init__(
        self,
        user_id: "int",
        first_name: "str" = None,
        last_name: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "SharedUser" | None:
        return (
            SharedUser(
                client=client,
                user_id=d.get("user_id"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                username=d.get("username"),
                photo=[PhotoSize._parse(i) for i in d.get("photo")]
                if d.get("photo", None)
                else None,
            )
            if d
            else None
        )


class UsersShared(Type_):
    def __init__(
        self, request_id: "int", users: List["SharedUser"], client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.request_id = request_id
        self.users = users

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "UsersShared" | None:
        return (
            UsersShared(
                client=client,
                request_id=d.get("request_id"),
                users=[SharedUser._parse(i) for i in d.get("users")]
                if d.get("users", None)
                else None,
            )
            if d
            else None
        )


class ChatShared(Type_):
    def __init__(
        self,
        request_id: "int",
        chat_id: "int",
        title: "str" = None,
        username: "str" = None,
        photo: List["PhotoSize"] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatShared" | None:
        return (
            ChatShared(
                client=client,
                request_id=d.get("request_id"),
                chat_id=d.get("chat_id"),
                title=d.get("title"),
                username=d.get("username"),
                photo=[PhotoSize._parse(i) for i in d.get("photo")]
                if d.get("photo", None)
                else None,
            )
            if d
            else None
        )


class WriteAccessAllowed(Type_):
    def __init__(
        self,
        from_request: "bool" = None,
        web_app_name: "str" = None,
        from_attachment_menu: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "WriteAccessAllowed" | None:
        return (
            WriteAccessAllowed(
                client=client,
                from_request=d.get("from_request"),
                web_app_name=d.get("web_app_name"),
                from_attachment_menu=d.get("from_attachment_menu"),
            )
            if d
            else None
        )


class VideoChatScheduled(Type_):
    def __init__(self, start_date: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.start_date = start_date

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "VideoChatScheduled" | None:
        return (
            VideoChatScheduled(
                client=client,
                start_date=d.get("start_date"),
            )
            if d
            else None
        )


class VideoChatStarted(Type_):
    def __init__(self, duration: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.duration = duration

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "VideoChatStarted" | None:
        return (
            VideoChatStarted(
                client=client,
                duration=d.get("duration"),
            )
            if d
            else None
        )


class VideoChatEnded(Type_):
    def __init__(self, duration: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.duration = duration

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "VideoChatEnded" | None:
        return (
            VideoChatEnded(
                client=client,
                duration=d.get("duration"),
            )
            if d
            else None
        )


class VideoChatParticipantsInvited(Type_):
    def __init__(self, users: List["User"], client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.users = users

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "VideoChatParticipantsInvited" | None:
        return (
            VideoChatParticipantsInvited(
                client=client,
                users=[User._parse(i) for i in d.get("users")]
                if d.get("users", None)
                else None,
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.premium_subscription_month_count = premium_subscription_month_count

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "GiveawayCreated" | None:
        return (
            GiveawayCreated(
                client=client,
                chats=[Chat._parse(i) for i in d.get("chats")]
                if d.get("chats", None)
                else None,
                winners_selection_date=d.get("winners_selection_date"),
                winner_count=d.get("winner_count"),
                only_new_members=d.get("only_new_members"),
                has_public_winners=d.get("has_public_winners"),
                prize_description=d.get("prize_description"),
                country_codes=[str._parse(i) for i in d.get("country_codes")]
                if d.get("country_codes", None)
                else None,
                premium_subscription_month_count=d.get(
                    "premium_subscription_month_count"
                ),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.premium_subscription_month_count = premium_subscription_month_count

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Giveaway" | None:
        return (
            Giveaway(
                client=client,
                chats=[Chat._parse(i) for i in d.get("chats")]
                if d.get("chats", None)
                else None,
                winners_selection_date=d.get("winners_selection_date"),
                winner_count=d.get("winner_count"),
                only_new_members=d.get("only_new_members"),
                has_public_winners=d.get("has_public_winners"),
                prize_description=d.get("prize_description"),
                country_codes=[str._parse(i) for i in d.get("country_codes")]
                if d.get("country_codes", None)
                else None,
                premium_subscription_month_count=d.get(
                    "premium_subscription_month_count"
                ),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "GiveawayWinners" | None:
        return (
            GiveawayWinners(
                client=client,
                chat=Chat._parse(d.get("chat")),
                giveaway_message_id=d.get("giveaway_message_id"),
                winners_selection_date=d.get("winners_selection_date"),
                winner_count=d.get("winner_count"),
                winners=[User._parse(i) for i in d.get("winners")]
                if d.get("winners", None)
                else None,
                additional_chat_count=d.get("additional_chat_count"),
                premium_subscription_month_count=d.get(
                    "premium_subscription_month_count"
                ),
                unclaimed_prize_count=d.get("unclaimed_prize_count"),
                only_new_members=d.get("only_new_members"),
                was_refunded=d.get("was_refunded"),
                prize_description=d.get("prize_description"),
            )
            if d
            else None
        )


class GiveawayCompleted(Type_):
    def __init__(
        self,
        winner_count: "int",
        unclaimed_prize_count: "int" = None,
        giveaway_message: "Message" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.winner_count = winner_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.giveaway_message = giveaway_message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "GiveawayCompleted" | None:
        return (
            GiveawayCompleted(
                client=client,
                winner_count=d.get("winner_count"),
                unclaimed_prize_count=d.get("unclaimed_prize_count"),
                giveaway_message=Message._parse(d.get("giveaway_message")),
            )
            if d
            else None
        )


class LinkPreviewOptions(Type_):
    def __init__(
        self,
        is_disabled: "bool" = None,
        url: "str" = None,
        prefer_small_media: "bool" = None,
        prefer_large_media: "bool" = None,
        show_above_text: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "LinkPreviewOptions" | None:
        return (
            LinkPreviewOptions(
                client=client,
                is_disabled=d.get("is_disabled"),
                url=d.get("url"),
                prefer_small_media=d.get("prefer_small_media"),
                prefer_large_media=d.get("prefer_large_media"),
                show_above_text=d.get("show_above_text"),
            )
            if d
            else None
        )


class UserProfilePhotos(Type_):
    def __init__(
        self,
        total_count: "int",
        photos: List[List["PhotoSize"]],
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.total_count = total_count
        self.photos = photos

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "UserProfilePhotos" | None:
        return (
            UserProfilePhotos(
                client=client,
                total_count=d.get("total_count"),
                photos=[PhotoSize._parse(i) for i in d.get("photos")]
                if d.get("photos", None)
                else None,
            )
            if d
            else None
        )


class File(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        file_size: "int" = None,
        file_path: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "File" | None:
        return (
            File(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                file_size=d.get("file_size"),
                file_path=d.get("file_path"),
            )
            if d
            else None
        )


class WebAppInfo(Type_):
    def __init__(self, url: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.url = url

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "WebAppInfo" | None:
        return (
            WebAppInfo(
                client=client,
                url=d.get("url"),
            )
            if d
            else None
        )


class ReplyKeyboardMarkup(Type_):
    def __init__(
        self,
        keyboard: List[List["KeyboardButton"]],
        is_persistent: "bool" = None,
        resize_keyboard: "bool" = None,
        one_time_keyboard: "bool" = None,
        input_field_placeholder: "str" = None,
        selective: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ReplyKeyboardMarkup" | None:
        return (
            ReplyKeyboardMarkup(
                client=client,
                keyboard=[KeyboardButton._parse(i) for i in d.get("keyboard")]
                if d.get("keyboard", None)
                else None,
                is_persistent=d.get("is_persistent"),
                resize_keyboard=d.get("resize_keyboard"),
                one_time_keyboard=d.get("one_time_keyboard"),
                input_field_placeholder=d.get("input_field_placeholder"),
                selective=d.get("selective"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "KeyboardButton" | None:
        return (
            KeyboardButton(
                client=client,
                text=d.get("text"),
                request_users=KeyboardButtonRequestUsers._parse(d.get("request_users")),
                request_chat=KeyboardButtonRequestChat._parse(d.get("request_chat")),
                request_contact=d.get("request_contact"),
                request_location=d.get("request_location"),
                request_poll=KeyboardButtonPollType._parse(d.get("request_poll")),
                web_app=WebAppInfo._parse(d.get("web_app")),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.request_id = request_id
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity
        self.request_name = request_name
        self.request_username = request_username
        self.request_photo = request_photo

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "KeyboardButtonRequestUsers" | None:
        return (
            KeyboardButtonRequestUsers(
                client=client,
                request_id=d.get("request_id"),
                user_is_bot=d.get("user_is_bot"),
                user_is_premium=d.get("user_is_premium"),
                max_quantity=d.get("max_quantity"),
                request_name=d.get("request_name"),
                request_username=d.get("request_username"),
                request_photo=d.get("request_photo"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "KeyboardButtonRequestChat" | None:
        return (
            KeyboardButtonRequestChat(
                client=client,
                request_id=d.get("request_id"),
                chat_is_channel=d.get("chat_is_channel"),
                chat_is_forum=d.get("chat_is_forum"),
                chat_has_username=d.get("chat_has_username"),
                chat_is_created=d.get("chat_is_created"),
                user_administrator_rights=ChatAdministratorRights._parse(
                    d.get("user_administrator_rights")
                ),
                bot_administrator_rights=ChatAdministratorRights._parse(
                    d.get("bot_administrator_rights")
                ),
                bot_is_member=d.get("bot_is_member"),
                request_title=d.get("request_title"),
                request_username=d.get("request_username"),
                request_photo=d.get("request_photo"),
            )
            if d
            else None
        )


class KeyboardButtonPollType(Type_):
    def __init__(self, type: "str" = None, client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "KeyboardButtonPollType" | None:
        return (
            KeyboardButtonPollType(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class ReplyKeyboardRemove(Type_):
    def __init__(
        self,
        remove_keyboard: "bool",
        selective: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.remove_keyboard = remove_keyboard
        self.selective = selective

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ReplyKeyboardRemove" | None:
        return (
            ReplyKeyboardRemove(
                client=client,
                remove_keyboard=d.get("remove_keyboard"),
                selective=d.get("selective"),
            )
            if d
            else None
        )


class InlineKeyboardMarkup(Type_):
    def __init__(
        self,
        inline_keyboard: List[List["InlineKeyboardButton"]],
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.inline_keyboard = inline_keyboard

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineKeyboardMarkup" | None:
        return (
            InlineKeyboardMarkup(
                client=client,
                inline_keyboard=[
                    InlineKeyboardButton._parse(i) for i in d.get("inline_keyboard")
                ]
                if d.get("inline_keyboard", None)
                else None,
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineKeyboardButton" | None:
        return (
            InlineKeyboardButton(
                client=client,
                text=d.get("text"),
                url=d.get("url"),
                callback_data=d.get("callback_data"),
                web_app=WebAppInfo._parse(d.get("web_app")),
                login_url=LoginUrl._parse(d.get("login_url")),
                switch_inline_query=d.get("switch_inline_query"),
                switch_inline_query_current_chat=d.get(
                    "switch_inline_query_current_chat"
                ),
                switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat._parse(
                    d.get("switch_inline_query_chosen_chat")
                ),
                callback_game=CallbackGame._parse(d.get("callback_game")),
                pay=d.get("pay"),
            )
            if d
            else None
        )


class LoginUrl(Type_):
    def __init__(
        self,
        url: "str",
        forward_text: "str" = None,
        bot_username: "str" = None,
        request_write_access: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "LoginUrl" | None:
        return (
            LoginUrl(
                client=client,
                url=d.get("url"),
                forward_text=d.get("forward_text"),
                bot_username=d.get("bot_username"),
                request_write_access=d.get("request_write_access"),
            )
            if d
            else None
        )


class SwitchInlineQueryChosenChat(Type_):
    def __init__(
        self,
        query: "str" = None,
        allow_user_chats: "bool" = None,
        allow_bot_chats: "bool" = None,
        allow_group_chats: "bool" = None,
        allow_channel_chats: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "SwitchInlineQueryChosenChat" | None:
        return (
            SwitchInlineQueryChosenChat(
                client=client,
                query=d.get("query"),
                allow_user_chats=d.get("allow_user_chats"),
                allow_bot_chats=d.get("allow_bot_chats"),
                allow_group_chats=d.get("allow_group_chats"),
                allow_channel_chats=d.get("allow_channel_chats"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "CallbackQuery" | None:
        return (
            CallbackQuery(
                client=client,
                id=d.get("id"),
                from_user=User._parse(d.get("from")),
                chat_instance=d.get("chat_instance"),
                message=MaybeInaccessibleMessage._parse(d.get("message")),
                inline_message_id=d.get("inline_message_id"),
                data=d.get("data"),
                game_short_name=d.get("game_short_name"),
            )
            if d
            else None
        )


class ForceReply(Type_):
    def __init__(
        self,
        force_reply: "bool",
        input_field_placeholder: "str" = None,
        selective: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ForceReply" | None:
        return (
            ForceReply(
                client=client,
                force_reply=d.get("force_reply"),
                input_field_placeholder=d.get("input_field_placeholder"),
                selective=d.get("selective"),
            )
            if d
            else None
        )


class ChatPhoto(Type_):
    def __init__(
        self,
        small_file_id: "str",
        small_file_unique_id: "str",
        big_file_id: "str",
        big_file_unique_id: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatPhoto" | None:
        return (
            ChatPhoto(
                client=client,
                small_file_id=d.get("small_file_id"),
                small_file_unique_id=d.get("small_file_unique_id"),
                big_file_id=d.get("big_file_id"),
                big_file_unique_id=d.get("big_file_unique_id"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatInviteLink" | None:
        return (
            ChatInviteLink(
                client=client,
                invite_link=d.get("invite_link"),
                creator=User._parse(d.get("creator")),
                creates_join_request=d.get("creates_join_request"),
                is_primary=d.get("is_primary"),
                is_revoked=d.get("is_revoked"),
                name=d.get("name"),
                expire_date=d.get("expire_date"),
                member_limit=d.get("member_limit"),
                pending_join_request_count=d.get("pending_join_request_count"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatAdministratorRights" | None:
        return (
            ChatAdministratorRights(
                client=client,
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
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatMemberUpdated" | None:
        return (
            ChatMemberUpdated(
                client=client,
                chat=Chat._parse(d.get("chat")),
                from_user=User._parse(d.get("from")),
                date=d.get("date"),
                old_chat_member=ChatMember._parse(d.get("old_chat_member")),
                new_chat_member=ChatMember._parse(d.get("new_chat_member")),
                invite_link=ChatInviteLink._parse(d.get("invite_link")),
                via_join_request=d.get("via_join_request"),
                via_chat_folder_invite_link=d.get("via_chat_folder_invite_link"),
            )
            if d
            else None
        )


class ChatMember(Type_):
    def __init__(
        self,
        status: "str",
        user: "User",
        is_anonymous: "bool",
        custom_title: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatMember" | None:
        return (
            ChatMember(
                client=client,
                status=d.get("status"),
                user=User._parse(d.get("user")),
                is_anonymous=d.get("is_anonymous"),
                custom_title=d.get("custom_title"),
            )
            if d
            else None
        )


class ChatMemberOwner(Type_):
    def __init__(
        self,
        status: "str",
        user: "User",
        is_anonymous: "bool",
        custom_title: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatMemberOwner" | None:
        return (
            ChatMemberOwner(
                client=client,
                status=d.get("status"),
                user=User._parse(d.get("user")),
                is_anonymous=d.get("is_anonymous"),
                custom_title=d.get("custom_title"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatMemberAdministrator" | None:
        return (
            ChatMemberAdministrator(
                client=client,
                status=d.get("status"),
                user=User._parse(d.get("user")),
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
            if d
            else None
        )


class ChatMemberMember(Type_):
    def __init__(self, status: "str", user: "User", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.status = status
        self.user = user

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatMemberMember" | None:
        return (
            ChatMemberMember(
                client=client,
                status=d.get("status"),
                user=User._parse(d.get("user")),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatMemberRestricted" | None:
        return (
            ChatMemberRestricted(
                client=client,
                status=d.get("status"),
                user=User._parse(d.get("user")),
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
            if d
            else None
        )


class ChatMemberLeft(Type_):
    def __init__(self, status: "str", user: "User", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.status = status
        self.user = user

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatMemberLeft" | None:
        return (
            ChatMemberLeft(
                client=client,
                status=d.get("status"),
                user=User._parse(d.get("user")),
            )
            if d
            else None
        )


class ChatMemberBanned(Type_):
    def __init__(
        self,
        status: "str",
        user: "User",
        until_date: "int",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.status = status
        self.user = user
        self.until_date = until_date

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatMemberBanned" | None:
        return (
            ChatMemberBanned(
                client=client,
                status=d.get("status"),
                user=User._parse(d.get("user")),
                until_date=d.get("until_date"),
            )
            if d
            else None
        )


class ChatJoinRequest(Type_):
    def __init__(
        self,
        chat: "Chat",
        from_user: "User",
        user_chat_id: "int",
        date: "int",
        bio: "str" = None,
        invite_link: "ChatInviteLink" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatJoinRequest" | None:
        return (
            ChatJoinRequest(
                client=client,
                chat=Chat._parse(d.get("chat")),
                from_user=User._parse(d.get("from")),
                user_chat_id=d.get("user_chat_id"),
                date=d.get("date"),
                bio=d.get("bio"),
                invite_link=ChatInviteLink._parse(d.get("invite_link")),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatPermissions" | None:
        return (
            ChatPermissions(
                client=client,
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
            )
            if d
            else None
        )


class Birthdate(Type_):
    def __init__(
        self, day: "int", month: "int", year: "int" = None, client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Birthdate" | None:
        return (
            Birthdate(
                client=client,
                day=d.get("day"),
                month=d.get("month"),
                year=d.get("year"),
            )
            if d
            else None
        )


class BusinessIntro(Type_):
    def __init__(
        self,
        title: "str" = None,
        message: "str" = None,
        sticker: "Sticker" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.title = title
        self.message = message
        self.sticker = sticker

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "BusinessIntro" | None:
        return (
            BusinessIntro(
                client=client,
                title=d.get("title"),
                message=d.get("message"),
                sticker=Sticker._parse(d.get("sticker")),
            )
            if d
            else None
        )


class BusinessLocation(Type_):
    def __init__(
        self, address: "str", location: "Location" = None, client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.address = address
        self.location = location

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BusinessLocation" | None:
        return (
            BusinessLocation(
                client=client,
                address=d.get("address"),
                location=Location._parse(d.get("location")),
            )
            if d
            else None
        )


class BusinessOpeningHoursInterval(Type_):
    def __init__(
        self, opening_minute: "int", closing_minute: "int", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.opening_minute = opening_minute
        self.closing_minute = closing_minute

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BusinessOpeningHoursInterval" | None:
        return (
            BusinessOpeningHoursInterval(
                client=client,
                opening_minute=d.get("opening_minute"),
                closing_minute=d.get("closing_minute"),
            )
            if d
            else None
        )


class BusinessOpeningHours(Type_):
    def __init__(
        self,
        time_zone_name: "str",
        opening_hours: List["BusinessOpeningHoursInterval"],
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.time_zone_name = time_zone_name
        self.opening_hours = opening_hours

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BusinessOpeningHours" | None:
        return (
            BusinessOpeningHours(
                client=client,
                time_zone_name=d.get("time_zone_name"),
                opening_hours=[
                    BusinessOpeningHoursInterval._parse(i)
                    for i in d.get("opening_hours")
                ]
                if d.get("opening_hours", None)
                else None,
            )
            if d
            else None
        )


class ChatLocation(Type_):
    def __init__(
        self, location: "Location", address: "str", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.location = location
        self.address = address

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatLocation" | None:
        return (
            ChatLocation(
                client=client,
                location=Location._parse(d.get("location")),
                address=d.get("address"),
            )
            if d
            else None
        )


class ReactionType(Type_):
    def __init__(self, type: "str", emoji: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type
        self.emoji = emoji

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ReactionType" | None:
        return (
            ReactionType(
                client=client,
                type=d.get("type"),
                emoji=d.get("emoji"),
            )
            if d
            else None
        )


class ReactionTypeEmoji(Type_):
    def __init__(self, type: "str", emoji: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type
        self.emoji = emoji

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ReactionTypeEmoji" | None:
        return (
            ReactionTypeEmoji(
                client=client,
                type=d.get("type"),
                emoji=d.get("emoji"),
            )
            if d
            else None
        )


class ReactionTypeCustomEmoji(Type_):
    def __init__(
        self, type: "str", custom_emoji_id: "str", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.type = type
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ReactionTypeCustomEmoji" | None:
        return (
            ReactionTypeCustomEmoji(
                client=client,
                type=d.get("type"),
                custom_emoji_id=d.get("custom_emoji_id"),
            )
            if d
            else None
        )


class ReactionCount(Type_):
    def __init__(
        self, type: "ReactionType", total_count: "int", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.type = type
        self.total_count = total_count

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ReactionCount" | None:
        return (
            ReactionCount(
                client=client,
                type=ReactionType._parse(d.get("type")),
                total_count=d.get("total_count"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.chat = chat
        self.message_id = message_id
        self.user = user
        self.actor_chat = actor_chat
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MessageReactionUpdated" | None:
        return (
            MessageReactionUpdated(
                client=client,
                chat=Chat._parse(d.get("chat")),
                message_id=d.get("message_id"),
                date=d.get("date"),
                old_reaction=[ReactionType._parse(i) for i in d.get("old_reaction")]
                if d.get("old_reaction", None)
                else None,
                new_reaction=[ReactionType._parse(i) for i in d.get("new_reaction")]
                if d.get("new_reaction", None)
                else None,
                user=User._parse(d.get("user")),
                actor_chat=Chat._parse(d.get("actor_chat")),
            )
            if d
            else None
        )


class MessageReactionCountUpdated(Type_):
    def __init__(
        self,
        chat: "Chat",
        message_id: "int",
        date: "int",
        reactions: List["ReactionCount"],
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MessageReactionCountUpdated" | None:
        return (
            MessageReactionCountUpdated(
                client=client,
                chat=Chat._parse(d.get("chat")),
                message_id=d.get("message_id"),
                date=d.get("date"),
                reactions=[ReactionCount._parse(i) for i in d.get("reactions")]
                if d.get("reactions", None)
                else None,
            )
            if d
            else None
        )


class ForumTopic(Type_):
    def __init__(
        self,
        message_thread_id: "int",
        name: "str",
        icon_color: "int",
        icon_custom_emoji_id: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ForumTopic" | None:
        return (
            ForumTopic(
                client=client,
                message_thread_id=d.get("message_thread_id"),
                name=d.get("name"),
                icon_color=d.get("icon_color"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d
            else None
        )


class BotCommand(Type_):
    def __init__(
        self, command: "str", description: "str", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.command = command
        self.description = description

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "BotCommand" | None:
        return (
            BotCommand(
                client=client,
                command=d.get("command"),
                description=d.get("description"),
            )
            if d
            else None
        )


class BotCommandScope(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotCommandScope" | None:
        return (
            BotCommandScope(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class BotCommandScopeDefault(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotCommandScopeDefault" | None:
        return (
            BotCommandScopeDefault(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class BotCommandScopeAllPrivateChats(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotCommandScopeAllPrivateChats" | None:
        return (
            BotCommandScopeAllPrivateChats(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class BotCommandScopeAllGroupChats(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotCommandScopeAllGroupChats" | None:
        return (
            BotCommandScopeAllGroupChats(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class BotCommandScopeAllChatAdministrators(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotCommandScopeAllChatAdministrators" | None:
        return (
            BotCommandScopeAllChatAdministrators(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class BotCommandScopeChat(Type_):
    def __init__(
        self, type: "str", chat_id: Union["int", "str"], client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.type = type
        self.chat_id = chat_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotCommandScopeChat" | None:
        return (
            BotCommandScopeChat(
                client=client,
                type=d.get("type"),
                chat_id=d.get("chat_id"),
            )
            if d
            else None
        )


class BotCommandScopeChatAdministrators(Type_):
    def __init__(
        self, type: "str", chat_id: Union["int", "str"], client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.type = type
        self.chat_id = chat_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotCommandScopeChatAdministrators" | None:
        return (
            BotCommandScopeChatAdministrators(
                client=client,
                type=d.get("type"),
                chat_id=d.get("chat_id"),
            )
            if d
            else None
        )


class BotCommandScopeChatMember(Type_):
    def __init__(
        self,
        type: "str",
        chat_id: Union["int", "str"],
        user_id: "int",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotCommandScopeChatMember" | None:
        return (
            BotCommandScopeChatMember(
                client=client,
                type=d.get("type"),
                chat_id=d.get("chat_id"),
                user_id=d.get("user_id"),
            )
            if d
            else None
        )


class BotName(Type_):
    def __init__(self, name: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.name = name

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "BotName" | None:
        return (
            BotName(
                client=client,
                name=d.get("name"),
            )
            if d
            else None
        )


class BotDescription(Type_):
    def __init__(self, description: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.description = description

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "BotDescription" | None:
        return (
            BotDescription(
                client=client,
                description=d.get("description"),
            )
            if d
            else None
        )


class BotShortDescription(Type_):
    def __init__(self, short_description: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.short_description = short_description

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BotShortDescription" | None:
        return (
            BotShortDescription(
                client=client,
                short_description=d.get("short_description"),
            )
            if d
            else None
        )


class MenuButton(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "MenuButton" | None:
        return (
            MenuButton(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class MenuButtonCommands(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MenuButtonCommands" | None:
        return (
            MenuButtonCommands(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class MenuButtonWebApp(Type_):
    def __init__(
        self,
        type: "str",
        text: "str",
        web_app: "WebAppInfo",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.text = text
        self.web_app = web_app

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MenuButtonWebApp" | None:
        return (
            MenuButtonWebApp(
                client=client,
                type=d.get("type"),
                text=d.get("text"),
                web_app=WebAppInfo._parse(d.get("web_app")),
            )
            if d
            else None
        )


class MenuButtonDefault(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "MenuButtonDefault" | None:
        return (
            MenuButtonDefault(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class ChatBoostSource(Type_):
    def __init__(self, source: "str", user: "User", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.source = source
        self.user = user

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatBoostSource" | None:
        return (
            ChatBoostSource(
                client=client,
                source=d.get("source"),
                user=User._parse(d.get("user")),
            )
            if d
            else None
        )


class ChatBoostSourcePremium(Type_):
    def __init__(self, source: "str", user: "User", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.source = source
        self.user = user

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatBoostSourcePremium" | None:
        return (
            ChatBoostSourcePremium(
                client=client,
                source=d.get("source"),
                user=User._parse(d.get("user")),
            )
            if d
            else None
        )


class ChatBoostSourceGiftCode(Type_):
    def __init__(self, source: "str", user: "User", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.source = source
        self.user = user

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatBoostSourceGiftCode" | None:
        return (
            ChatBoostSourceGiftCode(
                client=client,
                source=d.get("source"),
                user=User._parse(d.get("user")),
            )
            if d
            else None
        )


class ChatBoostSourceGiveaway(Type_):
    def __init__(
        self,
        source: "str",
        giveaway_message_id: "int",
        user: "User" = None,
        is_unclaimed: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.is_unclaimed = is_unclaimed

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatBoostSourceGiveaway" | None:
        return (
            ChatBoostSourceGiveaway(
                client=client,
                source=d.get("source"),
                giveaway_message_id=d.get("giveaway_message_id"),
                user=User._parse(d.get("user")),
                is_unclaimed=d.get("is_unclaimed"),
            )
            if d
            else None
        )


class ChatBoost(Type_):
    def __init__(
        self,
        boost_id: "str",
        add_date: "int",
        expiration_date: "int",
        source: "ChatBoostSource",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ChatBoost" | None:
        return (
            ChatBoost(
                client=client,
                boost_id=d.get("boost_id"),
                add_date=d.get("add_date"),
                expiration_date=d.get("expiration_date"),
                source=ChatBoostSource._parse(d.get("source")),
            )
            if d
            else None
        )


class ChatBoostUpdated(Type_):
    def __init__(self, chat: "Chat", boost: "ChatBoost", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.chat = chat
        self.boost = boost

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatBoostUpdated" | None:
        return (
            ChatBoostUpdated(
                client=client,
                chat=Chat._parse(d.get("chat")),
                boost=ChatBoost._parse(d.get("boost")),
            )
            if d
            else None
        )


class ChatBoostRemoved(Type_):
    def __init__(
        self,
        chat: "Chat",
        boost_id: "str",
        remove_date: "int",
        source: "ChatBoostSource",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChatBoostRemoved" | None:
        return (
            ChatBoostRemoved(
                client=client,
                chat=Chat._parse(d.get("chat")),
                boost_id=d.get("boost_id"),
                remove_date=d.get("remove_date"),
                source=ChatBoostSource._parse(d.get("source")),
            )
            if d
            else None
        )


class UserChatBoosts(Type_):
    def __init__(self, boosts: List["ChatBoost"], client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.boosts = boosts

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "UserChatBoosts" | None:
        return (
            UserChatBoosts(
                client=client,
                boosts=[ChatBoost._parse(i) for i in d.get("boosts")]
                if d.get("boosts", None)
                else None,
            )
            if d
            else None
        )


class BusinessConnection(Type_):
    def __init__(
        self,
        id: "str",
        user: "User",
        user_chat_id: "int",
        date: "int",
        can_reply: "bool",
        is_enabled: "bool",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.id = id
        self.user = user
        self.user_chat_id = user_chat_id
        self.date = date
        self.can_reply = can_reply
        self.is_enabled = is_enabled

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BusinessConnection" | None:
        return (
            BusinessConnection(
                client=client,
                id=d.get("id"),
                user=User._parse(d.get("user")),
                user_chat_id=d.get("user_chat_id"),
                date=d.get("date"),
                can_reply=d.get("can_reply"),
                is_enabled=d.get("is_enabled"),
            )
            if d
            else None
        )


class BusinessMessagesDeleted(Type_):
    def __init__(
        self,
        business_connection_id: "str",
        chat: "Chat",
        message_ids: List["int"],
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.message_ids = message_ids

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "BusinessMessagesDeleted" | None:
        return (
            BusinessMessagesDeleted(
                client=client,
                business_connection_id=d.get("business_connection_id"),
                chat=Chat._parse(d.get("chat")),
                message_ids=[int._parse(i) for i in d.get("message_ids")]
                if d.get("message_ids", None)
                else None,
            )
            if d
            else None
        )


class ResponseParameters(Type_):
    def __init__(
        self,
        migrate_to_chat_id: "int" = None,
        retry_after: "int" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ResponseParameters" | None:
        return (
            ResponseParameters(
                client=client,
                migrate_to_chat_id=d.get("migrate_to_chat_id"),
                retry_after=d.get("retry_after"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "InputMedia" | None:
        return (
            InputMedia(
                client=client,
                type=d.get("type"),
                media=d.get("media"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                has_spoiler=d.get("has_spoiler"),
            )
            if d
            else None
        )


class InputMediaPhoto(Type_):
    def __init__(
        self,
        type: "str",
        media: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        has_spoiler: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputMediaPhoto" | None:
        return (
            InputMediaPhoto(
                client=client,
                type=d.get("type"),
                media=d.get("media"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                has_spoiler=d.get("has_spoiler"),
            )
            if d
            else None
        )


class InputMediaVideo(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputMediaVideo" | None:
        return (
            InputMediaVideo(
                client=client,
                type=d.get("type"),
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                supports_streaming=d.get("supports_streaming"),
                has_spoiler=d.get("has_spoiler"),
            )
            if d
            else None
        )


class InputMediaAnimation(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputMediaAnimation" | None:
        return (
            InputMediaAnimation(
                client=client,
                type=d.get("type"),
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                width=d.get("width"),
                height=d.get("height"),
                duration=d.get("duration"),
                has_spoiler=d.get("has_spoiler"),
            )
            if d
            else None
        )


class InputMediaAudio(Type_):
    def __init__(
        self,
        type: "str",
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        duration: "int" = None,
        performer: "str" = None,
        title: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputMediaAudio" | None:
        return (
            InputMediaAudio(
                client=client,
                type=d.get("type"),
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                duration=d.get("duration"),
                performer=d.get("performer"),
                title=d.get("title"),
            )
            if d
            else None
        )


class InputMediaDocument(Type_):
    def __init__(
        self,
        type: "str",
        media: "str",
        thumbnail: Union["InputFile", "str"] = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        disable_content_type_detection: "bool" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputMediaDocument" | None:
        return (
            InputMediaDocument(
                client=client,
                type=d.get("type"),
                media=d.get("media"),
                thumbnail=d.get("thumbnail"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                disable_content_type_detection=d.get("disable_content_type_detection"),
            )
            if d
            else None
        )


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
        reply_markup: Union[
            "InlineKeyboardMarkup",
            "ReplyKeyboardMarkup",
            "ReplyKeyboardRemove",
            "ForceReply",
        ] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "InputFile" | None:
        return (
            InputFile(
                client=client,
                chat_id=d.get("chat_id"),
                text=d.get("text"),
                business_connection_id=d.get("business_connection_id"),
                message_thread_id=d.get("message_thread_id"),
                parse_mode=d.get("parse_mode"),
                entities=[MessageEntity._parse(i) for i in d.get("entities")]
                if d.get("entities", None)
                else None,
                link_preview_options=LinkPreviewOptions._parse(
                    d.get("link_preview_options")
                ),
                disable_notification=d.get("disable_notification"),
                protect_content=d.get("protect_content"),
                message_effect_id=d.get("message_effect_id"),
                reply_parameters=ReplyParameters._parse(d.get("reply_parameters")),
                reply_markup=d.get("reply_markup"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Sticker" | None:
        return (
            Sticker(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                type=d.get("type"),
                width=d.get("width"),
                height=d.get("height"),
                is_animated=d.get("is_animated"),
                is_video=d.get("is_video"),
                thumbnail=PhotoSize._parse(d.get("thumbnail")),
                emoji=d.get("emoji"),
                set_name=d.get("set_name"),
                premium_animation=File._parse(d.get("premium_animation")),
                mask_position=MaskPosition._parse(d.get("mask_position")),
                custom_emoji_id=d.get("custom_emoji_id"),
                needs_repainting=d.get("needs_repainting"),
                file_size=d.get("file_size"),
            )
            if d
            else None
        )


class StickerSet(Type_):
    def __init__(
        self,
        name: "str",
        title: "str",
        sticker_type: "str",
        stickers: List["Sticker"],
        thumbnail: "PhotoSize" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.stickers = stickers
        self.thumbnail = thumbnail

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "StickerSet" | None:
        return (
            StickerSet(
                client=client,
                name=d.get("name"),
                title=d.get("title"),
                sticker_type=d.get("sticker_type"),
                stickers=[Sticker._parse(i) for i in d.get("stickers")]
                if d.get("stickers", None)
                else None,
                thumbnail=PhotoSize._parse(d.get("thumbnail")),
            )
            if d
            else None
        )


class MaskPosition(Type_):
    def __init__(
        self,
        point: "str",
        x_shift: "float",
        y_shift: "float",
        scale: "float",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "MaskPosition" | None:
        return (
            MaskPosition(
                client=client,
                point=d.get("point"),
                x_shift=d.get("x_shift"),
                y_shift=d.get("y_shift"),
                scale=d.get("scale"),
            )
            if d
            else None
        )


class InputSticker(Type_):
    def __init__(
        self,
        sticker: Union["InputFile", "str"],
        format: "str",
        emoji_list: List["str"],
        mask_position: "MaskPosition" = None,
        keywords: List["str"] = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.sticker = sticker
        self.format = format
        self.emoji_list = emoji_list
        self.mask_position = mask_position
        self.keywords = keywords

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "InputSticker" | None:
        return (
            InputSticker(
                client=client,
                sticker=d.get("sticker"),
                format=d.get("format"),
                emoji_list=[str._parse(i) for i in d.get("emoji_list")]
                if d.get("emoji_list", None)
                else None,
                mask_position=MaskPosition._parse(d.get("mask_position")),
                keywords=[str._parse(i) for i in d.get("keywords")]
                if d.get("keywords", None)
                else None,
            )
            if d
            else None
        )


class InlineQuery(Type_):
    def __init__(
        self,
        id: "str",
        from_user: "User",
        query: "str",
        offset: "str",
        chat_type: "str" = None,
        location: "Location" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "InlineQuery" | None:
        return (
            InlineQuery(
                client=client,
                id=d.get("id"),
                from_user=User._parse(d.get("from")),
                query=d.get("query"),
                offset=d.get("offset"),
                chat_type=d.get("chat_type"),
                location=Location._parse(d.get("location")),
            )
            if d
            else None
        )


class InlineQueryResultsButton(Type_):
    def __init__(
        self,
        text: "str",
        web_app: "WebAppInfo" = None,
        start_parameter: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultsButton" | None:
        return (
            InlineQueryResultsButton(
                client=client,
                text=d.get("text"),
                web_app=WebAppInfo._parse(d.get("web_app")),
                start_parameter=d.get("start_parameter"),
            )
            if d
            else None
        )


class InlineQueryResult(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResult" | None:
        return (
            InlineQueryResult(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                title=d.get("title"),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                url=d.get("url"),
                hide_url=d.get("hide_url"),
                description=d.get("description"),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d
            else None
        )


class InlineQueryResultArticle(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultArticle" | None:
        return (
            InlineQueryResultArticle(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                title=d.get("title"),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                url=d.get("url"),
                hide_url=d.get("hide_url"),
                description=d.get("description"),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d
            else None
        )


class InlineQueryResultPhoto(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultPhoto" | None:
        return (
            InlineQueryResultPhoto(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                photo_url=d.get("photo_url"),
                thumbnail_url=d.get("thumbnail_url"),
                photo_width=d.get("photo_width"),
                photo_height=d.get("photo_height"),
                title=d.get("title"),
                description=d.get("description"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultGif(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultGif" | None:
        return (
            InlineQueryResultGif(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                gif_url=d.get("gif_url"),
                thumbnail_url=d.get("thumbnail_url"),
                gif_width=d.get("gif_width"),
                gif_height=d.get("gif_height"),
                gif_duration=d.get("gif_duration"),
                thumbnail_mime_type=d.get("thumbnail_mime_type"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultMpeg4Gif(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultMpeg4Gif" | None:
        return (
            InlineQueryResultMpeg4Gif(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                mpeg4_url=d.get("mpeg4_url"),
                thumbnail_url=d.get("thumbnail_url"),
                mpeg4_width=d.get("mpeg4_width"),
                mpeg4_height=d.get("mpeg4_height"),
                mpeg4_duration=d.get("mpeg4_duration"),
                thumbnail_mime_type=d.get("thumbnail_mime_type"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultVideo(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultVideo" | None:
        return (
            InlineQueryResultVideo(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                video_url=d.get("video_url"),
                mime_type=d.get("mime_type"),
                thumbnail_url=d.get("thumbnail_url"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                video_width=d.get("video_width"),
                video_height=d.get("video_height"),
                video_duration=d.get("video_duration"),
                description=d.get("description"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultAudio(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultAudio" | None:
        return (
            InlineQueryResultAudio(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                audio_url=d.get("audio_url"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                performer=d.get("performer"),
                audio_duration=d.get("audio_duration"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultVoice(Type_):
    def __init__(
        self,
        type: "str",
        id: "str",
        voice_url: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        voice_duration: "int" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultVoice" | None:
        return (
            InlineQueryResultVoice(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                voice_url=d.get("voice_url"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                voice_duration=d.get("voice_duration"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultDocument(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultDocument" | None:
        return (
            InlineQueryResultDocument(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                title=d.get("title"),
                document_url=d.get("document_url"),
                mime_type=d.get("mime_type"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                description=d.get("description"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d
            else None
        )


class InlineQueryResultLocation(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultLocation" | None:
        return (
            InlineQueryResultLocation(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                horizontal_accuracy=d.get("horizontal_accuracy"),
                live_period=d.get("live_period"),
                heading=d.get("heading"),
                proximity_alert_radius=d.get("proximity_alert_radius"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d
            else None
        )


class InlineQueryResultVenue(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultVenue" | None:
        return (
            InlineQueryResultVenue(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                address=d.get("address"),
                foursquare_id=d.get("foursquare_id"),
                foursquare_type=d.get("foursquare_type"),
                google_place_id=d.get("google_place_id"),
                google_place_type=d.get("google_place_type"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d
            else None
        )


class InlineQueryResultContact(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultContact" | None:
        return (
            InlineQueryResultContact(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                phone_number=d.get("phone_number"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                vcard=d.get("vcard"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d
            else None
        )


class InlineQueryResultGame(Type_):
    def __init__(
        self,
        type: "str",
        id: "str",
        game_short_name: "str",
        reply_markup: "InlineKeyboardMarkup" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.id = id
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultGame" | None:
        return (
            InlineQueryResultGame(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                game_short_name=d.get("game_short_name"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
            )
            if d
            else None
        )


class InlineQueryResultCachedPhoto(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultCachedPhoto" | None:
        return (
            InlineQueryResultCachedPhoto(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                photo_file_id=d.get("photo_file_id"),
                title=d.get("title"),
                description=d.get("description"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultCachedGif(Type_):
    def __init__(
        self,
        type: "str",
        id: "str",
        gif_file_id: "str",
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultCachedGif" | None:
        return (
            InlineQueryResultCachedGif(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                gif_file_id=d.get("gif_file_id"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultCachedMpeg4Gif(Type_):
    def __init__(
        self,
        type: "str",
        id: "str",
        mpeg4_file_id: "str",
        title: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultCachedMpeg4Gif" | None:
        return (
            InlineQueryResultCachedMpeg4Gif(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                mpeg4_file_id=d.get("mpeg4_file_id"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultCachedSticker(Type_):
    def __init__(
        self,
        type: "str",
        id: "str",
        sticker_file_id: "str",
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultCachedSticker" | None:
        return (
            InlineQueryResultCachedSticker(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                sticker_file_id=d.get("sticker_file_id"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultCachedDocument(Type_):
    def __init__(
        self,
        type: "str",
        id: "str",
        title: "str",
        document_file_id: "str",
        description: "str" = None,
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultCachedDocument" | None:
        return (
            InlineQueryResultCachedDocument(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                title=d.get("title"),
                document_file_id=d.get("document_file_id"),
                description=d.get("description"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultCachedVideo(Type_):
    def __init__(
        self,
        type: "str",
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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultCachedVideo" | None:
        return (
            InlineQueryResultCachedVideo(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                video_file_id=d.get("video_file_id"),
                title=d.get("title"),
                description=d.get("description"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultCachedVoice(Type_):
    def __init__(
        self,
        type: "str",
        id: "str",
        voice_file_id: "str",
        title: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.id = id
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultCachedVoice" | None:
        return (
            InlineQueryResultCachedVoice(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                voice_file_id=d.get("voice_file_id"),
                title=d.get("title"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InlineQueryResultCachedAudio(Type_):
    def __init__(
        self,
        type: "str",
        id: "str",
        audio_file_id: "str",
        caption: "str" = None,
        parse_mode: "str" = None,
        caption_entities: List["MessageEntity"] = None,
        reply_markup: "InlineKeyboardMarkup" = None,
        input_message_content: "InputMessageContent" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InlineQueryResultCachedAudio" | None:
        return (
            InlineQueryResultCachedAudio(
                client=client,
                type=d.get("type"),
                id=d.get("id"),
                audio_file_id=d.get("audio_file_id"),
                caption=d.get("caption"),
                parse_mode=d.get("parse_mode"),
                caption_entities=[
                    MessageEntity._parse(i) for i in d.get("caption_entities")
                ]
                if d.get("caption_entities", None)
                else None,
                reply_markup=InlineKeyboardMarkup._parse(d.get("reply_markup")),
                input_message_content=InputMessageContent._parse(
                    d.get("input_message_content")
                ),
            )
            if d
            else None
        )


class InputMessageContent(Type_):
    def __init__(
        self,
        message_text: "str",
        parse_mode: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputMessageContent" | None:
        return (
            InputMessageContent(
                client=client,
                message_text=d.get("message_text"),
                parse_mode=d.get("parse_mode"),
                entities=[MessageEntity._parse(i) for i in d.get("entities")]
                if d.get("entities", None)
                else None,
                link_preview_options=LinkPreviewOptions._parse(
                    d.get("link_preview_options")
                ),
            )
            if d
            else None
        )


class InputTextMessageContent(Type_):
    def __init__(
        self,
        message_text: "str",
        parse_mode: "str" = None,
        entities: List["MessageEntity"] = None,
        link_preview_options: "LinkPreviewOptions" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputTextMessageContent" | None:
        return (
            InputTextMessageContent(
                client=client,
                message_text=d.get("message_text"),
                parse_mode=d.get("parse_mode"),
                entities=[MessageEntity._parse(i) for i in d.get("entities")]
                if d.get("entities", None)
                else None,
                link_preview_options=LinkPreviewOptions._parse(
                    d.get("link_preview_options")
                ),
            )
            if d
            else None
        )


class InputLocationMessageContent(Type_):
    def __init__(
        self,
        latitude: "float",
        longitude: "float",
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputLocationMessageContent" | None:
        return (
            InputLocationMessageContent(
                client=client,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                horizontal_accuracy=d.get("horizontal_accuracy"),
                live_period=d.get("live_period"),
                heading=d.get("heading"),
                proximity_alert_radius=d.get("proximity_alert_radius"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputVenueMessageContent" | None:
        return (
            InputVenueMessageContent(
                client=client,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                address=d.get("address"),
                foursquare_id=d.get("foursquare_id"),
                foursquare_type=d.get("foursquare_type"),
                google_place_id=d.get("google_place_id"),
                google_place_type=d.get("google_place_type"),
            )
            if d
            else None
        )


class InputContactMessageContent(Type_):
    def __init__(
        self,
        phone_number: "str",
        first_name: "str",
        last_name: "str" = None,
        vcard: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputContactMessageContent" | None:
        return (
            InputContactMessageContent(
                client=client,
                phone_number=d.get("phone_number"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                vcard=d.get("vcard"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "InputInvoiceMessageContent" | None:
        return (
            InputInvoiceMessageContent(
                client=client,
                title=d.get("title"),
                description=d.get("description"),
                payload=d.get("payload"),
                currency=d.get("currency"),
                prices=[LabeledPrice._parse(i) for i in d.get("prices")]
                if d.get("prices", None)
                else None,
                provider_token=d.get("provider_token"),
                max_tip_amount=d.get("max_tip_amount"),
                suggested_tip_amounts=[
                    int._parse(i) for i in d.get("suggested_tip_amounts")
                ]
                if d.get("suggested_tip_amounts", None)
                else None,
                provider_data=d.get("provider_data"),
                photo_url=d.get("photo_url"),
                photo_size=d.get("photo_size"),
                photo_width=d.get("photo_width"),
                photo_height=d.get("photo_height"),
                need_name=d.get("need_name"),
                need_phone_number=d.get("need_phone_number"),
                need_email=d.get("need_email"),
                need_shipping_address=d.get("need_shipping_address"),
                send_phone_number_to_provider=d.get("send_phone_number_to_provider"),
                send_email_to_provider=d.get("send_email_to_provider"),
                is_flexible=d.get("is_flexible"),
            )
            if d
            else None
        )


class ChosenInlineResult(Type_):
    def __init__(
        self,
        result_id: "str",
        from_user: "User",
        query: "str",
        location: "Location" = None,
        inline_message_id: "str" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.result_id = result_id
        self.from_user = from_user
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ChosenInlineResult" | None:
        return (
            ChosenInlineResult(
                client=client,
                result_id=d.get("result_id"),
                from_user=User._parse(d.get("from")),
                query=d.get("query"),
                location=Location._parse(d.get("location")),
                inline_message_id=d.get("inline_message_id"),
            )
            if d
            else None
        )


class SentWebAppMessage(Type_):
    def __init__(self, inline_message_id: "str" = None, client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.inline_message_id = inline_message_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "SentWebAppMessage" | None:
        return (
            SentWebAppMessage(
                client=client,
                inline_message_id=d.get("inline_message_id"),
            )
            if d
            else None
        )


class getStarTransactions(Type_):
    def __init__(
        self, offset: "int" = None, limit: "int" = None, client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.offset = offset
        self.limit = limit

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "getStarTransactions" | None:
        return (
            getStarTransactions(
                client=client,
                offset=d.get("offset"),
                limit=d.get("limit"),
            )
            if d
            else None
        )


class LabeledPrice(Type_):
    def __init__(self, label: "str", amount: "int", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.label = label
        self.amount = amount

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "LabeledPrice" | None:
        return (
            LabeledPrice(
                client=client,
                label=d.get("label"),
                amount=d.get("amount"),
            )
            if d
            else None
        )


class Invoice(Type_):
    def __init__(
        self,
        title: "str",
        description: "str",
        start_parameter: "str",
        currency: "str",
        total_amount: "int",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Invoice" | None:
        return (
            Invoice(
                client=client,
                title=d.get("title"),
                description=d.get("description"),
                start_parameter=d.get("start_parameter"),
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
            )
            if d
            else None
        )


class ShippingAddress(Type_):
    def __init__(
        self,
        country_code: "str",
        state: "str",
        city: "str",
        street_line1: "str",
        street_line2: "str",
        post_code: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "ShippingAddress" | None:
        return (
            ShippingAddress(
                client=client,
                country_code=d.get("country_code"),
                state=d.get("state"),
                city=d.get("city"),
                street_line1=d.get("street_line1"),
                street_line2=d.get("street_line2"),
                post_code=d.get("post_code"),
            )
            if d
            else None
        )


class OrderInfo(Type_):
    def __init__(
        self,
        name: "str" = None,
        phone_number: "str" = None,
        email: "str" = None,
        shipping_address: "ShippingAddress" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "OrderInfo" | None:
        return (
            OrderInfo(
                client=client,
                name=d.get("name"),
                phone_number=d.get("phone_number"),
                email=d.get("email"),
                shipping_address=ShippingAddress._parse(d.get("shipping_address")),
            )
            if d
            else None
        )


class ShippingOption(Type_):
    def __init__(
        self,
        id: "str",
        title: "str",
        prices: List["LabeledPrice"],
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.id = id
        self.title = title
        self.prices = prices

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ShippingOption" | None:
        return (
            ShippingOption(
                client=client,
                id=d.get("id"),
                title=d.get("title"),
                prices=[LabeledPrice._parse(i) for i in d.get("prices")]
                if d.get("prices", None)
                else None,
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "SuccessfulPayment" | None:
        return (
            SuccessfulPayment(
                client=client,
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
                invoice_payload=d.get("invoice_payload"),
                telegram_payment_charge_id=d.get("telegram_payment_charge_id"),
                provider_payment_charge_id=d.get("provider_payment_charge_id"),
                shipping_option_id=d.get("shipping_option_id"),
                order_info=OrderInfo._parse(d.get("order_info")),
            )
            if d
            else None
        )


class ShippingQuery(Type_):
    def __init__(
        self,
        id: "str",
        from_user: "User",
        invoice_payload: "str",
        shipping_address: "ShippingAddress",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "ShippingQuery" | None:
        return (
            ShippingQuery(
                client=client,
                id=d.get("id"),
                from_user=User._parse(d.get("from")),
                invoice_payload=d.get("invoice_payload"),
                shipping_address=ShippingAddress._parse(d.get("shipping_address")),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PreCheckoutQuery" | None:
        return (
            PreCheckoutQuery(
                client=client,
                id=d.get("id"),
                from_user=User._parse(d.get("from")),
                currency=d.get("currency"),
                total_amount=d.get("total_amount"),
                invoice_payload=d.get("invoice_payload"),
                shipping_option_id=d.get("shipping_option_id"),
                order_info=OrderInfo._parse(d.get("order_info")),
            )
            if d
            else None
        )


class RevenueWithdrawalState(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "RevenueWithdrawalState" | None:
        return (
            RevenueWithdrawalState(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class RevenueWithdrawalStatePending(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "RevenueWithdrawalStatePending" | None:
        return (
            RevenueWithdrawalStatePending(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class RevenueWithdrawalStateSucceeded(Type_):
    def __init__(
        self, type: "str", date: "int", url: "str", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.type = type
        self.date = date
        self.url = url

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "RevenueWithdrawalStateSucceeded" | None:
        return (
            RevenueWithdrawalStateSucceeded(
                client=client,
                type=d.get("type"),
                date=d.get("date"),
                url=d.get("url"),
            )
            if d
            else None
        )


class RevenueWithdrawalStateFailed(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "RevenueWithdrawalStateFailed" | None:
        return (
            RevenueWithdrawalStateFailed(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class TransactionPartner(Type_):
    def __init__(
        self,
        type: "str",
        withdrawal_state: "RevenueWithdrawalState" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.withdrawal_state = withdrawal_state

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "TransactionPartner" | None:
        return (
            TransactionPartner(
                client=client,
                type=d.get("type"),
                withdrawal_state=RevenueWithdrawalState._parse(
                    d.get("withdrawal_state")
                ),
            )
            if d
            else None
        )


class TransactionPartnerFragment(Type_):
    def __init__(
        self,
        type: "str",
        withdrawal_state: "RevenueWithdrawalState" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.type = type
        self.withdrawal_state = withdrawal_state

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "TransactionPartnerFragment" | None:
        return (
            TransactionPartnerFragment(
                client=client,
                type=d.get("type"),
                withdrawal_state=RevenueWithdrawalState._parse(
                    d.get("withdrawal_state")
                ),
            )
            if d
            else None
        )


class TransactionPartnerUser(Type_):
    def __init__(self, type: "str", user: "User", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type
        self.user = user

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "TransactionPartnerUser" | None:
        return (
            TransactionPartnerUser(
                client=client,
                type=d.get("type"),
                user=User._parse(d.get("user")),
            )
            if d
            else None
        )


class TransactionPartnerOther(Type_):
    def __init__(self, type: "str", client: "tgram.TgBot" = None):
        super().__init__(client=client)
        self.type = type

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "TransactionPartnerOther" | None:
        return (
            TransactionPartnerOther(
                client=client,
                type=d.get("type"),
            )
            if d
            else None
        )


class StarTransaction(Type_):
    def __init__(
        self,
        id: "str",
        amount: "int",
        date: "int",
        source: "TransactionPartner" = None,
        receiver: "TransactionPartner" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.id = id
        self.amount = amount
        self.date = date
        self.source = source
        self.receiver = receiver

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "StarTransaction" | None:
        return (
            StarTransaction(
                client=client,
                id=d.get("id"),
                amount=d.get("amount"),
                date=d.get("date"),
                source=TransactionPartner._parse(d.get("source")),
                receiver=TransactionPartner._parse(d.get("receiver")),
            )
            if d
            else None
        )


class StarTransactions(Type_):
    def __init__(
        self, transactions: List["StarTransaction"], client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.transactions = transactions

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "StarTransactions" | None:
        return (
            StarTransactions(
                client=client,
                transactions=[StarTransaction._parse(i) for i in d.get("transactions")]
                if d.get("transactions", None)
                else None,
            )
            if d
            else None
        )


class PassportData(Type_):
    def __init__(
        self,
        data: List["EncryptedPassportElement"],
        credentials: "EncryptedCredentials",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.data = data
        self.credentials = credentials

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "PassportData" | None:
        return (
            PassportData(
                client=client,
                data=[EncryptedPassportElement._parse(i) for i in d.get("data")]
                if d.get("data", None)
                else None,
                credentials=EncryptedCredentials._parse(d.get("credentials")),
            )
            if d
            else None
        )


class PassportFile(Type_):
    def __init__(
        self,
        file_id: "str",
        file_unique_id: "str",
        file_size: "int",
        file_date: "int",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "PassportFile" | None:
        return (
            PassportFile(
                client=client,
                file_id=d.get("file_id"),
                file_unique_id=d.get("file_unique_id"),
                file_size=d.get("file_size"),
                file_date=d.get("file_date"),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
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

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "EncryptedPassportElement" | None:
        return (
            EncryptedPassportElement(
                client=client,
                type=d.get("type"),
                hash=d.get("hash"),
                data=d.get("data"),
                phone_number=d.get("phone_number"),
                email=d.get("email"),
                files=[PassportFile._parse(i) for i in d.get("files")]
                if d.get("files", None)
                else None,
                front_side=PassportFile._parse(d.get("front_side")),
                reverse_side=PassportFile._parse(d.get("reverse_side")),
                selfie=PassportFile._parse(d.get("selfie")),
                translation=[PassportFile._parse(i) for i in d.get("translation")]
                if d.get("translation", None)
                else None,
            )
            if d
            else None
        )


class EncryptedCredentials(Type_):
    def __init__(
        self, data: "str", hash: "str", secret: "str", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.data = data
        self.hash = hash
        self.secret = secret

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "EncryptedCredentials" | None:
        return (
            EncryptedCredentials(
                client=client,
                data=d.get("data"),
                hash=d.get("hash"),
                secret=d.get("secret"),
            )
            if d
            else None
        )


class PassportElementError(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        field_name: "str",
        data_hash: "str",
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementError" | None:
        return (
            PassportElementError(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                field_name=d.get("field_name"),
                data_hash=d.get("data_hash"),
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorDataField(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        field_name: "str",
        data_hash: "str",
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorDataField" | None:
        return (
            PassportElementErrorDataField(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                field_name=d.get("field_name"),
                data_hash=d.get("data_hash"),
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorFrontSide(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorFrontSide" | None:
        return (
            PassportElementErrorFrontSide(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorReverseSide(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorReverseSide" | None:
        return (
            PassportElementErrorReverseSide(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorSelfie(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorSelfie" | None:
        return (
            PassportElementErrorSelfie(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorFile(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorFile" | None:
        return (
            PassportElementErrorFile(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorFiles(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hashes: List["str"],
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorFiles" | None:
        return (
            PassportElementErrorFiles(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                file_hashes=[str._parse(i) for i in d.get("file_hashes")]
                if d.get("file_hashes", None)
                else None,
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorTranslationFile(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hash: "str",
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorTranslationFile" | None:
        return (
            PassportElementErrorTranslationFile(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                file_hash=d.get("file_hash"),
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorTranslationFiles(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        file_hashes: List["str"],
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorTranslationFiles" | None:
        return (
            PassportElementErrorTranslationFiles(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                file_hashes=[str._parse(i) for i in d.get("file_hashes")]
                if d.get("file_hashes", None)
                else None,
                message=d.get("message"),
            )
            if d
            else None
        )


class PassportElementErrorUnspecified(Type_):
    def __init__(
        self,
        source: "str",
        type: "str",
        element_hash: "str",
        message: "str",
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message

    @staticmethod
    def _parse(
        client: "tgram.TgBot" = None, d: dict = None
    ) -> "PassportElementErrorUnspecified" | None:
        return (
            PassportElementErrorUnspecified(
                client=client,
                source=d.get("source"),
                type=d.get("type"),
                element_hash=d.get("element_hash"),
                message=d.get("message"),
            )
            if d
            else None
        )


class Game(Type_):
    def __init__(
        self,
        title: "str",
        description: "str",
        photo: List["PhotoSize"],
        text: "str" = None,
        text_entities: List["MessageEntity"] = None,
        animation: "Animation" = None,
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "Game" | None:
        return (
            Game(
                client=client,
                title=d.get("title"),
                description=d.get("description"),
                photo=[PhotoSize._parse(i) for i in d.get("photo")]
                if d.get("photo", None)
                else None,
                text=d.get("text"),
                text_entities=[MessageEntity._parse(i) for i in d.get("text_entities")]
                if d.get("text_entities", None)
                else None,
                animation=Animation._parse(d.get("animation")),
            )
            if d
            else None
        )


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
        client: "tgram.TgBot" = None,
    ):
        super().__init__(client=client)
        self.user_id = user_id
        self.score = score
        self.force = force
        self.disable_edit_message = disable_edit_message
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "CallbackGame" | None:
        return (
            CallbackGame(
                client=client,
                user_id=d.get("user_id"),
                score=d.get("score"),
                force=d.get("force"),
                disable_edit_message=d.get("disable_edit_message"),
                chat_id=d.get("chat_id"),
                message_id=d.get("message_id"),
                inline_message_id=d.get("inline_message_id"),
            )
            if d
            else None
        )


class GameHighScore(Type_):
    def __init__(
        self, position: "int", user: "User", score: "int", client: "tgram.TgBot" = None
    ):
        super().__init__(client=client)
        self.position = position
        self.user = user
        self.score = score

    @staticmethod
    def _parse(client: "tgram.TgBot" = None, d: dict = None) -> "GameHighScore" | None:
        return (
            GameHighScore(
                client=client,
                position=d.get("position"),
                user=User._parse(d.get("user")),
                score=d.get("score"),
            )
            if d
            else None
        )
