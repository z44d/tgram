#🔧 edit_message_live_location

**Use this method to edit live location messages.**

##⚙️ Parameters

- **`latitude`** (**`float`** )
- **`longitude`** (**`float`** )
- **`business_connection_id`** (**`str`** ) (`optional`)
- **`chat_id`** (**`int` or `str`** ) (`optional`)
- **`message_id`** (**`int`** ) (`optional`)
- **`inline_message_id`** (**`str`** ) (`optional`)
- **`live_period`** (**`int`** ) (`optional`)
- **`horizontal_accuracy`** (**`float`** ) (`optional`)
- **`heading`** (**`int`** ) (`optional`)
- **`proximity_alert_radius`** (**`int`** ) (`optional`)
- **`reply_markup`** (**[InlineKeyboardMarkup](../types/InlineKeyboardMarkup.md)** ) (`optional`)

##📲 Returns

#### [Message](../types/Message.md) or `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.edit_message_live_location(
    latitude=your_latitude_here,
    longitude=your_longitude_here
)
```

-🔋 **All Parameters**

```python
await bot.edit_message_live_location(
    latitude=your_latitude_here,
    longitude=your_longitude_here,
    business_connection_id=your_business_connection_id_here,
    chat_id=your_chat_id_here,
    message_id=your_message_id_here,
    inline_message_id=your_inline_message_id_here,
    live_period=your_live_period_here,
    horizontal_accuracy=your_horizontal_accuracy_here,
    heading=your_heading_here,
    proximity_alert_radius=your_proximity_alert_radius_here,
    reply_markup=your_reply_markup_here
)
```
