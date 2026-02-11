#🔧 restrict_chat_member

**Use this method to restrict a user in a supergroup.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target group or username of the target supergroup
or channel (in the format @channelusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`permissions`** (**[ChatPermissions](../types/ChatPermissions.md)** ): **Pass ChatPermissions object to set all permissions at once. Use this parameter instead of
passing all boolean parameters to avoid backward compatibility problems in future.**
- **`use_independent_chat_permissions`** (**`bool`** ) (`optional`): **Pass True if chat permissions are set independently.
Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,
can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes
permissions; the can_send_polls permission will imply the can_send_messages permission.**
- **`until_date`** (**`int`** ) (`optional`): **Date when restrictions will be lifted for the user, unix time.
If user is restricted for more than 366 days or less than 30 seconds from the current time,
they are considered to be restricted forever**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.restrict_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    permissions=your_permissions_here
)
```

-🔋 **All Parameters**

```python
await bot.restrict_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    permissions=your_permissions_here,
    use_independent_chat_permissions=your_use_independent_chat_permissions_here,
    until_date=your_until_date_here
)
```
