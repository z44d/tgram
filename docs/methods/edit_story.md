#🔧 edit_story

**Edits a story previously posted by the bot on behalf of a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`story_id`** (**`int`** ): **Unique identifier of the story to edit**
- **`content`** (**[InputStoryContentPhoto](../types/InputStoryContentPhoto.md) or [InputStoryContentVideo](../types/InputStoryContentVideo.md)** ): **Content of the story**
- **`caption`** (**`str`** ) (`optional`): **Caption of the story, 0-2048 characters after entities parsing**
- **`parse_mode`** (**`str`** ) (`optional`): **Mode for parsing entities in the story caption**
- **`caption_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **A JSON-serialized list of special entities that appear in the caption**
- **`areas`** (**List of [StoryArea](../types/StoryArea.md)** ) (`optional`): **A JSON-serialized list of clickable areas to be shown on the story**

##📲 Returns

#### [Story](../types/Story.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_story(
    business_connection_id=your_business_connection_id_here,
    story_id=your_story_id_here,
    content=your_content_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_story(
    business_connection_id=your_business_connection_id_here,
    story_id=your_story_id_here,
    content=your_content_here,
    caption=your_caption_here,
    parse_mode=your_parse_mode_here,
    caption_entities=your_caption_entities_here,
    areas=your_areas_here
)
```
