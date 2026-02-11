#🔮 User

**This object represents a Telegram user or bot.**

##⚙️ Properties

- **`id`** (**`int`** ): **Unique identifier for this user or bot. This number may have more than 32 significant bits and some
programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant
bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.**
- **`is_bot`** (**`bool`** ): **True, if this user is a bot**
- **`first_name`** (**`str`** ): **User's or bot's first name**
- **`last_name`** (**`str`** ): **Optional. User's or bot's last name**
- **`username`** (**`str`** ): **Optional. User's or bot's username**
- **`language_code`** (**`str`** ): **Optional. IETF language tag of the user's language**
- **`is_premium`** (**`bool`** ): **Optional. :obj:`bool`, if this user is a Telegram Premium user**
- **`added_to_attachment_menu`** (**`bool`** ): **Optional. :obj:`bool`, if this user added the bot to the attachment menu**
- **`can_join_groups`** (**`bool`** ): **Optional. True, if the bot can be invited to groups. Returned only in getMe.**
- **`can_read_all_group_messages`** (**`bool`** ): **Optional. True, if privacy mode is disabled for the bot. Returned only in
getMe.**
- **`supports_inline_queries`** (**`bool`** ): **Optional. True, if the bot supports inline queries. Returned only in getMe.**
- **`can_connect_to_business`** (**`bool`** ): **Optional. True, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in getMe.**
- **`has_main_web_app`** (**`bool`** ): **Optional. True, if the bot has a main Web App. Returned only in getMe.**
- **`has_topics_enabled`** (**`bool`** ): **Optional. True, if forum topic mode is enabled for the bot in private chats.**
- **`allows_users_to_create_topics`** (**`bool`** ): **Optional. True, if the bot allows users to create and delete topics in private chats. Returned only in getMe.**
