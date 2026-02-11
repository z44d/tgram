#🔧 create_chat_subscription_invite_link

**Use this method to create a subscription invite link for a channel chat.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Id: Unique identifier for the target chat or username of the target channel
(in the format @channelusername)**
- **`subscription_period`** (**`int`** ): **The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days).**
- **`subscription_price`** (**`int`** ): **The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-2500**
- **`name`** (**`str`** ) (`optional`): **Invite link name; 0-32 characters**

##📲 Returns

#### [ChatInviteLink](../types/ChatInviteLink.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.create_chat_subscription_invite_link(
    chat_id=your_chat_id_here,
    subscription_period=your_subscription_period_here,
    subscription_price=your_subscription_price_here
)
```

-🔋 **All Parameters**

```python
await bot.create_chat_subscription_invite_link(
    chat_id=your_chat_id_here,
    subscription_period=your_subscription_period_here,
    subscription_price=your_subscription_price_here,
    name=your_name_here
)
```
