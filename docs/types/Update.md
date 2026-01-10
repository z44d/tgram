#🔮 Update

**This object represents an incoming update.At most one of the optional parameters can be present in any given update.**

##⚙️ Properties

- **`update_id`** (**`int`** ): **The update's unique identifier. Update identifiers start from a certain positive number and
increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore
repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates
for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.**
- **`message`** (**[Message](Message.md)** ): **Optional. New incoming message of any kind - text, photo, sticker, etc.**
- **`edited_message`** (**[Message](Message.md)** ): **Optional. New version of a message that is known to the bot and was edited**
- **`channel_post`** (**[Message](Message.md)** ): **Optional. New incoming channel post of any kind - text, photo, sticker, etc.**
- **`edited_channel_post`** (**[Message](Message.md)** ): **Optional. New version of a channel post that is known to the bot and was edited**
- **`business_connection`** (**[BusinessConnection](BusinessConnection.md)** ): **Optional. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot**
- **`business_message`** (**[Message](Message.md)** ): **Optional. New non-service message from a connected business account**
- **`edited_business_message`** (**[Message](Message.md)** ): **Optional. New version of a non-service message from a connected business account that is known to the bot and was edited**
- **`deleted_business_messages`** (**[BusinessMessagesDeleted](BusinessMessagesDeleted.md)** ): **Optional. Service message: the chat connected to the business account was deleted**
- **`message_reaction`** (**[MessageReactionUpdated](MessageReactionUpdated.md)** ): **Optional. A reaction to a message was changed by a user. The bot must be an administrator in the chat
and must explicitly specify "message_reaction" in the list of allowed_updates to receive these updates. The update isn't received for reactions set by bots.**
- **`message_reaction_count`** (**[MessageReactionCountUpdated](MessageReactionCountUpdated.md)** ): **Optional. Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify
"message_reaction_count" in the list of allowed_updates to receive these updates.**
- **`inline_query`** (**[InlineQuery](InlineQuery.md)** ): **Optional. New incoming inline query**
- **`chosen_inline_result`** (**[ChosenInlineResult](ChosenInlineResult.md)** ): **Optional. The result of an inline query that was chosen by a user and sent to their chat
partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your
bot.**
- **`callback_query`** (**[CallbackQuery](CallbackQuery.md)** ): **Optional. New incoming callback query**
- **`shipping_query`** (**[ShippingQuery](ShippingQuery.md)** ): **Optional. New incoming shipping query. Only for invoices with flexible price**
- **`pre_checkout_query`** (**[PreCheckoutQuery](PreCheckoutQuery.md)** ): **Optional. New incoming pre-checkout query. Contains full information about
checkout**
- **`purchased_paid_media`** (**[PaidMediaPurchased](PaidMediaPurchased.md)** ): **Optional. A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat**
- **`poll`** (**[Poll](Poll.md)** ): **Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the
bot**
- **`poll_answer`** (**[PollAnswer](PollAnswer.md)** ): **Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in
polls that were sent by the bot itself.**
- **`my_chat_member`** (**[ChatMemberUpdated](ChatMemberUpdated.md)** ): **Optional. The bot's chat member status was updated in a chat. For private chats, this update
is received only when the bot is blocked or unblocked by the user.**
- **`chat_member`** (**[ChatMemberUpdated](ChatMemberUpdated.md)** ): **Optional. A chat member's status was updated in a chat. The bot must be an administrator in the
chat and must explicitly specify “chat_member” in the list of allowed_updates to receive these updates.**
- **`chat_join_request`** (**[ChatJoinRequest](ChatJoinRequest.md)** ): **Optional. A request to join the chat has been sent. The bot must have the
can_invite_users administrator right in the chat to receive these updates.**
- **`chat_boost`** (**[ChatBoostUpdated](ChatBoostUpdated.md)** ): **Optional. A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates.**
- **`removed_chat_boost`** (**[ChatBoostRemoved](ChatBoostRemoved.md)** ): **Optional. A chat boost was removed. The bot must be an administrator in the chat to receive these updates.**
