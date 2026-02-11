#🔮 ChatFullInfo

**This object contains full information about a chat.**

##⚙️ Properties

- **`id`** (**`int`** ): **Unique identifier for this chat. This number may have more than 32 significant bits and some programming
languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed
64-bit integer or double-precision float type are safe for storing this identifier.**
- **`type`** (**`ChatType`** ): **Type of the chat, can be either “private”, “group”, “supergroup” or “channel”**
- **`title`** (**`str`** ): **Optional. Title, for supergroups, channels and group chats**
- **`username`** (**`str`** ): **Optional. Username, for private chats, supergroups and channels if available**
- **`first_name`** (**`str`** ): **Optional. First name of the other party in a private chat**
- **`last_name`** (**`str`** ): **Optional. Last name of the other party in a private chat**
- **`is_forum`** (**`bool`** ): **Optional. True, if the supergroup chat is a forum (has topics enabled)**
- **`is_direct_messages`** (**`bool`** ): **Optional. True, if the chat is the direct messages chat of a channel**
- **`accent_color_id`** (**`int`** ): **Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview.**
- **`max_reaction_count`** (**`int`** ): **The maximum number of reactions that can be set on a message in the chat**
- **`photo`** (**[ChatPhoto](ChatPhoto.md)** ): **Optional. Chat photo**
- **`active_usernames`** (**List of `str`** ): **Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels**
- **`birthdate`** (**[Birthdate](Birthdate.md)** ): **Optional. For private chats, the date of birth of the user**
- **`business_intro`** (**[BusinessIntro](BusinessIntro.md)** ): **Optional. For private chats with business accounts, the intro of the business**
- **`business_location`** (**[BusinessLocation](BusinessLocation.md)** ): **Optional. For private chats with business accounts, the location of the business**
- **`first_profile_audio`** (**[Audio](Audio.md)** ): **Optional. For private chats, the first audio added to the profile of the user**
- **`business_opening_hours`** (**[BusinessOpeningHours](BusinessOpeningHours.md)** ): **Optional. For private chats with business accounts, the opening hours of the business**
- **`personal_chat`** (**[Chat](Chat.md)** ): **Optional. For private chats, the personal channel of the user**
- **`parent_chat`** (**[Chat](Chat.md)** ): **Optional. Information about the corresponding channel chat; for direct messages chats only**
- **`available_reactions`** (**List of `ReactionType`** ): **Optional. List of available reactions allowed in the chat. If omitted, then all emoji reactions are allowed.**
- **`background_custom_emoji_id`** (**`str`** ): **Optional. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background**
- **`profile_accent_color_id`** (**`int`** ): **Optional. Identifier of the accent color for the chat's profile background. See profile accent colors for more details.**
- **`profile_background_custom_emoji_id`** (**`str`** ): **Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background**
- **`emoji_status_custom_emoji_id`** (**`str`** ): **Optional. Custom emoji identifier of the emoji status of the chat or the other party in a private chat**
- **`emoji_status_expiration_date`** (**`int`** ): **Optional. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any**
- **`bio`** (**`str`** ): **Optional. Bio of the other party in a private chat**
- **`has_private_forwards`** (**`bool`** ): **Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user**
- **`has_restricted_voice_and_video_messages`** (**`bool`** ): **Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat**
- **`join_to_send_messages`** (**`bool`** ): **Optional. True, if users need to join the supergroup before they can send messages**
- **`join_by_request`** (**`bool`** ): **Optional. True, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators**
- **`description`** (**`str`** ): **Optional. Description, for groups, supergroups and channel chats**
- **`invite_link`** (**`str`** ): **Optional. Primary invite link, for groups, supergroups and channel chats**
- **`pinned_message`** (**[Message](Message.md)** ): **Optional. The most recent pinned message (by sending date)**
- **`permissions`** (**[ChatPermissions](ChatPermissions.md)** ): **Optional. Default chat member permissions, for groups and supergroups**
- **`accepted_gift_types`** (**[AcceptedGiftTypes](AcceptedGiftTypes.md)** ): **Information about types of gifts that are accepted by the chat or by the corresponding user for private chats**
- **`can_send_paid_media`** (**`bool`** ): **Optional. True, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.**
- **`slow_mode_delay`** (**`int`** ): **Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds**
- **`unrestrict_boost_count`** (**`int`** ): **Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions**
- **`message_auto_delete_time`** (**`int`** ): **Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds**
- **`has_aggressive_anti_spam_enabled`** (**`bool`** ): **Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.**
- **`has_hidden_members`** (**`bool`** ): **Optional. True, if non-administrators can only get the list of bots and administrators in the chat**
- **`has_protected_content`** (**`bool`** ): **Optional. True, if messages from the chat can't be forwarded to other chats**
- **`has_visible_history`** (**`bool`** ): **Optional. True, if new chat members will have access to old messages; available only to chat administrators**
- **`sticker_set_name`** (**`str`** ): **Optional. For supergroups, name of the group sticker set**
- **`can_set_sticker_set`** (**`bool`** ): **Optional. True, if the bot can change the group sticker set**
- **`custom_emoji_sticker_set_name`** (**`str`** ): **Optional. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.**
- **`linked_chat_id`** (**`int`** ): **Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats.**
- **`location`** (**[ChatLocation](ChatLocation.md)** ): **Optional. For supergroups, the location to which the supergroup is connected**
- **`rating`** (**[UserRating](UserRating.md)** ): **Optional. User rating for the chat**
- **`paid_message_star_count`** (**`int`** ): **Optional. The number of Telegram Stars that must be paid to send a paid message to the chat**
- **`unique_gift_colors`** (**[UniqueGiftColors](UniqueGiftColors.md)** ): **Optional. The colors of the unique gift that a user in a private chat has chosen to display**
