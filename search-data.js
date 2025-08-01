// Search data for tgram documentation
window.tgramMethods = {
  "add_sticker_to_set": {
    "description": "Use this method to add a new sticker to a set created by the bot.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "User identifier of created sticker set owner"
      },
      "name": {
        "type": "str",
        "required": true,
        "description": "Sticker set name"
      },
      "sticker": {
        "type": "InputSticker",
        "required": true,
        "description": "A JSON-serialized object for sticker to be added to the sticker set"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.add_sticker_to_set.AddStickerToSet.add_sticker_to_set"
  },
  "answer_callback_query": {
    "description": "Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to",
    "parameters": {
      "callback_query_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier for the query to be answered"
      },
      "text": {
        "type": "str",
        "required": false,
        "description": "Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters"
      },
      "show_alert": {
        "type": "bool",
        "required": false,
        "description": "If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false."
      },
      "url": {
        "type": "str",
        "required": false,
        "description": "URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your\ngame - note that this will only work if the query comes from a callback_game button."
      },
      "cache_time": {
        "type": "int",
        "required": false,
        "description": "The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching\nstarting in version 3.14. Defaults to 0."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.other.answer_callback_query.AnswerCallbackQuery.answer_callback_query"
  },
  "answer_inline_query": {
    "description": "Use this method to send answers to an inline query. On success, True is returned.",
    "parameters": {
      "inline_query_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier for the answered query"
      },
      "results": {
        "type": "List",
        "required": true,
        "description": "Array of results for the inline query"
      },
      "cache_time": {
        "type": "int",
        "required": false,
        "description": "The maximum amount of time in seconds that the result of the inline query\nmay be cached on the server."
      },
      "is_personal": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if results may be cached on the server side only for\nthe user that sent the query."
      },
      "next_offset": {
        "type": "str",
        "required": false,
        "description": "Pass the offset that a client should send in the next query with the same text\nto receive more results."
      },
      "button": {
        "type": "InlineQueryResultsButton",
        "required": false,
        "description": "A JSON-serialized object describing a button to be shown above inline query results"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.other.answer_inline_query.AnswerInlineQuery.answer_inline_query"
  },
  "answer_pre_checkout_query": {
    "description": "Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the",
    "parameters": {
      "pre_checkout_query_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier for the query to be answered"
      },
      "ok": {
        "type": "bool",
        "required": true,
        "description": "Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems."
      },
      "error_message": {
        "type": "str",
        "required": false,
        "description": "Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout\n(e.g. \"Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different\ncolor or garment!\"). Telegram will display this message to the user."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.other.answer_pre_checkout_query.AnswerPreCheckoutQuery.answer_pre_checkout_query"
  },
  "answer_shipping_query": {
    "description": "Asks for an answer to a shipping question.",
    "parameters": {
      "shipping_query_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier for the query to be answered"
      },
      "ok": {
        "type": "bool",
        "required": true,
        "description": "Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)"
      },
      "shipping_options": {
        "type": "List",
        "required": false,
        "description": "Required if ok is True. A JSON-serialized array of available shipping options."
      },
      "error_message": {
        "type": "str",
        "required": false,
        "description": "Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order\n(e.g. \"Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.other.answer_shipping_query.AnswerShippingQuery.answer_shipping_query"
  },
  "answer_web_app_query": {
    "description": "Use this method to set the result of an interaction with a Web App and",
    "parameters": {
      "web_app_query_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier for the query to be answered"
      },
      "result": {
        "type": "Union",
        "required": true,
        "description": "A JSON-serialized object describing the message to be sent"
      }
    },
    "returns": "SentWebAppMessage",
    "path": "tgram.methods.other.answer_web_app_query.AnswerWebAppQuery.answer_web_app_query"
  },
  "approve_chat_join_request": {
    "description": "Use this method to approve a chat join request.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup\n(in the format @supergroupusername)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.approve_chat_join_request.ApproveChatJoinRequest.approve_chat_join_request"
  },
  "ask": {
    "description": "Waits for a user response matching given filters within a time limit.",
    "parameters": {
      "chat_id": {
        "type": "int",
        "required": true,
        "description": "The target chat to listen in."
      },
      "update_type": {
        "type": "str",
        "required": false,
        "description": "Type of update to listen for ('message', 'callback_query', etc.)."
      },
      "user_id": {
        "type": "int",
        "required": false,
        "description": "Filter responses to a specific user."
      },
      "sender_id": {
        "type": "int",
        "required": false,
        "description": "Filter responses to a specific sender chat (channel's speaker)."
      },
      "cancel": {
        "type": "Callable",
        "required": false,
        "description": "A function that cancels the waiting when it returns True."
      },
      "filters": {
        "type": "tgram.filters.Filter",
        "required": false,
        "description": "Custom filters to match incoming updates."
      },
      "timeout": {
        "type": "float",
        "required": false,
        "description": "Timeout in seconds."
      }
    },
    "returns": "Union",
    "path": "tgram.methods.messages.ask.Ask.ask"
  },
  "ban_chat_member": {
    "description": "Use this method to ban a user in a group, a supergroup or a channel.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target group or username of the target supergroup\nor channel (in the format @channelusername)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      },
      "until_date": {
        "type": "int",
        "required": false,
        "description": "Date when the user will be unbanned, unix time. If user is banned for more than 366 days or\nless than 30 seconds from the current time they are considered to be banned forever"
      },
      "revoke_messages": {
        "type": "bool",
        "required": false,
        "description": "Bool: Pass True to delete all messages from the chat for the user that is being removed.\nIf False, the user will be able to see messages in the group that were sent before the user was removed.\nAlways True for supergroups and channels."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.ban_chat_member.BanChatMember.ban_chat_member"
  },
  "ban_chat_sender_chat": {
    "description": "Use this method to ban a channel chat in a supergroup or a channel.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "sender_chat_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target sender chat"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.ban_chat_sender_chat.BanChatSenderChat.ban_chat_sender_chat"
  },
  "close": {
    "description": "Use this method to close the bot instance before moving it from one local server to another.",
    "parameters": {},
    "returns": "bool",
    "path": "tgram.methods.bot.close.Close.close"
  },
  "close_forum_topic": {
    "description": "Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "message_thread_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the topic to close"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.close_forum_topic.CloseForumTopic.close_forum_topic"
  },
  "close_general_forum_topic": {
    "description": "Use this method to close the 'General' topic in a forum supergroup chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.close_general_forum_topic.CloseGeneralForumTopic.close_general_forum_topic"
  },
  "convert_gift_to_stars": {
    "description": "Converts a given regular gift to Telegram Stars. Requires the can_convert_gifts_to_stars business bot right. Returns True on success.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection."
      },
      "owned_gift_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the regular gift that should be converted to Telegram Stars."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.convert_gift_to_stars.ConvertGiftToStars.convert_gift_to_stars"
  },
  "copy_message": {
    "description": "Use this method to copy messages of any kind.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "from_chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)"
      },
      "message_id": {
        "type": "int",
        "required": true,
        "description": "Message identifier in the chat specified in from_chat_id"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the message will be sent"
      },
      "video_start_timestamp": {
        "type": "int",
        "required": false,
        "description": "New start timestamp for the copied video in the message"
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the new caption."
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages."
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard\nor to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "MessageId",
    "path": "tgram.methods.messages.copy_message.CopyMessage.copy_message"
  },
  "copy_messages": {
    "description": "Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "from_chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)"
      },
      "message_ids": {
        "type": "List",
        "required": true,
        "description": "Message identifiers in the chat specified in from_chat_id"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the messages will be sent"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound"
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the forwarded message from forwarding and saving"
      },
      "remove_caption": {
        "type": "bool",
        "required": false,
        "description": "Pass True to copy the messages without their captions"
      }
    },
    "returns": "List",
    "path": "tgram.methods.messages.copy_messages.CopyMessages.copy_messages"
  },
  "create_chat_invite_link": {
    "description": "Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Id: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "name": {
        "type": "str",
        "required": false,
        "description": "Invite link name; 0-32 characters"
      },
      "expire_date": {
        "type": "int",
        "required": false,
        "description": "Point in time (Unix timestamp) when the link will expire"
      },
      "member_limit": {
        "type": "int",
        "required": false,
        "description": "Maximum number of users that can be members of the chat simultaneously"
      },
      "creates_join_request": {
        "type": "bool",
        "required": false,
        "description": "True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified"
      }
    },
    "returns": "ChatInviteLink",
    "path": "tgram.methods.chats.create_chat_invite_link.CreateChatInviteLink.create_chat_invite_link"
  },
  "create_chat_subscription_invite_link": {
    "description": "Use this method to create a subscription invite link for a channel chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Id: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "subscription_period": {
        "type": "int",
        "required": true,
        "description": "The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days)."
      },
      "subscription_price": {
        "type": "int",
        "required": true,
        "description": "The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-2500"
      },
      "name": {
        "type": "str",
        "required": false,
        "description": "Invite link name; 0-32 characters"
      }
    },
    "returns": "ChatInviteLink",
    "path": "tgram.methods.chats.create_chat_subscription_invite_link.CreateChatSubscriptionInviteLink.create_chat_subscription_invite_link"
  },
  "create_forum_topic": {
    "description": "Use this method to create a topic in a forum supergroup chat. The bot must be an administrator",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "name": {
        "type": "str",
        "required": true,
        "description": "Name of the topic, 1-128 characters"
      },
      "icon_color": {
        "type": "int",
        "required": false,
        "description": "Color of the topic icon in RGB format. Currently, must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F"
      },
      "icon_custom_emoji_id": {
        "type": "str",
        "required": false,
        "description": "Custom emoji for the topic icon. Must be an emoji of type \u201ctgs\u201d and must be exactly 1 character long"
      }
    },
    "returns": "ForumTopic",
    "path": "tgram.methods.forums.create_forum_topic.CreateForumTopic.create_forum_topic"
  },
  "create_invoice_link": {
    "description": "Use this method to create a link for an invoice.",
    "parameters": {
      "title": {
        "type": "str",
        "required": true,
        "description": "Product name, 1-32 characters"
      },
      "description": {
        "type": "str",
        "required": true,
        "description": "Product description, 1-255 characters"
      },
      "payload": {
        "type": "str",
        "required": true,
        "description": "Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,\nuse for your internal processes."
      },
      "currency": {
        "type": "str",
        "required": true,
        "description": "Three-letter ISO 4217 currency code,\nsee https://core.telegram.org/bots/payments#supported-currencies"
      },
      "prices": {
        "type": "List",
        "required": true,
        "description": "Price breakdown, a list of components\n(e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the business connection on behalf of which the link will be created."
      },
      "subscription_period": {
        "type": "int",
        "required": false,
        "description": "The number of seconds the subscription will be active for before the next payment.\nThe currency must be set to \u201cXTR\u201d (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified."
      },
      "provider_token": {
        "type": "str",
        "required": false,
        "description": "Payments provider token, obtained via @Botfather; Pass None to omit the parameter\nto use \"XTR\" currency"
      },
      "max_tip_amount": {
        "type": "int",
        "required": false,
        "description": "The maximum accepted amount for tips in the smallest units of the currency"
      },
      "suggested_tip_amounts": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized array of suggested amounts of tips in the smallest\nunits of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip\namounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount."
      },
      "provider_data": {
        "type": "str",
        "required": false,
        "description": "A JSON-serialized data about the invoice, which will be shared with the payment provider.\nA detailed description of required fields should be provided by the payment provider."
      },
      "photo_url": {
        "type": "str",
        "required": false,
        "description": "URL of the product photo for the invoice. Can be a photo of the goods\nor a photo of the invoice. People like it better when they see a photo of what they are paying for."
      },
      "photo_size": {
        "type": "int",
        "required": false,
        "description": "Photo size in bytes"
      },
      "photo_width": {
        "type": "int",
        "required": false,
        "description": "Photo width"
      },
      "photo_height": {
        "type": "int",
        "required": false,
        "description": "Photo height"
      },
      "need_name": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if you require the user's full name to complete the order"
      },
      "need_phone_number": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if you require the user's phone number to complete the order"
      },
      "need_email": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if you require the user's email to complete the order"
      },
      "need_shipping_address": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if you require the user's shipping address to complete the order"
      },
      "send_phone_number_to_provider": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if user's phone number should be sent to provider"
      },
      "send_email_to_provider": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if user's email address should be sent to provider"
      },
      "is_flexible": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the final price depends on the shipping method"
      }
    },
    "returns": "str",
    "path": "tgram.methods.other.create_invoice_link.CreateInvoiceLink.create_invoice_link"
  },
  "create_new_sticker_set": {
    "description": "Use this method to create new sticker set owned by a user.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "User identifier of created sticker set owner"
      },
      "name": {
        "type": "str",
        "required": true,
        "description": "Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only English letters,\ndigits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in \"_by_<bot_username>\".\n<bot_username> is case insensitive. 1-64 characters."
      },
      "title": {
        "type": "str",
        "required": true,
        "description": "Sticker set title, 1-64 characters"
      },
      "stickers": {
        "type": "List",
        "required": true,
        "description": "List of stickers to be added to the set"
      },
      "sticker_type": {
        "type": "str",
        "required": false,
        "description": "Type of stickers in the set, pass \u201cregular\u201d, \u201cmask\u201d, or \u201ccustom_emoji\u201d. By default, a regular sticker set is created."
      },
      "needs_repainting": {
        "type": "bool",
        "required": false,
        "description": "Pass True if stickers in the sticker set must be repainted to the color of text when used in messages,\nthe accent color if used as emoji status, white on chat photos, or another appropriate color based on context;\nfor custom emoji sticker sets only"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.create_new_sticker_set.CreateNewStickerSet.create_new_sticker_set"
  },
  "decline_chat_join_request": {
    "description": "Use this method to decline a chat join request.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup\n(in the format @supergroupusername)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.decline_chat_join_request.DeclineChatJoinRequest.decline_chat_join_request"
  },
  "delete_business_messages": {
    "description": "Deletes messages on behalf of a business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection on behalf of which to delete the messages"
      },
      "message_ids": {
        "type": "List",
        "required": true,
        "description": "A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.delete_business_messages.DeleteBusinessMessages.delete_business_messages"
  },
  "delete_chat_photo": {
    "description": "Use this method to delete a chat photo. Photos can't be changed for private chats.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Int or Str: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.delete_chat_photo.DeleteChatPhoto.delete_chat_photo"
  },
  "delete_chat_sticker_set": {
    "description": "Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.delete_chat_sticker_set.DeleteChatStickerSet.delete_chat_sticker_set"
  },
  "delete_forum_topic": {
    "description": "Use this method to delete a topic in a forum supergroup chat. The bot must be an administrator in the chat for this",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "message_thread_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the topic to delete"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.delete_forum_topic.DeleteForumTopic.delete_forum_topic"
  },
  "delete_message": {
    "description": "Use this method to delete a message, including service messages, with the following limitations:",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "message_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the message to delete"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.messages.delete_message.DeleteMessage.delete_message"
  },
  "delete_messages": {
    "description": "Use this method to delete multiple messages simultaneously.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "message_ids": {
        "type": "List",
        "required": true,
        "description": "Identifiers of the messages to be deleted"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.messages.delete_messages.DeleteMessages.delete_messages"
  },
  "delete_my_commands": {
    "description": "Use this method to delete the list of the bot's commands for the given scope and user language.",
    "parameters": {
      "scope": {
        "type": "BotCommandScope",
        "required": false,
        "description": "The scope of users for which the commands are relevant.\nDefaults to BotCommandScopeDefault."
      },
      "language_code": {
        "type": "str",
        "required": false,
        "description": "A two-letter ISO 639-1 language code. If empty,\ncommands will be applied to all users from the given scope,\nfor whose language there are no dedicated commands"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.bot.delete_my_commands.DeleteMyCommands.delete_my_commands"
  },
  "delete_sticker_from_set": {
    "description": "Use this method to delete a sticker from a set created by the bot. Returns True on success.",
    "parameters": {
      "sticker": {
        "type": "str",
        "required": true,
        "description": "File identifier of the sticker"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.delete_sticker_from_set.DeleteStickerFromSet.delete_sticker_from_set"
  },
  "delete_sticker_set": {
    "description": "Use this method to delete a sticker set. Returns True on success.",
    "parameters": {
      "name": {
        "type": "str",
        "required": true,
        "description": "Sticker set name"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.delete_sticker_set.DeleteStickerSet.delete_sticker_set"
  },
  "delete_story": {
    "description": "Deletes a story previously posted by the bot on behalf of a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "story_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the story to delete"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.delete_story.DeleteStory.delete_story"
  },
  "delete_webhook": {
    "description": "Use this method to remove webhook integration if you decide to switch back to getUpdates.",
    "parameters": {
      "drop_pending_updates": {
        "type": "bool",
        "required": false,
        "description": "Pass True to drop all pending updates, defaults to None"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.bot.delete_webhook.DeleteWebhook.delete_webhook"
  },
  "demote_chat_member": {
    "description": "Use this method to demote a user in a supergroup or a channel. The bot must be an administrator",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (\nin the format @channelusername)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.demote_chat_member.DemoteChatMember.demote_chat_member"
  },
  "download_file": {
    "description": "",
    "parameters": {
      "file_id": {
        "type": "str",
        "required": true,
        "description": ""
      },
      "file_path": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "in_memory": {
        "type": "bool",
        "required": false,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.files.download_file.DownloadFile.download_file"
  },
  "edit_chat_invite_link": {
    "description": "Use this method to edit a non-primary invite link created by the bot.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Id: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "invite_link": {
        "type": "str",
        "required": true,
        "description": "The invite link to edit"
      },
      "name": {
        "type": "str",
        "required": false,
        "description": "Invite link name; 0-32 characters"
      },
      "expire_date": {
        "type": "int",
        "required": false,
        "description": "Point in time (Unix timestamp) when the link will expire"
      },
      "member_limit": {
        "type": "int",
        "required": false,
        "description": "Maximum number of users that can be members of the chat simultaneously"
      },
      "creates_join_request": {
        "type": "bool",
        "required": false,
        "description": "True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified"
      }
    },
    "returns": "ChatInviteLink",
    "path": "tgram.methods.chats.edit_chat_invite_link.EditChatInviteLink.edit_chat_invite_link"
  },
  "edit_chat_subscription_invite_link": {
    "description": "Use this method to edit a subscription invite link created by the bot.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Id: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "invite_link": {
        "type": "str",
        "required": true,
        "description": "The invite link to edit"
      },
      "name": {
        "type": "str",
        "required": false,
        "description": "Invite link name; 0-32 characters"
      }
    },
    "returns": "ChatInviteLink",
    "path": "tgram.methods.chats.edit_chat_subscription_invite_link.EditChatSubscriptionInviteLink.edit_chat_subscription_invite_link"
  },
  "edit_forum_topic": {
    "description": "Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "message_thread_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the topic to edit"
      },
      "name": {
        "type": "str",
        "required": false,
        "description": "Optional, New name of the topic, 1-128 characters. If not specififed or empty,\nthe current name of the topic will be kept"
      },
      "icon_custom_emoji_id": {
        "type": "str",
        "required": false,
        "description": "Optional, New unique identifier of the custom emoji shown as the topic icon.\nUse getForumTopicIconStickers to get all allowed custom emoji identifiers. Pass an empty string to remove the\nicon. If not specified, the current icon will be kept"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.edit_forum_topic.EditForumTopic.edit_forum_topic"
  },
  "edit_general_forum_topic": {
    "description": "Use this method to edit the name of the 'General' topic in a forum supergroup chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "name": {
        "type": "str",
        "required": true,
        "description": "New topic name, 1-128 characters"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.edit_general_forum_topic.EditGeneralForumTopic.edit_general_forum_topic"
  },
  "edit_message_caption": {
    "description": "Use this method to edit captions of messages.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "chat_id": {
        "type": "Union",
        "required": false,
        "description": ""
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "inline_message_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": ""
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": ""
      },
      "show_caption_above_media": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.messages.edit_message_caption.EditMessageCaption.edit_message_caption"
  },
  "edit_message_checklist": {
    "description": "Use this method to edit a checklist on behalf of a connected business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection on behalf of which the message will be sent"
      },
      "chat_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier for the target chat"
      },
      "message_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier for the target message"
      },
      "checklist": {
        "type": "InputChecklist",
        "required": true,
        "description": "A JSON-serialized object for the new checklist"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": "A JSON-serialized object for the new inline keyboard for the message"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.edit_message_checklist.EditMessageChecklist.edit_message_checklist"
  },
  "edit_message_live_location": {
    "description": "Use this method to edit live location messages.",
    "parameters": {
      "latitude": {
        "type": "float",
        "required": true,
        "description": ""
      },
      "longitude": {
        "type": "float",
        "required": true,
        "description": ""
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "chat_id": {
        "type": "Union",
        "required": false,
        "description": ""
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "inline_message_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "live_period": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "horizontal_accuracy": {
        "type": "float",
        "required": false,
        "description": ""
      },
      "heading": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "proximity_alert_radius": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.messages.edit_message_live_location.EditMessageLiveLocation.edit_message_live_location"
  },
  "edit_message_media": {
    "description": "Use this method to edit animation, audio, document, photo, or video messages, or to add media to text messages.",
    "parameters": {
      "media": {
        "type": "Union",
        "required": true,
        "description": ""
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "chat_id": {
        "type": "Union",
        "required": false,
        "description": ""
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "inline_message_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.messages.edit_message_media.EditMessageMedia.edit_message_media"
  },
  "edit_message_reply_markup": {
    "description": "Use this method to edit only the reply markup of messages.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "chat_id": {
        "type": "Union",
        "required": false,
        "description": ""
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "inline_message_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.messages.edit_message_reply_markup.EditMessageReplyMarkup.edit_message_reply_markup"
  },
  "edit_message_text": {
    "description": "Use this method to edit text and game messages.",
    "parameters": {
      "text": {
        "type": "str",
        "required": true,
        "description": ""
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "chat_id": {
        "type": "Union",
        "required": false,
        "description": ""
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "inline_message_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": ""
      },
      "entities": {
        "type": "List",
        "required": false,
        "description": ""
      },
      "link_preview_options": {
        "type": "LinkPreviewOptions",
        "required": false,
        "description": ""
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.messages.edit_message_text.EditMessageText.edit_message_text"
  },
  "edit_story": {
    "description": "Edits a story previously posted by the bot on behalf of a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "story_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the story to edit"
      },
      "content": {
        "type": "tgram.types.InputStoryContent",
        "required": true,
        "description": "Content of the story"
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Caption of the story, 0-2048 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "required": false,
        "description": "Mode for parsing entities in the story caption"
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the caption"
      },
      "areas": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of clickable areas to be shown on the story"
      }
    },
    "returns": "tgram.types.Story",
    "path": "tgram.methods.payments_and_business.edit_story.EditStory.edit_story"
  },
  "edit_user_star_subscription": {
    "description": "Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns True on success.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": ""
      },
      "telegram_payment_charge_id": {
        "type": "str",
        "required": true,
        "description": ""
      },
      "is_canceled": {
        "type": "bool",
        "required": true,
        "description": ""
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.edit_user_star_subscription.EditUserStarSubscription.edit_user_star_subscription"
  },
  "export_chat_invite_link": {
    "description": "Use this method to export an invite link to a supergroup or a channel. The bot must be an administrator",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Id: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      }
    },
    "returns": "str",
    "path": "tgram.methods.chats.export_chat_invite_link.ExportChatInviteLink.export_chat_invite_link"
  },
  "forward_message": {
    "description": "Use this method to forward messages of any kind.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "from_chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)"
      },
      "message_id": {
        "type": "int",
        "required": true,
        "description": "Message identifier in the chat specified in from_chat_id"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Unique identifier for the target message thread (topic) of the forum; for forum supergroups only"
      },
      "video_start_timestamp": {
        "type": "int",
        "required": false,
        "description": "New start timestamp for the forwarded video in the message"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound"
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the forwarded message from forwarding and saving"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.forward_message.ForwardMessage.forward_message"
  },
  "forward_messages": {
    "description": "Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded,",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "from_chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)"
      },
      "message_ids": {
        "type": "List",
        "required": true,
        "description": "Message identifiers in the chat specified in from_chat_id"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the messages will be sent"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound"
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the forwarded message from forwarding and saving"
      }
    },
    "returns": "List",
    "path": "tgram.methods.messages.forward_messages.ForwardMessages.forward_messages"
  },
  "get_available_gifts": {
    "description": "Returns the list of gifts that can be sent by the bot to users. Requires no parameters. Returns a Gifts object.",
    "parameters": {},
    "returns": "Gifts",
    "path": "tgram.methods.bot.get_available_gifts.GetAvailableGifts.get_available_gifts"
  },
  "get_business_account_gifts": {
    "description": "Use this method to get the gifts received and owned by a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "exclude_unsaved": {
        "type": "bool",
        "required": false,
        "description": "Exclude gifts that aren't saved to the account's profile page"
      },
      "exclude_saved": {
        "type": "bool",
        "required": false,
        "description": "Exclude gifts that are saved to the account's profile page"
      },
      "exclude_unlimited": {
        "type": "bool",
        "required": false,
        "description": "Exclude gifts that can be purchased an unlimited number of times"
      },
      "exclude_limited": {
        "type": "bool",
        "required": false,
        "description": "Exclude gifts that can be purchased a limited number of times"
      },
      "exclude_unique": {
        "type": "bool",
        "required": false,
        "description": "Exclude unique gifts"
      },
      "sort_by_price": {
        "type": "bool",
        "required": false,
        "description": "Sort results by gift price instead of send date"
      },
      "offset": {
        "type": "str",
        "required": false,
        "description": "Offset of the first entry to return; use empty string for first chunk"
      },
      "limit": {
        "type": "int",
        "required": false,
        "description": "Maximum number of gifts to return; 1-100, defaults to 100"
      }
    },
    "returns": "OwnedGifts",
    "path": "tgram.methods.payments_and_business.get_business_account_gifts.GetBusinessAccountGifts.get_business_account_gifts"
  },
  "get_business_account_star_balance": {
    "description": "Returns the amount of Telegram Stars owned by a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      }
    },
    "returns": "StarAmount",
    "path": "tgram.methods.payments_and_business.get_business_account_star_balance.GetBusinessAccountStarBalance.get_business_account_star_balance"
  },
  "get_business_connection": {
    "description": "Use this method to get information about the connection of the bot with a business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      }
    },
    "returns": "BusinessConnection",
    "path": "tgram.methods.payments_and_business.get_business_connection.GetBusinessConnection.get_business_connection"
  },
  "get_chat": {
    "description": "Use this method to get up to date information about the chat (current name of the user for one-on-one",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"
      }
    },
    "returns": "ChatFullInfo",
    "path": "tgram.methods.chats.get_chat.GetChat.get_chat"
  },
  "get_chat_administrators": {
    "description": "",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": ""
      }
    },
    "returns": "List",
    "path": "tgram.methods.chats.get_chat_administrators.GetChatAdministrators.get_chat_administrators"
  },
  "get_chat_member": {
    "description": "",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": ""
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.chats.get_chat_member.GetChatMember.get_chat_member"
  },
  "get_chat_member_count": {
    "description": "Use this method to get the number of members in a chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"
      }
    },
    "returns": "int",
    "path": "tgram.methods.chats.get_chat_member_count.GetChatMemberCount.get_chat_member_count"
  },
  "get_chat_menu_button": {
    "description": "Use this method to get the current value of the bot's menu button",
    "parameters": {
      "chat_id": {
        "type": "int",
        "required": false,
        "description": "Unique identifier for the target private chat.\nIf not specified, default bot's menu button will be returned."
      }
    },
    "returns": "MenuButton",
    "path": "tgram.methods.chats.get_chat_menu_button.GetChatMenuButton.get_chat_menu_button"
  },
  "get_custom_emoji_stickers": {
    "description": "Use this method to get information about custom emoji stickers by their identifiers.",
    "parameters": {
      "custom_emoji_ids": {
        "type": "List",
        "required": true,
        "description": "List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified."
      }
    },
    "returns": "List",
    "path": "tgram.methods.chats.get_custom_emoji_stickers.GetCustomEmojiStickers.get_custom_emoji_stickers"
  },
  "get_file": {
    "description": "Use this method to get basic info about a file and prepare it for downloading.",
    "parameters": {
      "file_id": {
        "type": "str",
        "required": true,
        "description": "File identifier"
      }
    },
    "returns": "File",
    "path": "tgram.methods.files.get_file.GetFile.get_file"
  },
  "get_file_url": {
    "description": "Get a valid URL for downloading a file.",
    "parameters": {
      "file_id": {
        "type": "str",
        "required": true,
        "description": "File identifier to get download URL for."
      }
    },
    "returns": "str",
    "path": "tgram.methods.files.get_file_url.GetFileUrl.get_file_url"
  },
  "get_forum_topic_icon_stickers": {
    "description": "Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user.",
    "parameters": {},
    "returns": "List",
    "path": "tgram.methods.forums.get_forum_topic_icon_stickers.GetForumTopicIconStickers.get_forum_topic_icon_stickers"
  },
  "get_game_high_scores": {
    "description": "Use this method to get data for high score tables. Will return the score of the specified user and several of",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "User identifier"
      },
      "chat_id": {
        "type": "int",
        "required": false,
        "description": "Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": "Required if inline_message_id is not specified. Identifier of the sent message"
      },
      "inline_message_id": {
        "type": "str",
        "required": false,
        "description": "Required if chat_id and message_id are not specified. Identifier of the inline message"
      }
    },
    "returns": "List",
    "path": "tgram.methods.other.get_game_high_scores.GetGameHighScores.get_game_high_scores"
  },
  "get_me": {
    "description": "Returns basic information about the bot in form of a User object.",
    "parameters": {},
    "returns": "User",
    "path": "tgram.methods.bot.get_me.GetMe.get_me"
  },
  "get_my_commands": {
    "description": "Use this method to get the current list of the bot's commands.",
    "parameters": {
      "scope": {
        "type": "BotCommandScope",
        "required": false,
        "description": "The scope of users for which the commands are relevant.\nDefaults to BotCommandScopeDefault."
      },
      "language_code": {
        "type": "str",
        "required": false,
        "description": "A two-letter ISO 639-1 language code. If empty,\ncommands will be applied to all users from the given scope,\nfor whose language there are no dedicated commands"
      }
    },
    "returns": "List",
    "path": "tgram.methods.bot.get_my_commands.GetMyCommands.get_my_commands"
  },
  "get_my_default_administrator_rights": {
    "description": "Use this method to get the current default administrator rights of the bot.",
    "parameters": {
      "for_channels": {
        "type": "bool",
        "required": false,
        "description": "Pass True to get the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be returned."
      }
    },
    "returns": "ChatAdministratorRights",
    "path": "tgram.methods.bot.get_my_default_administrator_rights.GetMyDefaultAdministratorRights.get_my_default_administrator_rights"
  },
  "get_my_description": {
    "description": "Use this method to get the current bot description for the given user language.",
    "parameters": {
      "language_code": {
        "type": "str",
        "required": false,
        "description": "A two-letter ISO 639-1 language code or an empty string"
      }
    },
    "returns": "BotDescription",
    "path": "tgram.methods.bot.get_my_description.GetMyDescription.get_my_description"
  },
  "get_my_name": {
    "description": "Use this method to get the current bot name for the given user language.",
    "parameters": {
      "language_code": {
        "type": "str",
        "required": false,
        "description": "Optional. A two-letter ISO 639-1 language code or an empty string"
      }
    },
    "returns": "BotName",
    "path": "tgram.methods.bot.get_my_name.GetMyName.get_my_name"
  },
  "get_my_short_description": {
    "description": "Use this method to get the current bot short description for the given user language.",
    "parameters": {
      "language_code": {
        "type": "str",
        "required": false,
        "description": "A two-letter ISO 639-1 language code or an empty string"
      }
    },
    "returns": "BotShortDescription",
    "path": "tgram.methods.bot.get_my_short_description.GetMyShortDescription.get_my_short_description"
  },
  "get_my_star_balance": {
    "description": "Use this method to get the current Telegram Stars balance of the bot.",
    "parameters": {},
    "returns": "StarAmount",
    "path": "tgram.methods.bot.get_my_stars_balance.GetMyStarBalance.get_my_star_balance"
  },
  "get_star_transactions": {
    "description": "Returns the bot's Telegram Star transactions in chronological order.",
    "parameters": {
      "offset": {
        "type": "int",
        "required": false,
        "description": "Number of transactions to skip in the response"
      },
      "limit": {
        "type": "int",
        "required": false,
        "description": "The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100."
      }
    },
    "returns": "StarTransactions",
    "path": "tgram.methods.payments_and_business.get_star_transactions.GetStarTransactions.get_star_transactions"
  },
  "get_sticker_set": {
    "description": "Use this method to get a sticker set. On success, a StickerSet object is returned.",
    "parameters": {
      "name": {
        "type": "str",
        "required": true,
        "description": "Sticker set name"
      }
    },
    "returns": "StickerSet",
    "path": "tgram.methods.stickers.get_sticker_set.GetStickerSet.get_sticker_set"
  },
  "get_updates": {
    "description": "Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.",
    "parameters": {
      "offset": {
        "type": "int",
        "required": false,
        "description": "Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates.\nBy default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset\nhigher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue.\nAll previous updates will forgotten."
      },
      "limit": {
        "type": "int",
        "required": false,
        "description": "Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100."
      },
      "timeout": {
        "type": "int",
        "required": false,
        "description": "Request connection timeout"
      },
      "allowed_updates": {
        "type": "List",
        "required": false,
        "description": "Array of string. List the types of updates you want your bot to receive."
      }
    },
    "returns": "List",
    "path": "tgram.methods.bot.get_updates.GetUpdates.get_updates"
  },
  "get_user_chat_boosts": {
    "description": "Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      }
    },
    "returns": "UserChatBoosts",
    "path": "tgram.methods.chats.get_user_chat_boosts.GetUserChatBoosts.get_user_chat_boosts"
  },
  "get_user_profile_photos": {
    "description": "Use this method to get a list of profile pictures for a user.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      },
      "offset": {
        "type": "int",
        "required": false,
        "description": "Sequential number of the first photo to be returned. By default, all photos are returned."
      },
      "limit": {
        "type": "int",
        "required": false,
        "description": "Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100."
      }
    },
    "returns": "UserProfilePhotos",
    "path": "tgram.methods.chats.get_user_profile_photos.GetUserProfilePhotos.get_user_profile_photos"
  },
  "get_webhook_info": {
    "description": "Use this method to get current webhook status. Requires no parameters.",
    "parameters": {},
    "returns": "WebhookInfo",
    "path": "tgram.methods.bot.get_webhook_info.GetWebhookInfo.get_webhook_info"
  },
  "gift_premium_subscription": {
    "description": "Gifts a Telegram Premium subscription to the given user.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user who will receive a Telegram Premium subscription"
      },
      "month_count": {
        "type": "int",
        "required": true,
        "description": "Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12"
      },
      "star_count": {
        "type": "int",
        "required": true,
        "description": "Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months"
      },
      "text": {
        "type": "str",
        "required": false,
        "description": "Text that will be shown along with the service message about the subscription; 0-128 characters"
      },
      "text_parse_mode": {
        "type": "str",
        "required": false,
        "description": "Mode for parsing entities in the text"
      },
      "text_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the gift text"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.gift_premium_subscription.GiftPremiumSubscription.gift_premium_subscription"
  },
  "hide_general_forum_topic": {
    "description": "Use this method to hide the 'General' topic in a forum supergroup chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.hide_general_forum_topic.HideGeneralForumTopic.hide_general_forum_topic"
  },
  "leave_chat": {
    "description": "Use this method for your bot to leave a group, supergroup or channel. Returns True on success.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.leave_chat.LeaveChat.leave_chat"
  },
  "log_out": {
    "description": "Use this method to log out from the cloud Bot API server before launching the bot locally.",
    "parameters": {},
    "returns": "bool",
    "path": "tgram.methods.bot.log_out.LogOut.log_out"
  },
  "pin_chat_message": {
    "description": "Use this method to pin a message in a supergroup.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "message_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of a message to pin"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if it is not necessary to send a notification\nto all group members about the new pinned message"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the business connection on behalf of which the message will be pinned"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.pin_chat_message.PinChatMessage.pin_chat_message"
  },
  "post_story": {
    "description": "Posts a story on behalf of a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "content": {
        "type": "tgram.types.InputStoryContent",
        "required": true,
        "description": "Content of the story"
      },
      "active_period": {
        "type": "int",
        "required": true,
        "description": "Period after which the story is moved to the archive, in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400"
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Caption of the story, 0-2048 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "required": false,
        "description": "Mode for parsing entities in the story caption"
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the caption"
      },
      "areas": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of clickable areas to be shown on the story"
      },
      "post_to_chat_page": {
        "type": "bool",
        "required": false,
        "description": "Pass True to keep the story accessible after it expires"
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Pass True if the content of the story must be protected from forwarding and screenshotting"
      }
    },
    "returns": "tgram.types.Story",
    "path": "tgram.methods.payments_and_business.post_story.PostStory.post_story"
  },
  "promote_chat_member": {
    "description": "Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (\nin the format @channelusername)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      },
      "is_anonymous": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator's presence in the chat is hidden"
      },
      "can_manage_chat": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can access the chat event log, chat statistics,\nmessage statistics in channels, see channel members,\nsee anonymous administrators in supergroups and ignore slow mode.\nImplied by any other administrator privilege"
      },
      "can_delete_messages": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can delete messages of other users"
      },
      "can_manage_video_chats": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can manage voice chats\nFor now, bots can use this privilege only for passing to other administrators."
      },
      "can_restrict_members": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can restrict, ban or unban chat members"
      },
      "can_promote_members": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can add new administrators with a subset\nof his own privileges or demote administrators that he has promoted, directly or indirectly\n(promoted by administrators that were appointed by him)"
      },
      "can_change_info": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can change chat title, photo and other settings"
      },
      "can_invite_users": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can invite new users to the chat"
      },
      "can_post_stories": {
        "type": "bool",
        "required": false,
        "description": "Pass True if the administrator can create the channel's stories"
      },
      "can_edit_stories": {
        "type": "bool",
        "required": false,
        "description": "Pass True if the administrator can edit the channel's stories"
      },
      "can_delete_stories": {
        "type": "bool",
        "required": false,
        "description": "Pass True if the administrator can delete the channel's stories"
      },
      "can_post_messages": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can create channel posts, channels only"
      },
      "can_edit_messages": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can edit messages of other users, channels only"
      },
      "can_pin_messages": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the administrator can pin messages, supergroups only"
      },
      "can_manage_topics": {
        "type": "bool",
        "required": false,
        "description": "Pass True if the user is allowed to create, rename, close,\nand reopen forum topics, supergroups only"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.promote_chat_member.PromoteChatMember.promote_chat_member"
  },
  "read_business_message": {
    "description": "Marks an incoming message as read on behalf of a business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection on behalf of which to read the message"
      },
      "chat_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours."
      },
      "message_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the message to mark as read"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.read_business_message.ReadBusinessMessage.read_business_message"
  },
  "refund_star_payment": {
    "description": "Refunds a successful payment in Telegram Stars. Returns True on success.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the user whose payment will be refunded"
      },
      "telegram_payment_charge_id": {
        "type": "str",
        "required": true,
        "description": "Telegram payment identifier"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.refund_star_payment.RefundStarPayment.refund_star_payment"
  },
  "remove_business_account_profile_photo": {
    "description": "Removes the current profile photo of a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "is_public": {
        "type": "bool",
        "required": false,
        "description": "Pass True to remove the public photo, which is visible even if the main photo is hidden by the business account's privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.remove_business_account_profile_photo.RemoveBusinessAccountProfilePhoto.remove_business_account_profile_photo"
  },
  "remove_chat_verification": {
    "description": "Removes verification from a chat that is currently verified on behalf of the organization represented by the bot. Returns True on success.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.remove_chat_verification.RemoveChatVerification.remove_chat_verification"
  },
  "remove_user_verification": {
    "description": "Removes verification from a user who is currently verified on behalf of the organization represented by the bot. Returns True on success.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.remove_user_verification.RemoveUserVerification.remove_user_verification"
  },
  "reopen_forum_topic": {
    "description": "Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "message_thread_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the topic to reopen"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.reopen_forum_topic.ReopenForumTopic.reopen_forum_topic"
  },
  "reopen_general_forum_topic": {
    "description": "Use this method to reopen the 'General' topic in a forum supergroup chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.reopen_general_forum_topic.ReopenGeneralForumTopic.reopen_general_forum_topic"
  },
  "replace_sticker_in_set": {
    "description": "Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling deleteStickerFromSet, then addStickerToSet,",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "User identifier of the sticker set owner"
      },
      "name": {
        "type": "str",
        "required": true,
        "description": "Sticker set name"
      },
      "old_sticker": {
        "type": "str",
        "required": true,
        "description": "File identifier of the replaced sticker"
      },
      "sticker": {
        "type": "InputSticker",
        "required": true,
        "description": "A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.replace_sticker_in_set.ReplaceStickerInSet.replace_sticker_in_set"
  },
  "restrict_chat_member": {
    "description": "Use this method to restrict a user in a supergroup.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target group or username of the target supergroup\nor channel (in the format @channelusername)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      },
      "permissions": {
        "type": "ChatPermissions",
        "required": true,
        "description": "Pass ChatPermissions object to set all permissions at once. Use this parameter instead of\npassing all boolean parameters to avoid backward compatibility problems in future."
      },
      "use_independent_chat_permissions": {
        "type": "bool",
        "required": false,
        "description": "Pass True if chat permissions are set independently.\nOtherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,\ncan_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes\npermissions; the can_send_polls permission will imply the can_send_messages permission."
      },
      "until_date": {
        "type": "int",
        "required": false,
        "description": "Date when restrictions will be lifted for the user, unix time.\nIf user is restricted for more than 366 days or less than 30 seconds from the current time,\nthey are considered to be restricted forever"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.restrict_chat_member.RestrictChatMember.restrict_chat_member"
  },
  "revoke_chat_invite_link": {
    "description": "Use this method to revoke an invite link created by the bot.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Id: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "invite_link": {
        "type": "str",
        "required": true,
        "description": "The invite link to revoke"
      }
    },
    "returns": "ChatInviteLink",
    "path": "tgram.methods.chats.revoke_chat_invite_link.RevokeChatInviteLink.revoke_chat_invite_link"
  },
  "run": {
    "description": "Use this method to run a couroutine function or handle new updates.",
    "parameters": {
      "main": {
        "type": "Optional",
        "required": false,
        "description": "The couroutine function."
      }
    },
    "returns": "Any",
    "path": "tgram.methods.bot.runner.Runner.run"
  },
  "save_prepared_inline_message": {
    "description": "Stores a message that can be sent by a user of a Mini App. Returns a PreparedInlineMessage object.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": ""
      },
      "result": {
        "type": "Union",
        "required": true,
        "description": ""
      },
      "allow_user_chats": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "allow_bot_chats": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "allow_group_chats": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "allow_channel_chats": {
        "type": "bool",
        "required": false,
        "description": ""
      }
    },
    "returns": "PreparedInlineMessage",
    "path": "tgram.methods.other.save_prepared_inline_message.SavePreparedInlineMessage.save_prepared_inline_message"
  },
  "send_animation": {
    "description": "Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound).",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "animation": {
        "type": "Union",
        "required": true,
        "description": "Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended),\npass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data."
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of a business connection, in which the message will be sent"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the video will be sent"
      },
      "duration": {
        "type": "int",
        "required": false,
        "description": "Duration of sent animation in seconds"
      },
      "width": {
        "type": "int",
        "required": false,
        "description": "Animation width"
      },
      "height": {
        "type": "int",
        "required": false,
        "description": "Animation height"
      },
      "thumbnail": {
        "type": "Union",
        "required": false,
        "description": "Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.\nThe thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.\nIgnored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,\nso you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>."
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the animation caption"
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "List of special entities that appear in the caption, which can be specified instead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages."
      },
      "has_spoiler": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the animation should be sent as a spoiler"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard\nor to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_animation.SendAnimation.send_animation"
  },
  "send_audio": {
    "description": "Use this method to send audio files, if you want Telegram clients to display them in the music player.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "audio": {
        "type": "Union",
        "required": true,
        "description": "Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended),\npass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data.\nAudio must be in the .MP3 or .M4A format."
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the target business connection"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the message will be sent"
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Audio caption, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the audio caption. See formatting options for more details."
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode"
      },
      "duration": {
        "type": "int",
        "required": false,
        "description": "Duration of the audio in seconds"
      },
      "performer": {
        "type": "str",
        "required": false,
        "description": "Performer"
      },
      "title": {
        "type": "str",
        "required": false,
        "description": "Track name"
      },
      "thumbnail": {
        "type": "Union",
        "required": false,
        "description": "Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.\nThe thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.\nIgnored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,\nso you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": ""
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_audio.SendAudio.send_audio"
  },
  "send_chat_action": {
    "description": "Use this method when you need to tell the user that something is happening on the bot's side.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel"
      },
      "action": {
        "type": "str",
        "required": true,
        "description": "Type of action to broadcast. Choose one, depending on what the user is about\nto receive: typing for text messages, upload_photo for photos, record_video or upload_video\nfor videos, record_voice or upload_voice for voice notes, upload_document for general files,\nchoose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes."
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of a business connection, in which the message will be sent"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "The thread to which the message will be sent(supergroups only)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.messages.send_chat_action.SendChatAction.send_chat_action"
  },
  "send_checklist": {
    "description": "Use this method to send a checklist on behalf of a connected business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection on behalf of which the message will be sent"
      },
      "chat_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier for the target chat"
      },
      "checklist": {
        "type": "InputChecklist",
        "required": true,
        "description": "A JSON-serialized object for the checklist to send"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound"
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the message effect to be added to the message"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "A JSON-serialized object for description of the message to reply to"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": "A JSON-serialized object for an inline keyboard"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_checklist.SendChecklist.send_checklist"
  },
  "send_contact": {
    "description": "Use this method to send phone contacts. On success, the sent Message is returned.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel"
      },
      "phone_number": {
        "type": "str",
        "required": true,
        "description": "Contact's phone number"
      },
      "first_name": {
        "type": "str",
        "required": true,
        "description": "Contact's first name"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of a business connection, in which the message will be sent"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "The thread to which the message will be sent"
      },
      "last_name": {
        "type": "str",
        "required": false,
        "description": "Contact's last name"
      },
      "vcard": {
        "type": "str",
        "required": false,
        "description": "Additional data about the contact in the form of a vCard, 0-2048 bytes"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard,\ncustom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_contact.SendContact.send_contact"
  },
  "send_dice": {
    "description": "Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the target business connection"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "The identifier of a message thread, unique within the chat to which the message with the thread identifier belongs"
      },
      "emoji": {
        "type": "str",
        "required": false,
        "description": "Emoji on which the dice throw animation is based. Currently, must be one of \u201c\ud83c\udfb2\u201d, \u201c\ud83c\udfaf\u201d, \u201c\ud83c\udfc0\u201d, \u201c\u26bd\u201d, \u201c\ud83c\udfb3\u201d, or \u201c\ud83c\udfb0\u201d.\nDice can have values 1-6 for \u201c\ud83c\udfb2\u201d, \u201c\ud83c\udfaf\u201d and \u201c\ud83c\udfb3\u201d, values 1-5 for \u201c\ud83c\udfc0\u201d and \u201c\u26bd\u201d, and values 1-64 for \u201c\ud83c\udfb0\u201d. Defaults to \u201c\ud83c\udfb2\u201d"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions\nto remove reply keyboard or to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_dice.SendDice.send_dice"
  },
  "send_document": {
    "description": "Use this method to send general files.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "document": {
        "type": "Union",
        "required": true,
        "description": "(document) File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a\nString for Telegram to get a file from the Internet, or upload a new one using multipart/form-data"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the target business connection"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the message will be sent"
      },
      "thumbnail": {
        "type": "Union",
        "required": false,
        "description": "InputFile or String : Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>"
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the document caption"
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode"
      },
      "disable_content_type_detection": {
        "type": "bool",
        "required": false,
        "description": "Disables automatic server-side content type detection for files uploaded using multipart/form-data"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard\nor to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_document.SendDocument.send_document"
  },
  "send_game": {
    "description": "Used to send the game.",
    "parameters": {
      "chat_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "game_short_name": {
        "type": "str",
        "required": true,
        "description": "Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather."
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of the business connection."
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of the thread to which the message will be sent."
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if content of the message needs to be protected from being viewed by the bot."
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of the message effect."
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_game.SendGame.send_game"
  },
  "send_gift": {
    "description": "Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns True on success.",
    "parameters": {
      "gift_id": {
        "type": "str",
        "required": true,
        "description": "Identifier of the gift"
      },
      "user_id": {
        "type": "int",
        "required": false,
        "description": "Required if chat_id is not specified. Unique identifier of the target user who will receive the gift."
      },
      "chat_id": {
        "type": "Union",
        "required": false,
        "description": "Required if user_id is not specified. Unique identifier for the chat or username of the channel (in the format @channelusername) that will receive the gift."
      },
      "pay_for_upgrade": {
        "type": "bool",
        "required": false,
        "description": "Pass True to pay for the gift upgrade from the bot's balance,\nthereby making the upgrade free for the receiver"
      },
      "text": {
        "type": "str",
        "required": false,
        "description": "Text that will be shown along with the gift; 0-255 characters"
      },
      "text_parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the text. See formatting options for more details.\nEntities other than \u201cbold\u201d, \u201citalic\u201d, \u201cunderline\u201d, \u201cstrikethrough\u201d, \u201cspoiler\u201d, and \u201ccustom_emoji\u201d are ignored."
      },
      "text_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of text_parse_mode. Entities other than \u201cbold\u201d, \u201citalic\u201d, \u201cunderline\u201d, \u201cstrikethrough\u201d, \u201cspoiler\u201d, and \u201ccustom_emoji\u201d are ignored."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.messages.send_gift.SendGift.send_gift"
  },
  "send_invoice": {
    "description": "Sends invoice.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target private chat"
      },
      "title": {
        "type": "str",
        "required": true,
        "description": "Product name, 1-32 characters"
      },
      "description": {
        "type": "str",
        "required": true,
        "description": "Product description, 1-255 characters"
      },
      "payload": {
        "type": "str",
        "required": true,
        "description": ""
      },
      "currency": {
        "type": "str",
        "required": true,
        "description": "Three-letter ISO 4217 currency code,\nsee https://core.telegram.org/bots/payments#supported-currencies"
      },
      "prices": {
        "type": "List",
        "required": true,
        "description": "Price breakdown, a list of components\n(e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "The identifier of a message thread, in which the invoice message will be sent"
      },
      "provider_token": {
        "type": "str",
        "required": false,
        "description": "Payments provider token, obtained via @Botfather; Pass None to omit the parameter\nto use \"XTR\" currency"
      },
      "max_tip_amount": {
        "type": "int",
        "required": false,
        "description": "The maximum accepted amount for tips in the smallest units of the currency"
      },
      "suggested_tip_amounts": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized array of suggested amounts of tips in the smallest\nunits of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip\namounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount."
      },
      "start_parameter": {
        "type": "str",
        "required": false,
        "description": "Unique deep-linking parameter that can be used to generate this invoice\nwhen used as a start parameter"
      },
      "provider_data": {
        "type": "str",
        "required": false,
        "description": "A JSON-serialized data about the invoice, which will be shared with the payment provider.\nA detailed description of required fields should be provided by the payment provider."
      },
      "photo_url": {
        "type": "str",
        "required": false,
        "description": "URL of the product photo for the invoice. Can be a photo of the goods\nor a marketing image for a service. People like it better when they see what they are paying for."
      },
      "photo_size": {
        "type": "int",
        "required": false,
        "description": "Photo size in bytes"
      },
      "photo_width": {
        "type": "int",
        "required": false,
        "description": "Photo width"
      },
      "photo_height": {
        "type": "int",
        "required": false,
        "description": "Photo height"
      },
      "need_name": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if you require the user's full name to complete the order"
      },
      "need_phone_number": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if you require the user's phone number to complete the order"
      },
      "need_email": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if you require the user's email to complete the order"
      },
      "need_shipping_address": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if you require the user's shipping address to complete the order"
      },
      "send_phone_number_to_provider": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if user's phone number should be sent to provider"
      },
      "send_email_to_provider": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if user's email address should be sent to provider"
      },
      "is_flexible": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the final price depends on the shipping method"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "The identifier of a message effect to be applied to the message"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": "A JSON-serialized object for an inline keyboard. If empty,\none 'Pay total price' button will be shown. If not empty, the first button must be a Pay button"
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_invoice.SendInvoice.send_invoice"
  },
  "send_location": {
    "description": "Use this method to send point on the map. On success, the sent Message is returned.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "latitude": {
        "type": "float",
        "required": true,
        "description": "Latitude of the location"
      },
      "longitude": {
        "type": "float",
        "required": true,
        "description": "Longitude of the location"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of a business connection, in which the message will be sent"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the message will be sent"
      },
      "horizontal_accuracy": {
        "type": "float",
        "required": false,
        "description": "The radius of uncertainty for the location, measured in meters; 0-1500"
      },
      "live_period": {
        "type": "int",
        "required": false,
        "description": "Period in seconds during which the location will be updated (see Live Locations, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely."
      },
      "heading": {
        "type": "int",
        "required": false,
        "description": "For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified."
      },
      "proximity_alert_radius": {
        "type": "int",
        "required": false,
        "description": "For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified."
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard\nor to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_location.SendLocation.send_location"
  },
  "send_media_from_file_id": {
    "description": "",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": ""
      },
      "file_id": {
        "type": "str",
        "required": true,
        "description": ""
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": ""
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": ""
      },
      "show_caption_above_media": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": ""
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": ""
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": ""
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_media_from_file_id.SendMediaFromFileId.send_media_from_file_id"
  },
  "send_media_group": {
    "description": "Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "media": {
        "type": "List",
        "required": true,
        "description": "A JSON-serialized array describing messages to be sent, must include 2-10 items"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of a business connection, in which the message will be sent"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the messages will be sent"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the messages silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "List",
    "path": "tgram.methods.messages.send_media_group.SendMediaGroup.send_media_group"
  },
  "send_message": {
    "description": "Use this method to send text messages.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "text": {
        "type": "str",
        "required": true,
        "description": "Text of the message to be sent"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the target business connection"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Unique identifier for the target message thread (topic) of the forum; for forum supergroups only"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the message text."
      },
      "entities": {
        "type": "List",
        "required": false,
        "description": "List of special entities that appear in message text, which can be specified instead of parse_mode"
      },
      "link_preview_options": {
        "type": "LinkPreviewOptions",
        "required": false,
        "description": "Options for previewing links."
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "If True, the message content will be hidden for all users except for the target user"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_message.SendMessage.send_message"
  },
  "send_paid_media": {
    "description": "Use this method to send paid media to channel chats. On success, the sent Message is returned.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "star_count": {
        "type": "int",
        "required": true,
        "description": "The number of Telegram Stars that must be paid to buy access to the media"
      },
      "media": {
        "type": "List",
        "required": true,
        "description": "A JSON-serialized array describing the media to be sent; up to 10 items"
      },
      "payload": {
        "type": "str",
        "required": false,
        "description": "Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes."
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Media caption, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the media caption"
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "List of special entities that appear in the caption, which can be specified instead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the caption must be shown above the message media"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Description of the message to reply to"
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the business connection on behalf of which the message will be sent"
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_paid_media.SendPaidMedia.send_paid_media"
  },
  "send_photo": {
    "description": "Use this method to send photos. On success, the sent Message is returned.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "photo": {
        "type": "Union",
        "required": true,
        "description": "Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended),\npass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data.\nThe photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20."
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the target business connection"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the message will be sent"
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the photo caption."
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages."
      },
      "has_spoiler": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the photo should be sent as a spoiler"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions\nto remove reply keyboard or to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_photo.SendPhoto.send_photo"
  },
  "send_poll": {
    "description": "Use this method to send a native poll.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel"
      },
      "question": {
        "type": "str",
        "required": true,
        "description": "Poll question, 1-300 characters"
      },
      "options": {
        "type": "List",
        "required": true,
        "description": "A JSON-serialized list of 2-10 answer options"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of the business connection to send the message through"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "The identifier of a message thread, in which the poll will be sent"
      },
      "question_parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the question. See formatting options for more details. Currently, only custom emoji entities are allowed"
      },
      "question_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of question_parse_mode"
      },
      "is_anonymous": {
        "type": "bool",
        "required": false,
        "description": "True, if the poll needs to be anonymous, defaults to True"
      },
      "type": {
        "type": "str",
        "required": false,
        "description": "Poll type, \u201cquiz\u201d or \u201cregular\u201d, defaults to \u201cregular\u201d"
      },
      "allows_multiple_answers": {
        "type": "bool",
        "required": false,
        "description": "True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False"
      },
      "correct_option_id": {
        "type": "int",
        "required": false,
        "description": "0-based identifier of the correct answer option. Available only for polls in quiz mode,\ndefaults to None"
      },
      "explanation": {
        "type": "str",
        "required": false,
        "description": "Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll,\n0-200 characters with at most 2 line feeds after entities parsing"
      },
      "explanation_parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the explanation. See formatting options for more details."
      },
      "explanation_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the explanation,\nwhich can be specified instead of parse_mode"
      },
      "open_period": {
        "type": "int",
        "required": false,
        "description": "Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date."
      },
      "close_date": {
        "type": "int",
        "required": false,
        "description": "Point in time (Unix timestamp) when the poll will be automatically closed."
      },
      "is_closed": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the poll needs to be immediately closed. This can be useful for poll preview."
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of the message effect to apply to the sent message"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard,\ninstructions to remove reply keyboard or to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_poll.SendPoll.send_poll"
  },
  "send_sticker": {
    "description": "Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "sticker": {
        "type": "Union",
        "required": true,
        "description": "Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL\nas a String for Telegram to get a .webp file from the Internet, or upload a new one using multipart/form-data."
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the target business connection"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the message will be sent"
      },
      "emoji": {
        "type": "str",
        "required": false,
        "description": "Emoji associated with the sticker; only for just uploaded stickers"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "to disable the notification"
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard\nor to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_sticker.SendSticker.send_sticker"
  },
  "send_venue": {
    "description": "Use this method to send information about a venue. On success, the sent Message is returned.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel"
      },
      "latitude": {
        "type": "float",
        "required": true,
        "description": "Latitude of the venue"
      },
      "longitude": {
        "type": "float",
        "required": true,
        "description": "Longitude of the venue"
      },
      "title": {
        "type": "str",
        "required": true,
        "description": "Name of the venue"
      },
      "address": {
        "type": "str",
        "required": true,
        "description": "Address of the venue"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of a business connection, in which the message will be sent"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "The thread to which the message will be sent"
      },
      "foursquare_id": {
        "type": "str",
        "required": false,
        "description": "Foursquare identifier of the venue"
      },
      "foursquare_type": {
        "type": "str",
        "required": false,
        "description": "Foursquare type of the venue, if known. (For example, \u201carts_entertainment/default\u201d,\n\u201carts_entertainment/aquarium\u201d or \u201cfood/icecream\u201d.)"
      },
      "google_place_id": {
        "type": "str",
        "required": false,
        "description": "Google Places identifier of the venue"
      },
      "google_place_type": {
        "type": "str",
        "required": false,
        "description": "Google Places type of the venue."
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard,\ncustom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_venue.SendVenue.send_venue"
  },
  "send_video": {
    "description": "Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "video": {
        "type": "Union",
        "required": true,
        "description": "Video to send. You can either pass a file_id as String to resend a video that is already on the Telegram servers, or upload a new video file using multipart/form-data."
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of a business connection, in which the message will be sent"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the video will be sent"
      },
      "duration": {
        "type": "int",
        "required": false,
        "description": "Duration of sent video in seconds"
      },
      "width": {
        "type": "int",
        "required": false,
        "description": "Video width"
      },
      "height": {
        "type": "int",
        "required": false,
        "description": "Video height"
      },
      "thumbnail": {
        "type": "Union",
        "required": false,
        "description": "Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>."
      },
      "cover": {
        "type": "Union",
        "required": false,
        "description": "Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass \u201cattach://<file_attach_name>\u201d to upload a new one using multipart/form-data under <file_attach_name> name."
      },
      "start_timestamp": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the video caption"
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "List of special entities that appear in the caption, which can be specified instead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages."
      },
      "has_spoiler": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the video should be sent as a spoiler"
      },
      "supports_streaming": {
        "type": "bool",
        "required": false,
        "description": "Pass True, if the uploaded video is suitable for streaming"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard\nor to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_video.SendVideo.send_video"
  },
  "send_video_note": {
    "description": "As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "video_note": {
        "type": "Union",
        "required": true,
        "description": ""
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of a business connection, in which the message will be sent"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the video note will be sent"
      },
      "duration": {
        "type": "int",
        "required": false,
        "description": "Duration of sent video in seconds"
      },
      "length": {
        "type": "int",
        "required": false,
        "description": "Video width and height, i.e. diameter of the video message"
      },
      "thumbnail": {
        "type": "Union",
        "required": false,
        "description": "Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.\nThe thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.\nIgnored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,\nso you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>."
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard\nor to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_video_note.SendVideoNote.send_video_note"
  },
  "send_voice": {
    "description": "Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "voice": {
        "type": "Union",
        "required": true,
        "description": "Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended),\npass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data."
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the target business connection"
      },
      "message_thread_id": {
        "type": "int",
        "required": false,
        "description": "Identifier of a message thread, in which the message will be sent"
      },
      "caption": {
        "type": "str",
        "required": false,
        "description": "Voice message caption, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "Literal",
        "required": false,
        "description": "Mode for parsing entities in the voice message caption. See formatting options for more details."
      },
      "caption_entities": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode"
      },
      "duration": {
        "type": "int",
        "required": false,
        "description": "Duration of the voice message in seconds"
      },
      "disable_notification": {
        "type": "bool",
        "required": false,
        "description": "Sends the message silently. Users will receive a notification with no sound."
      },
      "protect_content": {
        "type": "bool",
        "required": false,
        "description": "Protects the contents of the sent message from forwarding and saving"
      },
      "message_effect_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier for the message effect"
      },
      "reply_parameters": {
        "type": "ReplyParameters",
        "required": false,
        "description": "Reply parameters."
      },
      "reply_markup": {
        "type": "Union",
        "required": false,
        "description": "Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions\nto remove reply keyboard or to force a reply from the user."
      },
      "allow_paid_broadcast": {
        "type": "bool",
        "required": false,
        "description": "Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.\nThe relevant Stars will be withdrawn from the bot's balance"
      }
    },
    "returns": "Message",
    "path": "tgram.methods.messages.send_voice.SendVoice.send_voice"
  },
  "set_business_account_bio": {
    "description": "Changes the bio of a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "bio": {
        "type": "str",
        "required": false,
        "description": "The new value of the bio for the business account; 0-140 characters"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.set_business_account_bio.SetBusinessAccountBio.set_business_account_bio"
  },
  "set_business_account_gift_settings": {
    "description": "Changes the privacy settings pertaining to incoming gifts in a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "show_gift_button": {
        "type": "bool",
        "required": true,
        "description": "Pass True, if a button for sending a gift to the user or by the business account must always be shown in the input field"
      },
      "accepted_gift_types": {
        "type": "tgram.types.AcceptedGiftTypes",
        "required": true,
        "description": "Types of gifts accepted by the business account"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.set_business_account_gift_settings.SetBusinessAccountGiftSettings.set_business_account_gift_settings"
  },
  "set_business_account_name": {
    "description": "Changes the first and last name of a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "first_name": {
        "type": "str",
        "required": true,
        "description": "The new value of the first name for the business account; 1-64 characters"
      },
      "last_name": {
        "type": "str",
        "required": false,
        "description": "The new value of the last name for the business account; 0-64 characters"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.set_business_account_name.SetBusinessAccountName.set_business_account_name"
  },
  "set_business_account_profile_photo": {
    "description": "Changes the profile photo of a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "photo": {
        "type": "Union",
        "required": true,
        "description": "The new profile photo to set"
      },
      "is_public": {
        "type": "bool",
        "required": false,
        "description": "Pass True to set the public photo, which will be visible even if the main photo is hidden by the business account's privacy settings. An account can have only one public photo."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.set_business_account_profile_photo.SetBusinessAccountProfilePhoto.set_business_account_profile_photo"
  },
  "set_business_account_username": {
    "description": "Changes the username of a managed business account.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "username": {
        "type": "str",
        "required": false,
        "description": "The new value of the username for the business account; 0-32 characters"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.set_business_account_username.SetBusinessAccountUsername.set_business_account_username"
  },
  "set_chat_administrator_custom_title": {
    "description": "Use this method to set a custom title for an administrator in a supergroup promoted by the bot.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup\n(in the format @supergroupusername)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      },
      "custom_title": {
        "type": "str",
        "required": true,
        "description": "New custom title for the administrator;\n0-16 characters, emoji are not allowed"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle.set_chat_administrator_custom_title"
  },
  "set_chat_description": {
    "description": "Use this method to change the description of a supergroup or a channel.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "description": {
        "type": "str",
        "required": false,
        "description": "Str: New chat description, 0-255 characters"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.set_chat_description.SetChatDescription.set_chat_description"
  },
  "set_chat_menu_button": {
    "description": "Use this method to change the bot's menu button in a private chat,",
    "parameters": {
      "chat_id": {
        "type": "int",
        "required": false,
        "description": "Unique identifier for the target private chat.\nIf not specified, default bot's menu button will be changed."
      },
      "menu_button": {
        "type": "MenuButton",
        "required": false,
        "description": "A JSON-serialized object for the new bot's menu button. Defaults to MenuButtonDefault"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.set_chat_menu_button.SetChatMenuButton.set_chat_menu_button"
  },
  "set_chat_permissions": {
    "description": "Use this method to set default chat permissions for all members.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup\n(in the format @supergroupusername)"
      },
      "permissions": {
        "type": "ChatPermissions",
        "required": true,
        "description": "New default chat permissions"
      },
      "use_independent_chat_permissions": {
        "type": "bool",
        "required": false,
        "description": "Pass True if chat permissions are set independently. Otherwise,\nthe can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,\ncan_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and\ncan_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.set_chat_permissions.SetChatPermissions.set_chat_permissions"
  },
  "set_chat_photo": {
    "description": "Use this method to set a new profile photo for the chat. Photos can't be changed for private chats.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Int or Str: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "photo": {
        "type": "Union",
        "required": true,
        "description": "InputFile: New chat photo, uploaded using multipart/form-data"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.set_chat_photo.SetChatPhoto.set_chat_photo"
  },
  "set_chat_sticker_set": {
    "description": "Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)"
      },
      "sticker_set_name": {
        "type": "str",
        "required": true,
        "description": "Name of the sticker set to be set as the group sticker set"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.set_chat_sticker_set.SetChatStickerSet.set_chat_sticker_set"
  },
  "set_chat_title": {
    "description": "Use this method to change the title of a chat. Titles can't be changed for private chats.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "title": {
        "type": "str",
        "required": true,
        "description": "New chat title, 1-255 characters"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.set_chat_title.SetChatTitle.set_chat_title"
  },
  "set_custom_emoji_sticker_set_thumbnail": {
    "description": "Use this method to set the thumbnail of a custom emoji sticker set.",
    "parameters": {
      "name": {
        "type": "str",
        "required": true,
        "description": "Sticker set name"
      },
      "custom_emoji_id": {
        "type": "str",
        "required": false,
        "description": "Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.set_custom_emoji_sticker_set_thumbnail.SetCustomEmojiStickerSetThumbnail.set_custom_emoji_sticker_set_thumbnail"
  },
  "set_game_score": {
    "description": "",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": ""
      },
      "score": {
        "type": "int",
        "required": true,
        "description": ""
      },
      "force": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "disable_edit_message": {
        "type": "bool",
        "required": false,
        "description": ""
      },
      "chat_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "inline_message_id": {
        "type": "str",
        "required": false,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.other.set_game_score.SetGameScore.set_game_score"
  },
  "set_message_reaction": {
    "description": "Use this method to change the chosen reactions on a message.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"
      },
      "message_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the message to set reaction to"
      },
      "reaction": {
        "type": "List",
        "required": false,
        "description": "New list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message.\nA custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators."
      },
      "is_big": {
        "type": "bool",
        "required": false,
        "description": "Pass True to set the reaction with a big animation"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.messages.set_message_reaction.SetMessageReaction.set_message_reaction"
  },
  "set_my_commands": {
    "description": "Use this method to change the list of the bot's commands.",
    "parameters": {
      "commands": {
        "type": "List",
        "required": true,
        "description": "List of BotCommand. At most 100 commands can be specified."
      },
      "scope": {
        "type": "BotCommandScope",
        "required": false,
        "description": "The scope of users for which the commands are relevant.\nDefaults to BotCommandScopeDefault."
      },
      "language_code": {
        "type": "str",
        "required": false,
        "description": "A two-letter ISO 639-1 language code. If empty,\ncommands will be applied to all users from the given scope,\nfor whose language there are no dedicated commands"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.bot.set_my_commands.SetMyCommands.set_my_commands"
  },
  "set_my_default_administrator_rights": {
    "description": "Use this method to change the default administrator rights requested by the bot",
    "parameters": {
      "rights": {
        "type": "ChatAdministratorRights",
        "required": false,
        "description": "A JSON-serialized object describing new default administrator rights. If not specified,\nthe default administrator rights will be cleared."
      },
      "for_channels": {
        "type": "bool",
        "required": false,
        "description": "Pass True to change the default administrator rights of the bot in channels.\nOtherwise, the default administrator rights of the bot for groups and supergroups will be changed."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.bot.set_my_default_administrator_rights.SetMyDefaultAdministratorRights.set_my_default_administrator_rights"
  },
  "set_my_description": {
    "description": "Use this method to change the bot's description, which is shown in",
    "parameters": {
      "description": {
        "type": "str",
        "required": false,
        "description": "New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language."
      },
      "language_code": {
        "type": "str",
        "required": false,
        "description": "A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for\nwhose language there is no dedicated description."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.bot.set_my_description.SetMyDescription.set_my_description"
  },
  "set_my_name": {
    "description": "Use this method to change the bot's name. Returns True on success.",
    "parameters": {
      "name": {
        "type": "str",
        "required": false,
        "description": "Optional. New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language."
      },
      "language_code": {
        "type": "str",
        "required": false,
        "description": "Optional. A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose\nlanguage there is no dedicated name."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.bot.set_my_name.SetMyName.set_my_name"
  },
  "set_my_short_description": {
    "description": "Use this method to change the bot's short description, which is shown on the bot's profile page and",
    "parameters": {
      "short_description": {
        "type": "str",
        "required": false,
        "description": "New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language."
      },
      "language_code": {
        "type": "str",
        "required": false,
        "description": "A two-letter ISO 639-1 language code.\nIf empty, the short description will be applied to all users for whose language there is no dedicated short description."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.bot.set_my_short_description.SetMyShortDescription.set_my_short_description"
  },
  "set_passport_data_errors": {
    "description": "",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": ""
      },
      "errors": {
        "type": "List",
        "required": true,
        "description": ""
      }
    },
    "returns": "bool",
    "path": "tgram.methods.other.set_passport_data_errors.SetPassportDataErrors.set_passport_data_errors"
  },
  "set_sticker_emoji_list": {
    "description": "Use this method to set the emoji list of a sticker set.",
    "parameters": {
      "sticker": {
        "type": "str",
        "required": true,
        "description": ""
      },
      "emoji_list": {
        "type": "List",
        "required": true,
        "description": "List of emojis"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.set_sticker_emoji_list.SetStickerEmojiList.set_sticker_emoji_list"
  },
  "set_sticker_keywords": {
    "description": "Use this method to change search keywords assigned to a regular or custom emoji sticker.",
    "parameters": {
      "sticker": {
        "type": "str",
        "required": true,
        "description": "File identifier of the sticker."
      },
      "keywords": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.set_sticker_keywords.SetStickerKeywords.set_sticker_keywords"
  },
  "set_sticker_mask_position": {
    "description": "Use this method to change the mask position of a mask sticker.",
    "parameters": {
      "sticker": {
        "type": "str",
        "required": true,
        "description": "File identifier of the sticker."
      },
      "mask_position": {
        "type": "MaskPosition",
        "required": false,
        "description": "A JSON-serialized object for position where the mask should be placed on faces."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.set_sticker_mask_position.SetStickerMaskPosition.set_sticker_mask_position"
  },
  "set_sticker_position_in_set": {
    "description": "Use this method to move a sticker in a set created by the bot to a specific position . Returns True on success.",
    "parameters": {
      "sticker": {
        "type": "str",
        "required": true,
        "description": "File identifier of the sticker"
      },
      "position": {
        "type": "int",
        "required": true,
        "description": "New sticker position in the set, zero-based"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.set_sticker_position_in_set.SetStickerPositionInSet.set_sticker_position_in_set"
  },
  "set_sticker_set_thumbnail": {
    "description": "Use this method to set the thumbnail of a sticker set.",
    "parameters": {
      "name": {
        "type": "str",
        "required": true,
        "description": "Sticker set name"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "User identifier"
      },
      "format": {
        "type": "str",
        "required": true,
        "description": ""
      },
      "thumbnail": {
        "type": "Union",
        "required": false,
        "description": "A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a .TGS animation\nwith a thumbnail up to 32 kilobytes in size (see https://core.telegram.org/stickers#animated-sticker-requirements for animated sticker technical requirements),\nor a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-sticker-requirements for video sticker technical\nrequirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from\nthe Internet, or upload a new one using multipart/form-data. More information on Sending Files \u00bb. Animated and video sticker set thumbnails can't be uploaded via\nHTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.set_sticker_set_thumbnail.SetStickerSetThumbnail.set_sticker_set_thumbnail"
  },
  "set_sticker_set_title": {
    "description": "Use this method to set the title of a created sticker set.",
    "parameters": {
      "name": {
        "type": "str",
        "required": true,
        "description": "Sticker set name"
      },
      "title": {
        "type": "str",
        "required": true,
        "description": "New sticker set title"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.stickers.set_sticker_set_title.SetStickerSetTitle.set_sticker_set_title"
  },
  "set_user_emoji_status": {
    "description": "Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method requestEmojiStatusAccess. Returns True on success.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "OUnique identifier of the target user."
      },
      "emoji_status_custom_emoji_id": {
        "type": "str",
        "required": false,
        "description": "Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status."
      },
      "emoji_status_expiration_date": {
        "type": "int",
        "required": false,
        "description": "Expiration date of the emoji status, if any."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.other.set_user_emoji_status.SetUserEmojiStatus.set_user_emoji_status"
  },
  "set_webhook": {
    "description": "Use this method to specify a URL and receive incoming updates via an outgoing webhook.",
    "parameters": {
      "url": {
        "type": "str",
        "required": true,
        "description": "HTTPS URL to send updates to. Use an empty string to remove webhook integration, defaults to None"
      },
      "certificate": {
        "type": "Union",
        "required": false,
        "description": "Upload your public key certificate so that the root certificate in use can be checked, defaults to None"
      },
      "ip_address": {
        "type": "str",
        "required": false,
        "description": "The fixed IP address which will be used to send webhook requests instead of the IP address\nresolved through DNS, defaults to None"
      },
      "max_connections": {
        "type": "int",
        "required": false,
        "description": "The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100.\nDefaults to 40. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput,\ndefaults to None"
      },
      "allowed_updates": {
        "type": "List",
        "required": false,
        "description": "A JSON-serialized list of the update types you want your bot to receive. For example,\nspecify [\u201cmessage\u201d, \u201cedited_channel_post\u201d, \u201ccallback_query\u201d] to only receive updates of these types. See Update\nfor a complete list of available update types. Specify an empty list to receive all update types except chat_member (default).\nIf not specified, the previous setting will be used.\n\nPlease note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received\nfor a short period of time. Defaults to None"
      },
      "drop_pending_updates": {
        "type": "bool",
        "required": false,
        "description": "Pass True to drop all pending updates, defaults to None"
      },
      "secret_token": {
        "type": "str",
        "required": false,
        "description": "A secret token to be sent in a header \u201cX-Telegram-Bot-Api-Secret-Token\u201d in every webhook request, 1-256 characters.\nOnly characters A-Z, a-z, 0-9, _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you. Defaults to None"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.bot.set_webhook.SetWebhook.set_webhook"
  },
  "stop": {
    "description": "Use this method to stop getting and handling new updates.",
    "parameters": {},
    "returns": "Literal",
    "path": "tgram.methods.bot.runner.Runner.stop"
  },
  "stop_message_live_location": {
    "description": "",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "chat_id": {
        "type": "Union",
        "required": false,
        "description": ""
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": ""
      },
      "inline_message_id": {
        "type": "str",
        "required": false,
        "description": ""
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": ""
      }
    },
    "returns": "Union",
    "path": "tgram.methods.messages.stop_message_live_location.StopMessageLiveLocation.stop_message_live_location"
  },
  "stop_poll": {
    "description": "Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel"
      },
      "message_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the original message with the poll"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Identifier of the business connection to send the message through"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "required": false,
        "description": "A JSON-serialized object for a new message markup."
      }
    },
    "returns": "Poll",
    "path": "tgram.methods.messages.stop_poll.StopPoll.stop_poll"
  },
  "transfer_business_account_stars": {
    "description": "Transfers Telegram Stars from the business account balance to the bot's balance.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection"
      },
      "star_count": {
        "type": "int",
        "required": true,
        "description": "Number of Telegram Stars to transfer; 1-10000"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.transfer_business_account_stars.TransferBusinessAccountStars.transfer_business_account_stars"
  },
  "transfer_gift": {
    "description": "Transfers an owned unique gift to another user. Requires the can_transfer_and_upgrade_gifts business bot right.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection."
      },
      "owned_gift_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the regular gift that should be transferred."
      },
      "new_owner_chat_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the chat which will own the gift. The chat must be active in the last 24 hours."
      },
      "star_count": {
        "type": "int",
        "required": false,
        "description": "The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the can_transfer_stars business bot right is required."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.transfer_gift.TransferGift.transfer_gift"
  },
  "unban_chat_member": {
    "description": "Use this method to unban a previously kicked user in a supergroup or channel.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target group or username of the target supergroup or channel\n(in the format @username)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      },
      "only_if_banned": {
        "type": "bool",
        "required": false,
        "description": "Do nothing if the user is not banned"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.unban_chat_member.UnbanChatMember.unban_chat_member"
  },
  "unban_chat_sender_chat": {
    "description": "Use this method to unban a previously banned channel chat in a supergroup or channel.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "sender_chat_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target sender chat."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.unban_chat_sender_chat.UnbanChatSenderChat.unban_chat_sender_chat"
  },
  "unhide_general_forum_topic": {
    "description": "Use this method to unhide the 'General' topic in a forum supergroup chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.unhide_general_forum_topic.UnhideGeneralForumTopic.unhide_general_forum_topic"
  },
  "unpin_all_chat_messages": {
    "description": "Use this method to unpin a all pinned messages in a supergroup chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Int or Str: Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.unpin_all_chat_messages.UnpinAllChatMessages.unpin_all_chat_messages"
  },
  "unpin_all_forum_topic_messages": {
    "description": "Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "message_thread_id": {
        "type": "int",
        "required": true,
        "description": "Identifier of the topic"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.unpin_all_forum_topic_messages.UnpinAllForumTopicMessages.unpin_all_forum_topic_messages"
  },
  "unpin_all_general_forum_topic_messages": {
    "description": "Use this method to clear the list of pinned messages in a General forum topic.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of chat"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.forums.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages.unpin_all_general_forum_topic_messages"
  },
  "unpin_chat_message": {
    "description": "Use this method to unpin specific pinned message in a supergroup chat.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel\n(in the format @channelusername)"
      },
      "message_id": {
        "type": "int",
        "required": false,
        "description": "Int: Identifier of a message to unpin"
      },
      "business_connection_id": {
        "type": "str",
        "required": false,
        "description": "Unique identifier of the business connection on behalf of which the message will be pinned"
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.unpin_chat_message.UnpinChatMessage.unpin_chat_message"
  },
  "unrestrict_chat_member": {
    "description": "Use this method to unrestrict a user in a supergroup.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target group or username of the target supergroup\nor channel (in the format @channelusername)"
      },
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      },
      "use_independent_chat_permissions": {
        "type": "bool",
        "required": false,
        "description": "Pass True if chat permissions are set independently.\nOtherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,\ncan_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes\npermissions; the can_send_polls permission will imply the can_send_messages permission."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.unrestrict_chat_member.UnRestrictChatMember.unrestrict_chat_member"
  },
  "upgrade_gift": {
    "description": "Upgrades a given regular gift to a unique gift. Requires the can_transfer_and_upgrade_gifts business bot right.",
    "parameters": {
      "business_connection_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the business connection."
      },
      "owned_gift_id": {
        "type": "str",
        "required": true,
        "description": "Unique identifier of the regular gift that should be upgraded to a unique one."
      },
      "keep_original_details": {
        "type": "bool",
        "required": false,
        "description": "Pass True to keep the original gift text, sender and receiver in the upgraded gift."
      },
      "star_count": {
        "type": "int",
        "required": false,
        "description": "The amount of Telegram Stars that will be paid for the upgrade from the business account balance."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.payments_and_business.upgrade_gift.UpgradeGift.upgrade_gift"
  },
  "upload_sticker_file": {
    "description": "Use this method to upload a .png file with a sticker for later use in createNewStickerSet and addStickerToSet",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "User identifier of sticker set owner"
      },
      "sticker": {
        "type": "Union",
        "required": true,
        "description": "A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format.\nSee https://core.telegram.org/stickers for technical requirements. More information on Sending Files \u00bb"
      },
      "sticker_format": {
        "type": "str",
        "required": true,
        "description": "One of \"static\", \"animated\", \"video\"."
      }
    },
    "returns": "File",
    "path": "tgram.methods.stickers.upload_sticker_file.UploadStickerFile.upload_sticker_file"
  },
  "verify_chat": {
    "description": "Verifies a chat on behalf of the organization which is represented by the bot. Returns True on success.",
    "parameters": {
      "chat_id": {
        "type": "Union",
        "required": true,
        "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername)"
      },
      "custom_description": {
        "type": "str",
        "required": false,
        "description": "UCustom description for the verification; 0-70 characters.\nMust be empty if the organization isn't allowed to provide a custom verification description."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.verify_chat.VerifyChat.verify_chat"
  },
  "verify_user": {
    "description": "Verifies a user on behalf of the organization which is represented by the bot. Returns True on success.",
    "parameters": {
      "user_id": {
        "type": "int",
        "required": true,
        "description": "Unique identifier of the target user"
      },
      "custom_description": {
        "type": "str",
        "required": false,
        "description": "UCustom description for the verification; 0-70 characters.\nMust be empty if the organization isn't allowed to provide a custom verification description."
      }
    },
    "returns": "bool",
    "path": "tgram.methods.chats.verify_user.VerifyUser.verify_user"
  }
};
window.tgramTypes = {
  "Response": {
    "description": "dict() -> new empty dictionary",
    "properties": {
      "ok": {
        "type": "bool",
        "description": ""
      },
      "result": {
        "type": "Union",
        "description": ""
      },
      "error_code": {
        "type": "int",
        "description": ""
      },
      "description": {
        "type": "str",
        "description": ""
      },
      "parameters": {
        "type": "dict",
        "description": ""
      }
    }
  },
  "AcceptedGiftTypes": {
    "description": "This object describes the types of gifts that can be gifted to a user or a chat.",
    "properties": {
      "unlimited_gifts": {
        "type": "bool",
        "description": "True, if unlimited regular gifts are accepted"
      },
      "limited_gifts": {
        "type": "bool",
        "description": "True, if limited regular gifts are accepted"
      },
      "unique_gifts": {
        "type": "bool",
        "description": "True, if unique gifts or gifts that can be upgraded to unique for free are accepted"
      },
      "premium_subscription": {
        "type": "bool",
        "description": "True, if a Telegram Premium subscription is accepted"
      }
    }
  },
  "AffiliateInfo": {
    "description": "This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).",
    "properties": {
      "affiliate_user": {
        "type": "User",
        "description": "Optional. The bot or the user that received an affiliate commission if it was received by a bot or a user"
      },
      "affiliate_chat": {
        "type": "Chat",
        "description": "Optional. The chat that received an affiliate commission if it was received by a chat"
      },
      "commission_per_mille": {
        "type": "int",
        "description": "The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users"
      },
      "amount": {
        "type": "int",
        "description": "Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds"
      },
      "nanostar_amount": {
        "type": "int",
        "description": "Optional. The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds"
      }
    }
  },
  "Animation": {
    "description": "This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "width": {
        "type": "int",
        "description": "Video width as defined by sender"
      },
      "height": {
        "type": "int",
        "description": "Video height as defined by sender"
      },
      "duration": {
        "type": "int",
        "description": "Duration of the video in seconds as defined by sender"
      },
      "thumbnail": {
        "type": "PhotoSize",
        "description": "Optional. Animation thumbnail as defined by sender"
      },
      "file_name": {
        "type": "str",
        "description": "Optional. Original animation filename as defined by sender"
      },
      "mime_type": {
        "type": "str",
        "description": "Optional. MIME type of the file as defined by sender"
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have\ndifficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or\ndouble-precision float type are safe for storing this value."
      }
    }
  },
  "Audio": {
    "description": "This object represents an audio file to be treated as music by the Telegram clients.",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "duration": {
        "type": "int",
        "description": "Duration of the audio in seconds as defined by sender"
      },
      "performer": {
        "type": "str",
        "description": "Optional. Performer of the audio as defined by sender or by audio tags"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title of the audio as defined by sender or by audio tags"
      },
      "file_name": {
        "type": "str",
        "description": "Optional. Original filename as defined by sender"
      },
      "mime_type": {
        "type": "str",
        "description": "Optional. MIME type of the file as defined by sender"
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have\ndifficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or\ndouble-precision float type are safe for storing this value."
      },
      "thumbnail": {
        "type": "PhotoSize",
        "description": "Optional. Thumbnail of the album cover to which the music file belongs"
      }
    }
  },
  "BackgroundFill": {
    "description": "This object describes the way a background is filled based on the selected colors. Currently, it can be one of",
    "properties": {}
  },
  "BackgroundFillFreeformGradient": {
    "description": "The background is a freeform gradient that rotates after every message in the chat.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the background fill, always \u201cfreeform_gradient\u201d"
      },
      "colors": {
        "type": "List",
        "description": "A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format"
      }
    }
  },
  "BackgroundFillGradient": {
    "description": "The background is a gradient fill.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the background fill, always \u201cgradient\u201d"
      },
      "top_color": {
        "type": "int",
        "description": "Top color of the gradient in the RGB24 format"
      },
      "bottom_color": {
        "type": "int",
        "description": "Bottom color of the gradient in the RGB24 format"
      },
      "rotation_angle": {
        "type": "int",
        "description": "Clockwise rotation angle of the background fill in degrees; 0-359"
      }
    }
  },
  "BackgroundFillSolid": {
    "description": "The background is filled using the selected color.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the background fill, always \u201csolid\u201d"
      },
      "color": {
        "type": "int",
        "description": "The color of the background fill in the RGB24 format"
      }
    }
  },
  "BackgroundType": {
    "description": "This object describes the type of a background. Currently, it can be one of",
    "properties": {}
  },
  "BackgroundTypeChatTheme": {
    "description": "The background is taken directly from a built-in chat theme.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the background, always \u201cchat_theme\u201d"
      },
      "theme_name": {
        "type": "str",
        "description": "Intensity of the pattern when it is shown above the filled background; 0-100"
      }
    }
  },
  "BackgroundTypeFill": {
    "description": "The background is automatically filled based on the selected colors.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the background, always \u201cfill\u201d"
      },
      "fill": {
        "type": "BackgroundFill",
        "description": "The background fill"
      },
      "dark_theme_dimming": {
        "type": "int",
        "description": "Dimming of the background in dark themes, as a percentage; 0-100"
      }
    }
  },
  "BackgroundTypePattern": {
    "description": "The background is a wallpaper in the JPEG format.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the background, always \u201cpattern\u201d"
      },
      "document": {
        "type": "Document",
        "description": "Document with the pattern"
      },
      "fill": {
        "type": "BackgroundFill",
        "description": "The background fill that is combined with the pattern"
      },
      "intensity": {
        "type": "int",
        "description": "Intensity of the pattern when it is shown above the filled background; 0-100"
      },
      "is_inverted": {
        "type": "bool",
        "description": "Optional. True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only"
      },
      "is_moving": {
        "type": "bool",
        "description": "Optional. True, if the background moves slightly when the device is tilted"
      }
    }
  },
  "BackgroundTypeWallpaper": {
    "description": "The background is a wallpaper in the JPEG format.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the background, always \u201cwallpaper\u201d"
      },
      "document": {
        "type": "Document",
        "description": "Document with the wallpaper"
      },
      "dark_theme_dimming": {
        "type": "int",
        "description": "Dimming of the background in dark themes, as a percentage; 0-100"
      },
      "is_blurred": {
        "type": "bool",
        "description": "Optional. True, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12"
      },
      "is_moving": {
        "type": "bool",
        "description": "Optional. True, if the background moves slightly when the device is tilted"
      }
    }
  },
  "Birthdate": {
    "description": "This object represents a user's birthdate.",
    "properties": {
      "day": {
        "type": "int",
        "description": "Day of the user's birth; 1-31"
      },
      "month": {
        "type": "int",
        "description": "Month of the user's birth; 1-12"
      },
      "year": {
        "type": "int",
        "description": "Optional. Year of the user's birth"
      }
    }
  },
  "BotCommand": {
    "description": "This object represents a bot command.",
    "properties": {
      "command": {
        "type": "str",
        "description": "Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and\nunderscores."
      },
      "description": {
        "type": "str",
        "description": "Description of the command; 1-256 characters."
      }
    }
  },
  "BotCommandScope": {
    "description": "This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:",
    "properties": {}
  },
  "BotCommandScopeAllChatAdministrators": {
    "description": "Represents the scope of bot commands, covering all group and supergroup chat administrators.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Scope type, must be all_chat_administrators"
      }
    }
  },
  "BotCommandScopeAllGroupChats": {
    "description": "Represents the scope of bot commands, covering all group and supergroup chats.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Scope type, must be all_group_chats"
      }
    }
  },
  "BotCommandScopeAllPrivateChats": {
    "description": "Represents the scope of bot commands, covering all private chats.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Scope type, must be all_private_chats"
      }
    }
  },
  "BotCommandScopeChat": {
    "description": "Represents the scope of bot commands, covering a specific chat.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Scope type, must be chat"
      },
      "chat_id": {
        "type": "Union",
        "description": "Unique identifier for the target chat or username of the target supergroup (in the format\n@supergroupusername)"
      }
    }
  },
  "BotCommandScopeChatAdministrators": {
    "description": "Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Scope type, must be chat_administrators"
      },
      "chat_id": {
        "type": "Union",
        "description": "Unique identifier for the target chat or username of the target supergroup (in the format\n@supergroupusername)"
      }
    }
  },
  "BotCommandScopeChatMember": {
    "description": "Represents the scope of bot commands, covering a specific member of a group or supergroup chat.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Scope type, must be chat_member"
      },
      "chat_id": {
        "type": "Union",
        "description": "Unique identifier for the target chat or username of the target supergroup (in the format\n@supergroupusername)"
      },
      "user_id": {
        "type": "int",
        "description": "Unique identifier of the target user"
      }
    }
  },
  "BotCommandScopeDefault": {
    "description": "Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Scope type, must be default"
      }
    }
  },
  "BotDescription": {
    "description": "This object represents a bot description.",
    "properties": {
      "description": {
        "type": "str",
        "description": "Bot description"
      }
    }
  },
  "BotName": {
    "description": "This object represents a bot name.",
    "properties": {
      "name": {
        "type": "str",
        "description": "The bot name"
      }
    }
  },
  "BotShortDescription": {
    "description": "This object represents a bot short description.",
    "properties": {
      "short_description": {
        "type": "str",
        "description": "Bot short description"
      }
    }
  },
  "BusinessConnection": {
    "description": "This object describes the connection of the bot with a business account.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique identifier of the business connection"
      },
      "user": {
        "type": "User",
        "description": "Business account user that created the business connection"
      },
      "user_chat_id": {
        "type": "int",
        "description": "Identifier of a private chat with the user who created the business connection"
      },
      "date": {
        "type": "int",
        "description": "Date the connection was established in Unix time"
      },
      "rights": {
        "type": "BusinessBotRights",
        "description": "Optional. Rights of the business bot"
      },
      "is_enabled": {
        "type": "bool",
        "description": "True, if the connection is active"
      }
    }
  },
  "BusinessIntro": {
    "description": "This object represents a business intro.",
    "properties": {
      "title": {
        "type": "str",
        "description": "Optional. Title text of the business intro"
      },
      "message": {
        "type": "str",
        "description": "Optional. Message text of the business intro"
      },
      "sticker": {
        "type": "Sticker",
        "description": "Optional. Sticker of the business intro"
      }
    }
  },
  "BusinessLocation": {
    "description": "This object represents a business location.",
    "properties": {
      "address": {
        "type": "str",
        "description": "Address of the business"
      },
      "location": {
        "type": "Location",
        "description": "Optional. Location of the business"
      }
    }
  },
  "BusinessMessagesDeleted": {
    "description": "This object is received when messages are deleted from a connected business account.",
    "properties": {
      "business_connection_id": {
        "type": "str",
        "description": "Unique identifier of the business connection"
      },
      "chat": {
        "type": "Chat",
        "description": "Information about a chat in the business account. The bot may not have access to the chat or the corresponding user."
      },
      "message_ids": {
        "type": "List",
        "description": "A JSON-serialized list of identifiers of deleted messages in the chat of the business account"
      }
    }
  },
  "BusinessOpeningHours": {
    "description": "This object represents business opening hours.",
    "properties": {
      "time_zone_name": {
        "type": "str",
        "description": "Unique name of the time zone for which the opening hours are defined"
      },
      "opening_hours": {
        "type": "List",
        "description": "List of time intervals describing business opening hours"
      }
    }
  },
  "BusinessOpeningHoursInterval": {
    "description": "This object represents a business opening hours interval.",
    "properties": {
      "opening_minute": {
        "type": "int",
        "description": "The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 24 60"
      },
      "closing_minute": {
        "type": "int",
        "description": "The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 24 60"
      }
    }
  },
  "CallbackGame": {
    "description": "",
    "properties": {
      "user_id": {
        "type": "int",
        "description": ""
      },
      "score": {
        "type": "int",
        "description": ""
      },
      "force": {
        "type": "bool",
        "description": ""
      },
      "disable_edit_message": {
        "type": "bool",
        "description": ""
      },
      "chat_id": {
        "type": "int",
        "description": ""
      },
      "message_id": {
        "type": "int",
        "description": ""
      },
      "inline_message_id": {
        "type": "str",
        "description": ""
      }
    }
  },
  "CallbackQuery": {
    "description": "This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique identifier for this query"
      },
      "from_user": {
        "type": "User",
        "description": "Sender"
      },
      "chat_instance": {
        "type": "str",
        "description": "Global identifier, uniquely corresponding to the chat to which the message with the callback\nbutton was sent. Useful for high scores in games."
      },
      "message": {
        "type": "Message",
        "description": "Optional. Message sent by the bot with the callback button that originated the query"
      },
      "inline_message_id": {
        "type": "str",
        "description": "Optional. Identifier of the message sent via the bot in inline mode, that originated the\nquery."
      },
      "data": {
        "type": "str",
        "description": "Optional. Data associated with the callback button. Be aware that the message originated the query can\ncontain no callback buttons with this data."
      },
      "game_short_name": {
        "type": "str",
        "description": "Optional. Short name of a Game to be returned, serves as the unique identifier for the game"
      }
    }
  },
  "Chat": {
    "description": "In BotAPI 7.3 Chat was reduced and full info moved to ChatFullInfo:",
    "properties": {
      "id": {
        "type": "int",
        "description": ""
      },
      "type": {
        "type": "ChatType",
        "description": ""
      },
      "title": {
        "type": "str",
        "description": ""
      },
      "username": {
        "type": "str",
        "description": ""
      },
      "first_name": {
        "type": "str",
        "description": ""
      },
      "last_name": {
        "type": "str",
        "description": ""
      },
      "is_forum": {
        "type": "bool",
        "description": ""
      }
    }
  },
  "ChatAdministratorRights": {
    "description": "Represents the rights of an administrator in a chat.",
    "properties": {
      "is_anonymous": {
        "type": "bool",
        "description": "True, if the user's presence in the chat is hidden"
      },
      "can_manage_chat": {
        "type": "bool",
        "description": "True, if the administrator can access the chat event log, chat statistics, message\nstatistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode.\nImplied by any other administrator privilege"
      },
      "can_delete_messages": {
        "type": "bool",
        "description": "True, if the administrator can delete messages of other users"
      },
      "can_manage_video_chats": {
        "type": "bool",
        "description": "True, if the administrator can manage video chats"
      },
      "can_restrict_members": {
        "type": "bool",
        "description": "True, if the administrator can restrict, ban or unban chat members"
      },
      "can_promote_members": {
        "type": "bool",
        "description": "True, if the administrator can add new administrators with a subset of their own\nprivileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that\nwere appointed by the user)"
      },
      "can_change_info": {
        "type": "bool",
        "description": "True, if the user is allowed to change the chat title, photo and other settings"
      },
      "can_invite_users": {
        "type": "bool",
        "description": "True, if the user is allowed to invite new users to the chat"
      },
      "can_post_stories": {
        "type": "bool",
        "description": "Optional. True, if the administrator can post channel stories"
      },
      "can_edit_stories": {
        "type": "bool",
        "description": "Optional. True, if the administrator can edit stories"
      },
      "can_delete_stories": {
        "type": "bool",
        "description": "Optional. True, if the administrator can delete stories of other users"
      },
      "can_post_messages": {
        "type": "bool",
        "description": "Optional. True, if the administrator can post in the channel; channels only"
      },
      "can_edit_messages": {
        "type": "bool",
        "description": "Optional. True, if the administrator can edit messages of other users and can pin\nmessages; channels only"
      },
      "can_pin_messages": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to pin messages; groups and supergroups only"
      },
      "can_manage_topics": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; supergroups only"
      }
    }
  },
  "ChatBackground": {
    "description": "This object represents a chat background.",
    "properties": {
      "type": {
        "type": "BackgroundType",
        "description": "Type of the background"
      }
    }
  },
  "ChatBoost": {
    "description": "This object contains information about a chat boost.",
    "properties": {
      "boost_id": {
        "type": "str",
        "description": "Unique identifier of the boost"
      },
      "add_date": {
        "type": "int",
        "description": "Point in time (Unix timestamp) when the chat was boosted"
      },
      "expiration_date": {
        "type": "int",
        "description": "Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged"
      },
      "source": {
        "type": "ChatBoostSource",
        "description": "Optional. Source of the added boost (made Optional for now due to API error)"
      }
    }
  },
  "ChatBoostAdded": {
    "description": "This object represents a service message about a user boosting a chat.",
    "properties": {
      "boost_count": {
        "type": "int",
        "description": "Number of boosts added by the user"
      }
    }
  },
  "ChatBoostRemoved": {
    "description": "This object represents a boost removed from a chat.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "Chat which was boosted"
      },
      "boost_id": {
        "type": "str",
        "description": "Unique identifier of the boost"
      },
      "remove_date": {
        "type": "int",
        "description": "Point in time (Unix timestamp) when the boost was removed"
      },
      "source": {
        "type": "ChatBoostSource",
        "description": "Source of the removed boost"
      }
    }
  },
  "ChatBoostSource": {
    "description": "This object describes the source of a chat boost. It can be one of",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "user": {
        "type": "User",
        "description": ""
      }
    }
  },
  "ChatBoostSourceGiftCode": {
    "description": "The boost was obtained by the creation of Telegram Premium gift codes to boost a chat.",
    "properties": {
      "source": {
        "type": "str",
        "description": "Source of the boost, always \u201cgift_code\u201d"
      },
      "user": {
        "type": "User",
        "description": "User for which the gift code was created"
      }
    }
  },
  "ChatBoostSourceGiveaway": {
    "description": "The boost was obtained by the creation of a Telegram Premium giveaway.",
    "properties": {
      "source": {
        "type": "str",
        "description": "Source of the boost, always \u201cgiveaway\u201d"
      },
      "giveaway_message_id": {
        "type": "int",
        "description": "Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet."
      },
      "user": {
        "type": "User",
        "description": "User that won the prize in the giveaway if any"
      },
      "prize_star_count": {
        "type": "int",
        "description": "Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only"
      },
      "is_unclaimed": {
        "type": "bool",
        "description": "True, if the giveaway was completed, but there was no user to win the prize"
      }
    }
  },
  "ChatBoostSourcePremium": {
    "description": "The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.",
    "properties": {
      "source": {
        "type": "str",
        "description": "Source of the boost, always \u201cpremium\u201d"
      },
      "user": {
        "type": "User",
        "description": "User that boosted the chat"
      }
    }
  },
  "ChatBoostUpdated": {
    "description": "This object represents a boost added to a chat or changed.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "Chat which was boosted"
      },
      "boost": {
        "type": "ChatBoost",
        "description": "Infomation about the chat boost"
      }
    }
  },
  "ChatFullInfo": {
    "description": "This object represents a chat.",
    "properties": {
      "id": {
        "type": "int",
        "description": "Unique identifier for this chat. This number may have more than 32 significant bits and some programming\nlanguages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed\n64-bit integer or double-precision float type are safe for storing this identifier."
      },
      "type": {
        "type": "ChatType",
        "description": "Type of chat, can be either \u201cprivate\u201d, \u201cgroup\u201d, \u201csupergroup\u201d or \u201cchannel\u201d"
      },
      "accent_color_id": {
        "type": "int",
        "description": "Optional. Optional. Identifier of the accent color for the chat name and backgrounds of the chat photo,\nreply header, and link preview. See accent colors for more details. Returned only in getChat. Always returned in getChat."
      },
      "max_reaction_count": {
        "type": "int",
        "description": "Optional. The maximum number of reactions that can be set on a message in the chat"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title, for supergroups, channels and group chats"
      },
      "username": {
        "type": "str",
        "description": "Optional. Username, for private chats, supergroups and channels if available"
      },
      "first_name": {
        "type": "str",
        "description": "Optional. First name of the other party in a private chat"
      },
      "last_name": {
        "type": "str",
        "description": "Optional. Last name of the other party in a private chat"
      },
      "is_forum": {
        "type": "bool",
        "description": "Optional. True, if the supergroup chat is a forum (has topics enabled)"
      },
      "photo": {
        "type": "ChatPhoto",
        "description": "Optional. Chat photo. Returned only in getChat."
      },
      "active_usernames": {
        "type": "List",
        "description": "Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels. Returned only in getChat."
      },
      "birthdate": {
        "type": "Birthdate",
        "description": "Optional. Birthdate of the other party in a private chat. Returned only in getChat."
      },
      "business_intro": {
        "type": "BusinessIntro",
        "description": "Optional. Business intro for the chat. Returned only in getChat."
      },
      "business_location": {
        "type": "BusinessLocation",
        "description": "Optional. Business location for the chat. Returned only in getChat."
      },
      "business_opening_hours": {
        "type": "BusinessOpeningHours",
        "description": "Optional. Business opening hours for the chat. Returned only in getChat."
      },
      "personal_chat": {
        "type": "Chat",
        "description": "Optional. For private chats, the personal channel of the user. Returned only in getChat."
      },
      "available_reactions": {
        "type": "List",
        "description": "Optional. List of available chat reactions; for private chats, supergroups and channels. Returned only in getChat."
      },
      "background_custom_emoji_id": {
        "type": "str",
        "description": "Optional. Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background. Returned only in getChat."
      },
      "profile_accent_color_id": {
        "type": "int",
        "description": "Optional. Identifier of the accent color for the chat's profile background. See profile accent colors for more details. Returned only in getChat."
      },
      "profile_background_custom_emoji_id": {
        "type": "str",
        "description": "Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background. Returned only in getChat."
      },
      "emoji_status_custom_emoji_id": {
        "type": "str",
        "description": "Optional. Custom emoji identifier of emoji status of the other party in a private chat. Returned only in getChat."
      },
      "emoji_status_expiration_date": {
        "type": "int",
        "description": "Optional. Expiration date of the emoji status of the other party in a private chat, if any. Returned only in getChat."
      },
      "bio": {
        "type": "str",
        "description": "Optional. Bio of the other party in a private chat. Returned only in getChat."
      },
      "has_private_forwards": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat."
      },
      "has_restricted_voice_and_video_messages": {
        "type": "bool",
        "description": "Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat."
      },
      "join_to_send_messages": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if users need to join the supergroup before they can send messages. Returned only in getChat."
      },
      "join_by_request": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat."
      },
      "description": {
        "type": "str",
        "description": "Optional. Description, for groups, supergroups and channel chats. Returned only in getChat."
      },
      "invite_link": {
        "type": "str",
        "description": "Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat."
      },
      "pinned_message": {
        "type": "Message",
        "description": "Optional. The most recent pinned message (by sending date). Returned only in getChat."
      },
      "permissions": {
        "type": "ChatPermissions",
        "description": "Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat."
      },
      "accepted_gift_types": {
        "type": "AcceptedGiftTypes",
        "description": ""
      },
      "can_send_paid_media": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats."
      },
      "slow_mode_delay": {
        "type": "int",
        "description": "Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat."
      },
      "unrestrict_boost_count": {
        "type": "int",
        "description": "Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions. Returned only in getChat."
      },
      "message_auto_delete_time": {
        "type": "int",
        "description": "Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat."
      },
      "has_aggressive_anti_spam_enabled": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if the chat has enabled aggressive anti-spam protection. Returned only in getChat."
      },
      "has_hidden_members": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if the chat has enabled hidden members. Returned only in getChat."
      },
      "has_protected_content": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if messages from the chat can't be forwarded to other chats. Returned only in getChat."
      },
      "has_visible_history": {
        "type": "bool",
        "description": "Optional. True, if new chat members will have access to old messages; available only to chat administrators. Returned only in getChat."
      },
      "sticker_set_name": {
        "type": "str",
        "description": "Optional. For supergroups, name of group sticker set. Returned only in getChat."
      },
      "can_set_sticker_set": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if the bot can change the group sticker set. Returned only in getChat."
      },
      "custom_emoji_sticker_set_name": {
        "type": "str",
        "description": ":obj:`str`"
      },
      "linked_chat_id": {
        "type": "int",
        "description": "Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for\na channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some\nprogramming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a\nsigned 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat."
      },
      "location": {
        "type": "ChatLocation",
        "description": "Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat."
      }
    }
  },
  "ChatInviteLink": {
    "description": "Represents an invite link for a chat.",
    "properties": {
      "invite_link": {
        "type": "str",
        "description": "The invite link. If the link was created by another chat administrator, then the second part of\nthe link will be replaced with \u201c\u2026\u201d."
      },
      "creator": {
        "type": "User",
        "description": "Creator of the link"
      },
      "creates_join_request": {
        "type": "bool",
        "description": "True, if users joining the chat via the link need to be approved by chat administrators"
      },
      "is_primary": {
        "type": "bool",
        "description": "True, if the link is primary"
      },
      "is_revoked": {
        "type": "bool",
        "description": "True, if the link is revoked"
      },
      "name": {
        "type": "str",
        "description": "Optional. Invite link name"
      },
      "expire_date": {
        "type": "int",
        "description": "Optional. Point in time (Unix timestamp) when the link will expire or has been expired"
      },
      "member_limit": {
        "type": "int",
        "description": "Optional. The maximum number of users that can be members of the chat simultaneously after\njoining the chat via this invite link; 1-99999"
      },
      "pending_join_request_count": {
        "type": "int",
        "description": "Optional. Number of pending join requests created using this link"
      }
    }
  },
  "ChatJoinRequest": {
    "description": "Represents a join request sent to a chat.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "Chat to which the request was sent"
      },
      "from_user": {
        "type": "User",
        "description": "User that sent the join request"
      },
      "user_chat_id": {
        "type": "int",
        "description": "Optional. Identifier of a private chat with the user who sent the join request.\nThis number may have more than 32 significant bits and some programming languages may have difficulty/silent\ndefects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision\nfloat type are safe for storing this identifier. The bot can use this identifier for 24 hours to send messages\nuntil the join request is processed, assuming no other administrator contacted the user."
      },
      "date": {
        "type": "int",
        "description": "Date the request was sent in Unix time"
      },
      "bio": {
        "type": "str",
        "description": "Optional. Bio of the user."
      },
      "invite_link": {
        "type": "ChatInviteLink",
        "description": "Optional. Chat invite link that was used by the user to send the join request"
      }
    }
  },
  "ChatLocation": {
    "description": "Represents a location to which a chat is connected.",
    "properties": {
      "location": {
        "type": "Location",
        "description": "The location to which the supergroup is connected. Can't be a live location."
      },
      "address": {
        "type": "str",
        "description": "Location address; 1-64 characters, as defined by the chat owner"
      }
    }
  },
  "ChatMember": {
    "description": "This object contains information about one member of a chat.",
    "properties": {}
  },
  "ChatMemberAdministrator": {
    "description": "Represents a chat member that has some additional privileges.",
    "properties": {
      "status": {
        "type": "ChatMemberStatus",
        "description": "The member's status in the chat, always \u201cadministrator\u201d"
      },
      "user": {
        "type": "User",
        "description": "Information about the user"
      },
      "can_be_edited": {
        "type": "bool",
        "description": "True, if the bot is allowed to edit administrator privileges of that user"
      },
      "is_anonymous": {
        "type": "bool",
        "description": "True, if the user's presence in the chat is hidden"
      },
      "can_manage_chat": {
        "type": "bool",
        "description": "True, if the administrator can access the chat event log, chat statistics, message\nstatistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode.\nImplied by any other administrator privilege"
      },
      "can_delete_messages": {
        "type": "bool",
        "description": "True, if the administrator can delete messages of other users"
      },
      "can_manage_video_chats": {
        "type": "bool",
        "description": "True, if the administrator can manage video chats"
      },
      "can_restrict_members": {
        "type": "bool",
        "description": "True, if the administrator can restrict, ban or unban chat members"
      },
      "can_promote_members": {
        "type": "bool",
        "description": "True, if the administrator can add new administrators with a subset of their own\nprivileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that\nwere appointed by the user)"
      },
      "can_change_info": {
        "type": "bool",
        "description": "True, if the user is allowed to change the chat title, photo and other settings"
      },
      "can_invite_users": {
        "type": "bool",
        "description": "True, if the user is allowed to invite new users to the chat"
      },
      "can_post_stories": {
        "type": "bool",
        "description": "Optional. True, if the administrator can post channel stories"
      },
      "can_edit_stories": {
        "type": "bool",
        "description": "Optional. True, if the administrator can edit stories"
      },
      "can_delete_stories": {
        "type": "bool",
        "description": "Optional. True, if the administrator can delete stories of other users"
      },
      "can_post_messages": {
        "type": "bool",
        "description": "Optional. True, if the administrator can post in the channel; channels only"
      },
      "can_edit_messages": {
        "type": "bool",
        "description": "Optional. True, if the administrator can edit messages of other users and can pin\nmessages; channels only"
      },
      "can_pin_messages": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to pin messages; groups and supergroups only"
      },
      "can_manage_topics": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to create, rename, close, and reopen forum topics;\nsupergroups only"
      },
      "custom_title": {
        "type": "str",
        "description": "Optional. Custom title for this user"
      }
    }
  },
  "ChatMemberBanned": {
    "description": "Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.",
    "properties": {
      "status": {
        "type": "ChatMemberStatus",
        "description": "The member's status in the chat, always \u201ckicked\u201d"
      },
      "user": {
        "type": "User",
        "description": "Information about the user"
      },
      "until_date": {
        "type": "int",
        "description": "Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned\nforever"
      }
    }
  },
  "ChatMemberLeft": {
    "description": "Represents a chat member that isn't currently a member of the chat, but may join it themselves.",
    "properties": {
      "status": {
        "type": "ChatMemberStatus",
        "description": "The member's status in the chat, always \u201cleft\u201d"
      },
      "user": {
        "type": "User",
        "description": "Information about the user"
      }
    }
  },
  "ChatMemberMember": {
    "description": "Represents a chat member that has no additional privileges or restrictions.",
    "properties": {
      "status": {
        "type": "ChatMemberStatus",
        "description": "The member's status in the chat, always \u201cmember\u201d"
      },
      "user": {
        "type": "User",
        "description": "Information about the user"
      },
      "until_date": {
        "type": "int",
        "description": "Optional. Date when the user's subscription will expire; Unix time"
      }
    }
  },
  "ChatMemberOwner": {
    "description": "Represents a chat member that owns the chat and has all administrator privileges.",
    "properties": {
      "status": {
        "type": "ChatMemberStatus",
        "description": "The member's status in the chat, always \u201ccreator\u201d"
      },
      "user": {
        "type": "User",
        "description": "Information about the user"
      },
      "is_anonymous": {
        "type": "bool",
        "description": "True, if the user's presence in the chat is hidden"
      },
      "custom_title": {
        "type": "str",
        "description": "Optional. Custom title for this user"
      }
    }
  },
  "ChatMemberRestricted": {
    "description": "Represents a chat member that is under certain restrictions in the chat. Supergroups only.",
    "properties": {
      "status": {
        "type": "ChatMemberStatus",
        "description": "The member's status in the chat, always \u201crestricted\u201d"
      },
      "user": {
        "type": "User",
        "description": "Information about the user"
      },
      "is_member": {
        "type": "bool",
        "description": "True, if the user is a member of the chat at the moment of the request"
      },
      "can_send_messages": {
        "type": "bool",
        "description": "True, if the user is allowed to send text messages, contacts, locations and venues"
      },
      "can_send_audios": {
        "type": "bool",
        "description": "True, if the user is allowed to send audios"
      },
      "can_send_documents": {
        "type": "bool",
        "description": "True, if the user is allowed to send documents"
      },
      "can_send_photos": {
        "type": "bool",
        "description": "True, if the user is allowed to send photos"
      },
      "can_send_videos": {
        "type": "bool",
        "description": "True, if the user is allowed to send videos"
      },
      "can_send_video_notes": {
        "type": "bool",
        "description": "True, if the user is allowed to send video notes"
      },
      "can_send_voice_notes": {
        "type": "bool",
        "description": "True, if the user is allowed to send voice notes"
      },
      "can_send_polls": {
        "type": "bool",
        "description": "True, if the user is allowed to send polls"
      },
      "can_send_other_messages": {
        "type": "bool",
        "description": "True, if the user is allowed to send animations, games, stickers and use inline\nbots"
      },
      "can_add_web_page_previews": {
        "type": "bool",
        "description": "True, if the user is allowed to add web page previews to their messages"
      },
      "can_change_info": {
        "type": "bool",
        "description": "True, if the user is allowed to change the chat title, photo and other settings"
      },
      "can_invite_users": {
        "type": "bool",
        "description": "True, if the user is allowed to invite new users to the chat"
      },
      "can_pin_messages": {
        "type": "bool",
        "description": "True, if the user is allowed to pin messages"
      },
      "can_manage_topics": {
        "type": "bool",
        "description": "True, if the user is allowed to create forum topics"
      },
      "until_date": {
        "type": "int",
        "description": "Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted\nforever"
      }
    }
  },
  "ChatMemberUpdated": {
    "description": "This object represents changes in the status of a chat member.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "Chat the user belongs to"
      },
      "from_user": {
        "type": "User",
        "description": "Performer of the action, which resulted in the change"
      },
      "date": {
        "type": "int",
        "description": "Date the change was done in Unix time"
      },
      "old_chat_member": {
        "type": "Union",
        "description": "Previous information about the chat member"
      },
      "new_chat_member": {
        "type": "Union",
        "description": "New information about the chat member"
      },
      "invite_link": {
        "type": "ChatInviteLink",
        "description": "Optional. Chat invite link, which was used by the user to join the chat; for joining by invite\nlink events only."
      },
      "via_join_request": {
        "type": "bool",
        "description": "Optional. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator"
      },
      "via_chat_folder_invite_link": {
        "type": "bool",
        "description": "Optional. True, if the user joined the chat via a chat folder invite link"
      }
    }
  },
  "ChatPermissions": {
    "description": "Describes actions that a non-administrator user is allowed to take in a chat.",
    "properties": {
      "can_send_messages": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send text messages, contacts, locations and\nvenues"
      },
      "can_send_audios": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send audios"
      },
      "can_send_documents": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send documents"
      },
      "can_send_photos": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send photos"
      },
      "can_send_videos": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send videos"
      },
      "can_send_video_notes": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send video notes"
      },
      "can_send_voice_notes": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send voice notes"
      },
      "can_send_polls": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send polls, implies can_send_messages"
      },
      "can_send_other_messages": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to send animations, games, stickers and use\ninline bots"
      },
      "can_add_web_page_previews": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to add web page previews to their\nmessages"
      },
      "can_change_info": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to change the chat title, photo and other settings.\nIgnored in public supergroups"
      },
      "can_invite_users": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to invite new users to the chat"
      },
      "can_pin_messages": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to pin messages. Ignored in public supergroups"
      },
      "can_manage_topics": {
        "type": "bool",
        "description": "Optional. True, if the user is allowed to create forum topics. If omitted defaults to the\nvalue of can_pin_messages"
      }
    }
  },
  "ChatPhoto": {
    "description": "This object represents a chat photo.",
    "properties": {
      "small_file_id": {
        "type": "str",
        "description": "File identifier of small (160x160) chat photo. This file_id can be used only for photo\ndownload and only for as long as the photo is not changed."
      },
      "small_file_unique_id": {
        "type": "str",
        "description": "Unique file identifier of small (160x160) chat photo, which is supposed to be the same\nover time and for different bots. Can't be used to download or reuse the file."
      },
      "big_file_id": {
        "type": "str",
        "description": "File identifier of big (640x640) chat photo. This file_id can be used only for photo download and\nonly for as long as the photo is not changed."
      },
      "big_file_unique_id": {
        "type": "str",
        "description": "Unique file identifier of big (640x640) chat photo, which is supposed to be the same over\ntime and for different bots. Can't be used to download or reuse the file."
      }
    }
  },
  "ChatShared": {
    "description": "This object contains information about the chat whose identifier was shared with the bot using a",
    "properties": {
      "request_id": {
        "type": "int",
        "description": "identifier of the request"
      },
      "chat_id": {
        "type": "int",
        "description": "Identifier of the shared chat. This number may have more than 32 significant bits and some programming\nlanguages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit\ninteger or double-precision float type are safe for storing this identifier. The bot may not have access to the chat\nand could be unable to use this identifier, unless the chat is already known to the bot by some other means."
      },
      "title": {
        "type": "str",
        "description": "Optional. Title of the shared chat"
      },
      "username": {
        "type": "str",
        "description": "Optional. Username of the shared chat"
      },
      "photo": {
        "type": "List",
        "description": "Optional. Array of Photosize"
      }
    }
  },
  "Checklist": {
    "description": "Describes a checklist.",
    "properties": {
      "title": {
        "type": "String",
        "description": "Title of the checklist"
      },
      "title_entities": {
        "type": "List",
        "description": "Optional. Special entities that appear in the checklist title"
      },
      "tasks": {
        "type": "List",
        "description": "List of tasks in the checklist"
      },
      "others_can_add_tasks": {
        "type": "bool",
        "description": "Optional. True, if users other than the creator of the list can add tasks to the list"
      },
      "others_can_mark_tasks_as_done": {
        "type": "bool",
        "description": "Optional. True, if users other than the creator of the list can mark tasks as done or not done"
      }
    }
  },
  "ChecklistTask": {
    "description": "Describes a task in a checklist.",
    "properties": {
      "id": {
        "type": "int",
        "description": "Unique identifier of the task"
      },
      "text": {
        "type": "str",
        "description": "Text of the task"
      },
      "text_entities": {
        "type": "List",
        "description": "Optional. Special entities that appear in the task text"
      },
      "completed_by_user": {
        "type": "User",
        "description": "Optional. User that completed the task; omitted if the task wasn't completed"
      },
      "completion_date": {
        "type": "int",
        "description": "Optional. Point in time (Unix timestamp) when the task was completed; 0 if the task wasn't completed"
      }
    }
  },
  "ChecklistTasksAdded": {
    "description": "Describes a service message about tasks added to a checklist.",
    "properties": {
      "checklist_message": {
        "type": "Message",
        "description": "Optional. Message containing the checklist to which the tasks were added.\nNote that the Message object in this field will not contain the reply_to_message field even if it itself is a reply."
      },
      "tasks": {
        "type": "List",
        "description": "List of tasks added to the checklist"
      }
    }
  },
  "ChecklistTasksDone": {
    "description": "Describes a service message about checklist tasks marked as done or not done.",
    "properties": {
      "checklist_message": {
        "type": "Message",
        "description": "Optional. Message containing the checklist whose tasks were marked as done or not done. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply."
      },
      "marked_as_done_task_ids": {
        "type": "List",
        "description": "Optional. Identifiers of the tasks that were marked as done"
      },
      "marked_as_not_done_task_ids": {
        "type": "List",
        "description": "Optional. Identifiers of the tasks that were marked as not done"
      }
    }
  },
  "ChosenInlineResult": {
    "description": "Represents a result of an inline query that was chosen by the user and sent to their chat partner.",
    "properties": {
      "result_id": {
        "type": "str",
        "description": "The unique identifier for the result that was chosen"
      },
      "from_user": {
        "type": "User",
        "description": ""
      },
      "query": {
        "type": "str",
        "description": "The query that was used to obtain the result"
      },
      "location": {
        "type": "Location",
        "description": "Optional. Sender location, only for bots that require user location"
      },
      "inline_message_id": {
        "type": "str",
        "description": "Optional. Identifier of the sent inline message. Available only if there is an inline\nkeyboard attached to the message. Will be also received in callback queries and can be used to edit the message."
      }
    }
  },
  "Contact": {
    "description": "This object represents a phone contact.",
    "properties": {
      "phone_number": {
        "type": "str",
        "description": "Contact's phone number"
      },
      "first_name": {
        "type": "str",
        "description": "Contact's first name"
      },
      "last_name": {
        "type": "str",
        "description": "Optional. Contact's last name"
      },
      "user_id": {
        "type": "int",
        "description": "Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits\nand some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52\nsignificant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier."
      },
      "vcard": {
        "type": "str",
        "description": "Optional. Additional data about the contact in the form of a vCard"
      }
    }
  },
  "CopyTextButton": {
    "description": "This object represents an inline keyboard button that copies specified text to the clipboard.",
    "properties": {
      "text": {
        "type": "str",
        "description": "The text to be copied to the clipboard; 1-256 characters"
      }
    }
  },
  "Dice": {
    "description": "This object represents an animated emoji that displays a random value.",
    "properties": {
      "emoji": {
        "type": "str",
        "description": "Emoji on which the dice throw animation is based"
      },
      "value": {
        "type": "int",
        "description": "Value of the dice, 1-6 for \u201c\ud83c\udfb2\u201d, \u201c\ud83c\udfaf\u201d and \u201c\ud83c\udfb3\u201d base emoji, 1-5 for \u201c\ud83c\udfc0\u201d and \u201c\u26bd\u201d base emoji, 1-64 for \u201c\ud83c\udfb0\u201d base emoji"
      }
    }
  },
  "DirectMessagePriceChanged": {
    "description": "Describes a service message about a change in the price of direct messages sent to a channel chat.",
    "properties": {
      "are_direct_messages_enabled": {
        "type": "bool",
        "description": "True, if direct messages are enabled for the channel chat; false otherwise"
      },
      "direct_message_star_count": {
        "type": "Optional",
        "description": "Optional. The new number of Telegram Stars that must be paid by users for each direct message sent to the channel. Does not apply to users who have been exempted by administrators. Defaults to 0."
      }
    }
  },
  "Document": {
    "description": "This object represents a general file (as opposed to photos, voice messages and audio files).",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "thumbnail": {
        "type": "PhotoSize",
        "description": "Optional. Document thumbnail as defined by sender"
      },
      "file_name": {
        "type": "str",
        "description": "Optional. Original filename as defined by sender"
      },
      "mime_type": {
        "type": "str",
        "description": "Optional. MIME type of the file as defined by sender"
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have\ndifficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or\ndouble-precision float type are safe for storing this value."
      }
    }
  },
  "EncryptedCredentials": {
    "description": "",
    "properties": {
      "data": {
        "type": "str",
        "description": ""
      },
      "hash": {
        "type": "str",
        "description": ""
      },
      "secret": {
        "type": "str",
        "description": ""
      }
    }
  },
  "EncryptedPassportElement": {
    "description": "",
    "properties": {
      "type": {
        "type": "str",
        "description": ""
      },
      "hash": {
        "type": "str",
        "description": ""
      },
      "data": {
        "type": "str",
        "description": ""
      },
      "phone_number": {
        "type": "str",
        "description": ""
      },
      "email": {
        "type": "str",
        "description": ""
      },
      "files": {
        "type": "List",
        "description": ""
      },
      "front_side": {
        "type": "PassportFile",
        "description": ""
      },
      "reverse_side": {
        "type": "PassportFile",
        "description": ""
      },
      "selfie": {
        "type": "PassportFile",
        "description": ""
      },
      "translation": {
        "type": "List",
        "description": ""
      }
    }
  },
  "ExternalReplyInfo": {
    "description": "This object contains information about a message that is being replied to,",
    "properties": {
      "origin": {
        "type": "MessageOrigin",
        "description": "Origin of the message replied to by the given message"
      },
      "chat": {
        "type": "Chat",
        "description": "Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel."
      },
      "message_id": {
        "type": "int",
        "description": "Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel."
      },
      "link_preview_options": {
        "type": "LinkPreviewOptions",
        "description": "Optional. Options used for link preview generation for the original message, if it is a text message"
      },
      "animation": {
        "type": "Animation",
        "description": "Optional. Message is an animation, information about the animation"
      },
      "audio": {
        "type": "Audio",
        "description": "Optional. Message is an audio file, information about the file"
      },
      "document": {
        "type": "Document",
        "description": "Optional. Message is a general file, information about the file"
      },
      "paid_media": {
        "type": "PaidMediaInfo",
        "description": ""
      },
      "photo": {
        "type": "List",
        "description": "Optional. Message is a photo, available sizes of the photo"
      },
      "sticker": {
        "type": "Sticker",
        "description": "Optional. Message is a sticker, information about the sticker"
      },
      "story": {
        "type": "Story",
        "description": "Optional. Message is a forwarded story"
      },
      "video": {
        "type": "Video",
        "description": "Optional. Message is a video, information about the video"
      },
      "video_note": {
        "type": "VideoNote",
        "description": "Optional. Message is a video note, information about the video message"
      },
      "voice": {
        "type": "Voice",
        "description": "Optional. Message is a voice message, information about the file"
      },
      "has_media_spoiler": {
        "type": "bool",
        "description": "Optional. True, if the message media is covered by a spoiler animation"
      },
      "checklist": {
        "type": "Checklist",
        "description": "Optional. Message is a checklist"
      },
      "contact": {
        "type": "Contact",
        "description": "Optional. Message is a shared contact, information about the contact"
      },
      "dice": {
        "type": "Dice",
        "description": "Optional. Message is a dice with random value"
      },
      "game": {
        "type": "Game",
        "description": "Optional. Message is a game, information about the game. More about games \u00bb"
      },
      "giveaway": {
        "type": "Giveaway",
        "description": "Optional. Message is a scheduled giveaway, information about the giveaway"
      },
      "giveaway_winners": {
        "type": "GiveawayWinners",
        "description": "Optional. A giveaway with public winners was completed"
      },
      "invoice": {
        "type": "Invoice",
        "description": "Optional. Message is an invoice for a payment, information about the invoice. More about payments \u00bb"
      },
      "location": {
        "type": "Location",
        "description": "Optional. Message is a shared location, information about the location"
      },
      "poll": {
        "type": "Poll",
        "description": "Optional. Message is a native poll, information about the poll"
      },
      "venue": {
        "type": "Venue",
        "description": "Optional. Message is a venue, information about the venue"
      }
    }
  },
  "File": {
    "description": "This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have\ndifficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or\ndouble-precision float type are safe for storing this value."
      },
      "file_path": {
        "type": "str",
        "description": "Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the\nfile."
      }
    }
  },
  "ForceReply": {
    "description": "Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.",
    "properties": {
      "force_reply": {
        "type": "bool",
        "description": "Shows reply interface to the user, as if they manually selected the bot's message and tapped\n'Reply'"
      },
      "input_field_placeholder": {
        "type": "str",
        "description": "Optional. The placeholder to be shown in the input field when the reply is active;\n1-64 characters"
      },
      "selective": {
        "type": "bool",
        "description": "Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users\nthat are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same\nchat and forum topic, sender of the original message."
      }
    }
  },
  "ForumTopic": {
    "description": "This object represents a forum topic.",
    "properties": {
      "message_thread_id": {
        "type": "int",
        "description": "Unique identifier of the forum topic"
      },
      "name": {
        "type": "str",
        "description": "Name of the topic"
      },
      "icon_color": {
        "type": "int",
        "description": "Color of the topic icon in RGB format"
      },
      "icon_custom_emoji_id": {
        "type": "str",
        "description": "Optional. Unique identifier of the custom emoji shown as the topic icon"
      }
    }
  },
  "ForumTopicClosed": {
    "description": "This object represents a service message about a forum topic closed in the chat. Currently holds no information.",
    "properties": {
      "name": {
        "type": "str",
        "description": ""
      },
      "icon_custom_emoji_id": {
        "type": "str",
        "description": ""
      }
    }
  },
  "ForumTopicCreated": {
    "description": "This object represents a service message about a new forum topic created in the chat.",
    "properties": {
      "name": {
        "type": "str",
        "description": "Name of the topic"
      },
      "icon_color": {
        "type": "int",
        "description": "Color of the topic icon in RGB format"
      },
      "icon_custom_emoji_id": {
        "type": "str",
        "description": "Optional. Unique identifier of the custom emoji shown as the topic icon"
      }
    }
  },
  "ForumTopicEdited": {
    "description": "This object represents a service message about an edited forum topic.",
    "properties": {
      "name": {
        "type": "str",
        "description": "Optional, Name of the topic(if updated)"
      },
      "icon_custom_emoji_id": {
        "type": "str",
        "description": "Optional. New identifier of the custom emoji shown as the topic icon, if it was edited;\nan empty string if the icon was removed"
      }
    }
  },
  "ForumTopicReopened": {
    "description": "This object represents a service message about a forum topic reopened in the chat. Currently holds no information.",
    "properties": {
      "user_id": {
        "type": "int",
        "description": ""
      },
      "first_name": {
        "type": "str",
        "description": ""
      },
      "last_name": {
        "type": "str",
        "description": ""
      },
      "username": {
        "type": "str",
        "description": ""
      },
      "photo": {
        "type": "List",
        "description": ""
      }
    }
  },
  "Game": {
    "description": "This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.",
    "properties": {
      "title": {
        "type": "str",
        "description": "Title of the game"
      },
      "description": {
        "type": "str",
        "description": "Description of the game"
      },
      "photo": {
        "type": "List",
        "description": "Photo that will be displayed in the game message in chats."
      },
      "text": {
        "type": "str",
        "description": "Optional. Brief description of the game or high scores included in the game message. Can be\nautomatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited\nusing editMessageText. 0-4096 characters."
      },
      "text_entities": {
        "type": "List",
        "description": "Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc."
      },
      "animation": {
        "type": "Animation",
        "description": "Optional. Animation that will be displayed in the game message in chats. Upload via BotFather"
      }
    }
  },
  "GameHighScore": {
    "description": "This object represents one row of the high scores table for a game.",
    "properties": {
      "position": {
        "type": "int",
        "description": "Position in high score table for the game"
      },
      "user": {
        "type": "User",
        "description": "User"
      },
      "score": {
        "type": "int",
        "description": "Score"
      }
    }
  },
  "GeneralForumTopicHidden": {
    "description": "This object represents a service message about General forum topic hidden in the chat.",
    "properties": {
      "user_id": {
        "type": "int",
        "description": ""
      },
      "first_name": {
        "type": "str",
        "description": ""
      },
      "last_name": {
        "type": "str",
        "description": ""
      },
      "username": {
        "type": "str",
        "description": ""
      },
      "photo": {
        "type": "List",
        "description": ""
      }
    }
  },
  "GeneralForumTopicUnhidden": {
    "description": "This object represents a service message about General forum topic unhidden in the chat.",
    "properties": {
      "user_id": {
        "type": "int",
        "description": ""
      },
      "first_name": {
        "type": "str",
        "description": ""
      },
      "last_name": {
        "type": "str",
        "description": ""
      },
      "username": {
        "type": "str",
        "description": ""
      },
      "photo": {
        "type": "List",
        "description": ""
      }
    }
  },
  "Gift": {
    "description": "This object represents a gift that can be sent by the bot.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique identifier of the gift."
      },
      "sticker": {
        "type": "Sticker",
        "description": "The sticker that represents the gift"
      },
      "star_count": {
        "type": "int",
        "description": "The number of Telegram Stars that must be paid to send the sticker"
      },
      "upgrade_star_count": {
        "type": "int",
        "description": "Optional. The number of Telegram Stars that must be paid to upgrade the gift to a unique one"
      },
      "total_count": {
        "type": "int",
        "description": "Optional. The total number of the gifts of this type that can be sent; for limited gifts only"
      },
      "remaining_count": {
        "type": "int",
        "description": "Optional. The number of remaining gifts of this type that can be sent; for limited gifts only"
      }
    }
  },
  "GiftInfo": {
    "description": "Describes a service message about a regular gift that was sent or received.",
    "properties": {
      "gift": {
        "type": "Gift",
        "description": "Information about the gift"
      },
      "owned_gift_id": {
        "type": "str",
        "description": "Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts"
      },
      "convert_star_count": {
        "type": "int",
        "description": "Optional. Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible"
      },
      "prepaid_upgrade_star_count": {
        "type": "int",
        "description": "Optional. Number of Telegram Stars that were prepaid by the sender for the ability to upgrade the gift"
      },
      "can_be_upgraded": {
        "type": "bool",
        "description": "Optional. True, if the gift can be upgraded to a unique gift"
      },
      "text": {
        "type": "str",
        "description": "Optional. Text of the message that was added to the gift"
      },
      "entities": {
        "type": "List",
        "description": "Optional. Special entities that appear in the text"
      },
      "is_private": {
        "type": "bool",
        "description": "Optional. True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them"
      }
    }
  },
  "Gifts": {
    "description": "This object represent a list of gifts.",
    "properties": {
      "gifts": {
        "type": "List",
        "description": "Photo that will be displayed in the game message in chats."
      }
    }
  },
  "Giveaway": {
    "description": "This object represents a message about a scheduled giveaway.",
    "properties": {
      "chats": {
        "type": "List",
        "description": "The list of chats which the user must join to participate in the giveaway"
      },
      "winners_selection_date": {
        "type": "int",
        "description": "Point in time (Unix timestamp) when winners of the giveaway will be selected"
      },
      "winner_count": {
        "type": "int",
        "description": "The number of users which are supposed to be selected as winners of the giveaway"
      },
      "only_new_members": {
        "type": "bool",
        "description": "Optional. True, if only users who join the chats after the giveaway started should be eligible to win"
      },
      "has_public_winners": {
        "type": "bool",
        "description": "Optional. True, if the list of giveaway winners will be visible to everyone"
      },
      "prize_description": {
        "type": "str",
        "description": "Optional. Description of additional giveaway prize"
      },
      "country_codes": {
        "type": "List",
        "description": "Optional. A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway."
      },
      "prize_star_count": {
        "type": "int",
        "description": "Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only"
      },
      "premium_subscription_month_count": {
        "type": "int",
        "description": "Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for"
      }
    }
  },
  "GiveawayCompleted": {
    "description": "This object represents a service message about the completion of a giveaway without public winners.",
    "properties": {
      "winner_count": {
        "type": "int",
        "description": "Number of winners in the giveaway"
      },
      "unclaimed_prize_count": {
        "type": "int",
        "description": "Optional. Number of undistributed prizes"
      },
      "giveaway_message": {
        "type": "Message",
        "description": "Optional. Message with the giveaway that was completed, if it wasn't deleted"
      },
      "is_star_giveaway": {
        "type": "bool",
        "description": "Optional. True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway."
      }
    }
  },
  "GiveawayCreated": {
    "description": "This object represents a service message about the creation of a scheduled giveaway.",
    "properties": {
      "prize_star_count": {
        "type": "int",
        "description": "Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only"
      }
    }
  },
  "GiveawayWinners": {
    "description": "This object represents a message about the completion of a giveaway with public winners.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "The chat that created the giveaway"
      },
      "giveaway_message_id": {
        "type": "int",
        "description": "Identifier of the messsage with the giveaway in the chat"
      },
      "winners_selection_date": {
        "type": "int",
        "description": "Point in time (Unix timestamp) when winners of the giveaway were selected"
      },
      "winner_count": {
        "type": "int",
        "description": "Total number of winners in the giveaway"
      },
      "winners": {
        "type": "List",
        "description": "List of up to 100 winners of the giveaway"
      },
      "additional_chat_count": {
        "type": "int",
        "description": "Optional. The number of other chats the user had to join in order to be eligible for the giveaway"
      },
      "prize_star_count": {
        "type": "int",
        "description": "Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only"
      },
      "premium_subscription_month_count": {
        "type": "int",
        "description": "Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for"
      },
      "unclaimed_prize_count": {
        "type": "int",
        "description": "Optional. Number of undistributed prizes"
      },
      "only_new_members": {
        "type": "bool",
        "description": "Optional. True, if only users who had joined the chats after the giveaway started were eligible to win"
      },
      "was_refunded": {
        "type": "bool",
        "description": "Optional. True, if the giveaway was canceled because the payment for it was refunded"
      },
      "prize_description": {
        "type": "str",
        "description": "Optional. Description of additional giveaway prize"
      }
    }
  },
  "InaccessibleMessage": {
    "description": "This object describes a message that was deleted or is otherwise inaccessible to the bot.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "Chat the message belonged to"
      },
      "message_id": {
        "type": "int",
        "description": "Unique message identifier inside the chat"
      },
      "date": {
        "type": "int",
        "description": "Always 0. The field can be used to differentiate regular and inaccessible messages."
      }
    }
  },
  "InlineKeyboardButton": {
    "description": "This object represents one button of an inline keyboard. You must use exactly one of the optional fields.",
    "properties": {
      "text": {
        "type": "str",
        "description": "Label text on the button"
      },
      "callback_data": {
        "type": "str",
        "description": "Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes"
      },
      "url": {
        "type": "str",
        "description": "Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be\nused to mention a user by their ID without using a username, if this is allowed by their privacy settings."
      },
      "web_app": {
        "type": "WebAppInfo",
        "description": "Optional. Description of the Web App that will be launched when the user presses the button. The Web\nApp will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only\nin private chats between a user and the bot."
      },
      "login_url": {
        "type": "LoginUrl",
        "description": "Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for\nthe Telegram Login Widget."
      },
      "switch_inline_query": {
        "type": "str",
        "description": "Optional. If set, pressing the button will prompt the user to select one of their chats,\nopen that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which\ncase just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline\nmode when they are currently in a private chat with it. Especially useful when combined with switch_pm\u2026 actions - in\nthis case the user will be automatically returned to the chat they switched from, skipping the chat selection screen."
      },
      "switch_inline_query_current_chat": {
        "type": "str",
        "description": "Optional. If set, pressing the button will insert the bot's username\nand the specified inline query in the current chat's input field. May be empty, in which case only the bot's username\nwill be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting\nsomething from multiple options."
      },
      "switch_inline_query_chosen_chat": {
        "type": "SwitchInlineQueryChosenChat",
        "description": "Optional. If set, pressing the button will prompt the user to select one of their chats of the\nspecified type, open that chat and insert the bot's username and the specified inline query in the input field"
      },
      "copy_text": {
        "type": "CopyTextButton",
        "description": "Optional. Description of the button that copies the specified text to the clipboard."
      },
      "callback_game": {
        "type": "CallbackGame",
        "description": "Optional. Description of the game that will be launched when the user presses the\nbutton. NOTE: This type of button must always be the first button in the first row."
      },
      "pay": {
        "type": "bool",
        "description": "Optional. Specify True, to send a Pay button. NOTE: This type of button must always be the first button in\nthe first row and can only be used in invoice messages."
      },
      "user_id": {
        "type": "int",
        "description": ""
      }
    }
  },
  "InlineKeyboardMarkup": {
    "description": "This object represents an inline keyboard that appears right next to the message it belongs to.",
    "properties": {
      "inline_keyboard": {
        "type": "List",
        "description": ""
      }
    }
  },
  "InlineQuery": {
    "description": "This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique identifier for this query"
      },
      "from_user": {
        "type": "User",
        "description": "Sender"
      },
      "query": {
        "type": "str",
        "description": "Text of the query (up to 256 characters)"
      },
      "offset": {
        "type": "str",
        "description": "Offset of the results to be returned, can be controlled by the bot"
      },
      "chat_type": {
        "type": "ChatType",
        "description": "Optional. Type of the chat from which the inline query was sent. Can be either \u201csender\u201d for a private\nchat with the inline query sender, \u201cprivate\u201d, \u201cgroup\u201d, \u201csupergroup\u201d, or \u201cchannel\u201d. The chat type should be always\nknown for requests sent from official clients and most third-party clients, unless the request was sent from a secret\nchat"
      },
      "location": {
        "type": "Location",
        "description": "Optional. Sender location, only for bots that request user location"
      }
    }
  },
  "InlineQueryResultArticle": {
    "description": "Represents a link to an article or web page.",
    "properties": {
      "title": {
        "type": "str",
        "description": "Title of the result"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Content of the message to be sent"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "url": {
        "type": "str",
        "description": "Optional. URL of the result"
      },
      "description": {
        "type": "str",
        "description": "Optional. Short description of the result"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "Optional. Url of the thumbnail for the result"
      },
      "thumbnail_width": {
        "type": "int",
        "description": "Optional. Thumbnail width"
      },
      "thumbnail_height": {
        "type": "int",
        "description": "Optional. Thumbnail height"
      }
    }
  },
  "InlineQueryResultAudio": {
    "description": "Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.",
    "properties": {
      "audio_url": {
        "type": "str",
        "description": "A valid URL for the audio file"
      },
      "title": {
        "type": "str",
        "description": "Title"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the audio caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "performer": {
        "type": "str",
        "description": "Optional. Performer"
      },
      "audio_duration": {
        "type": "int",
        "description": "Optional. Audio duration in seconds"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the audio"
      }
    }
  },
  "InlineQueryResultCachedAudio": {
    "description": "Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.",
    "properties": {
      "audio_file_id": {
        "type": "str",
        "description": "A valid file identifier for the audio file"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the audio caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the audio"
      }
    }
  },
  "InlineQueryResultCachedDocument": {
    "description": "Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.",
    "properties": {
      "title": {
        "type": "str",
        "description": "Title for the result"
      },
      "document_file_id": {
        "type": "str",
        "description": "A valid file identifier for the file"
      },
      "description": {
        "type": "str",
        "description": "Optional. Short description of the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the document to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the document caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the file"
      }
    }
  },
  "InlineQueryResultCachedGif": {
    "description": "Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.",
    "properties": {
      "gif_file_id": {
        "type": "str",
        "description": "A valid file identifier for the GIF file"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title for the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the caption. See formatting options for more details."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. Pass True, if a caption is not required for the media"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the GIF animation"
      }
    }
  },
  "InlineQueryResultCachedMpeg4Gif": {
    "description": "Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.",
    "properties": {
      "mpeg4_file_id": {
        "type": "str",
        "description": "A valid file identifier for the MPEG4 file"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title for the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the caption. See formatting options for more details."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. Pass True, if caption should be shown above the media"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the video animation"
      }
    }
  },
  "InlineQueryResultCachedPhoto": {
    "description": "Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.",
    "properties": {
      "photo_file_id": {
        "type": "str",
        "description": "A valid file identifier of the photo"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title for the result"
      },
      "description": {
        "type": "str",
        "description": "Optional. Short description of the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the photo caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. Pass True, if a caption is not required for the media"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the photo"
      }
    }
  },
  "InlineQueryResultCachedSticker": {
    "description": "Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.",
    "properties": {
      "sticker_file_id": {
        "type": "str",
        "description": "A valid file identifier of the sticker"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the sticker"
      }
    }
  },
  "InlineQueryResultCachedVideo": {
    "description": "Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.",
    "properties": {
      "video_file_id": {
        "type": "str",
        "description": "A valid file identifier for the video file"
      },
      "title": {
        "type": "str",
        "description": "Title for the result"
      },
      "description": {
        "type": "str",
        "description": "Optional. Short description of the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the video to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the video caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. Pass True, if a caption is not required for the media"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the video"
      }
    }
  },
  "InlineQueryResultCachedVoice": {
    "description": "Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.",
    "properties": {
      "voice_file_id": {
        "type": "str",
        "description": "A valid file identifier for the voice message"
      },
      "title": {
        "type": "str",
        "description": "Voice message title"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the voice message caption. See formatting options for\nmore details."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the voice message"
      }
    }
  },
  "InlineQueryResultContact": {
    "description": "Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.",
    "properties": {
      "phone_number": {
        "type": "str",
        "description": "Contact's phone number"
      },
      "first_name": {
        "type": "str",
        "description": "Contact's first name"
      },
      "last_name": {
        "type": "str",
        "description": "Optional. Contact's last name"
      },
      "vcard": {
        "type": "str",
        "description": "Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the contact"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "Optional. Url of the thumbnail for the result"
      },
      "thumbnail_width": {
        "type": "int",
        "description": "Optional. Thumbnail width"
      },
      "thumbnail_height": {
        "type": "int",
        "description": "Optional. Thumbnail height"
      }
    }
  },
  "InlineQueryResultDocument": {
    "description": "Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.",
    "properties": {
      "title": {
        "type": "str",
        "description": "Title for the result"
      },
      "document_url": {
        "type": "str",
        "description": "A valid URL for the file"
      },
      "mime_type": {
        "type": "str",
        "description": "MIME type of the content of the file, either \u201capplication/pdf\u201d or \u201capplication/zip\u201d"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the document to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the document caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "description": {
        "type": "str",
        "description": "Optional. Short description of the result"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the file"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "Optional. URL of the thumbnail (JPEG only) for the file"
      },
      "thumbnail_width": {
        "type": "int",
        "description": "Optional. Thumbnail width"
      },
      "thumbnail_height": {
        "type": "int",
        "description": "Optional. Thumbnail height"
      }
    }
  },
  "InlineQueryResultGame": {
    "description": "Represents a Game.",
    "properties": {
      "game_short_name": {
        "type": "str",
        "description": "Short name of the game"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      }
    }
  },
  "InlineQueryResultGif": {
    "description": "Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.",
    "properties": {
      "gif_url": {
        "type": "str",
        "description": "A valid URL for the GIF file. File size must not exceed 1MB"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result"
      },
      "gif_width": {
        "type": "int",
        "description": "Optional. Width of the GIF"
      },
      "gif_height": {
        "type": "int",
        "description": "Optional. Height of the GIF"
      },
      "gif_duration": {
        "type": "int",
        "description": "Optional. Duration of the GIF in seconds"
      },
      "thumbnail_mime_type": {
        "type": "str",
        "description": "Optional. MIME type of the thumbnail, must be one of \u201cimage/jpeg\u201d, \u201cimage/gif\u201d, or\n\u201cvideo/mp4\u201d. Defaults to \u201cimage/jpeg\u201d"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title for the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the caption. See formatting options for more details."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. If true, a caption is shown over the photo or video"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the GIF animation"
      }
    }
  },
  "InlineQueryResultLocation": {
    "description": "Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.",
    "properties": {
      "latitude": {
        "type": "float",
        "description": "Location latitude in degrees"
      },
      "longitude": {
        "type": "float",
        "description": "Location longitude in degrees"
      },
      "title": {
        "type": "str",
        "description": "Location title"
      },
      "horizontal_accuracy": {
        "type": "float",
        "description": "Optional. The radius of uncertainty for the location, measured in meters; 0-1500"
      },
      "live_period": {
        "type": "int",
        "description": "Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely."
      },
      "heading": {
        "type": "int",
        "description": "Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified."
      },
      "proximity_alert_radius": {
        "type": "int",
        "description": "Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified."
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the location"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "Optional. Url of the thumbnail for the result"
      },
      "thumbnail_width": {
        "type": "int",
        "description": "Optional. Thumbnail width"
      },
      "thumbnail_height": {
        "type": "int",
        "description": "Optional. Thumbnail height"
      }
    }
  },
  "InlineQueryResultMpeg4Gif": {
    "description": "Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.",
    "properties": {
      "mpeg4_url": {
        "type": "str",
        "description": "A valid URL for the MPEG4 file. File size must not exceed 1MB"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result"
      },
      "mpeg4_width": {
        "type": "int",
        "description": "Optional. Video width"
      },
      "mpeg4_height": {
        "type": "int",
        "description": "Optional. Video height"
      },
      "mpeg4_duration": {
        "type": "int",
        "description": "Optional. Video duration in seconds"
      },
      "thumbnail_mime_type": {
        "type": "str",
        "description": "Optional. MIME type of the thumbnail, must be one of \u201cimage/jpeg\u201d, \u201cimage/gif\u201d, or\n\u201cvideo/mp4\u201d. Defaults to \u201cimage/jpeg\u201d"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title for the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the caption. See formatting options for more details."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. If true, a caption is shown over the photo or video"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the video animation"
      }
    }
  },
  "InlineQueryResultPhoto": {
    "description": "Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.",
    "properties": {
      "photo_url": {
        "type": "str",
        "description": "A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "URL of the thumbnail for the photo"
      },
      "photo_width": {
        "type": "int",
        "description": "Optional. Width of the photo"
      },
      "photo_height": {
        "type": "int",
        "description": "Optional. Height of the photo"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title for the result"
      },
      "description": {
        "type": "str",
        "description": "Optional. Short description of the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the photo caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. If true, a caption is shown over the photo or video"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the photo"
      }
    }
  },
  "InlineQueryResultVenue": {
    "description": "Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.",
    "properties": {
      "latitude": {
        "type": "float",
        "description": "Latitude of the venue location in degrees"
      },
      "longitude": {
        "type": "float",
        "description": "Longitude of the venue location in degrees"
      },
      "title": {
        "type": "str",
        "description": "Title of the venue"
      },
      "address": {
        "type": "str",
        "description": "Address of the venue"
      },
      "foursquare_id": {
        "type": "str",
        "description": "Optional. Foursquare identifier of the venue if known"
      },
      "foursquare_type": {
        "type": "str",
        "description": "Optional. Foursquare type of the venue, if known. (For example,\n\u201carts_entertainment/default\u201d, \u201carts_entertainment/aquarium\u201d or \u201cfood/icecream\u201d.)"
      },
      "google_place_id": {
        "type": "str",
        "description": "Optional. Google Places identifier of the venue"
      },
      "google_place_type": {
        "type": "str",
        "description": "Optional. Google Places type of the venue. (See supported types.)"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the venue"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "Optional. Url of the thumbnail for the result"
      },
      "thumbnail_width": {
        "type": "int",
        "description": "Optional. Thumbnail width"
      },
      "thumbnail_height": {
        "type": "int",
        "description": "Optional. Thumbnail height"
      }
    }
  },
  "InlineQueryResultVideo": {
    "description": "Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.",
    "properties": {
      "video_url": {
        "type": "str",
        "description": "A valid URL for the embedded video player or video file"
      },
      "mime_type": {
        "type": "str",
        "description": "MIME type of the content of the video URL, \u201ctext/html\u201d or \u201cvideo/mp4\u201d"
      },
      "thumbnail_url": {
        "type": "str",
        "description": "URL of the thumbnail (JPEG only) for the video"
      },
      "title": {
        "type": "str",
        "description": "Title for the result"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the video to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the video caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. If true, a caption is shown over the video"
      },
      "video_width": {
        "type": "int",
        "description": "Optional. Video width"
      },
      "video_height": {
        "type": "int",
        "description": "Optional. Video height"
      },
      "video_duration": {
        "type": "int",
        "description": "Optional. Video duration in seconds"
      },
      "description": {
        "type": "str",
        "description": "Optional. Short description of the result"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the video. This field is\nrequired if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video)."
      }
    }
  },
  "InlineQueryResultVoice": {
    "description": "Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.",
    "properties": {
      "voice_url": {
        "type": "str",
        "description": "A valid URL for the voice recording"
      },
      "title": {
        "type": "str",
        "description": "Recording title"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the voice message caption. See formatting options for\nmore details."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "voice_duration": {
        "type": "int",
        "description": "Optional. Recording duration in seconds"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message"
      },
      "input_message_content": {
        "type": "InputMessageContent",
        "description": "Optional. Content of the message to be sent instead of the voice recording"
      }
    }
  },
  "InlineQueryResultsButton": {
    "description": "This object represents a button to be shown above inline query results.",
    "properties": {
      "text": {
        "type": "str",
        "description": "Label text on the button"
      },
      "web_app": {
        "type": "WebAppInfo",
        "description": "Optional. Description of the Web App that will be launched when the user presses the button.\nThe Web App will be able to switch back to the inline mode using the method web_app_switch_inline_query inside the Web App."
      },
      "start_parameter": {
        "type": "str",
        "description": "Optional. Deep-linking parameter for the /start message sent to the bot when a user presses the button.\n1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed.\nExample: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search\nresults accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing\nany. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs\nthe bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat\nwhere they wanted to use the bot's inline capabilities."
      }
    }
  },
  "InputChecklist": {
    "description": "Describes a checklist to create.",
    "properties": {
      "title": {
        "type": "str",
        "description": "Title of the checklist; 1-255 characters after entities parsing"
      },
      "tasks": {
        "type": "List",
        "description": "List of 1-30 tasks in the checklist"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the title. See formatting options for more details."
      },
      "title_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the title, which can be specified instead of parse_mode.\nCurrently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed."
      },
      "others_can_add_tasks": {
        "type": "bool",
        "description": "Optional. Pass True if other users can add tasks to the checklist"
      },
      "others_can_mark_tasks_as_done": {
        "type": "bool",
        "description": "Optional. Pass True if other users can mark tasks as done or not done in the checklist"
      }
    }
  },
  "InputChecklistTask": {
    "description": "Describes a task to add to a checklist.",
    "properties": {
      "text": {
        "type": "str",
        "description": "Text of the task; 1-100 characters after entities parsing"
      },
      "parse_mode": {
        "type": "Optional",
        "description": "Optional. Mode for parsing entities in the text. See formatting options for more details."
      },
      "text_entities": {
        "type": "Optional",
        "description": "Optional. List of special entities that appear in the text, which can be specified instead of parse_mode.\nCurrently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed."
      }
    }
  },
  "InputContactMessageContent": {
    "description": "Represents the content of a contact message to be sent as the result of an inline query.",
    "properties": {
      "phone_number": {
        "type": "str",
        "description": "Contact's phone number"
      },
      "first_name": {
        "type": "str",
        "description": "Contact's first name"
      },
      "last_name": {
        "type": "str",
        "description": "Optional. Contact's last name"
      },
      "vcard": {
        "type": "str",
        "description": "Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes"
      }
    }
  },
  "InputInvoiceMessageContent": {
    "description": "Represents the content of an invoice message to be sent as the result of an inline query.",
    "properties": {
      "title": {
        "type": "str",
        "description": "Product name, 1-32 characters"
      },
      "description": {
        "type": "str",
        "description": "Product description, 1-255 characters"
      },
      "payload": {
        "type": "str",
        "description": "Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your\ninternal processes."
      },
      "currency": {
        "type": "str",
        "description": "Three-letter ISO 4217 currency code, see more on currencies"
      },
      "prices": {
        "type": "List",
        "description": "Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery\ncost, delivery tax, bonus, etc.)"
      },
      "provider_token": {
        "type": "str",
        "description": "Payment provider token, obtained via @BotFather"
      },
      "max_tip_amount": {
        "type": "int",
        "description": "Optional. The maximum accepted amount for tips in the smallest units of the currency\n(integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp\nparameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the\nmajority of currencies). Defaults to 0"
      },
      "suggested_tip_amounts": {
        "type": "List",
        "description": "Optional. A JSON-serialized array of suggested amounts of tip in the smallest units\nof the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip\namounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount."
      },
      "provider_data": {
        "type": "str",
        "description": "Optional. A JSON-serialized object for data about the invoice, which will be shared with the\npayment provider. A detailed description of the required fields should be provided by the payment provider."
      },
      "photo_url": {
        "type": "str",
        "description": "Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image\nfor a service."
      },
      "photo_size": {
        "type": "int",
        "description": "Optional. Photo size in bytes"
      },
      "photo_width": {
        "type": "int",
        "description": "Optional. Photo width"
      },
      "photo_height": {
        "type": "int",
        "description": "Optional. Photo height"
      },
      "need_name": {
        "type": "bool",
        "description": "Optional. Pass True, if you require the user's full name to complete the order"
      },
      "need_phone_number": {
        "type": "bool",
        "description": "Optional. Pass True, if you require the user's phone number to complete the order"
      },
      "need_email": {
        "type": "bool",
        "description": "Optional. Pass True, if you require the user's email address to complete the order"
      },
      "need_shipping_address": {
        "type": "bool",
        "description": "Optional. Pass True, if you require the user's shipping address to complete the\norder"
      },
      "send_phone_number_to_provider": {
        "type": "bool",
        "description": "Optional. Pass True, if the user's phone number should be sent to provider"
      },
      "send_email_to_provider": {
        "type": "bool",
        "description": "Optional. Pass True, if the user's email address should be sent to provider"
      },
      "is_flexible": {
        "type": "bool",
        "description": "Optional. Pass True, if the final price depends on the shipping method"
      }
    }
  },
  "InputLocationMessageContent": {
    "description": "Represents the content of a location message to be sent as the result of an inline query.",
    "properties": {
      "latitude": {
        "type": "float",
        "description": "Latitude of the location in degrees"
      },
      "longitude": {
        "type": "float",
        "description": "Longitude of the location in degrees"
      },
      "horizontal_accuracy": {
        "type": "float",
        "description": "Optional. The radius of uncertainty for the location, measured in meters; 0-1500"
      },
      "live_period": {
        "type": "int",
        "description": "Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely."
      },
      "heading": {
        "type": "int",
        "description": "Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified."
      },
      "proximity_alert_radius": {
        "type": "int",
        "description": "Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified."
      }
    }
  },
  "InputMediaAnimation": {
    "description": "Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.",
    "properties": {
      "media": {
        "type": "Union",
        "description": "File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an\nHTTP URL for Telegram to get a file from the Internet, or pass \u201cattach://<file_attach_name>\u201d to upload a new one using\nmultipart/form-data under <file_attach_name> name. More information on Sending Files \u00bb"
      },
      "thumbnail": {
        "type": "Union",
        "description": "Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported\nserver-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should\nnot exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be\nonly uploaded as a new file, so you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using\nmultipart/form-data under <file_attach_name>. More information on Sending Files \u00bb"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the animation caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. True, if the caption should be shown above the animation"
      },
      "width": {
        "type": "int",
        "description": "Optional. Animation width"
      },
      "height": {
        "type": "int",
        "description": "Optional. Animation height"
      },
      "duration": {
        "type": "int",
        "description": "Optional. Animation duration in seconds"
      },
      "has_spoiler": {
        "type": "bool",
        "description": "Optional. True, if the uploaded animation is a spoiler"
      }
    }
  },
  "InputMediaAudio": {
    "description": "Represents an audio file to be treated as music to be sent.",
    "properties": {
      "media": {
        "type": "Union",
        "description": "File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an\nHTTP URL for Telegram to get a file from the Internet, or pass \u201cattach://<file_attach_name>\u201d to upload a new one using\nmultipart/form-data under <file_attach_name> name. More information on Sending Files \u00bb"
      },
      "thumbnail": {
        "type": "Union",
        "description": "Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported\nserver-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should\nnot exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be\nonly uploaded as a new file, so you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using\nmultipart/form-data under <file_attach_name>. More information on Sending Files \u00bb"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the audio caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "duration": {
        "type": "int",
        "description": "Optional. Duration of the audio in seconds"
      },
      "performer": {
        "type": "str",
        "description": "Optional. Performer of the audio"
      },
      "title": {
        "type": "str",
        "description": "Optional. Title of the audio"
      }
    }
  },
  "InputMediaDocument": {
    "description": "Represents a general file to be sent.",
    "properties": {
      "media": {
        "type": "Union",
        "description": "File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an\nHTTP URL for Telegram to get a file from the Internet, or pass \u201cattach://<file_attach_name>\u201d to upload a new one using\nmultipart/form-data under <file_attach_name> name. More information on Sending Files \u00bb"
      },
      "thumbnail": {
        "type": "Union",
        "description": "Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported\nserver-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should\nnot exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be\nonly uploaded as a new file, so you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using\nmultipart/form-data under <file_attach_name>. More information on Sending Files \u00bb"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the document to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the document caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "disable_content_type_detection": {
        "type": "bool",
        "description": "Optional. Disables automatic server-side content type detection for\nfiles uploaded using multipart/form-data. Always True, if the document is sent as part of an album."
      }
    }
  },
  "InputMediaPhoto": {
    "description": "Represents a photo to be sent.",
    "properties": {
      "media": {
        "type": "Union",
        "description": "File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an\nHTTP URL for Telegram to get a file from the Internet, or pass \u201cattach://<file_attach_name>\u201d to upload a new one using\nmultipart/form-data under <file_attach_name> name. More information on Sending Files \u00bb"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the photo caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. True, if the caption should be shown above the photo"
      },
      "has_spoiler": {
        "type": "bool",
        "description": "Optional. True, if the uploaded photo is a spoiler"
      }
    }
  },
  "InputMediaVideo": {
    "description": "Represents a video to be sent.",
    "properties": {
      "media": {
        "type": "Union",
        "description": "File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an\nHTTP URL for Telegram to get a file from the Internet, or pass \u201cattach://<file_attach_name>\u201d to upload a new one using\nmultipart/form-data under <file_attach_name> name. More information on Sending Files \u00bb"
      },
      "thumbnail": {
        "type": "InputFile",
        "description": "Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported\nserver-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should\nnot exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be\nonly uploaded as a new file, so you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using\nmultipart/form-data under <file_attach_name>. More information on Sending Files \u00bb"
      },
      "cover": {
        "type": "InputFile",
        "description": "Optional. Cover for the video in the message.\nPass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet,\nor pass \u201cattach://<file_attach_name>\u201d to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files \u00bb"
      },
      "start_timestamp": {
        "type": "int",
        "description": "Optional. Start timestamp for the video in the message"
      },
      "caption": {
        "type": "str",
        "description": "Optional. Caption of the video to be sent, 0-1024 characters after entities parsing"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the video caption. See formatting options for more\ndetails."
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in the caption, which can be specified\ninstead of parse_mode"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. True, if the caption should be shown above the video"
      },
      "width": {
        "type": "int",
        "description": "Optional. Video width"
      },
      "height": {
        "type": "int",
        "description": "Optional. Video height"
      },
      "duration": {
        "type": "int",
        "description": "Optional. Video duration in seconds"
      },
      "supports_streaming": {
        "type": "bool",
        "description": "Optional. Pass True, if the uploaded video is suitable for streaming"
      },
      "has_spoiler": {
        "type": "bool",
        "description": "Optional. True, if the uploaded video is a spoiler"
      }
    }
  },
  "InputMessageContent": {
    "description": "",
    "properties": {
      "message_text": {
        "type": "str",
        "description": ""
      },
      "parse_mode": {
        "type": "str",
        "description": ""
      },
      "entities": {
        "type": "List",
        "description": ""
      },
      "link_preview_options": {
        "type": "LinkPreviewOptions",
        "description": ""
      }
    }
  },
  "InputPaidMediaPhoto": {
    "description": "The paid media to send is a photo.",
    "properties": {
      "media": {
        "type": "Union",
        "description": "File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for\nTelegram to get a file from the Internet, or pass \u201cattach://<file_attach_name>\u201d to upload a new one using multipart/form-data\nunder <file_attach_name> name. More information on Sending Files \u00bb"
      }
    }
  },
  "InputPaidMediaVideo": {
    "description": "The paid media to send is a video.",
    "properties": {
      "media": {
        "type": "Union",
        "description": "File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for\nTelegram to get a file from the Internet, or pass \u201cattach://<file_attach_name>\u201d to upload a new one using multipart/form-data\nunder <file_attach_name> name. More information on Sending Files \u00bb"
      },
      "thumbnail": {
        "type": "InputFile",
        "description": "Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.\nThe thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.\nIgnored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,\nso you can pass \u201cattach://<file_attach_name>\u201d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.\nMore information on Sending Files \u00bb"
      },
      "cover": {
        "type": "InputFile",
        "description": "Optional. Cover for the video in the message.\nPass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet,\nor pass \u201cattach://<file_attach_name>\u201d to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files \u00bb"
      },
      "start_timestamp": {
        "type": "int",
        "description": "Optional. Start timestamp for the video in the message"
      },
      "width": {
        "type": "int",
        "description": "Optional. Video width"
      },
      "height": {
        "type": "int",
        "description": "Optional. Video height"
      },
      "duration": {
        "type": "int",
        "description": "Optional. Video duration in seconds"
      },
      "supports_streaming": {
        "type": "bool",
        "description": "Optional. Pass True if the uploaded video is suitable for streaming"
      }
    }
  },
  "InputPollOption": {
    "description": "This object contains information about one answer option in a poll to send.",
    "properties": {
      "text": {
        "type": "str",
        "description": "Option text, 1-100 characters"
      },
      "text_parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the text. See formatting options for more details. Currently, only custom emoji entities are allowed"
      },
      "text_entities": {
        "type": "List",
        "description": "Optional. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of text_parse_mode"
      }
    }
  },
  "InputProfilePhotoAnimated": {
    "description": "An animated profile photo in the MPEG4 format.",
    "properties": {
      "animation": {
        "type": "Union",
        "description": "The animated profile photo. Profile photos can't be reused and can only be uploaded as a new file,\nso you can pass \u201cattach://<file_attach_name>\u201d if the photo was uploaded using multipart/form-data under <file_attach_name>.\nMore information on Sending Files \u00bb"
      },
      "main_frame_timestamp": {
        "type": "Optional",
        "description": "Optional. Timestamp in seconds of the frame that will be used as the static profile photo. Defaults to 0.0."
      }
    }
  },
  "InputProfilePhotoStatic": {
    "description": "A static profile photo in the .JPG format.",
    "properties": {
      "photo": {
        "type": "Union",
        "description": "The static profile photo. Profile photos can't be reused and can only be uploaded as a new file,\nso you can pass \u201cattach://<file_attach_name>\u201d if the photo was uploaded using multipart/form-data under <file_attach_name>.\nMore information on Sending Files \u00bb"
      }
    }
  },
  "InputSticker": {
    "description": "This object describes a sticker to be added to a sticker set.",
    "properties": {
      "sticker": {
        "type": "Union",
        "description": "The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers,\npass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.\nAnimated and video stickers can't be uploaded via HTTP URL."
      },
      "format": {
        "type": "str",
        "description": "Format of the added sticker, must be one of \u201cstatic\u201d for a .WEBP or .PNG image, \u201canimated\u201d for a .TGS animation, \u201cvideo\u201d for a WEBM video"
      },
      "emoji_list": {
        "type": "List",
        "description": "One or more(up to 20) emoji(s) corresponding to the sticker"
      },
      "mask_position": {
        "type": "MaskPosition",
        "description": "Optional. Position where the mask should be placed on faces. For \u201cmask\u201d stickers only."
      },
      "keywords": {
        "type": "List",
        "description": "Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters.\nFor \u201cregular\u201d and \u201ccustom_emoji\u201d stickers only."
      }
    }
  },
  "InputStoryContentPhoto": {
    "description": "Describes a photo to post as a story.",
    "properties": {
      "photo": {
        "type": "str",
        "description": "The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB."
      }
    }
  },
  "InputStoryContentVideo": {
    "description": "Describes a video to post as a story.",
    "properties": {
      "video": {
        "type": "str",
        "description": "The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB."
      },
      "duration": {
        "type": "float",
        "description": "Optional. Precise duration of the video in seconds; 0-60"
      },
      "cover_frame_timestamp": {
        "type": "float",
        "description": "Optional. Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0."
      },
      "is_animation": {
        "type": "bool",
        "description": "Optional. Pass True if the video has no sound"
      }
    }
  },
  "InputTextMessageContent": {
    "description": "Represents the content of a text message to be sent as the result of an inline query.",
    "properties": {
      "message_text": {
        "type": "str",
        "description": "Text of the message to be sent, 1-4096 characters"
      },
      "parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the message text. See formatting options for more\ndetails."
      },
      "entities": {
        "type": "List",
        "description": "Optional. List of special entities that appear in message text, which can be specified instead of\nparse_mode"
      },
      "link_preview_options": {
        "type": "LinkPreviewOptions",
        "description": "Optional. Link preview generation options for the message"
      }
    }
  },
  "InputVenueMessageContent": {
    "description": "Represents the content of a venue message to be sent as the result of an inline query.",
    "properties": {
      "latitude": {
        "type": "float",
        "description": "Latitude of the venue in degrees"
      },
      "longitude": {
        "type": "float",
        "description": "Longitude of the venue in degrees"
      },
      "title": {
        "type": "str",
        "description": "Name of the venue"
      },
      "address": {
        "type": "str",
        "description": "Address of the venue"
      },
      "foursquare_id": {
        "type": "str",
        "description": "Optional. Foursquare identifier of the venue, if known"
      },
      "foursquare_type": {
        "type": "str",
        "description": "Optional. Foursquare type of the venue, if known. (For example,\n\u201carts_entertainment/default\u201d, \u201carts_entertainment/aquarium\u201d or \u201cfood/icecream\u201d.)"
      },
      "google_place_id": {
        "type": "str",
        "description": "Optional. Google Places identifier of the venue"
      },
      "google_place_type": {
        "type": "str",
        "description": "Optional. Google Places type of the venue. (See supported types.)"
      }
    }
  },
  "Invoice": {
    "description": "This object contains basic information about an invoice.",
    "properties": {
      "title": {
        "type": "str",
        "description": "Product name"
      },
      "description": {
        "type": "str",
        "description": "Product description"
      },
      "start_parameter": {
        "type": "str",
        "description": "Unique bot deep-linking parameter that can be used to generate this invoice"
      },
      "currency": {
        "type": "str",
        "description": "Three-letter ISO 4217 currency code"
      },
      "total_amount": {
        "type": "int",
        "description": "Total price in the smallest units of the currency (integer, not float/double). For example,\nfor a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past\nthe decimal point for each currency (2 for the majority of currencies)."
      }
    }
  },
  "KeyboardButton": {
    "description": "This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive.",
    "properties": {
      "text": {
        "type": "str",
        "description": "Text of the button. If none of the optional fields are used, it will be sent as a message when the button is\npressed"
      },
      "request_users": {
        "type": "KeyboardButtonRequestUsers",
        "description": "Optional. If specified, pressing the button will open a list of suitable users.\nIdentifiers of selected users will be sent to the bot in a \u201cusers_shared\u201d service message. Available in private chats only."
      },
      "request_chat": {
        "type": "KeyboardButtonRequestChat",
        "description": "Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will\nsend its identifier to the bot in a \u201cchat_shared\u201d service message. Available in private chats only."
      },
      "request_contact": {
        "type": "bool",
        "description": "Optional. If True, the user's phone number will be sent as a contact when the button is\npressed. Available in private chats only."
      },
      "request_location": {
        "type": "bool",
        "description": "Optional. If True, the user's current location will be sent when the button is pressed.\nAvailable in private chats only."
      },
      "request_poll": {
        "type": "KeyboardButtonPollType",
        "description": "Optional. If specified, the user will be asked to create a poll and send it to the bot when the\nbutton is pressed. Available in private chats only."
      },
      "web_app": {
        "type": "WebAppInfo",
        "description": "Optional. If specified, the described Web App will be launched when the button is pressed. The Web App\nwill be able to send a \u201cweb_app_data\u201d service message. Available in private chats only."
      }
    }
  },
  "KeyboardButtonPollType": {
    "description": "This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type."
      }
    }
  },
  "KeyboardButtonRequestChat": {
    "description": "This object defines the criteria used to request a suitable chat. The identifier of the selected chat will",
    "properties": {
      "chat_is_channel": {
        "type": "bool",
        "description": "Pass True to request a channel chat, pass False to request a group or a supergroup chat."
      },
      "chat_is_forum": {
        "type": "bool",
        "description": "Optional. Pass True to request a forum supergroup, pass False to request a non-forum chat.\nIf not specified, no additional restrictions are applied."
      },
      "chat_has_username": {
        "type": "bool",
        "description": "Optional. Pass True to request a supergroup or a channel with a username, pass False to request a\nchat without a username. If not specified, no additional restrictions are applied."
      },
      "chat_is_created": {
        "type": "bool",
        "description": "Optional. Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied."
      },
      "user_administrator_rights": {
        "type": "ChatAdministratorRights",
        "description": "Optional. A JSON-serialized object listing the required administrator rights of the user in the chat.\nThe rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied."
      },
      "bot_administrator_rights": {
        "type": "ChatAdministratorRights",
        "description": "Optional. A JSON-serialized object listing the required administrator rights of the bot in the chat.\nThe rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied."
      },
      "bot_is_member": {
        "type": "bool",
        "description": "Optional. Pass True to request a chat where the bot is a member. Otherwise, no additional restrictions are applied."
      },
      "request_title": {
        "type": "bool",
        "description": "Optional. Request title"
      },
      "request_username": {
        "type": "bool",
        "description": "Optional. Request username"
      },
      "request_photo": {
        "type": "bool",
        "description": "Optional. Request photo"
      }
    }
  },
  "KeyboardButtonRequestUsers": {
    "description": "This object defines the criteria used to request a suitable user.",
    "properties": {
      "user_is_bot": {
        "type": "bool",
        "description": "Optional. Pass True to request a bot, pass False to request a regular user.\nIf not specified, no additional restrictions are applied."
      },
      "user_is_premium": {
        "type": "bool",
        "description": "Optional. Pass True to request a premium user, pass False to request a non-premium user.\nIf not specified, no additional restrictions are applied."
      },
      "max_quantity": {
        "type": "int",
        "description": "Optional. The maximum number of users to be selected; 1-10. Defaults to 1."
      },
      "request_name": {
        "type": "bool",
        "description": "Optional. Request name"
      },
      "request_username": {
        "type": "bool",
        "description": "Optional. Request username"
      },
      "request_photo": {
        "type": "bool",
        "description": "Optional. Request photo"
      }
    }
  },
  "LabeledPrice": {
    "description": "This object represents a portion of the price for goods or services.",
    "properties": {
      "label": {
        "type": "str",
        "description": "Portion label"
      },
      "amount": {
        "type": "int",
        "description": "Price of the product in the smallest units of the currency (integer, not float/double). For example,\nfor a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past\nthe decimal point for each currency (2 for the majority of currencies)."
      }
    }
  },
  "LinkPreviewOptions": {
    "description": "Describes the options used for link preview generation.",
    "properties": {
      "is_disabled": {
        "type": "bool",
        "description": "Optional. True, if the link preview is disabled"
      },
      "url": {
        "type": "str",
        "description": "Optional. URL to use for the link preview. If empty, then the first URL found in the message text will be used"
      },
      "prefer_small_media": {
        "type": "bool",
        "description": "Optional. True, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview"
      },
      "prefer_large_media": {
        "type": "bool",
        "description": "Optional. True, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview"
      },
      "show_above_text": {
        "type": "bool",
        "description": "Optional. True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text"
      }
    }
  },
  "Listener": {
    "description": "",
    "properties": {
      "chat_id": {
        "type": "int",
        "description": ""
      },
      "future": {
        "type": "Future",
        "description": ""
      },
      "user_id": {
        "type": "int",
        "description": ""
      },
      "sender_id": {
        "type": "int",
        "description": ""
      },
      "update_type": {
        "type": "str",
        "description": ""
      },
      "cancel": {
        "type": "Callable",
        "description": ""
      },
      "filters": {
        "type": "Filter",
        "description": ""
      }
    }
  },
  "Location": {
    "description": "This object represents a point on the map.",
    "properties": {
      "latitude": {
        "type": "float",
        "description": "Latitude as defined by sender"
      },
      "longitude": {
        "type": "float",
        "description": "Longitude as defined by sender"
      },
      "horizontal_accuracy": {
        "type": "float",
        "description": "Optional. The radius of uncertainty for the location, measured in meters; 0-1500"
      },
      "live_period": {
        "type": "int",
        "description": "Optional. Time relative to the message sending date, during which the location can be updated;\nin seconds. For active live locations only."
      },
      "heading": {
        "type": "int",
        "description": "Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only."
      },
      "proximity_alert_radius": {
        "type": "int",
        "description": "Optional. The maximum distance for proximity alerts about approaching another\nchat member, in meters. For sent live locations only."
      }
    }
  },
  "LocationAddress": {
    "description": "Describes the physical address of a location.",
    "properties": {
      "country_code": {
        "type": "str",
        "description": "The two-letter ISO 3166-1 alpha-2 country code of the country where the location is located"
      },
      "state": {
        "type": "str",
        "description": "Optional. State of the location"
      },
      "city": {
        "type": "str",
        "description": "Optional. City of the location"
      },
      "street": {
        "type": "str",
        "description": "Optional. Street address of the location"
      }
    }
  },
  "LoginUrl": {
    "description": "This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:",
    "properties": {
      "url": {
        "type": "str",
        "description": "An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed.\nIf the user refuses to provide authorization data, the original URL without information about the user will be\nopened. The data added is the same as described in Receiving authorization data. NOTE: You must always check the hash\nof the received data to verify the authentication and the integrity of the data as described in Checking\nauthorization."
      },
      "forward_text": {
        "type": "str",
        "description": "Optional. New text of the button in forwarded messages."
      },
      "bot_username": {
        "type": "str",
        "description": "Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for\nmore details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the\ndomain linked with the bot. See Linking your domain to the bot for more details."
      },
      "request_write_access": {
        "type": "bool",
        "description": "Optional. Pass True to request the permission for your bot to send messages to the\nuser."
      }
    }
  },
  "MaskPosition": {
    "description": "This object describes the position on faces where a mask should be placed by default.",
    "properties": {
      "point": {
        "type": "str",
        "description": "The part of the face relative to which the mask should be placed. One of \u201cforehead\u201d, \u201ceyes\u201d, \u201cmouth\u201d, or\n\u201cchin\u201d."
      },
      "x_shift": {
        "type": "float",
        "description": "Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example,\nchoosing -1.0 will place mask just to the left of the default mask position."
      },
      "y_shift": {
        "type": "float",
        "description": "Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For\nexample, 1.0 will place the mask just below the default mask position."
      },
      "scale": {
        "type": "float",
        "description": "Mask scaling coefficient. For example, 2.0 means double size."
      }
    }
  },
  "MenuButton": {
    "description": "This object describes the bot's menu button in a private chat. It should be one of",
    "properties": {
      "type": {
        "type": "str",
        "description": ""
      }
    }
  },
  "MenuButtonCommands": {
    "description": "Represents a menu button, which opens the bot's list of commands.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the button, must be commands"
      }
    }
  },
  "MenuButtonDefault": {
    "description": "Describes that no specific value for the menu button was set.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the button, must be default"
      }
    }
  },
  "MenuButtonWebApp": {
    "description": "Represents a menu button, which launches a Web App.",
    "properties": {
      "type": {
        "type": "str",
        "description": "Type of the button, must be web_app"
      },
      "text": {
        "type": "str",
        "description": "Text on the button"
      },
      "web_app": {
        "type": "WebAppInfo",
        "description": "Description of the Web App that will be launched when the user presses the button. The Web App will be\nable to send an arbitrary message on behalf of the user using the method answerWebAppQuery."
      }
    }
  },
  "Message": {
    "description": "This object represents a message.",
    "properties": {
      "message_id": {
        "type": "int",
        "description": "Unique message identifier inside this chat"
      },
      "date": {
        "type": "int",
        "description": "Date the message was sent in Unix time"
      },
      "chat": {
        "type": "Chat",
        "description": "Conversation the message belongs to"
      },
      "message_thread_id": {
        "type": "int",
        "description": "Optional. Unique identifier of a message thread to which the message belongs; for supergroups only"
      },
      "from_user": {
        "type": "User",
        "description": "Optional. Sender of the message; empty for messages sent to channels. For backward compatibility, the\nfield contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat."
      },
      "sender_chat": {
        "type": "Chat",
        "description": "Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself for\nchannel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for\nmessages automatically forwarded to the discussion group. For backward compatibility, the field from contains a\nfake sender user in non-channel chats, if the message was sent on behalf of a chat."
      },
      "sender_boost_count": {
        "type": "int",
        "description": "Optional. If the sender of the message boosted the chat, the number of boosts added by the user"
      },
      "sender_business_bot": {
        "type": "User",
        "description": ""
      },
      "business_connection_id": {
        "type": "str",
        "description": "Optional. Unique identifier of the business connection from which the message was received. If non-empty,\nthe message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier."
      },
      "forward_origin": {
        "type": "MessageOrigin",
        "description": ""
      },
      "is_topic_message": {
        "type": "bool",
        "description": "Optional. True, if the message is sent to a forum topic"
      },
      "is_automatic_forward": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if the message is a channel post that was automatically\nforwarded to the connected discussion group"
      },
      "reply_to_message": {
        "type": "Message",
        "description": "Optional. For replies, the original message. Note that the Message object in this field\nwill not contain further reply_to_message fields even if it itself is a reply."
      },
      "external_reply": {
        "type": "ExternalReplyInfo",
        "description": "Optional. Information about the message that is being replied to, which may come from another chat or forum topic"
      },
      "quote": {
        "type": "TextQuote",
        "description": "Optional. For replies that quote part of the original message, the quoted part of the message"
      },
      "reply_to_story": {
        "type": "Story",
        "description": "Optional. For replies to a story, the original story"
      },
      "via_bot": {
        "type": "User",
        "description": "Optional. Bot through which the message was sent"
      },
      "edit_date": {
        "type": "int",
        "description": "Optional. Date the message was last edited in Unix time"
      },
      "has_protected_content": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if the message can't be forwarded"
      },
      "is_from_offline": {
        "type": "bool",
        "description": "Optional. True, if the message was sent by an implicit action, for example,\nas an away or a greeting business message, or as a scheduled message"
      },
      "media_group_id": {
        "type": "str",
        "description": "Optional. The unique identifier of a media message group this message belongs to"
      },
      "author_signature": {
        "type": "str",
        "description": "Optional. Signature of the post author for messages in channels, or the custom title of an\nanonymous group administrator"
      },
      "text": {
        "type": "String",
        "description": "Optional. For text messages, the actual UTF-8 text of the message"
      },
      "entities": {
        "type": "List",
        "description": "Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that\nappear in the text"
      },
      "link_preview_options": {
        "type": "LinkPreviewOptions",
        "description": "Optional. Options used for link preview generation for the message,\nif it is a text message and link preview options were changed"
      },
      "effect_id": {
        "type": "str",
        "description": "Optional. Unique identifier of the message effect added to the message"
      },
      "animation": {
        "type": "Animation",
        "description": "Optional. Message is an animation, information about the animation. For backward\ncompatibility, when this field is set, the document field will also be set"
      },
      "audio": {
        "type": "Audio",
        "description": "Optional. Message is an audio file, information about the file"
      },
      "document": {
        "type": "Document",
        "description": "Optional. Message is a general file, information about the file"
      },
      "paid_media": {
        "type": "PaidMediaInfo",
        "description": ""
      },
      "photo": {
        "type": "List",
        "description": "Optional. Message is a photo, available sizes of the photo"
      },
      "sticker": {
        "type": "Sticker",
        "description": "Optional. Message is a sticker, information about the sticker"
      },
      "story": {
        "type": "Story",
        "description": "Optional. Message is a forwarded story"
      },
      "video": {
        "type": "Video",
        "description": "Optional. Message is a video, information about the video"
      },
      "video_note": {
        "type": "VideoNote",
        "description": "Optional. Message is a video note, information about the video message"
      },
      "voice": {
        "type": "Voice",
        "description": "Optional. Message is a voice message, information about the file"
      },
      "caption": {
        "type": "String",
        "description": "Optional. Caption for the animation, audio, document, photo, video or voice"
      },
      "caption_entities": {
        "type": "List",
        "description": "Optional. For messages with a caption, special entities like usernames, URLs, bot\ncommands, etc. that appear in the caption"
      },
      "show_caption_above_media": {
        "type": "bool",
        "description": "Optional. True, if the caption must be shown above the message media"
      },
      "has_media_spoiler": {
        "type": "bool",
        "description": "Optional. True, if the message media is covered by a spoiler animation"
      },
      "checklist": {
        "type": "Checklist",
        "description": "Optional. Message is a checklist"
      },
      "contact": {
        "type": "Contact",
        "description": "Optional. Message is a shared contact, information about the contact"
      },
      "dice": {
        "type": "Dice",
        "description": "Optional. Message is a dice with random value"
      },
      "game": {
        "type": "Game",
        "description": "Optional. Message is a game, information about the game. More about games \u00bb"
      },
      "poll": {
        "type": "Poll",
        "description": "Optional. Message is a native poll, information about the poll"
      },
      "venue": {
        "type": "Venue",
        "description": "Optional. Message is a venue, information about the venue. For backward compatibility, when this\nfield is set, the location field will also be set"
      },
      "location": {
        "type": "Location",
        "description": "Optional. Message is a shared location, information about the location"
      },
      "new_chat_members": {
        "type": "List",
        "description": "Optional. New members that were added to the group or supergroup and information about\nthem (the bot itself may be one of these members)"
      },
      "left_chat_member": {
        "type": "User",
        "description": "Optional. A member was removed from the group, information about them (this member may be\nthe bot itself)"
      },
      "new_chat_title": {
        "type": "str",
        "description": "Optional. A chat title was changed to this value"
      },
      "new_chat_photo": {
        "type": "List",
        "description": "Optional. A chat photo was change to this value"
      },
      "delete_chat_photo": {
        "type": "bool",
        "description": "Optional. Service message: the chat photo was deleted"
      },
      "group_chat_created": {
        "type": "bool",
        "description": "Optional. Service message: the group has been created"
      },
      "supergroup_chat_created": {
        "type": "bool",
        "description": "Optional. Service message: the supergroup has been created. This field can't be\nreceived in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can\nonly be found in reply_to_message if someone replies to a very first message in a directly created supergroup."
      },
      "channel_chat_created": {
        "type": "bool",
        "description": "Optional. Service message: the channel has been created. This field can't be\nreceived in a message coming through updates, because bot can't be a member of a channel when it is created. It can only\nbe found in reply_to_message if someone replies to a very first message in a channel."
      },
      "message_auto_delete_timer_changed": {
        "type": "MessageAutoDeleteTimerChanged",
        "description": "Optional. Service message: auto-delete timer settings changed in\nthe chat"
      },
      "migrate_to_chat_id": {
        "type": "int",
        "description": "Optional. The group has been migrated to a supergroup with the specified identifier.\nThis number may have more than 32 significant bits and some programming languages may have difficulty/silent\ndefects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision\nfloat type are safe for storing this identifier."
      },
      "migrate_from_chat_id": {
        "type": "int",
        "description": "Optional. The supergroup has been migrated from a group with the specified\nidentifier. This number may have more than 32 significant bits and some programming languages may have\ndifficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or\ndouble-precision float type are safe for storing this identifier."
      },
      "pinned_message": {
        "type": "Message",
        "description": "Optional. Specified message was pinned. Note that the Message object in this field will not\ncontain further reply_to_message fields even if it is itself a reply."
      },
      "invoice": {
        "type": "Invoice",
        "description": "Optional. Message is an invoice for a payment, information about the invoice. More about payments \u00bb"
      },
      "successful_payment": {
        "type": "SuccessfulPayment",
        "description": "Optional. Message is a service message about a successful payment, information about\nthe payment. More about payments \u00bb"
      },
      "refunded_payment": {
        "type": "RefundedPayment",
        "description": ""
      },
      "users_shared": {
        "type": "UsersShared",
        "description": "Optional. Service message: a user was shared with the bot"
      },
      "chat_shared": {
        "type": "ChatShared",
        "description": "Optional. Service message: a chat was shared with the bot"
      },
      "gift": {
        "type": "GiftInfo",
        "description": "Optional. Service message: a regular gift was sent or received\n:type gift: :class:`tgram.types.GiftInfo`"
      },
      "unique_gift": {
        "type": "UniqueGiftInfo",
        "description": "Optional. Service message: a unique gift was sent or received"
      },
      "connected_website": {
        "type": "str",
        "description": "Optional. The domain name of the website on which the user has logged in. More about\nTelegram Login \u00bb"
      },
      "write_access_allowed": {
        "type": "WriteAccessAllowed",
        "description": "Optional. Service message: the user allowed the bot added to the attachment\nmenu to write messages"
      },
      "passport_data": {
        "type": "PassportData",
        "description": "Optional. Telegram Passport data"
      },
      "proximity_alert_triggered": {
        "type": "ProximityAlertTriggered",
        "description": "Optional. Service message. A user in the chat triggered another user's\nproximity alert while sharing Live Location."
      },
      "boost_added": {
        "type": "ChatBoostAdded",
        "description": "Optional. Service message: user boosted the chat"
      },
      "chat_background_set": {
        "type": "ChatBackground",
        "description": "Optional. Service message: chat background set"
      },
      "checklist_tasks_done": {
        "type": "ChecklistTasksDone",
        "description": "Optional. Service message: some tasks in a checklist were marked as done or not done"
      },
      "checklist_tasks_added": {
        "type": "ChecklistTasksAdded",
        "description": "Optional. Service message: tasks were added to a checklist"
      },
      "direct_message_price_changed": {
        "type": "DirectMessagePriceChanged",
        "description": "Optional. Service message: the price for paid messages in the corresponding direct messages chat of a channel has changed"
      },
      "forum_topic_created": {
        "type": "ForumTopicCreated",
        "description": "Optional. Service message: forum topic created"
      },
      "forum_topic_edited": {
        "type": "ForumTopicEdited",
        "description": "Optional. Service message: forum topic edited"
      },
      "forum_topic_closed": {
        "type": "ForumTopicClosed",
        "description": "Optional. Service message: forum topic closed"
      },
      "forum_topic_reopened": {
        "type": "ForumTopicReopened",
        "description": "Optional. Service message: forum topic reopened"
      },
      "general_forum_topic_hidden": {
        "type": "GeneralForumTopicHidden",
        "description": "Optional. Service message: the 'General' forum topic hidden"
      },
      "general_forum_topic_unhidden": {
        "type": "GeneralForumTopicUnhidden",
        "description": "Optional. Service message: the 'General' forum topic unhidden"
      },
      "giveaway_created": {
        "type": "GiveawayCreated",
        "description": "Optional. Service message: a giveaway has been created"
      },
      "giveaway": {
        "type": "Giveaway",
        "description": "Optional. The message is a scheduled giveaway message"
      },
      "giveaway_winners": {
        "type": "GiveawayWinners",
        "description": "Optional. Service message: giveaway winners(public winners)"
      },
      "giveaway_completed": {
        "type": "GiveawayCompleted",
        "description": "Optional. Service message: giveaway completed, without public winners"
      },
      "paid_message_price_changed": {
        "type": "PaidMessagePriceChanged",
        "description": "Optional. Service message: the price for paid messages has changed in the chat"
      },
      "video_chat_scheduled": {
        "type": "VideoChatScheduled",
        "description": "Optional. Service message: video chat scheduled"
      },
      "video_chat_started": {
        "type": "VideoChatStarted",
        "description": "Optional. Service message: video chat started"
      },
      "video_chat_ended": {
        "type": "VideoChatEnded",
        "description": "Optional. Service message: video chat ended"
      },
      "video_chat_participants_invited": {
        "type": "VideoChatParticipantsInvited",
        "description": "Optional. Service message: new participants invited to a video chat"
      },
      "web_app_data": {
        "type": "WebAppData",
        "description": "Optional. Service message: data sent by a Web App"
      },
      "reply_markup": {
        "type": "InlineKeyboardMarkup",
        "description": "Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons."
      }
    }
  },
  "MessageAutoDeleteTimerChanged": {
    "description": "This object represents a service message about a change in auto-delete timer settings.",
    "properties": {
      "message_auto_delete_time": {
        "type": "int",
        "description": "New auto-delete time for messages in the chat; in seconds"
      }
    }
  },
  "MessageEntity": {
    "description": "This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.",
    "properties": {
      "type": {
        "type": "MessageEntityType",
        "description": "Type of the entity. Currently, can be \u201cmention\u201d (@username), \u201chashtag\u201d (#hashtag), \u201ccashtag\u201d ($USD),\n\u201cbot_command\u201d (/start@jobs_bot),\u201curl\u201d (https://telegram.org), \u201cemail\u201d (do-not-reply@telegram.org), \u201cphone_number\u201d (+1-212-555-0123),\n\u201cbold\u201d (bold text), \u201citalic\u201d (italic text), \u201cunderline\u201d (underlined text), \u201cstrikethrough\u201d (strikethrough text),\n\u201cspoiler\u201d (spoiler message), \u201cblockquote\u201d (block quotation), \u201cexpandable_blockquote\u201d (collapsed-by-default block quotation),\n\u201ccode\u201d (monowidth string), \u201cpre\u201d (monowidth block), \u201ctext_link\u201d (for clickable text URLs),\n\u201ctext_mention\u201d (for users without usernames), \u201ccustom_emoji\u201d (for inline custom emoji stickers)"
      },
      "offset": {
        "type": "int",
        "description": "Offset in UTF-16 code units to the start of the entity"
      },
      "length": {
        "type": "int",
        "description": "Length of the entity in UTF-16 code units"
      },
      "url": {
        "type": "str",
        "description": "Optional. For \u201ctext_link\u201d only, URL that will be opened after user taps on the text"
      },
      "user": {
        "type": "User",
        "description": "Optional. For \u201ctext_mention\u201d only, the mentioned user"
      },
      "language": {
        "type": "str",
        "description": "Optional. For \u201cpre\u201d only, the programming language of the entity text"
      },
      "custom_emoji_id": {
        "type": "str",
        "description": "Optional. For \u201ccustom_emoji\u201d only, unique identifier of the custom emoji.\nUse get_custom_emoji_stickers to get full information about the sticker."
      }
    }
  },
  "MessageId": {
    "description": "",
    "properties": {
      "message_id": {
        "type": "int",
        "description": ""
      }
    }
  },
  "MessageOriginChannel": {
    "description": "The message was originally sent to a channel chat.",
    "properties": {
      "type": {
        "type": "str",
        "description": ""
      },
      "date": {
        "type": "int",
        "description": ""
      },
      "chat": {
        "type": "Chat",
        "description": "Channel chat to which the message was originally sent"
      },
      "message_id": {
        "type": "int",
        "description": "Unique message identifier inside the chat"
      },
      "author_signature": {
        "type": "str",
        "description": "Optional. Signature of the original post author"
      }
    }
  },
  "MessageOriginChat": {
    "description": "The message was originally sent on behalf of a chat to a group chat.",
    "properties": {
      "type": {
        "type": "str",
        "description": ""
      },
      "date": {
        "type": "int",
        "description": ""
      },
      "sender_chat": {
        "type": "Chat",
        "description": "Chat that sent the message originally"
      },
      "author_signature": {
        "type": "str",
        "description": "Optional. For messages originally sent by an anonymous chat administrator, original message author signature"
      }
    }
  },
  "MessageOriginHiddenUser": {
    "description": "The message was originally sent by an unknown user.",
    "properties": {
      "type": {
        "type": "str",
        "description": ""
      },
      "date": {
        "type": "int",
        "description": ""
      },
      "sender_user_name": {
        "type": "str",
        "description": "Name of the user that sent the message originally"
      }
    }
  },
  "MessageOriginUser": {
    "description": "The message was originally sent by a known user.",
    "properties": {
      "type": {
        "type": "str",
        "description": ""
      },
      "date": {
        "type": "int",
        "description": ""
      },
      "sender_user": {
        "type": "User",
        "description": "User that sent the message originally"
      }
    }
  },
  "MessageReactionCountUpdated": {
    "description": "This object represents a service message about a change in the list of the current user's reactions to a message.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "The chat containing the message"
      },
      "message_id": {
        "type": "int",
        "description": "Unique message identifier inside the chat"
      },
      "date": {
        "type": "int",
        "description": "Date of the change in Unix time"
      },
      "reactions": {
        "type": "List",
        "description": "List of reactions that are present on the message"
      }
    }
  },
  "MessageReactionUpdated": {
    "description": "This object represents a service message about a change in the list of the current user's reactions to a message.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "The chat containing the message the user reacted to"
      },
      "message_id": {
        "type": "int",
        "description": "Unique identifier of the message inside the chat"
      },
      "date": {
        "type": "int",
        "description": "Date of the change in Unix time"
      },
      "old_reaction": {
        "type": "List",
        "description": "Previous list of reaction types that were set by the user"
      },
      "new_reaction": {
        "type": "List",
        "description": "New list of reaction types that have been set by the user"
      },
      "user": {
        "type": "User",
        "description": "Optional. The user that changed the reaction, if the user isn't anonymous"
      },
      "actor_chat": {
        "type": "Chat",
        "description": "Optional. The chat on behalf of which the reaction was changed, if the user is anonymous"
      }
    }
  },
  "OrderInfo": {
    "description": "This object represents information about an order.",
    "properties": {
      "name": {
        "type": "str",
        "description": "Optional. User name"
      },
      "phone_number": {
        "type": "str",
        "description": "Optional. User's phone number"
      },
      "email": {
        "type": "str",
        "description": "Optional. User email"
      },
      "shipping_address": {
        "type": "ShippingAddress",
        "description": "Optional. User shipping address"
      }
    }
  },
  "OwnedGiftRegular": {
    "description": "Describes a regular gift owned by a user or a chat.",
    "properties": {
      "gift": {
        "type": "Gift",
        "description": "Information about the regular gift"
      },
      "owned_gift_id": {
        "type": "str",
        "description": "Optional. Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only"
      },
      "sender_user": {
        "type": "User",
        "description": "Optional. Sender of the gift if it is a known user"
      },
      "send_date": {
        "type": "int",
        "description": "Date the gift was sent in Unix time"
      },
      "text": {
        "type": "str",
        "description": "Optional. Text of the message that was added to the gift"
      },
      "entities": {
        "type": "List",
        "description": "Optional. Special entities that appear in the text"
      },
      "is_private": {
        "type": "bool",
        "description": "Optional. True, if the sender and gift text are shown only to the gift receiver"
      },
      "is_saved": {
        "type": "bool",
        "description": "Optional. True, if the gift is displayed on the account's profile page"
      },
      "can_be_upgraded": {
        "type": "bool",
        "description": "Optional. True, if the gift can be upgraded to a unique gift"
      },
      "was_refunded": {
        "type": "bool",
        "description": "Optional. True, if the gift was refunded and isn't available anymore"
      },
      "convert_star_count": {
        "type": "int",
        "description": "Optional. Number of Telegram Stars that can be claimed by the receiver instead of the gift"
      },
      "prepaid_upgrade_star_count": {
        "type": "int",
        "description": "Optional. Number of Telegram Stars that were paid by the sender for the ability to upgrade the gift"
      }
    }
  },
  "OwnedGiftUnique": {
    "description": "Describes a unique gift received and owned by a user or a chat.",
    "properties": {
      "gift": {
        "type": "UniqueGift",
        "description": "Information about the unique gift"
      },
      "owned_gift_id": {
        "type": "str",
        "description": "Optional. Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only"
      },
      "sender_user": {
        "type": "User",
        "description": "Optional. Sender of the gift if it is a known user"
      },
      "send_date": {
        "type": "int",
        "description": "Date the gift was sent in Unix time"
      },
      "is_saved": {
        "type": "bool",
        "description": "Optional. True, if the gift is displayed on the account's profile page"
      },
      "can_be_transferred": {
        "type": "bool",
        "description": "Optional. True, if the gift can be transferred to another owner"
      },
      "transfer_star_count": {
        "type": "int",
        "description": "Optional. Number of Telegram Stars that must be paid to transfer the gift"
      },
      "next_transfer_date": {
        "type": "int",
        "description": ""
      }
    }
  },
  "OwnedGifts": {
    "description": "Contains the list of gifts received and owned by a user or a chat.",
    "properties": {
      "total_count": {
        "type": "int",
        "description": "The total number of gifts owned by the user or the chat"
      },
      "gifts": {
        "type": "List",
        "description": "The list of gifts"
      },
      "next_offset": {
        "type": "str",
        "description": "Optional. Offset for the next request. If empty, then there are no more results"
      }
    }
  },
  "PaidMediaInfo": {
    "description": "Describes the paid media added to a message.",
    "properties": {
      "star_count": {
        "type": "int",
        "description": "The number of Telegram Stars that must be paid to buy access to the media"
      },
      "paid_media": {
        "type": "List",
        "description": "Information about the paid media"
      }
    }
  },
  "PaidMediaPhoto": {
    "description": "The paid media is a photo.",
    "properties": {
      "photo": {
        "type": "List",
        "description": "The photo"
      }
    }
  },
  "PaidMediaPreview": {
    "description": "The paid media isn't available before the payment.",
    "properties": {
      "width": {
        "type": "int",
        "description": "Optional. Media width as defined by the sender"
      },
      "height": {
        "type": "int",
        "description": "Optional. Media height as defined by the sender"
      },
      "duration": {
        "type": "int",
        "description": "Optional. Duration of the media in seconds as defined by the sender"
      }
    }
  },
  "PaidMediaPurchased": {
    "description": "This object contains information about a paid media purchase.",
    "properties": {
      "from_user": {
        "type": "User",
        "description": "User who purchased the media"
      },
      "paid_media_payload": {
        "type": "str",
        "description": "Bot-specified paid media payload"
      }
    }
  },
  "PaidMediaVideo": {
    "description": "The paid media is a video.",
    "properties": {
      "video": {
        "type": "Video",
        "description": "The video"
      }
    }
  },
  "PaidMessagePriceChanged": {
    "description": "Describes a service message about a change in the price of paid messages within a chat.",
    "properties": {
      "paid_message_star_count": {
        "type": "int",
        "description": "The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message"
      }
    }
  },
  "PassportData": {
    "description": "",
    "properties": {
      "data": {
        "type": "List",
        "description": ""
      },
      "credentials": {
        "type": "EncryptedCredentials",
        "description": ""
      }
    }
  },
  "PassportElementError": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "field_name": {
        "type": "str",
        "description": ""
      },
      "data_hash": {
        "type": "str",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorDataField": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "field_name": {
        "type": "str",
        "description": ""
      },
      "data_hash": {
        "type": "str",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorFile": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "file_hash": {
        "type": "str",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorFiles": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "file_hashes": {
        "type": "List",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorFrontSide": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "file_hash": {
        "type": "str",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorReverseSide": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "file_hash": {
        "type": "str",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorSelfie": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "file_hash": {
        "type": "str",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorTranslationFile": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "file_hash": {
        "type": "str",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorTranslationFiles": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "file_hashes": {
        "type": "List",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportElementErrorUnspecified": {
    "description": "",
    "properties": {
      "source": {
        "type": "str",
        "description": ""
      },
      "type": {
        "type": "str",
        "description": ""
      },
      "element_hash": {
        "type": "str",
        "description": ""
      },
      "message": {
        "type": "str",
        "description": ""
      }
    }
  },
  "PassportFile": {
    "description": "",
    "properties": {
      "file_id": {
        "type": "str",
        "description": ""
      },
      "file_unique_id": {
        "type": "str",
        "description": ""
      },
      "file_size": {
        "type": "int",
        "description": ""
      },
      "file_date": {
        "type": "int",
        "description": ""
      }
    }
  },
  "PhotoSize": {
    "description": "This object represents one size of a photo or a file / sticker thumbnail.",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "width": {
        "type": "int",
        "description": "Photo width"
      },
      "height": {
        "type": "int",
        "description": "Photo height"
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes"
      }
    }
  },
  "Poll": {
    "description": "This object contains information about a poll.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique poll identifier"
      },
      "question": {
        "type": "String",
        "description": "Poll question, 1-300 characters"
      },
      "options": {
        "type": "List",
        "description": "List of poll options"
      },
      "total_voter_count": {
        "type": "int",
        "description": "Total number of users that voted in the poll"
      },
      "is_closed": {
        "type": "bool",
        "description": "True, if the poll is closed"
      },
      "is_anonymous": {
        "type": "bool",
        "description": "True, if the poll is anonymous"
      },
      "type": {
        "type": "str",
        "description": "Poll type, currently can be \u201cregular\u201d or \u201cquiz\u201d"
      },
      "allows_multiple_answers": {
        "type": "bool",
        "description": "True, if the poll allows multiple answers"
      },
      "question_entities": {
        "type": "List",
        "description": "Optional. Special entities that appear in the question. Currently, only custom emoji entities are allowed in poll questions"
      },
      "correct_option_id": {
        "type": "int",
        "description": "Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot."
      },
      "explanation": {
        "type": "String",
        "description": "Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters"
      },
      "explanation_entities": {
        "type": "List",
        "description": "Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation"
      },
      "open_period": {
        "type": "int",
        "description": "Optional. Amount of time in seconds the poll will be active after creation"
      },
      "close_date": {
        "type": "int",
        "description": "Optional. Point in time (Unix timestamp) when the poll will be automatically closed"
      }
    }
  },
  "PollAnswer": {
    "description": "This object represents an answer of a user in a non-anonymous poll.",
    "properties": {
      "poll_id": {
        "type": "str",
        "description": "Unique poll identifier"
      },
      "option_ids": {
        "type": "List",
        "description": "0-based identifiers of answer options, chosen by the user. May be empty if the user retracted\ntheir vote."
      },
      "voter_chat": {
        "type": "Chat",
        "description": "Optional. The chat that changed the answer to the poll, if the voter is anonymous"
      },
      "user": {
        "type": "User",
        "description": "Optional. The user, who changed the answer to the poll"
      }
    }
  },
  "PollOption": {
    "description": "This object contains information about one answer option in a poll.",
    "properties": {
      "text": {
        "type": "String",
        "description": "Option text, 1-100 characters"
      },
      "voter_count": {
        "type": "int",
        "description": "Number of users that voted for this option"
      },
      "text_entities": {
        "type": "List",
        "description": "Optional. Special entities that appear in the option text. Currently, only custom emoji entities are allowed in poll option texts"
      }
    }
  },
  "PreCheckoutQuery": {
    "description": "This object contains information about an incoming pre-checkout query.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique query identifier"
      },
      "from_user": {
        "type": "User",
        "description": ""
      },
      "currency": {
        "type": "str",
        "description": "Three-letter ISO 4217 currency code"
      },
      "total_amount": {
        "type": "int",
        "description": "Total price in the smallest units of the currency (integer, not float/double). For example,\nfor a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past\nthe decimal point for each currency (2 for the majority of currencies)."
      },
      "invoice_payload": {
        "type": "str",
        "description": "Bot specified invoice payload"
      },
      "shipping_option_id": {
        "type": "str",
        "description": "Optional. Identifier of the shipping option chosen by the user"
      },
      "order_info": {
        "type": "OrderInfo",
        "description": "Optional. Order information provided by the user"
      }
    }
  },
  "PreparedInlineMessage": {
    "description": "Describes an inline message to be sent by a user of a Mini App.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique identifier of the prepared message"
      },
      "expiration_date": {
        "type": "int",
        "description": "Expiration date of the prepared message, in Unix time.\nExpired prepared messages can no longer be used"
      }
    }
  },
  "ProximityAlertTriggered": {
    "description": "This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.",
    "properties": {
      "traveler": {
        "type": "User",
        "description": "User that triggered the alert"
      },
      "watcher": {
        "type": "User",
        "description": "User that set the alert"
      },
      "distance": {
        "type": "int",
        "description": "The distance between the users"
      }
    }
  },
  "ReactionCount": {
    "description": "This object represents a reaction added to a message along with the number of times it was added.",
    "properties": {
      "type": {
        "type": "ReactionType",
        "description": "Type of the reaction"
      },
      "total_count": {
        "type": "int",
        "description": "Number of times the reaction was added"
      }
    }
  },
  "ReactionTypeCustomEmoji": {
    "description": "This object represents a custom emoji reaction type.",
    "properties": {
      "custom_emoji_id": {
        "type": "str",
        "description": "Identifier of the custom emoji"
      }
    }
  },
  "ReactionTypeEmoji": {
    "description": "This object represents an emoji reaction type.",
    "properties": {
      "emoji": {
        "type": "str",
        "description": "Reaction emoji. List is available on the API doc."
      }
    }
  },
  "ReactionTypePaid": {
    "description": "The reaction is paid.",
    "properties": {}
  },
  "RefundedPayment": {
    "description": "",
    "properties": {
      "currency": {
        "type": "str",
        "description": ""
      },
      "total_amount": {
        "type": "int",
        "description": ""
      },
      "invoice_payload": {
        "type": "str",
        "description": ""
      },
      "telegram_payment_charge_id": {
        "type": "str",
        "description": ""
      },
      "provider_payment_charge_id": {
        "type": "str",
        "description": ""
      }
    }
  },
  "ReplyKeyboardMarkup": {
    "description": "This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).",
    "properties": {
      "keyboard": {
        "type": "List",
        "description": ":obj:`list` of button rows, each represented by an :obj:`list` of\n:class:`tgram.types.KeyboardButton` or :obj:`str` objects"
      },
      "is_persistent": {
        "type": "bool",
        "description": "Optional. Use this parameter if you want to show the keyboard to specific users only.\nTargets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a\nreply (has reply_to_message_id), sender of the original message.\n\nExample: A user requests to change the bot's language, bot replies to the request with a keyboard to\nselect the new language. Other users in the group don't see the keyboard."
      },
      "resize_keyboard": {
        "type": "bool",
        "description": "Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make\nthe keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is\nalways of the same height as the app's standard keyboard."
      },
      "one_time_keyboard": {
        "type": "bool",
        "description": "Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard\nwill still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can\npress a special button in the input field to see the custom keyboard again. Defaults to false."
      },
      "input_field_placeholder": {
        "type": "str",
        "description": "Optional. The placeholder to be shown in the input field when the keyboard is\nactive; 1-64 characters"
      },
      "selective": {
        "type": "bool",
        "description": "Optional. Use this parameter if you want to show the keyboard to specific users only. Targets:\n1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message\nin the same chat and forum topic, sender of the original message. Example: A user requests to change the bot's\nlanguage, bot replies to the request with a keyboard to select the new language. Other users in the group don't\nsee the keyboard."
      }
    }
  },
  "ReplyKeyboardRemove": {
    "description": "Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).",
    "properties": {
      "selective": {
        "type": "bool",
        "description": "Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets:\n1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has\nreply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation\nmessage in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options\nto users who haven't voted yet."
      }
    }
  },
  "ReplyParameters": {
    "description": "Describes reply parameters for the message that is being sent.",
    "properties": {
      "message_id": {
        "type": "int",
        "description": "Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified"
      },
      "chat_id": {
        "type": "Union",
        "description": "Optional. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername)"
      },
      "allow_sending_without_reply": {
        "type": "bool",
        "description": "Optional. Pass True if the message should be sent even if the specified message to be replied to is not found; can be used only for replies in the same chat and forum topic."
      },
      "quote": {
        "type": "str",
        "description": "Optional. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold, italic, underline, strikethrough, spoiler, and custom_emoji entities. The message will fail to send if the quote isn't found in the original message."
      },
      "quote_parse_mode": {
        "type": "str",
        "description": "Optional. Mode for parsing entities in the quote. See formatting options for more details."
      },
      "quote_entities": {
        "type": "List",
        "description": "Optional. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of quote_parse_mode."
      },
      "quote_position": {
        "type": "int",
        "description": "Optional. Position of the quote in the original message in UTF-16 code units"
      }
    }
  },
  "ResponseParameters": {
    "description": "",
    "properties": {
      "migrate_to_chat_id": {
        "type": "int",
        "description": ""
      },
      "retry_after": {
        "type": "int",
        "description": ""
      }
    }
  },
  "RevenueWithdrawalStateFailed": {
    "description": "The withdrawal failed and the transaction was refunded.",
    "properties": {}
  },
  "RevenueWithdrawalStatePending": {
    "description": "The withdrawal is in progress.",
    "properties": {}
  },
  "RevenueWithdrawalStateSucceeded": {
    "description": "The withdrawal succeeded.",
    "properties": {
      "date": {
        "type": "int",
        "description": "Date the withdrawal was completed in Unix time"
      },
      "url": {
        "type": "str",
        "description": "An HTTPS URL that can be used to see transaction details"
      }
    }
  },
  "SentWebAppMessage": {
    "description": "Describes an inline message sent by a Web App on behalf of a user.",
    "properties": {
      "inline_message_id": {
        "type": "str",
        "description": "Optional. Identifier of the sent inline message. Available only if there is an inline\nkeyboard attached to the message."
      }
    }
  },
  "SharedUser": {
    "description": "This object contains information about a user that was shared with the bot using a KeyboardButtonRequestUser button.",
    "properties": {
      "user_id": {
        "type": "int",
        "description": "Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means."
      },
      "first_name": {
        "type": "str",
        "description": "Optional. First name of the user, if the name was requested by the bot"
      },
      "last_name": {
        "type": "str",
        "description": "Optional. Last name of the user, if the name was requested by the bot"
      },
      "username": {
        "type": "str",
        "description": "Optional. Username of the user, if the username was requested by the bot"
      },
      "photo": {
        "type": "List",
        "description": "Optional. Available sizes of the chat photo, if the photo was requested by the bot"
      }
    }
  },
  "ShippingAddress": {
    "description": "This object represents a shipping address.",
    "properties": {
      "country_code": {
        "type": "str",
        "description": "Two-letter ISO 3166-1 alpha-2 country code"
      },
      "state": {
        "type": "str",
        "description": "State, if applicable"
      },
      "city": {
        "type": "str",
        "description": "City"
      },
      "street_line1": {
        "type": "str",
        "description": "First line for the address"
      },
      "street_line2": {
        "type": "str",
        "description": "Second line for the address"
      },
      "post_code": {
        "type": "str",
        "description": "Address post code"
      }
    }
  },
  "ShippingOption": {
    "description": "This object represents one shipping option.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Shipping option identifier"
      },
      "title": {
        "type": "str",
        "description": "Option title"
      },
      "prices": {
        "type": "List",
        "description": "List of price portions"
      }
    }
  },
  "ShippingQuery": {
    "description": "This object contains information about an incoming shipping query.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique query identifier"
      },
      "from_user": {
        "type": "User",
        "description": ""
      },
      "invoice_payload": {
        "type": "str",
        "description": "Bot specified invoice payload"
      },
      "shipping_address": {
        "type": "ShippingAddress",
        "description": "User specified shipping address"
      }
    }
  },
  "StarAmount": {
    "description": "Describes an amount of Telegram Stars.",
    "properties": {
      "amount": {
        "type": "int",
        "description": "Integer amount of Telegram Stars, rounded to 0; can be negative"
      },
      "nanostar_amount": {
        "type": "int",
        "description": "Optional. The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999; can be negative if and only if amount is non-positive"
      }
    }
  },
  "StarTransaction": {
    "description": "Describes a Telegram Star transaction.",
    "properties": {
      "id": {
        "type": "str",
        "description": "Unique identifier of the transaction. Coincides with the identifer of the original transaction for refund transactions. Coincides with SuccessfulPayment.telegram_payment_charge_id for successful incoming payments from users."
      },
      "amount": {
        "type": "int",
        "description": "Number of Telegram Stars transferred by the transaction"
      },
      "nanostar_amount": {
        "type": "int",
        "description": "Optional. The number of 1/1000000000 shares of Telegram Stars transferred by the transaction; from 0 to 999999999"
      },
      "date": {
        "type": "int",
        "description": "Date the transaction was created in Unix time"
      },
      "source": {
        "type": "TransactionPartner",
        "description": "Optional. Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions"
      },
      "receiver": {
        "type": "TransactionPartner",
        "description": "Optional. Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions"
      }
    }
  },
  "StarTransactions": {
    "description": "Contains a list of Telegram Star transactions.",
    "properties": {
      "transactions": {
        "type": "List",
        "description": "The list of transactions"
      }
    }
  },
  "Sticker": {
    "description": "This object represents a sticker.",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "type": {
        "type": "str",
        "description": "Type of the sticker, currently one of \u201cregular\u201d, \u201cmask\u201d, \u201ccustom_emoji\u201d. The type of the sticker is\nindependent from its format, which is determined by the fields is_animated and is_video."
      },
      "width": {
        "type": "int",
        "description": "Sticker width"
      },
      "height": {
        "type": "int",
        "description": "Sticker height"
      },
      "is_animated": {
        "type": "bool",
        "description": "True, if the sticker is animated"
      },
      "is_video": {
        "type": "bool",
        "description": "True, if the sticker is a video sticker"
      },
      "thumbnail": {
        "type": "PhotoSize",
        "description": "Optional. Sticker thumbnail in the .WEBP or .JPG format"
      },
      "emoji": {
        "type": "str",
        "description": "Optional. Emoji associated with the sticker"
      },
      "set_name": {
        "type": "str",
        "description": "Optional. Name of the sticker set to which the sticker belongs"
      },
      "premium_animation": {
        "type": "File",
        "description": "Optional. Premium animation for the sticker, if the sticker is premium"
      },
      "mask_position": {
        "type": "MaskPosition",
        "description": "Optional. For mask stickers, the position where the mask should be placed"
      },
      "custom_emoji_id": {
        "type": "str",
        "description": "Optional. For custom emoji stickers, unique identifier of the custom emoji"
      },
      "needs_repainting": {
        "type": "bool",
        "description": "Optional. True, if the sticker must be repainted to a text color in messages,\nthe color of the Telegram Premium badge in emoji status, white color on chat photos, or another\nappropriate color in other places"
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes"
      }
    }
  },
  "StickerSet": {
    "description": "This object represents a sticker set.",
    "properties": {
      "name": {
        "type": "str",
        "description": "Sticker set name"
      },
      "title": {
        "type": "str",
        "description": "Sticker set title"
      },
      "sticker_type": {
        "type": "str",
        "description": "Type of stickers in the set, currently one of \u201cregular\u201d, \u201cmask\u201d, \u201ccustom_emoji\u201d"
      },
      "stickers": {
        "type": "List",
        "description": "List of all set stickers"
      },
      "thumbnail": {
        "type": "PhotoSize",
        "description": "Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format"
      }
    }
  },
  "Story": {
    "description": "This object represents a story.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "Chat that posted the story"
      },
      "id": {
        "type": "int",
        "description": "Unique identifier for the story in the chat"
      }
    }
  },
  "StoryArea": {
    "description": "Describes a clickable area on a story media.",
    "properties": {
      "position": {
        "type": "StoryAreaPosition",
        "description": "Position of the area"
      },
      "type": {
        "type": "StoryAreaType",
        "description": "Type of the area"
      }
    }
  },
  "StoryAreaPosition": {
    "description": "Describes the position of a clickable area within a story.",
    "properties": {
      "x_percentage": {
        "type": "float",
        "description": "The abscissa of the area's center, as a percentage of the media width"
      },
      "y_percentage": {
        "type": "float",
        "description": "The ordinate of the area's center, as a percentage of the media height"
      },
      "width_percentage": {
        "type": "float",
        "description": "The width of the area's rectangle, as a percentage of the media width"
      },
      "height_percentage": {
        "type": "float",
        "description": "The height of the area's rectangle, as a percentage of the media height"
      },
      "rotation_angle": {
        "type": "float",
        "description": "The clockwise rotation angle of the rectangle, in degrees; 0-360"
      },
      "corner_radius_percentage": {
        "type": "float",
        "description": "The radius of the rectangle corner rounding, as a percentage of the media width"
      }
    }
  },
  "StoryAreaTypeLink": {
    "description": "Describes a story area pointing to an HTTP or tg:// link.",
    "properties": {
      "url": {
        "type": "str",
        "description": "HTTP or tg:// URL to be opened when the area is clicked"
      }
    }
  },
  "StoryAreaTypeLocation": {
    "description": "Describes a story area pointing to a location.",
    "properties": {
      "latitude": {
        "type": "float",
        "description": "Location latitude in degrees"
      },
      "longitude": {
        "type": "float",
        "description": "Location longitude in degrees"
      },
      "address": {
        "type": "LocationAddress",
        "description": "Optional. Address of the location"
      }
    }
  },
  "StoryAreaTypeSuggestedReaction": {
    "description": "Describes a story area pointing to a suggested reaction.",
    "properties": {
      "reaction_type": {
        "type": "ReactionType",
        "description": "Type of the reaction"
      },
      "is_dark": {
        "type": "bool",
        "description": "Optional. Pass True if the reaction area has a dark background"
      },
      "is_flipped": {
        "type": "bool",
        "description": "Optional. Pass True if reaction area corner is flipped"
      }
    }
  },
  "StoryAreaTypeUniqueGift": {
    "description": "Describes a story area pointing to a unique gift.",
    "properties": {
      "name": {
        "type": "str",
        "description": "Unique name of the gift"
      }
    }
  },
  "StoryAreaTypeWeather": {
    "description": "Describes a story area containing weather information.",
    "properties": {
      "temperature": {
        "type": "float",
        "description": "Temperature, in degree Celsius"
      },
      "emoji": {
        "type": "str",
        "description": "Emoji representing the weather"
      },
      "background_color": {
        "type": "int",
        "description": "A color of the area background in the ARGB format"
      }
    }
  },
  "SuccessfulPayment": {
    "description": "This object contains basic information about a successful payment.",
    "properties": {
      "currency": {
        "type": "str",
        "description": "Three-letter ISO 4217 currency code"
      },
      "total_amount": {
        "type": "int",
        "description": "Total price in the smallest units of the currency (integer, not float/double). For example,\nfor a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past\nthe decimal point for each currency (2 for the majority of currencies)."
      },
      "invoice_payload": {
        "type": "str",
        "description": "Bot specified invoice payload"
      },
      "subscription_expiration_date": {
        "type": "int",
        "description": ""
      },
      "is_recurring": {
        "type": "bool",
        "description": ""
      },
      "is_first_recurring": {
        "type": "bool",
        "description": ""
      },
      "telegram_payment_charge_id": {
        "type": "str",
        "description": "Telegram payment identifier"
      },
      "provider_payment_charge_id": {
        "type": "str",
        "description": "Provider payment identifier"
      },
      "shipping_option_id": {
        "type": "str",
        "description": "Optional. Identifier of the shipping option chosen by the user"
      },
      "order_info": {
        "type": "OrderInfo",
        "description": "Optional. Order information provided by the user"
      }
    }
  },
  "SwitchInlineQueryChosenChat": {
    "description": "Represents an inline button that switches the current user to inline mode in a chosen chat,",
    "properties": {
      "query": {
        "type": "str",
        "description": "Optional. The default inline query to be inserted in the input field.\nIf left empty, only the bot's username will be inserted"
      },
      "allow_user_chats": {
        "type": "bool",
        "description": "Optional. True, if private chats with users can be chosen"
      },
      "allow_bot_chats": {
        "type": "bool",
        "description": "Optional. True, if private chats with bots can be chosen"
      },
      "allow_group_chats": {
        "type": "bool",
        "description": "Optional. True, if group and supergroup chats can be chosen"
      },
      "allow_channel_chats": {
        "type": "bool",
        "description": "Optional. True, if channel chats can be chosen"
      }
    }
  },
  "TextQuote": {
    "description": "This object contains information about the quoted part of a message that is replied to by the given message.",
    "properties": {
      "text": {
        "type": "String",
        "description": "Text of the quoted part of a message that is replied to by the given message"
      },
      "position": {
        "type": "int",
        "description": "Approximate quote position in the original message in UTF-16 code units as specified by the sender"
      },
      "entities": {
        "type": "List",
        "description": "Optional. Special entities that appear in the quote. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes."
      },
      "is_manual": {
        "type": "bool",
        "description": "Optional. True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server."
      }
    }
  },
  "TransactionPartnerAffiliateProgram": {
    "description": "Describes the affiliate program that issued the affiliate commission received via this transaction.",
    "properties": {
      "sponsor_user": {
        "type": "User",
        "description": "Optional. Information about the bot that sponsored the affiliate program"
      },
      "commission_per_mille": {
        "type": "int",
        "description": "The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users"
      }
    }
  },
  "TransactionPartnerChat": {
    "description": "Describes a transaction with a chat.",
    "properties": {
      "chat": {
        "type": "Chat",
        "description": "Information about the chat"
      },
      "gift": {
        "type": "Gift",
        "description": "Optional. The gift sent to the chat by the bot"
      }
    }
  },
  "TransactionPartnerFragment": {
    "description": "Describes a withdrawal transaction with Fragment.",
    "properties": {
      "withdrawal_state": {
        "type": "RevenueWithdrawalState",
        "description": "Optional. State of the transaction if the transaction is outgoing"
      }
    }
  },
  "TransactionPartnerOther": {
    "description": "Describes a transaction with an unknown source or recipient.",
    "properties": {}
  },
  "TransactionPartnerTelegramAds": {
    "description": "",
    "properties": {}
  },
  "TransactionPartnerTelegramApi": {
    "description": "",
    "properties": {
      "request_count": {
        "type": "int",
        "description": ""
      }
    }
  },
  "TransactionPartnerUser": {
    "description": "Describes a transaction with a user.",
    "properties": {
      "user": {
        "type": "User",
        "description": "Information about the user"
      },
      "transaction_type": {
        "type": "str",
        "description": "Type of the transaction, currently one of \u201cinvoice_payment\u201d, \u201cpaid_media_payment\u201d, \u201cgift_purchase\u201d, \u201cpremium_purchase\u201d, \u201cbusiness_account_transfer\u201d"
      },
      "affiliate": {
        "type": "AffiliateInfo",
        "description": "Optional. Information about the affiliate that received a commission via this transaction. Can be available only for \u201cinvoice_payment\u201d and \u201cpaid_media_payment\u201d transactions."
      },
      "invoice_payload": {
        "type": "str",
        "description": "Optional. Bot-specified invoice payload. Can be available only for \u201cinvoice_payment\u201d transactions."
      },
      "subscription_period": {
        "type": "int",
        "description": "Optional. The duration of the paid subscription. Can be available only for \u201cinvoice_payment\u201d transactions."
      },
      "paid_media": {
        "type": "List",
        "description": "Optional. Information about the paid media bought by the user; for \u201cpaid_media_payment\u201d transactions only"
      },
      "paid_media_payload": {
        "type": "str",
        "description": "Optional. Bot-specified paid media payload. Can be available only for \u201cpaid_media_payment\u201d transactions."
      },
      "gift": {
        "type": "Gift",
        "description": "Optional. The gift sent to the user by the bot; for \u201cgift_purchase\u201d transactions only"
      },
      "premium_subscription_duration": {
        "type": "int",
        "description": "Optional. Number of months the gifted Telegram Premium subscription will be active for; for \u201cpremium_purchase\u201d transactions only"
      }
    }
  },
  "UniqueGift": {
    "description": "This object describes a unique gift that was upgraded from a regular gift.",
    "properties": {
      "base_name": {
        "type": "str",
        "description": "Human-readable name of the regular gift from which this unique gift was upgraded"
      },
      "name": {
        "type": "str",
        "description": "Unique name of the gift. This name can be used in https://t.me/nft/... links and story areas"
      },
      "number": {
        "type": "int",
        "description": "Unique number of the upgraded gift among gifts upgraded from the same regular gift"
      },
      "model": {
        "type": "UniqueGiftModel",
        "description": "Model of the gift"
      },
      "symbol": {
        "type": "UniqueGiftSymbol",
        "description": "Symbol of the gift"
      },
      "backdrop": {
        "type": "UniqueGiftBackdrop",
        "description": "Backdrop of the gift"
      }
    }
  },
  "UniqueGiftBackdrop": {
    "description": "This object describes the backdrop of a unique gift.",
    "properties": {
      "name": {
        "type": "str",
        "description": "Name of the backdrop"
      },
      "colors": {
        "type": "UniqueGiftBackdropColors",
        "description": "Colors of the backdrop"
      },
      "rarity_per_mille": {
        "type": "int",
        "description": "The number of unique gifts that receive this backdrop for every 1000 gifts upgraded"
      }
    }
  },
  "UniqueGiftBackdropColors": {
    "description": "This object describes the colors of the backdrop of a unique gift.",
    "properties": {
      "center_color": {
        "type": "int",
        "description": "The color in the center of the backdrop in RGB format"
      },
      "edge_color": {
        "type": "int",
        "description": "The color on the edges of the backdrop in RGB format"
      },
      "symbol_color": {
        "type": "int",
        "description": "The color to be applied to the symbol in RGB format"
      },
      "text_color": {
        "type": "int",
        "description": "The color for the text on the backdrop in RGB format"
      }
    }
  },
  "UniqueGiftInfo": {
    "description": "Describes a service message about a unique gift that was sent or received.",
    "properties": {
      "gift": {
        "type": "UniqueGift",
        "description": "Information about the gift"
      },
      "origin": {
        "type": "str",
        "description": "Origin of the gift. Currently, either \u201cupgrade\u201d for gifts upgraded from regular gifts, \u201ctransfer\u201d for gifts transferred from other users or channels, or \u201cresale\u201d for gifts bought from other users"
      },
      "last_resale_star_count": {
        "type": "int",
        "description": ""
      },
      "owned_gift_id": {
        "type": "str",
        "description": "Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts"
      },
      "transfer_star_count": {
        "type": "int",
        "description": "Optional. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift"
      },
      "next_transfer_date": {
        "type": "int",
        "description": ""
      }
    }
  },
  "UniqueGiftModel": {
    "description": "This object describes the model of a unique gift.",
    "properties": {
      "name": {
        "type": "str",
        "description": "Name of the model"
      },
      "sticker": {
        "type": "Sticker",
        "description": "The sticker that represents the unique gift"
      },
      "rarity_per_mille": {
        "type": "int",
        "description": "The number of unique gifts that receive this model for every 1000 gifts upgraded"
      }
    }
  },
  "UniqueGiftSymbol": {
    "description": "This object describes the symbol shown on the pattern of a unique gift.",
    "properties": {
      "name": {
        "type": "str",
        "description": "Name of the symbol"
      },
      "sticker": {
        "type": "Sticker",
        "description": "The sticker that represents the unique gift"
      },
      "rarity_per_mille": {
        "type": "int",
        "description": "The number of unique gifts that receive this model for every 1000 gifts upgraded"
      }
    }
  },
  "Update": {
    "description": "This object represents an incoming update.At most one of the optional parameters can be present in any given update.",
    "properties": {
      "update_id": {
        "type": "int",
        "description": "The update's unique identifier. Update identifiers start from a certain positive number and\nincrease sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore\nrepeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates\nfor at least a week, then identifier of the next update will be chosen randomly instead of sequentially."
      },
      "message": {
        "type": "Message",
        "description": "Optional. New incoming message of any kind - text, photo, sticker, etc."
      },
      "edited_message": {
        "type": "Message",
        "description": "Optional. New version of a message that is known to the bot and was edited"
      },
      "channel_post": {
        "type": "Message",
        "description": "Optional. New incoming channel post of any kind - text, photo, sticker, etc."
      },
      "edited_channel_post": {
        "type": "Message",
        "description": "Optional. New version of a channel post that is known to the bot and was edited"
      },
      "business_connection": {
        "type": "BusinessConnection",
        "description": "Optional. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot"
      },
      "business_message": {
        "type": "Message",
        "description": "Optional. New non-service message from a connected business account"
      },
      "edited_business_message": {
        "type": "Message",
        "description": "Optional. New version of a non-service message from a connected business account that is known to the bot and was edited"
      },
      "deleted_business_messages": {
        "type": "BusinessMessagesDeleted",
        "description": "Optional. Service message: the chat connected to the business account was deleted"
      },
      "message_reaction": {
        "type": "MessageReactionUpdated",
        "description": "Optional. A reaction to a message was changed by a user. The bot must be an administrator in the chat\nand must explicitly specify \"message_reaction\" in the list of allowed_updates to receive these updates. The update isn't received for reactions set by bots."
      },
      "message_reaction_count": {
        "type": "MessageReactionCountUpdated",
        "description": "Optional. Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify\n\"message_reaction_count\" in the list of allowed_updates to receive these updates."
      },
      "inline_query": {
        "type": "InlineQuery",
        "description": "Optional. New incoming inline query"
      },
      "chosen_inline_result": {
        "type": "ChosenInlineResult",
        "description": "Optional. The result of an inline query that was chosen by a user and sent to their chat\npartner. Please see our documentation on the feedback collecting for details on how to enable these updates for your\nbot."
      },
      "callback_query": {
        "type": "CallbackQuery",
        "description": "Optional. New incoming callback query"
      },
      "shipping_query": {
        "type": "ShippingQuery",
        "description": "Optional. New incoming shipping query. Only for invoices with flexible price"
      },
      "pre_checkout_query": {
        "type": "PreCheckoutQuery",
        "description": "Optional. New incoming pre-checkout query. Contains full information about\ncheckout"
      },
      "purchased_paid_media": {
        "type": "PaidMediaPurchased",
        "description": "Optional. A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat"
      },
      "poll": {
        "type": "Poll",
        "description": "Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the\nbot"
      },
      "poll_answer": {
        "type": "PollAnswer",
        "description": "Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in\npolls that were sent by the bot itself."
      },
      "my_chat_member": {
        "type": "ChatMemberUpdated",
        "description": "Optional. The bot's chat member status was updated in a chat. For private chats, this update\nis received only when the bot is blocked or unblocked by the user."
      },
      "chat_member": {
        "type": "ChatMemberUpdated",
        "description": "Optional. A chat member's status was updated in a chat. The bot must be an administrator in the\nchat and must explicitly specify \u201cchat_member\u201d in the list of allowed_updates to receive these updates."
      },
      "chat_join_request": {
        "type": "ChatJoinRequest",
        "description": "Optional. A request to join the chat has been sent. The bot must have the\ncan_invite_users administrator right in the chat to receive these updates."
      },
      "chat_boost": {
        "type": "ChatBoostUpdated",
        "description": "Optional. A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates."
      },
      "removed_chat_boost": {
        "type": "ChatBoostRemoved",
        "description": "Optional. A chat boost was removed. The bot must be an administrator in the chat to receive these updates."
      }
    }
  },
  "User": {
    "description": "This object represents a Telegram user or bot.",
    "properties": {
      "id": {
        "type": "int",
        "description": "Unique identifier for this user or bot. This number may have more than 32 significant bits and some\nprogramming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant\nbits, so a 64-bit integer or double-precision float type are safe for storing this identifier."
      },
      "is_bot": {
        "type": "bool",
        "description": "True, if this user is a bot"
      },
      "first_name": {
        "type": "str",
        "description": "User's or bot's first name"
      },
      "last_name": {
        "type": "str",
        "description": "Optional. User's or bot's last name"
      },
      "username": {
        "type": "str",
        "description": "Optional. User's or bot's username"
      },
      "language_code": {
        "type": "str",
        "description": "Optional. IETF language tag of the user's language"
      },
      "is_premium": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if this user is a Telegram Premium user"
      },
      "added_to_attachment_menu": {
        "type": "bool",
        "description": "Optional. :obj:`bool`, if this user added the bot to the attachment menu"
      },
      "can_join_groups": {
        "type": "bool",
        "description": "Optional. True, if the bot can be invited to groups. Returned only in getMe."
      },
      "can_read_all_group_messages": {
        "type": "bool",
        "description": "Optional. True, if privacy mode is disabled for the bot. Returned only in\ngetMe."
      },
      "supports_inline_queries": {
        "type": "bool",
        "description": "Optional. True, if the bot supports inline queries. Returned only in getMe."
      },
      "can_connect_to_business": {
        "type": "bool",
        "description": "Optional. True, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in getMe."
      },
      "has_main_web_app": {
        "type": "bool",
        "description": "Optional. True, if the bot has a main Web App. Returned only in getMe."
      }
    }
  },
  "UserChatBoosts": {
    "description": "This object represents a list of boosts added to a chat by a user.",
    "properties": {
      "boosts": {
        "type": "List",
        "description": "The list of boosts added to the chat by the user"
      }
    }
  },
  "UserProfilePhotos": {
    "description": "This object represent a user's profile pictures.",
    "properties": {
      "total_count": {
        "type": "int",
        "description": "Total number of profile pictures the target user has"
      },
      "photos": {
        "type": "List",
        "description": "Requested profile pictures (in up to 4 sizes each)"
      }
    }
  },
  "UsersShared": {
    "description": "This object contains information about the users whose identifiers were shared with the bot",
    "properties": {
      "request_id": {
        "type": "int",
        "description": "Identifier of the request"
      },
      "users": {
        "type": "List",
        "description": "Information about users shared with the bot"
      }
    }
  },
  "Venue": {
    "description": "This object represents a venue.",
    "properties": {
      "location": {
        "type": "Location",
        "description": "Venue location. Can't be a live location"
      },
      "title": {
        "type": "str",
        "description": "Name of the venue"
      },
      "address": {
        "type": "str",
        "description": "Address of the venue"
      },
      "foursquare_id": {
        "type": "str",
        "description": "Optional. Foursquare identifier of the venue"
      },
      "foursquare_type": {
        "type": "str",
        "description": "Optional. Foursquare type of the venue. (For example, \u201carts_entertainment/default\u201d,\n\u201carts_entertainment/aquarium\u201d or \u201cfood/icecream\u201d.)"
      },
      "google_place_id": {
        "type": "str",
        "description": "Optional. Google Places identifier of the venue"
      },
      "google_place_type": {
        "type": "str",
        "description": "Optional. Google Places type of the venue. (See supported types.)"
      }
    }
  },
  "Video": {
    "description": "This object represents a video file.",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "width": {
        "type": "int",
        "description": "Video width as defined by sender"
      },
      "height": {
        "type": "int",
        "description": "Video height as defined by sender"
      },
      "duration": {
        "type": "int",
        "description": "Duration of the video in seconds as defined by sender"
      },
      "thumbnail": {
        "type": "PhotoSize",
        "description": "Optional. Video thumbnail"
      },
      "cover": {
        "type": "List",
        "description": "Optional. Video thumbnail"
      },
      "start_timestamp": {
        "type": "int",
        "description": "Optional. Timestamp in seconds from which the video will play in the message"
      },
      "file_name": {
        "type": "str",
        "description": "Optional. Original filename as defined by sender"
      },
      "mime_type": {
        "type": "str",
        "description": "Optional. MIME type of the file as defined by sender"
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have\ndifficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or\ndouble-precision float type are safe for storing this value."
      }
    }
  },
  "VideoChatEnded": {
    "description": "This object represents a service message about a video chat ended in the chat.",
    "properties": {
      "duration": {
        "type": "int",
        "description": "Video chat duration in seconds"
      }
    }
  },
  "VideoChatParticipantsInvited": {
    "description": "This object represents a service message about new members invited to a video chat.",
    "properties": {
      "users": {
        "type": "List",
        "description": "New members that were invited to the video chat"
      }
    }
  },
  "VideoChatScheduled": {
    "description": "This object represents a service message about a video chat scheduled in the chat.",
    "properties": {
      "start_date": {
        "type": "int",
        "description": "Point in time (Unix timestamp) when the video chat is supposed to be started by a chat\nadministrator"
      }
    }
  },
  "VideoChatStarted": {
    "description": "This object represents a service message about a video chat started in the chat. Currently holds no information.",
    "properties": {
      "duration": {
        "type": "int",
        "description": ""
      }
    }
  },
  "VideoNote": {
    "description": "This object represents a video message (available in Telegram apps as of v.4.0).",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "length": {
        "type": "int",
        "description": "Video width and height (diameter of the video message) as defined by sender"
      },
      "duration": {
        "type": "int",
        "description": "Duration of the video in seconds as defined by sender"
      },
      "thumbnail": {
        "type": "PhotoSize",
        "description": "Optional. Video thumbnail"
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes"
      }
    }
  },
  "Voice": {
    "description": "This object represents a voice note.",
    "properties": {
      "file_id": {
        "type": "str",
        "description": "Identifier for this file, which can be used to download or reuse the file"
      },
      "file_unique_id": {
        "type": "str",
        "description": "Unique identifier for this file, which is supposed to be the same over time and for different\nbots. Can't be used to download or reuse the file."
      },
      "duration": {
        "type": "int",
        "description": "Duration of the audio in seconds as defined by sender"
      },
      "mime_type": {
        "type": "str",
        "description": "Optional. MIME type of the file as defined by sender"
      },
      "file_size": {
        "type": "int",
        "description": "Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have\ndifficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or\ndouble-precision float type are safe for storing this value."
      }
    }
  },
  "WebAppData": {
    "description": "Describes data sent from a Web App to the bot.",
    "properties": {
      "data": {
        "type": "str",
        "description": "The data. Be aware that a bad client can send arbitrary data in this field."
      },
      "button_text": {
        "type": "str",
        "description": "Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client\ncan send arbitrary data in this field."
      }
    }
  },
  "WebAppInfo": {
    "description": "Describes a Web App.",
    "properties": {
      "url": {
        "type": "str",
        "description": "An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps"
      }
    }
  },
  "WebhookInfo": {
    "description": "Describes the current status of a webhook.",
    "properties": {
      "url": {
        "type": "str",
        "description": "Webhook URL, may be empty if webhook is not set up"
      },
      "has_custom_certificate": {
        "type": "bool",
        "description": "True, if a custom certificate was provided for webhook certificate checks"
      },
      "pending_update_count": {
        "type": "int",
        "description": "Number of updates awaiting delivery"
      },
      "ip_address": {
        "type": "str",
        "description": "Optional. Currently used webhook IP address"
      },
      "last_error_date": {
        "type": "int",
        "description": "Optional. Unix time for the most recent error that happened when trying to deliver an\nupdate via webhook"
      },
      "last_error_message": {
        "type": "str",
        "description": "Optional. Error message in human-readable format for the most recent error that\nhappened when trying to deliver an update via webhook"
      },
      "last_synchronization_error_date": {
        "type": "int",
        "description": "Optional. Unix time of the most recent error that happened when trying\nto synchronize available updates with Telegram datacenters"
      },
      "max_connections": {
        "type": "int",
        "description": "Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook\nfor update delivery"
      },
      "allowed_updates": {
        "type": "List",
        "description": "Optional. A list of update types the bot is subscribed to. Defaults to all update types\nexcept chat_member"
      }
    }
  },
  "WriteAccessAllowed": {
    "description": "This object represents a service message about a user allowing a bot to write",
    "properties": {
      "from_request": {
        "type": "bool",
        "description": "Optional. True, if the access was granted after the user accepted an\nexplicit request from a Web App sent by the method requestWriteAccess"
      },
      "web_app_name": {
        "type": "str",
        "description": "Optional. Name of the Web App which was launched from a link"
      },
      "from_attachment_menu": {
        "type": "bool",
        "description": "Optional. True, if the access was granted when the bot was added to the attachment or side menu"
      }
    }
  }
};
