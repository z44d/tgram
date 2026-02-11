#🔧 set_chat_permissions

**Use this method to set default chat permissions for all members.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target supergroup
(in the format @supergroupusername)**
- **`permissions`** (**[ChatPermissions](../types/ChatPermissions.md)** ): **New default chat permissions**
- **`use_independent_chat_permissions`** (**`bool`** ) (`optional`): **Pass True if chat permissions are set independently. Otherwise,
the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,
can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and
can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_chat_permissions(
    chat_id=your_chat_id_here,
    permissions=your_permissions_here
)
```

-🔋 **All Parameters**

```python
await bot.set_chat_permissions(
    chat_id=your_chat_id_here,
    permissions=your_permissions_here,
    use_independent_chat_permissions=your_use_independent_chat_permissions_here
)
```
