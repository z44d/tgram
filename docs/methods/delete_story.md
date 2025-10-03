#🔧 delete_story

**Deletes a story previously posted by the bot on behalf of a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`story_id`** (**`int`** ): **Unique identifier of the story to delete**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.delete_story(
    business_connection_id=your_business_connection_id_here,
    story_id=your_story_id_here
)
```
