# Message

**This object represents a message.**

## Properties

- **`message_id`** (**`int`**): **Unique message identifier inside this chat**
- **`date`** (**`int`**): **Date the message was sent in Unix time**
- **`chat`** (**[Chat](Chat.md)**): **Conversation the message belongs to**
- **`message_thread_id`** (**`int`**): **Optional. Unique identifier of a message thread to which the message belongs; for supergroups only**
- **`from_user`** (**[User](User.md)**): **Optional. Sender of the message; empty for messages sent to channels. For backward compatibility, the
field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.**
- **`sender_chat`** (**[Chat](Chat.md)**): **Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself for
channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for
messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a
fake sender user in non-channel chats, if the message was sent on behalf of a chat.**
- **`sender_boost_count`** (**`int`**): **Optional. If the sender of the message boosted the chat, the number of boosts added by the user**
- **`sender_business_bot`** (**[User](User.md)**)
- **`business_connection_id`** (**`str`**): **Optional. Unique identifier of the business connection from which the message was received. If non-empty,
the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.**
- **`forward_origin`** (**`MessageOrigin`**)
- **`is_topic_message`** (**`bool`**): **Optional. True, if the message is sent to a forum topic**
- **`is_automatic_forward`** (**`bool`**): **Optional. :obj:`bool`, if the message is a channel post that was automatically
forwarded to the connected discussion group**
- **`reply_to_message`** (**[Message](Message.md)**): **Optional. For replies, the original message. Note that the Message object in this field
will not contain further reply_to_message fields even if it itself is a reply.**
- **`external_reply`** (**[ExternalReplyInfo](ExternalReplyInfo.md)**): **Optional. Information about the message that is being replied to, which may come from another chat or forum topic**
- **`quote`** (**[TextQuote](TextQuote.md)**): **Optional. For replies that quote part of the original message, the quoted part of the message**
- **`reply_to_story`** (**[Story](Story.md)**): **Optional. For replies to a story, the original story**
- **`via_bot`** (**[User](User.md)**): **Optional. Bot through which the message was sent**
- **`edit_date`** (**`int`**): **Optional. Date the message was last edited in Unix time**
- **`has_protected_content`** (**`bool`**): **Optional. :obj:`bool`, if the message can't be forwarded**
- **`is_from_offline`** (**`bool`**): **Optional. True, if the message was sent by an implicit action, for example,
as an away or a greeting business message, or as a scheduled message**
- **`media_group_id`** (**`str`**): **Optional. The unique identifier of a media message group this message belongs to**
- **`author_signature`** (**`str`**): **Optional. Signature of the post author for messages in channels, or the custom title of an
anonymous group administrator**
- **`text`** (**`String`**): **Optional. For text messages, the actual UTF-8 text of the message**
- **`entities`** (**List of `tgram.types.MessageEntity`**): **Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that
appear in the text**
- **`link_preview_options`** (**[LinkPreviewOptions](LinkPreviewOptions.md)**): **Optional. Options used for link preview generation for the message,
if it is a text message and link preview options were changed**
- **`effect_id`** (**`str`**): **Optional. Unique identifier of the message effect added to the message**
- **`animation`** (**[Animation](Animation.md)**): **Optional. Message is an animation, information about the animation. For backward
compatibility, when this field is set, the document field will also be set**
- **`audio`** (**[Audio](Audio.md)**): **Optional. Message is an audio file, information about the file**
- **`document`** (**[Document](Document.md)**): **Optional. Message is a general file, information about the file**
- **`paid_media`** (**[PaidMediaInfo](PaidMediaInfo.md)**)
- **`photo`** (**List of `tgram.types.PhotoSize`**): **Optional. Message is a photo, available sizes of the photo**
- **`sticker`** (**[Sticker](Sticker.md)**): **Optional. Message is a sticker, information about the sticker**
- **`story`** (**[Story](Story.md)**): **Optional. Message is a forwarded story**
- **`video`** (**[Video](Video.md)**): **Optional. Message is a video, information about the video**
- **`video_note`** (**[VideoNote](VideoNote.md)**): **Optional. Message is a video note, information about the video message**
- **`voice`** (**[Voice](Voice.md)**): **Optional. Message is a voice message, information about the file**
- **`caption`** (**`String`**): **Optional. Caption for the animation, audio, document, photo, video or voice**
- **`caption_entities`** (**List of `tgram.types.MessageEntity`**): **Optional. For messages with a caption, special entities like usernames, URLs, bot
commands, etc. that appear in the caption**
- **`show_caption_above_media`** (**`bool`**): **Optional. True, if the caption must be shown above the message media**
- **`has_media_spoiler`** (**`bool`**): **Optional. True, if the message media is covered by a spoiler animation**
- **`checklist`** (**[Checklist](Checklist.md)**): **Optional. Message is a checklist**
- **`contact`** (**[Contact](Contact.md)**): **Optional. Message is a shared contact, information about the contact**
- **`dice`** (**[Dice](Dice.md)**): **Optional. Message is a dice with random value**
- **`game`** (**[Game](Game.md)**): **Optional. Message is a game, information about the game. More about games »**
- **`poll`** (**[Poll](Poll.md)**): **Optional. Message is a native poll, information about the poll**
- **`venue`** (**[Venue](Venue.md)**): **Optional. Message is a venue, information about the venue. For backward compatibility, when this
field is set, the location field will also be set**
- **`location`** (**[Location](Location.md)**): **Optional. Message is a shared location, information about the location**
- **`new_chat_members`** (**List of `tgram.types.User`**): **Optional. New members that were added to the group or supergroup and information about
them (the bot itself may be one of these members)**
- **`left_chat_member`** (**[User](User.md)**): **Optional. A member was removed from the group, information about them (this member may be
the bot itself)**
- **`new_chat_title`** (**`str`**): **Optional. A chat title was changed to this value**
- **`new_chat_photo`** (**List of `tgram.types.PhotoSize`**): **Optional. A chat photo was change to this value**
- **`delete_chat_photo`** (**`bool`**): **Optional. Service message: the chat photo was deleted**
- **`group_chat_created`** (**`bool`**): **Optional. Service message: the group has been created**
- **`supergroup_chat_created`** (**`bool`**): **Optional. Service message: the supergroup has been created. This field can't be
received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can
only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.**
- **`channel_chat_created`** (**`bool`**): **Optional. Service message: the channel has been created. This field can't be
received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only
be found in reply_to_message if someone replies to a very first message in a channel.**
- **`message_auto_delete_timer_changed`** (**[MessageAutoDeleteTimerChanged](MessageAutoDeleteTimerChanged.md)**): **Optional. Service message: auto-delete timer settings changed in
the chat**
- **`migrate_to_chat_id`** (**`int`**): **Optional. The group has been migrated to a supergroup with the specified identifier.
This number may have more than 32 significant bits and some programming languages may have difficulty/silent
defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision
float type are safe for storing this identifier.**
- **`migrate_from_chat_id`** (**`int`**): **Optional. The supergroup has been migrated from a group with the specified
identifier. This number may have more than 32 significant bits and some programming languages may have
difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or
double-precision float type are safe for storing this identifier.**
- **`pinned_message`** (**[Message](Message.md)**): **Optional. Specified message was pinned. Note that the Message object in this field will not
contain further reply_to_message fields even if it is itself a reply.**
- **`invoice`** (**[Invoice](Invoice.md)**): **Optional. Message is an invoice for a payment, information about the invoice. More about payments »**
- **`successful_payment`** (**[SuccessfulPayment](SuccessfulPayment.md)**): **Optional. Message is a service message about a successful payment, information about
the payment. More about payments »**
- **`refunded_payment`** (**[RefundedPayment](RefundedPayment.md)**)
- **`users_shared`** (**[UsersShared](UsersShared.md)**): **Optional. Service message: a user was shared with the bot**
- **`chat_shared`** (**[ChatShared](ChatShared.md)**): **Optional. Service message: a chat was shared with the bot**
- **`gift`** (**[GiftInfo](GiftInfo.md)**): **Optional. Service message: a regular gift was sent or received
:type gift: :class:`tgram.types.GiftInfo`**
- **`unique_gift`** (**[UniqueGiftInfo](UniqueGiftInfo.md)**): **Optional. Service message: a unique gift was sent or received**
- **`connected_website`** (**`str`**): **Optional. The domain name of the website on which the user has logged in. More about
Telegram Login »**
- **`write_access_allowed`** (**[WriteAccessAllowed](WriteAccessAllowed.md)**): **Optional. Service message: the user allowed the bot added to the attachment
menu to write messages**
- **`passport_data`** (**[PassportData](PassportData.md)**): **Optional. Telegram Passport data**
- **`proximity_alert_triggered`** (**[ProximityAlertTriggered](ProximityAlertTriggered.md)**): **Optional. Service message. A user in the chat triggered another user's
proximity alert while sharing Live Location.**
- **`boost_added`** (**[ChatBoostAdded](ChatBoostAdded.md)**): **Optional. Service message: user boosted the chat**
- **`chat_background_set`** (**[ChatBackground](ChatBackground.md)**): **Optional. Service message: chat background set**
- **`checklist_tasks_done`** (**[ChecklistTasksDone](ChecklistTasksDone.md)**): **Optional. Service message: some tasks in a checklist were marked as done or not done**
- **`checklist_tasks_added`** (**[ChecklistTasksAdded](ChecklistTasksAdded.md)**): **Optional. Service message: tasks were added to a checklist**
- **`direct_message_price_changed`** (**[DirectMessagePriceChanged](DirectMessagePriceChanged.md)**): **Optional. Service message: the price for paid messages in the corresponding direct messages chat of a channel has changed**
- **`forum_topic_created`** (**[ForumTopicCreated](ForumTopicCreated.md)**): **Optional. Service message: forum topic created**
- **`forum_topic_edited`** (**[ForumTopicEdited](ForumTopicEdited.md)**): **Optional. Service message: forum topic edited**
- **`forum_topic_closed`** (**[ForumTopicClosed](ForumTopicClosed.md)**): **Optional. Service message: forum topic closed**
- **`forum_topic_reopened`** (**[ForumTopicReopened](ForumTopicReopened.md)**): **Optional. Service message: forum topic reopened**
- **`general_forum_topic_hidden`** (**[GeneralForumTopicHidden](GeneralForumTopicHidden.md)**): **Optional. Service message: the 'General' forum topic hidden**
- **`general_forum_topic_unhidden`** (**[GeneralForumTopicUnhidden](GeneralForumTopicUnhidden.md)**): **Optional. Service message: the 'General' forum topic unhidden**
- **`giveaway_created`** (**[GiveawayCreated](GiveawayCreated.md)**): **Optional. Service message: a giveaway has been created**
- **`giveaway`** (**[Giveaway](Giveaway.md)**): **Optional. The message is a scheduled giveaway message**
- **`giveaway_winners`** (**[GiveawayWinners](GiveawayWinners.md)**): **Optional. Service message: giveaway winners(public winners)**
- **`giveaway_completed`** (**[GiveawayCompleted](GiveawayCompleted.md)**): **Optional. Service message: giveaway completed, without public winners**
- **`paid_message_price_changed`** (**[PaidMessagePriceChanged](PaidMessagePriceChanged.md)**): **Optional. Service message: the price for paid messages has changed in the chat**
- **`video_chat_scheduled`** (**[VideoChatScheduled](VideoChatScheduled.md)**): **Optional. Service message: video chat scheduled**
- **`video_chat_started`** (**[VideoChatStarted](VideoChatStarted.md)**): **Optional. Service message: video chat started**
- **`video_chat_ended`** (**[VideoChatEnded](VideoChatEnded.md)**): **Optional. Service message: video chat ended**
- **`video_chat_participants_invited`** (**[VideoChatParticipantsInvited](VideoChatParticipantsInvited.md)**): **Optional. Service message: new participants invited to a video chat**
- **`web_app_data`** (**[WebAppData](WebAppData.md)**): **Optional. Service message: data sent by a Web App**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)**): **Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.**
