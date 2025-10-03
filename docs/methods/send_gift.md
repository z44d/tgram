#🔧 send_gift

**Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns True on success.**

##⚙️ Parameters

- **`gift_id`** (**`str`** ): **Identifier of the gift**
- **`user_id`** (**`int`** ) (`optional`): **Required if chat_id is not specified. Unique identifier of the target user who will receive the gift.**
- **`chat_id`** (**`int` or `str`** ) (`optional`): **Required if user_id is not specified. Unique identifier for the chat or username of the channel (in the format @channelusername) that will receive the gift.**
- **`pay_for_upgrade`** (**`bool`** ) (`optional`): **Pass True to pay for the gift upgrade from the bot's balance,
thereby making the upgrade free for the receiver**
- **`text`** (**`str`** ) (`optional`): **Text that will be shown along with the gift; 0-255 characters**
- **`text_parse_mode`** (**`Literal`** ) (`optional`): **Mode for parsing entities in the text. See formatting options for more details.
Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.**
- **`text_entities`** (**List of [MessageEntity](../types/MessageEntity.md)** ) (`optional`): **A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of text_parse_mode. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_gift(
    gift_id=your_gift_id_here
)
```

-🔋 **All Parameters**

```python
await bot.send_gift(
    gift_id=your_gift_id_here,
    user_id=your_user_id_here,
    chat_id=your_chat_id_here,
    pay_for_upgrade=your_pay_for_upgrade_here,
    text=your_text_here,
    text_parse_mode=your_text_parse_mode_here,
    text_entities=your_text_entities_here
)
```
