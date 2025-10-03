#🔧 unrestrict_chat_member

**Use this method to unrestrict a user in a supergroup.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target group or username of the target supergroup
or channel (in the format @channelusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`use_independent_chat_permissions`** (**`bool`** ) (`optional`): **Pass True if chat permissions are set independently.
Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,
can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes
permissions; the can_send_polls permission will imply the can_send_messages permission.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.unrestrict_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here
)
```

-🔋 **All Parameters**

```python
await bot.unrestrict_chat_member(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    use_independent_chat_permissions=your_use_independent_chat_permissions_here
)
```
