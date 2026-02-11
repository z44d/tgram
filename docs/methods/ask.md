#🔧 ask

**Waits for a user response matching given filters within a time limit.**

##⚙️ Parameters

- **`chat_id`** (**`int`** ): **The target chat to listen in.**
- **`update_type`** (**`str`** ) (`optional`): **Type of update to listen for ('message', 'callback_query', etc.).**
- **`user_id`** (**`int`** ) (`optional`): **Filter responses to a specific user.**
- **`sender_id`** (**`int`** ) (`optional`): **Filter responses to a specific sender chat (channel's speaker).**
- **`cancel`** (**`Callable`** ) (`optional`): **A function that cancels the waiting when it returns True.**
- **`filters`** (**`Filter`** ) (`optional`): **Custom filters to match incoming updates.**
- **`timeout`** (**`float`** ) (`optional`): **Timeout in seconds.**

##📲 Returns

#### [Message](../types/Message.md) or [CallbackQuery](../types/CallbackQuery.md) or [Update](../types/Update.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.ask(
    chat_id=your_chat_id_here
)
```

-🔋 **All Parameters**

```python
await bot.ask(
    chat_id=your_chat_id_here,
    update_type=your_update_type_here,
    user_id=your_user_id_here,
    sender_id=your_sender_id_here,
    cancel=your_cancel_here,
    filters=your_filters_here,
    timeout=your_timeout_here
)
```
