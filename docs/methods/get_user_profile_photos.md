#🔧 get_user_profile_photos

**Use this method to get a list of profile pictures for a user.**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`offset`** (**`int`** ) (`optional`): **Sequential number of the first photo to be returned. By default, all photos are returned.**
- **`limit`** (**`int`** ) (`optional`): **Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.**

##📲 Returns

#### [UserProfilePhotos](../types/UserProfilePhotos.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.get_user_profile_photos(
    user_id=your_user_id_here
)
```

-🔋 **All Parameters**

```python
await bot.get_user_profile_photos(
    user_id=your_user_id_here,
    offset=your_offset_here,
    limit=your_limit_here
)
```
