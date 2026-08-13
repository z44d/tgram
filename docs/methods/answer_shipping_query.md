#🔧 answer_shipping_query

**Asks for an answer to a shipping question.**

##⚙️ Parameters

- **`shipping_query_id`** (**`str`** ): **Unique identifier for the query to be answered**
- **`ok`** (**`bool`** ): **Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)**
- **`shipping_options`** (**List of [ShippingOption](../types/ShippingOption.md)** ) (`optional`): **Required if ok is True. A JSON-serialized array of available shipping options.**
- **`error_message`** (**`str`** ) (`optional`): **Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order
(e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.answer_shipping_query(
    shipping_query_id=your_shipping_query_id_here,
    ok=your_ok_here
)
```

-🔋 **All Parameters**

```python
await bot.answer_shipping_query(
    shipping_query_id=your_shipping_query_id_here,
    ok=your_ok_here,
    shipping_options=your_shipping_options_here,
    error_message=your_error_message_here
)
```
