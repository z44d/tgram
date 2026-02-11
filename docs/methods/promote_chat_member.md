#🔧 promote_chat_member

**Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target channel (
in the format @channelusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`is_anonymous`** (**`bool`** ) (`optional`): **Pass True, if the administrator's presence in the chat is hidden**
- **`can_manage_chat`** (**`bool`** ) (`optional`): **Pass True, if the administrator can access the chat event log, chat statistics,
message statistics in channels, see channel members,
see anonymous administrators in supergroups and ignore slow mode.
Implied by any other administrator privilege**
- **`can_delete_messages`** (**`bool`** ) (`optional`): **Pass True, if the administrator can delete messages of other users**
- **`can_manage_video_chats`** (**`bool`** ) (`optional`): **Pass True, if the administrator can manage voice chats
For now, bots can use this privilege only for passing to other administrators.**
- **`can_restrict_members`** (**`bool`** ) (`optional`): **Pass True, if the administrator can restrict, ban or unban chat members**
- **`can_promote_members`** (**`bool`** ) (`optional`): **Pass True, if the administrator can add new administrators with a subset
of his own privileges or demote administrators that he has promoted, directly or indirectly
(promoted by administrators that were appointed by him)**
- **`can_change_info`** (**`bool`** ) (`optional`): **Pass True, if the administrator can change chat title, photo and other settings**
- **`can_invite_users`** (**`bool`** ) (`optional`): **Pass True, if the administrator can invite new users to the chat**
- **`can_post_stories`** (**`bool`** ) (`optional`): **Pass True if the administrator can create the channel's stories**
- **`can_edit_stories`** (**`bool`** ) (`optional`): **Pass True if the administrator can edit the channel's stories**
- **`can_delete_stories`** (**`bool`** ) (`optional`): **Pass True if the administrator can delete the channel's stories**
- **`can_post_messages`** (**`bool`** ) (`optional`): **Pass True, if the administrator can create channel posts, channels only**
- **`can_edit_messages`** (**`bool`** ) (`optional`): **Pass True, if the administrator can edit messages of other users, channels only**
- **`can_pin_messages`** (**`bool`** ) (`optional`): **Pass True, if the administrator can pin messages, supergroups only**
- **`can_manage_topics`** (**`bool`** ) (`optional`): **Pass True if the user is allowed to create, rename, close,
and reopen forum topics, supergroups only**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.promote_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```

-🔋 **All Parameters**

```python
await bot.promote_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    is_anonymous=your_is_anonymous_here,
    can_manage_chat=your_can_manage_chat_here,
    can_delete_messages=your_can_delete_messages_here,
    can_manage_video_chats=your_can_manage_video_chats_here,
    can_restrict_members=your_can_restrict_members_here,
    can_promote_members=your_can_promote_members_here,
    can_change_info=your_can_change_info_here,
    can_invite_users=your_can_invite_users_here,
    can_post_stories=your_can_post_stories_here,
    can_edit_stories=your_can_edit_stories_here,
    can_delete_stories=your_can_delete_stories_here,
    can_post_messages=your_can_post_messages_here,
    can_edit_messages=your_can_edit_messages_here,
    can_pin_messages=your_can_pin_messages_here,
    can_manage_topics=your_can_manage_topics_here
)
```
