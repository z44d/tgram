# set_game_score

****

## Parameters

- **`user_id`** (**`int`**)
- **`score`** (**`int`**)
- **`force`** (**`bool`**) (`optional`)
- **`disable_edit_message`** (**`bool`**) (`optional`)
- **`chat_id`** (**`int`**) (`optional`)
- **`message_id`** (**`int`**) (`optional`)
- **`inline_message_id`** (**`str`**) (`optional`)

## Returns

#### `Message, bool`

## Examples

- **Required Parameters**

```python
await bot.set_game_score(
    user_id=your_user_id_here,
    score=your_score_here
)
```

- **All Parameters**

```python
await bot.set_game_score(
    user_id=your_user_id_here,
    score=your_score_here,
    force=your_force_here,
    disable_edit_message=your_disable_edit_message_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    inline_message_id=your_inline_message_id_here
)
```
