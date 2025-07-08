import tgram
from .type_ import Type_

from typing import List, Optional
from tgram import bound
from tgram.utils import String, message_origin_parse


class Message(Type_, bound.MessageB):
    """
    This object represents a message.

    Telegram Documentation: https://core.telegram.org/bots/api#message

    :param message_id: Unique message identifier inside this chat
    :type message_id: :obj:`int`

    :param message_thread_id: Optional. Unique identifier of a message thread to which the message belongs; for supergroups only
    :type message_thread_id: :obj:`int`

    :param from_user: Optional. Sender of the message; empty for messages sent to channels. For backward compatibility, the
        field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    :type from_user: :class:`tgram.types.User`

    :param sender_chat: Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself for
        channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for
        messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a
        fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    :type sender_chat: :class:`tgram.types.Chat`

    :param sender_boost_count: Optional. If the sender of the message boosted the chat, the number of boosts added by the user
    :type sender_boost_count: :obj:`int`

    :param sender_business_bot info: Optional. Information about the business bot that sent the message
    :type sender_business_bot_info: :class:`tgram.types.User`

    :param date: Date the message was sent in Unix time
    :type date: :obj:`int`

    :param business_connection_id: Optional. Unique identifier of the business connection from which the message was received. If non-empty,
        the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.
    :type business_connection_id: :obj:`str`

    :param chat: Conversation the message belongs to
    :type chat: :class:`tgram.types.Chat`

    :forward_origin: Optional. For forwarded messages, information about the original message;
    :type forward_origin: :class:`tgram.types.MessageOrigin`

    :param is_topic_message: Optional. True, if the message is sent to a forum topic
    :type is_topic_message: :obj:`bool`

    :param is_automatic_forward: Optional. :obj:`bool`, if the message is a channel post that was automatically
        forwarded to the connected discussion group
    :type is_automatic_forward: :obj:`bool`

    :param reply_to_message: Optional. For replies, the original message. Note that the Message object in this field
        will not contain further reply_to_message fields even if it itself is a reply.
    :type reply_to_message: :class:`tgram.types.Message`

    :param external_reply: Optional. Information about the message that is being replied to, which may come from another chat or forum topic
    :type external_reply: :class:`tgram.types.ExternalReplyInfo`

    :param quote: Optional. For replies that quote part of the original message, the quoted part of the message
    :type quote: :class:`tgram.types.TextQuote`

    :param reply_to_story: Optional. For replies to a story, the original story
    :type reply_to_story: :class:`tgram.types.Story`

    :param via_bot: Optional. Bot through which the message was sent
    :type via_bot: :class:`tgram.types.User`

    :param edit_date: Optional. Date the message was last edited in Unix time
    :type edit_date: :obj:`int`

    :param has_protected_content: Optional. :obj:`bool`, if the message can't be forwarded
    :type has_protected_content: :obj:`bool`

    :param is_from_offline: Optional. True, if the message was sent by an implicit action, for example,
        as an away or a greeting business message, or as a scheduled message
    :type is_from_offline: :obj:`bool`

    :param media_group_id: Optional. The unique identifier of a media message group this message belongs to
    :type media_group_id: :obj:`str`

    :param author_signature: Optional. Signature of the post author for messages in channels, or the custom title of an
        anonymous group administrator
    :type author_signature: :obj:`str`

    :param text: Optional. For text messages, the actual UTF-8 text of the message
    :type text: :class:`tgram.utils.String`

    :param entities: Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that
        appear in the text
    :type entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param link_preview_options: Optional. Options used for link preview generation for the message,
        if it is a text message and link preview options were changed
    :type link_preview_options: :class:`tgram.types.LinkPreviewOptions`

    :param effect_id: Optional. Unique identifier of the message effect added to the message
    :type effect_id: :obj:`str`

    :param animation: Optional. Message is an animation, information about the animation. For backward
        compatibility, when this field is set, the document field will also be set
    :type animation: :class:`tgram.types.Animation`

    :param audio: Optional. Message is an audio file, information about the file
    :type audio: :class:`tgram.types.Audio`

    :param document: Optional. Message is a general file, information about the file
    :type document: :class:`tgram.types.Document`

    :param photo: Optional. Message is a photo, available sizes of the photo
    :type photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param sticker: Optional. Message is a sticker, information about the sticker
    :type sticker: :class:`tgram.types.Sticker`

    :param story: Optional. Message is a forwarded story
    :type story: :class:`tgram.types.Story`

    :param video: Optional. Message is a video, information about the video
    :type video: :class:`tgram.types.Video`

    :param video_note: Optional. Message is a video note, information about the video message
    :type video_note: :class:`tgram.types.VideoNote`

    :param voice: Optional. Message is a voice message, information about the file
    :type voice: :class:`tgram.types.Voice`

    :param caption: Optional. Caption for the animation, audio, document, photo, video or voice
    :type caption: :obj:`str`

    :param caption_entities: Optional. For messages with a caption, special entities like usernames, URLs, bot
        commands, etc. that appear in the caption
    :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param show_caption_above_media: Optional. True, if the caption must be shown above the message media
    :type show_caption_above_media: :obj:`bool`

    :param has_media_spoiler: Optional. True, if the message media is covered by a spoiler animation
    :type has_media_spoiler: :obj:`bool`

    :param checklist: Optional. Message is a checklist
    :type checklist: :class:`tgram.types.Checklist`

    :param contact: Optional. Message is a shared contact, information about the contact
    :type contact: :class:`tgram.types.Contact`

    :param dice: Optional. Message is a dice with random value
    :type dice: :class:`tgram.types.Dice`

    :param game: Optional. Message is a game, information about the game. More about games »
    :type game: :class:`tgram.types.Game`

    :param poll: Optional. Message is a native poll, information about the poll
    :type poll: :class:`tgram.types.Poll`

    :param venue: Optional. Message is a venue, information about the venue. For backward compatibility, when this
        field is set, the location field will also be set
    :type venue: :class:`tgram.types.Venue`

    :param location: Optional. Message is a shared location, information about the location
    :type location: :class:`tgram.types.Location`

    :param new_chat_members: Optional. New members that were added to the group or supergroup and information about
        them (the bot itself may be one of these members)
    :type new_chat_members: :obj:`list` of :class:`tgram.types.User`

    :param left_chat_member: Optional. A member was removed from the group, information about them (this member may be
        the bot itself)
    :type left_chat_member: :class:`tgram.types.User`

    :param new_chat_title: Optional. A chat title was changed to this value
    :type new_chat_title: :obj:`str`

    :param new_chat_photo: Optional. A chat photo was change to this value
    :type new_chat_photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param delete_chat_photo: Optional. Service message: the chat photo was deleted
    :type delete_chat_photo: :obj:`bool`

    :param group_chat_created: Optional. Service message: the group has been created
    :type group_chat_created: :obj:`bool`

    :param supergroup_chat_created: Optional. Service message: the supergroup has been created. This field can't be
        received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can
        only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    :type supergroup_chat_created: :obj:`bool`

    :param channel_chat_created: Optional. Service message: the channel has been created. This field can't be
        received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only
        be found in reply_to_message if someone replies to a very first message in a channel.
    :type channel_chat_created: :obj:`bool`

    :param message_auto_delete_timer_changed: Optional. Service message: auto-delete timer settings changed in
        the chat
    :type message_auto_delete_timer_changed: :class:`tgram.types.MessageAutoDeleteTimerChanged`

    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier.
        This number may have more than 32 significant bits and some programming languages may have difficulty/silent
        defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision
        float type are safe for storing this identifier.
    :type migrate_to_chat_id: :obj:`int`

    :param migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified
        identifier. This number may have more than 32 significant bits and some programming languages may have
        difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this identifier.
    :type migrate_from_chat_id: :obj:`int`

    :param pinned_message: Optional. Specified message was pinned. Note that the Message object in this field will not
        contain further reply_to_message fields even if it is itself a reply.
    :type pinned_message: :class:`tgram.types.Message` or :class:`tgram.types.InaccessibleMessage`

    :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More about payments »
    :type invoice: :class:`tgram.types.Invoice`

    :param successful_payment: Optional. Message is a service message about a successful payment, information about
        the payment. More about payments »
    :type successful_payment: :class:`tgram.types.SuccessfulPayment`

    :param users_shared: Optional. Service message: a user was shared with the bot
    :type users_shared: :class:`tgram.types.UsersShared`

    :param chat_shared: Optional. Service message: a chat was shared with the bot
    :type chat_shared: :class:`tgram.types.ChatShared`

    :param gift: Optional. Service message: a regular gift was sent or received
        :type gift: :class:`tgram.types.GiftInfo`

    :param unique_gift: Optional. Service message: a unique gift was sent or received
    :type unique_gift: :class:`tgram.types.UniqueGiftInfo`

    :param connected_website: Optional. The domain name of the website on which the user has logged in. More about
        Telegram Login »
    :type connected_website: :obj:`str`

    :param write_access_allowed: Optional. Service message: the user allowed the bot added to the attachment
        menu to write messages
    :type write_access_allowed: :class:`tgram.types.WriteAccessAllowed`

    :param passport_data: Optional. Telegram Passport data
    :type passport_data: :class:`tgram.types.PassportData`

    :param proximity_alert_triggered: Optional. Service message. A user in the chat triggered another user's
        proximity alert while sharing Live Location.
    :type proximity_alert_triggered: :class:`tgram.types.ProximityAlertTriggered`

    :param boost_added: Optional. Service message: user boosted the chat
    :type boost_added: :class:`tgram.types.ChatBoostAdded`

    :param chat_background_set: Optional. Service message: chat background set
    :type chat_background_set: :class:`tgram.types.ChatBackground`

    :param checklist_tasks_done: Optional. Service message: some tasks in a checklist were marked as done or not done
    :type checklist_tasks_done: :class:`tgram.types.ChecklistTasksDone`

    :param forum_topic_created: Optional. Service message: forum topic created
    :type forum_topic_created: :class:`tgram.types.ForumTopicCreated`

    :param forum_topic_edited: Optional. Service message: forum topic edited
    :type forum_topic_edited: :class:`tgram.types.ForumTopicEdited`

    :param forum_topic_closed: Optional. Service message: forum topic closed
    :type forum_topic_closed: :class:`tgram.types.ForumTopicClosed`

    :param forum_topic_reopened: Optional. Service message: forum topic reopened
    :type forum_topic_reopened: :class:`tgram.types.ForumTopicReopened`

    :param general_forum_topic_hidden: Optional. Service message: the 'General' forum topic hidden
    :type general_forum_topic_hidden: :class:`tgram.types.GeneralForumTopicHidden`

    :param general_forum_topic_unhidden: Optional. Service message: the 'General' forum topic unhidden
    :type general_forum_topic_unhidden: :class:`tgram.types.GeneralForumTopicUnhidden`

    :param giveaway_created: Optional. Service message: a giveaway has been created
    :type giveaway_created: :class:`tgram.types.GiveawayCreated`

    :param giveaway: Optional. The message is a scheduled giveaway message
    :type giveaway: :class:`tgram.types.Giveaway`

    :param giveaway_winners: Optional. Service message: giveaway winners(public winners)
    :type giveaway_winners: :class:`tgram.types.GiveawayWinners`

    :param giveaway_completed: Optional. Service message: giveaway completed, without public winners
    :type giveaway_completed: :class:`tgram.types.GiveawayCompleted`

    :param video_chat_scheduled: Optional. Service message: video chat scheduled
    :type video_chat_scheduled: :class:`tgram.types.VideoChatScheduled`

    :param video_chat_started: Optional. Service message: video chat started
    :type video_chat_started: :class:`tgram.types.VideoChatStarted`

    :param video_chat_ended: Optional. Service message: video chat ended
    :type video_chat_ended: :class:`tgram.types.VideoChatEnded`

    :param video_chat_participants_invited: Optional. Service message: new participants invited to a video chat
    :type video_chat_participants_invited: :class:`tgram.types.VideoChatParticipantsInvited`

    :param web_app_data: Optional. Service message: data sent by a Web App
    :type web_app_data: :class:`tgram.types.WebAppData`

    :param reply_markup: Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param paid_message_price_changed: Optional. Service message: the price for paid messages has changed in the chat
    :type paid_message_price_changed: :class:`tgram.types.PaidMessagePriceChanged`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Message`
    """

    def __init__(
        self,
        message_id: "int" = None,
        date: "int" = None,
        chat: "tgram.types.Chat" = None,
        message_thread_id: "int" = None,
        from_user: "tgram.types.User" = None,
        sender_chat: "tgram.types.Chat" = None,
        sender_boost_count: "int" = None,
        sender_business_bot: "tgram.types.User" = None,
        business_connection_id: "str" = None,
        forward_origin: "tgram.types.MessageOrigin" = None,
        is_topic_message: "bool" = None,
        is_automatic_forward: "bool" = None,
        reply_to_message: "tgram.types.Message" = None,
        external_reply: "tgram.types.ExternalReplyInfo" = None,
        quote: "tgram.types.TextQuote" = None,
        reply_to_story: "tgram.types.Story" = None,
        via_bot: "tgram.types.User" = None,
        edit_date: "int" = None,
        has_protected_content: "bool" = None,
        is_from_offline: "bool" = None,
        media_group_id: "str" = None,
        author_signature: "str" = None,
        text: "String" = None,
        entities: List["tgram.types.MessageEntity"] = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        effect_id: "str" = None,
        animation: "tgram.types.Animation" = None,
        audio: "tgram.types.Audio" = None,
        document: "tgram.types.Document" = None,
        paid_media: "tgram.types.PaidMediaInfo" = None,
        photo: List["tgram.types.PhotoSize"] = None,
        sticker: "tgram.types.Sticker" = None,
        story: "tgram.types.Story" = None,
        video: "tgram.types.Video" = None,
        video_note: "tgram.types.VideoNote" = None,
        voice: "tgram.types.Voice" = None,
        caption: "String" = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        show_caption_above_media: "bool" = None,
        has_media_spoiler: "bool" = None,
        checklist: "tgram.types.Checklist" = None,
        contact: "tgram.types.Contact" = None,
        dice: "tgram.types.Dice" = None,
        game: "tgram.types.Game" = None,
        poll: "tgram.types.Poll" = None,
        venue: "tgram.types.Venue" = None,
        location: "tgram.types.Location" = None,
        new_chat_members: List["tgram.types.User"] = None,
        left_chat_member: "tgram.types.User" = None,
        new_chat_title: "str" = None,
        new_chat_photo: List["tgram.types.PhotoSize"] = None,
        delete_chat_photo: "bool" = None,
        group_chat_created: "bool" = None,
        supergroup_chat_created: "bool" = None,
        channel_chat_created: "bool" = None,
        message_auto_delete_timer_changed: "tgram.types.MessageAutoDeleteTimerChanged" = None,
        migrate_to_chat_id: "int" = None,
        migrate_from_chat_id: "int" = None,
        pinned_message: "tgram.types.Message" = None,
        invoice: "tgram.types.Invoice" = None,
        successful_payment: "tgram.types.SuccessfulPayment" = None,
        refunded_payment: "tgram.types.RefundedPayment" = None,
        users_shared: "tgram.types.UsersShared" = None,
        chat_shared: "tgram.types.ChatShared" = None,
        gift: "tgram.types.GiftInfo" = None,
        unique_gift: "tgram.types.UniqueGiftInfo" = None,
        connected_website: "str" = None,
        write_access_allowed: "tgram.types.WriteAccessAllowed" = None,
        passport_data: "tgram.types.PassportData" = None,
        proximity_alert_triggered: "tgram.types.ProximityAlertTriggered" = None,
        boost_added: "tgram.types.ChatBoostAdded" = None,
        chat_background_set: "tgram.types.ChatBackground" = None,
        checklist_tasks_done: "tgram.types.ChecklistTasksDone" = None,
        forum_topic_created: "tgram.types.ForumTopicCreated" = None,
        forum_topic_edited: "tgram.types.ForumTopicEdited" = None,
        forum_topic_closed: "tgram.types.ForumTopicClosed" = None,
        forum_topic_reopened: "tgram.types.ForumTopicReopened" = None,
        general_forum_topic_hidden: "tgram.types.GeneralForumTopicHidden" = None,
        general_forum_topic_unhidden: "tgram.types.GeneralForumTopicUnhidden" = None,
        giveaway_created: "tgram.types.GiveawayCreated" = None,
        giveaway: "tgram.types.Giveaway" = None,
        giveaway_winners: "tgram.types.GiveawayWinners" = None,
        giveaway_completed: "tgram.types.GiveawayCompleted" = None,
        paid_message_price_changed: "tgram.types.PaidMessagePriceChanged" = None,
        video_chat_scheduled: "tgram.types.VideoChatScheduled" = None,
        video_chat_started: "tgram.types.VideoChatStarted" = None,
        video_chat_ended: "tgram.types.VideoChatEnded" = None,
        video_chat_participants_invited: "tgram.types.VideoChatParticipantsInvited" = None,
        web_app_data: "tgram.types.WebAppData" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
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
        self.text = String(text).put(entities) if text else None
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.effect_id = effect_id
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paid_media = paid_media
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = String(caption).put(caption_entities) if caption else None
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_media_spoiler = has_media_spoiler
        self.checklist = checklist
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
        self.refunded_payment = refunded_payment
        self.users_shared = users_shared
        self.chat_shared = chat_shared
        self.gift = gift
        self.unique_gift = unique_gift
        self.connected_website = connected_website
        self.write_access_allowed = write_access_allowed
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.boost_added = boost_added
        self.chat_background_set = chat_background_set
        self.checklist_tasks_done = checklist_tasks_done
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
        self.paid_message_price_changed = paid_message_price_changed
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Message"]:
        return (
            Message(
                me=me,
                json=d,
                message_id=d.get("message_id"),
                date=d.get("date"),
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                message_thread_id=d.get("message_thread_id"),
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                sender_chat=tgram.types.Chat._parse(me=me, d=d.get("sender_chat")),
                sender_boost_count=d.get("sender_boost_count"),
                sender_business_bot=tgram.types.User._parse(
                    me=me, d=d.get("sender_business_bot")
                ),
                business_connection_id=d.get("business_connection_id"),
                forward_origin=message_origin_parse(d.get("forward_origin"), me),
                is_topic_message=d.get("is_topic_message"),
                is_automatic_forward=d.get("is_automatic_forward"),
                reply_to_message=tgram.types.Message._parse(
                    me=me, d=d.get("reply_to_message")
                ),
                external_reply=tgram.types.ExternalReplyInfo._parse(
                    me=me, d=d.get("external_reply")
                ),
                quote=tgram.types.TextQuote._parse(me=me, d=d.get("quote")),
                reply_to_story=tgram.types.Story._parse(
                    me=me, d=d.get("reply_to_story")
                ),
                via_bot=tgram.types.User._parse(me=me, d=d.get("via_bot")),
                edit_date=d.get("edit_date"),
                has_protected_content=d.get("has_protected_content"),
                is_from_offline=d.get("is_from_offline"),
                media_group_id=d.get("media_group_id"),
                author_signature=d.get("author_signature"),
                text=d.get("text"),
                entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("entities")
                ]
                if d.get("entities")
                else None,
                link_preview_options=tgram.types.LinkPreviewOptions._parse(
                    me=me, d=d.get("link_preview_options")
                ),
                effect_id=d.get("effect_id"),
                animation=tgram.types.Animation._parse(me=me, d=d.get("animation")),
                audio=tgram.types.Audio._parse(me=me, d=d.get("audio")),
                document=tgram.types.Document._parse(me=me, d=d.get("document")),
                paid_media=tgram.types.PaidMediaInfo._parse(
                    me=me, d=d.get("paid_media")
                ),
                photo=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
                sticker=tgram.types.Sticker._parse(me=me, d=d.get("sticker")),
                story=tgram.types.Story._parse(me=me, d=d.get("story")),
                video=tgram.types.Video._parse(me=me, d=d.get("video")),
                video_note=tgram.types.VideoNote._parse(me=me, d=d.get("video_note")),
                voice=tgram.types.Voice._parse(me=me, d=d.get("voice")),
                caption=d.get("caption"),
                caption_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("caption_entities")
                ]
                if d.get("caption_entities")
                else None,
                show_caption_above_media=d.get("show_caption_above_media"),
                has_media_spoiler=d.get("has_media_spoiler"),
                checklist=tgram.types.Checklist._parse(me=me, d=d.get("checklist")),
                contact=tgram.types.Contact._parse(me=me, d=d.get("contact")),
                dice=tgram.types.Dice._parse(me=me, d=d.get("dice")),
                game=tgram.types.Game._parse(me=me, d=d.get("game")),
                poll=tgram.types.Poll._parse(me=me, d=d.get("poll")),
                venue=tgram.types.Venue._parse(me=me, d=d.get("venue")),
                location=tgram.types.Location._parse(me=me, d=d.get("location")),
                new_chat_members=[
                    tgram.types.User._parse(me=me, d=i)
                    for i in d.get("new_chat_members")
                ]
                if d.get("new_chat_members")
                else None,
                left_chat_member=tgram.types.User._parse(
                    me=me, d=d.get("left_chat_member")
                ),
                new_chat_title=d.get("new_chat_title"),
                new_chat_photo=[
                    tgram.types.PhotoSize._parse(me=me, d=i)
                    for i in d.get("new_chat_photo")
                ]
                if d.get("new_chat_photo")
                else None,
                delete_chat_photo=d.get("delete_chat_photo"),
                group_chat_created=d.get("group_chat_created"),
                supergroup_chat_created=d.get("supergroup_chat_created"),
                channel_chat_created=d.get("channel_chat_created"),
                message_auto_delete_timer_changed=tgram.types.MessageAutoDeleteTimerChanged._parse(
                    me=me, d=d.get("message_auto_delete_timer_changed")
                ),
                migrate_to_chat_id=d.get("migrate_to_chat_id"),
                migrate_from_chat_id=d.get("migrate_from_chat_id"),
                pinned_message=tgram.types.Message._parse(
                    me=me, d=d.get("pinned_message")
                ),
                invoice=tgram.types.Invoice._parse(me=me, d=d.get("invoice")),
                successful_payment=tgram.types.SuccessfulPayment._parse(
                    me=me, d=d.get("successful_payment")
                ),
                refunded_payment=tgram.types.RefundedPayment._parse(
                    me=me, d=d.get("refunded_payment")
                ),
                users_shared=tgram.types.UsersShared._parse(
                    me=me, d=d.get("users_shared")
                ),
                chat_shared=tgram.types.ChatShared._parse(
                    me=me, d=d.get("chat_shared")
                ),
                gift=tgram.types.GiftInfo._parse(me=me, d=d.get("gift")),
                unique_gift=tgram.types.UniqueGiftInfo._parse(
                    me=me, d=d.get("unique_gift")
                ),
                connected_website=d.get("connected_website"),
                write_access_allowed=tgram.types.WriteAccessAllowed._parse(
                    me=me, d=d.get("write_access_allowed")
                ),
                passport_data=tgram.types.PassportData._parse(
                    me=me, d=d.get("passport_data")
                ),
                proximity_alert_triggered=tgram.types.ProximityAlertTriggered._parse(
                    me=me, d=d.get("proximity_alert_triggered")
                ),
                boost_added=tgram.types.ChatBoostAdded._parse(
                    me=me, d=d.get("boost_added")
                ),
                chat_background_set=tgram.types.ChatBackground._parse(
                    me=me, d=d.get("chat_background_set")
                ),
                checklist_tasks_done=tgram.types.ChecklistTasksDone._parse(
                    me=me, d=d.get("checklist_tasks_done")
                ),
                forum_topic_created=tgram.types.ForumTopicCreated._parse(
                    me=me, d=d.get("forum_topic_created")
                ),
                forum_topic_edited=tgram.types.ForumTopicEdited._parse(
                    me=me, d=d.get("forum_topic_edited")
                ),
                forum_topic_closed=tgram.types.ForumTopicClosed._parse(
                    me=me, d=d.get("forum_topic_closed")
                ),
                forum_topic_reopened=tgram.types.ForumTopicReopened._parse(
                    me=me, d=d.get("forum_topic_reopened")
                ),
                general_forum_topic_hidden=tgram.types.GeneralForumTopicHidden._parse(
                    me=me, d=d.get("general_forum_topic_hidden")
                ),
                general_forum_topic_unhidden=tgram.types.GeneralForumTopicUnhidden._parse(
                    me=me, d=d.get("general_forum_topic_unhidden")
                ),
                giveaway_created=tgram.types.GiveawayCreated._parse(
                    me=me, d=d.get("giveaway_created")
                ),
                giveaway=tgram.types.Giveaway._parse(me=me, d=d.get("giveaway")),
                giveaway_winners=tgram.types.GiveawayWinners._parse(
                    me=me, d=d.get("giveaway_winners")
                ),
                giveaway_completed=tgram.types.GiveawayCompleted._parse(
                    me=me, d=d.get("giveaway_completed")
                ),
                paid_message_price_changed=tgram.types.PaidMessagePriceChanged._parse(
                    me=me, d=d.get("paid_message_price_changed")
                ),
                video_chat_scheduled=tgram.types.VideoChatScheduled._parse(
                    me=me, d=d.get("video_chat_scheduled")
                ),
                video_chat_started=tgram.types.VideoChatStarted._parse(
                    me=me, d=d.get("video_chat_started")
                ),
                video_chat_ended=tgram.types.VideoChatEnded._parse(
                    me=me, d=d.get("video_chat_ended")
                ),
                video_chat_participants_invited=tgram.types.VideoChatParticipantsInvited._parse(
                    me=me, d=d.get("video_chat_participants_invited")
                ),
                web_app_data=tgram.types.WebAppData._parse(
                    me=me, d=d.get("web_app_data")
                ),
                reply_markup=tgram.types.InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
