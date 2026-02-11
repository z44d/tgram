#🔧 repost_story

**Use this method to repost a story from one business account to another.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection on behalf
of which the story will be reposted**
- **`story_sender_chat_id`** (**`int`** ): **Unique identifier of the chat that originally posted the story**
- **`story_id`** (**`int`** ): **Unique identifier of the story to repost**

##📲 Returns

#### [Story](../types/Story.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.repost_story(
    business_connection_id=your_business_connection_id_here,
    story_sender_chat_id=your_story_sender_chat_id_here,
    story_id=your_story_id_here
)
```
