#🔧 set_business_account_gift_settings

**Changes the privacy settings pertaining to incoming gifts in a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`show_gift_button`** (**`bool`** ): **Pass True, if a button for sending a gift to the user or by the business account must always be shown in the input field**
- **`accepted_gift_types`** (**[AcceptedGiftTypes](../types/AcceptedGiftTypes.md)** ): **Types of gifts accepted by the business account**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_business_account_gift_settings(
    business_connection_id=your_business_connection_id_here,
    show_gift_button=your_show_gift_button_here,
    accepted_gift_types=your_accepted_gift_types_here
)
```
