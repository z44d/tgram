# set_chat_description

**Use this method to change the description of a supergroup or a channel.**

## Parameters

- **`chat_id`** (**`int, str`**): **Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**
- **`description`** (**`str`**) (`optional`): **Str: New chat description, 0-255 characters**

## Returns

#### `bool`

## Examples

- **Required Parameters**

```python
await bot.set_chat_description(
    chat_id=your_chat_id_here
)
```

- **All Parameters**

```python
await bot.set_chat_description(
    chat_id=your_chat_id_here,
    description=your_description_here
)
```
