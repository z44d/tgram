#🔧 get_game_high_scores

**Use this method to get data for high score tables. Will return the score of the specified user and several of**

##⚙️ Parameters

- **`user_id`** (**`int`** ): **User identifier**
- **`chat_id`** (**`int`** ) (`optional`): **Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)**
- **`message_id`** (**`int`** ) (`optional`): **Required if inline_message_id is not specified. Identifier of the sent message**
- **`inline_message_id`** (**`str`** ) (`optional`): **Required if chat_id and message_id are not specified. Identifier of the inline message**

##📲 Returns

#### List of [GameHighScore](../types/GameHighScore.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.get_game_high_scores(
    user_id=your_user_id_here
)
```

-🔋 **All Parameters**

```python
await bot.get_game_high_scores(
    user_id=your_user_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    inline_message_id=your_inline_message_id_here
)
```
