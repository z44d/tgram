# ChatFullInfo

**This object represents a chat.**

## Properties

- **`id`** (**`int`**): **Unique identifier for this chat. This number may have more than 32 significant bits and some programming
languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed
64-bit integer or double-precision float type are safe for storing this identifier.**
- **`type`** (**`ChatType`**): **Type of chat, can be either “private”, “group”, “supergroup” or “channel”**
- **`accent_color_id`** (**`int`**): **Optional. Optional. Identifier of the accent color for the chat name and backgrounds of the chat photo,
reply header, and link preview. See accent colors for more details. Returned only in getChat. Always returned in getChat.**
- **`max_reaction_count`** (**`int`**): **Optional. The maximum number of reactions that can be set on a message in the chat**
- **`title`** (**`str`**): **Optional. Title, for supergroups, channels and group chats**
- **`username`** (**`str`**): **Optional. Username, for private chats, supergroups and channels if available**
- **`first_name`** (**`str`**): **Optional. First name of the other party in a private chat**
- **`last_name`** (**`str`**): **Optional. Last name of the other party in a private chat**
- **`is_forum`** (**`bool`**): **Optional. True, if the supergroup chat is a forum (has topics enabled)**
- **`photo`** (**[ChatPhoto](ChatPhoto.md)**): **Optional. Chat photo. Returned only in getChat.**
- **`active_usernames`** (**List of `str`**): **Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels. Returned only in getChat.**
- **`birthdate`** (**[Birthdate](Birthdate.md)**): **Optional. Birthdate of the other party in a private chat. Returned only in getChat.**
- **`business_intro`** (**[BusinessIntro](BusinessIntro.md)**): **Optional. Business intro for the chat. Returned only in getChat.**
- **`business_location`** (**[BusinessLocation](BusinessLocation.md)**): **Optional. Business location for the chat. Returned only in getChat.**
- **`business_opening_hours`** (**[BusinessOpeningHours](BusinessOpeningHours.md)**): **Optional. Business opening hours for the chat. Returned only in getChat.**
- **`personal_chat`** (**[Chat](Chat.md)**): **Optional. For private chats, the personal channel of the user. Returned only in getChat.**
- **`available_reactions`** (**List of `tgram.types.ReactionType`**): **Optional. List of available chat reactions; for private chats, supergroups and channels. Returned only in getChat.**
- **`background_custom_emoji_id`** (**`str`**): **Optional. Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background. Returned only in getChat.**
- **`profile_accent_color_id`** (**`int`**): **Optional. Identifier of the accent color for the chat's profile background. See profile accent colors for more details. Returned only in getChat.**
- **`profile_background_custom_emoji_id`** (**`str`**): **Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background. Returned only in getChat.**
- **`emoji_status_custom_emoji_id`** (**`str`**): **Optional. Custom emoji identifier of emoji status of the other party in a private chat. Returned only in getChat.**
- **`emoji_status_expiration_date`** (**`int`**): **Optional. Expiration date of the emoji status of the other party in a private chat, if any. Returned only in getChat.**
- **`bio`** (**`str`**): **Optional. Bio of the other party in a private chat. Returned only in getChat.**
- **`has_private_forwards`** (**`bool`**): **Optional. :obj:`bool`, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.**
- **`has_restricted_voice_and_video_messages`** (**`bool`**): **Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat.**
- **`join_to_send_messages`** (**`bool`**): **Optional. :obj:`bool`, if users need to join the supergroup before they can send messages. Returned only in getChat.**
- **`join_by_request`** (**`bool`**): **Optional. :obj:`bool`, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat.**
- **`description`** (**`str`**): **Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.**
- **`invite_link`** (**`str`**): **Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.**
- **`pinned_message`** (**[Message](Message.md)**): **Optional. The most recent pinned message (by sending date). Returned only in getChat.**
- **`permissions`** (**[ChatPermissions](ChatPermissions.md)**): **Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.**
- **`accepted_gift_types`** (**[AcceptedGiftTypes](AcceptedGiftTypes.md)**)
- **`can_send_paid_media`** (**`bool`**): **Optional. :obj:`bool`, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.**
- **`slow_mode_delay`** (**`int`**): **Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat.**
- **`unrestrict_boost_count`** (**`int`**): **Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions. Returned only in getChat.**
- **`message_auto_delete_time`** (**`int`**): **Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.**
- **`has_aggressive_anti_spam_enabled`** (**`bool`**): **Optional. :obj:`bool`, if the chat has enabled aggressive anti-spam protection. Returned only in getChat.**
- **`has_hidden_members`** (**`bool`**): **Optional. :obj:`bool`, if the chat has enabled hidden members. Returned only in getChat.**
- **`has_protected_content`** (**`bool`**): **Optional. :obj:`bool`, if messages from the chat can't be forwarded to other chats. Returned only in getChat.**
- **`has_visible_history`** (**`bool`**): **Optional. True, if new chat members will have access to old messages; available only to chat administrators. Returned only in getChat.**
- **`sticker_set_name`** (**`str`**): **Optional. For supergroups, name of group sticker set. Returned only in getChat.**
- **`can_set_sticker_set`** (**`bool`**): **Optional. :obj:`bool`, if the bot can change the group sticker set. Returned only in getChat.**
- **`custom_emoji_sticker_set_name`** (**`str`**): **:obj:`str`**
- **`linked_chat_id`** (**`int`**): **Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for
a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some
programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a
signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.**
- **`location`** (**[ChatLocation](ChatLocation.md)**): **Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat.**
