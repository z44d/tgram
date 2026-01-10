#🔧 post_story

**Posts a story on behalf of a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`content`** (**[InputStoryContentPhoto](../types/InputStoryContentPhoto.md) or [InputStoryContentVideo](../types/InputStoryContentVideo.md)** ): **Content of the story**
- **`active_period`** (**`int`** ): **Period after which the story is moved to the archive, in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400**
- **`caption`** (**`str`** ) (`optional`): **Caption of the story, 0-2048 characters after entities parsing**
- **`parse_mode`** (**`str`** ) (`optional`): **Mode for parsing entities in the story caption**
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **A JSON-serialized list of special entities that appear in the caption**
- **`areas`** (**List of [StoryArea](../types/StoryArea.md)** ) (`optional`): **A JSON-serialized list of clickable areas to be shown on the story**
- **`post_to_chat_page`** (**`bool`** ) (`optional`): **Pass True to keep the story accessible after it expires**
- **`protect_content`** (**`bool`** ) (`optional`): **Pass True if the content of the story must be protected from forwarding and screenshotting**

##📲 Returns

#### [Story](../types/Story.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.post_story(
    business_connection_id=your_business_connection_id_here,
    content=your_content_here,
    active_period=your_active_period_here
)
```

-🔋 **All Parameters**

```python
await bot.post_story(
    business_connection_id=your_business_connection_id_here,
    content=your_content_here,
    active_period=your_active_period_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    areas=your_areas_here,
    post_to_chat_page=your_post_to_chat_page_here,
    protect_content=your_protect_content_here
)
```
