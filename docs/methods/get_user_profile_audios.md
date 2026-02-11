#🔧 get_user_profile_audios

**Use this method to get a list of profile audios for a user. Returns a UserProfileAudios object.**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`offset`** (**`int`** ) (`optional`): **Optional. Sequential number of the first audio to be returned. By default, all audios are returned.**
- **`limit`** (**`int`** ) (`optional`): **Optional. Limits the number of audios to be retrieved. Values between 1–100 are accepted. Defaults to 100.**

##📲 Returns

#### [UserProfileAudios](../types/UserProfileAudios.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.get_user_profile_audios(
    user_id=your_user_id_here
)
```

-🔋 **All Parameters**

```python
await bot.get_user_profile_audios(
    user_id=your_user_id_here,
    offset=your_offset_here,
    limit=your_limit_here
)
```
