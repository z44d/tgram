#🔧 answer_pre_checkout_query

**Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the**

##⚙️ Parameters

- **`pre_checkout_query_id`** (**`str`** ): **Unique identifier for the query to be answered**
- **`ok`** (**`bool`** ): **Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.**
- **`error_message`** (**`str`** ) (`optional`): **Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout
(e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different
color or garment!"). Telegram will display this message to the user.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.answer_pre_checkout_query(
    pre_checkout_query_id=your_pre_checkout_query_id_here,
    ok=your_ok_here
)
```

-🔋 **All Parameters**

```python
await bot.answer_pre_checkout_query(
    pre_checkout_query_id=your_pre_checkout_query_id_here,
    ok=your_ok_here,
    error_message=your_error_message_here
)
```
