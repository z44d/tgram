#🔧 set_message_reaction

**Use this method to change the chosen reactions on a message.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)**
- **`message_id`** (**`int`** ): **Identifier of the message to set reaction to**
- **`reaction`** (**List of [ReactionTypeCustomEmoji](../types/ReactionTypeCustomEmoji.md) or [ReactionTypeEmoji](../types/ReactionTypeEmoji.md) or [ReactionTypePaid](../types/ReactionTypePaid.md)** ) (`optional`): **New list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message.
A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators.**
- **`is_big`** (**`bool`** ) (`optional`): **Pass True to set the reaction with a big animation**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_message_reaction(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here
)
```

-🔋 **All Parameters**

```python
await bot.set_message_reaction(
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    reaction=your_reaction_here,
    is_big=your_is_big_here
)
```
